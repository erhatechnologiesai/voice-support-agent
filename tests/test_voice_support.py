import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestVoiceSupport(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_voice_dialogue(self):
        res = self.client.post("/voice-turn", json={"caller_id": "CALL-101", "spoken_text": "I have an issue with an unauthorized charge."})
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data["intent"], "BILLING_INQUIRY")
        self.assertIn("billing statement", data["spoken_response"])

if __name__ == "__main__":
    unittest.main()
