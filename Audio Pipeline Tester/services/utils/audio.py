
import os, tempfile
from typing import Optional

def get_audio_metadata(path: str) -> dict:
    """Return basic metadata, trying soundfile or pydub."""
    try:
        import soundfile as sf
        info = sf.info(path)
        return {"duration": info.duration, "samplerate": info.samplerate, "channels": info.channels}
    except Exception:
        try:
            from pydub import AudioSegment
            a = AudioSegment.from_file(path)
            return {"duration": len(a)/1000.0, "samplerate": a.frame_rate, "channels": a.channels}
        except Exception:
            return {"duration": None, "samplerate": None, "channels": None}

def slice_audio_to_temp(path: str, start_sec: float, end_sec: float) -> Optional[str]:
    """
    Create a temporary sliced audio file. Try pydub, then soundfile+librosa.
    Returns path to temp wav or None.
    """
    try:
        from pydub import AudioSegment
        audio = AudioSegment.from_file(path)
        start_ms = int(start_sec*1000)
        end_ms = int(end_sec*1000)
        seg = audio[start_ms:end_ms]
        fd, out = tempfile.mkstemp(suffix=".wav")
        os.close(fd)
        seg.export(out, format="wav")
        return out
    except Exception:
        try:
            import librosa, soundfile as sf
            y, sr = librosa.load(path, sr=None, mono=True, offset=start_sec, duration=max(0.0, end_sec-start_sec))
            fd, out_path = tempfile.mkstemp(suffix=".wav")
            os.close(fd)
            sf.write(out_path, y, sr)
            return out_path
        except Exception:
            return None
