from pydantic import BaseModel
from typing import Optional

class AudioTranscriptInput(BaseModel):
    caller_id: str
    spoken_text: str

class VoiceDialogueOutput(BaseModel):
    caller_id: str
    spoken_response: str
    tts_voice_id: str = "alloy"
    intent: str
