import re
from datetime import datetime
from memory.memory_manager import MemoryManager
import json 

class EmailAgent:
    def __init__(self):
        self.memory = MemoryManager()

    def extract_email_fields(self, email_text):
        sender_match = re.search(r"From:\s*(.*)", email_text)
        sender = sender_match.group(1).strip() if sender_match else "unknown"

        subject_match = re.search(r"Subject:\s*(.*)", email_text)
        subject = subject_match.group(1).strip() if subject_match else "No subject"

        intent = self.detect_intent(email_text)
        urgency = self.detect_urgency(email_text)

        crm_format = {
            "sender": sender,
            "subject": subject,
            "intent": intent,
            "urgent": urgency,
            "summary": email_text[:100] + "..."
        }

        self.memory.log_entry(
            source="email_agent",
            data_type="Email",
            sender=sender,
            intent=intent,
            extracted_fields=crm_format
        )

        return crm_format

    def detect_intent(self, text):
        text = text.lower()
        if "invoice" in text:
            return "Invoice"
        elif "rfq" in text or "request for quote" in text:
            return "RFQ"
        elif "complaint" in text or "issue" in text:
            return "Complaint"
        elif "regulation" in text:
            return "Regulation"
        else:
            return "General"

    def detect_urgency(self, text):
        urgency_keywords = ["urgent", "asap", "immediately", "important", "priority"]
        text = text.lower()
        return any(word in text for word in urgency_keywords)
