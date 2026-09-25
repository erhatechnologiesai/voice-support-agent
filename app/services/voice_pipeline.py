def process_voice_turn(caller_id: str, spoken: str):
    s_low = spoken.lower()
    if "billing" in s_low or "charge" in s_low:
        intent = "BILLING_INQUIRY"
        reply = "I understand you have a question about your recent billing statement. Let me pull up your account records."
    elif "technical" in s_low or "down" in s_low or "broken" in s_low:
        intent = "TECHNICAL_INCIDENT"
        reply = "I hear that you are experiencing a technical issue. Our systems are currently monitoring for errors, and I am alerting an engineer."
    else:
        intent = "GENERAL_INQUIRY"
        reply = "Thank you for calling Erha Technologies. How can our AI support specialist assist your team today?"

    return reply, intent
