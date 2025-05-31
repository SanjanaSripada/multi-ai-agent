import json
from agents.email_agent import EmailAgent
from agents.json_agent import JSONAgent
from memory.memory_manager import MemoryManager
from agents.pdf_agent import PDFAgent
from datetime import datetime

class ClassifierAgent:
    def __init__(self):
        self.email_agent = EmailAgent()
        self.json_agent = JSONAgent()
        self.memory = MemoryManager()
        self.pdf_agent = PDFAgent()

    def classify_format(self, input_data):
        if isinstance(input_data, dict):
            return "JSON"
        elif isinstance(input_data, str):
            if "From:" in input_data and "Subject:" in input_data:
                return "Email"
            elif input_data.lower().endswith(".pdf"):
                return "PDF"
            else:
                return "UnknownText"
        else:
            return "Unknown"

    def classify_intent(self, text):
        lowered = text.lower()
        if "quote" in lowered or "rfq" in lowered:
            return "RFQ"
        elif "invoice" in lowered or "amount" in lowered:
            return "Invoice"
        elif "complaint" in lowered or "issue" in lowered:
            return "Complaint"
        elif "regulation" in lowered or "policy" in lowered:
            return "Regulation"
        else:
            return "Unknown"

    def route_input(self, input_data):
        try:
            input_type = self.classify_format(input_data)
            intent = self.classify_intent(str(input_data))

            if input_type == "Email":
                result = self.email_agent.extract_email_fields(input_data)
            elif input_type == "JSON":
                result = self.json_agent.process_json(input_data)
            elif input_type == "PDF":
                result = self.pdf_agent.extract_fields(input_data)
                intent = result.get("intent", "Unknown")
            else:
                result = {"error": "Unsupported input type."}

            print("LOGGING")
            self.memory.log_entry(
                source=str(input_data)[:30],
                data_type=input_type,
                sender=result.get("sender", "Unknown"),
                intent=intent,
                extracted_fields=result
            )
            return result
        except Exception as e:
            return {"status": "error", "message": str(e)}

