
import os, tempfile
from typing import Optional


def _configure_pydub_ffmpeg_paths() -> None:
    """Configure pydub to use explicit ffmpeg/ffprobe paths when provided.
    Looks for FFMPEG_BINARY and FFPROBE_BINARY in environment and applies
    them to pydub AudioSegment so imports succeed even if PATH is missing.
    """
    try:
        from pydub import AudioSegment
        from pydub.utils import which

        ffmpeg_path = os.environ.get("FFMPEG_BINARY") or which("ffmpeg")
        ffprobe_path = os.environ.get("FFPROBE_BINARY") or which("ffprobe")

        if ffmpeg_path:
            # pydub checks these attributes
            AudioSegment.converter = ffmpeg_path
            AudioSegment.ffmpeg = ffmpeg_path
        if ffprobe_path:
            AudioSegment.ffprobe = ffprobe_path
    except Exception:
        # Best-effort configuration; ignore if pydub not available yet
        pass

def get_audio_metadata(path: str) -> dict:
    """Return basic metadata, trying soundfile or pydub."""
    try:
        import soundfile as sf
        info = sf.info(path)
        return {"duration": info.duration, "samplerate": info.samplerate, "channels": info.channels}
    except Exception:
        try:
            _configure_pydub_ffmpeg_paths()
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
        _configure_pydub_ffmpeg_paths()
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
