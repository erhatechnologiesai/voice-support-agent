from fastapi import FastAPI
from app.config import settings
from app.models import AudioTranscriptInput, VoiceDialogueOutput
from app.services.voice_pipeline import process_voice_turn

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

@app.post("/voice-turn", response_model=VoiceDialogueOutput)
def voice_turn(req: AudioTranscriptInput):
    reply, intent = process_voice_turn(req.caller_id, req.spoken_text)
    return VoiceDialogueOutput(
        caller_id=req.caller_id,
        spoken_response=reply,
        intent=intent
    )
