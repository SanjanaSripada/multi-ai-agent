import fitz  # PyMuPDF
from memory.memory_manager import MemoryManager
from datetime import datetime
import json 

class PDFAgent:
    def __init__(self):
        self.memory = MemoryManager()

    def extract_text_from_pdf(self, file_path):
        doc = fitz.open(file_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text

    def extract_fields(self, file_path):
        text = self.extract_text_from_pdf(file_path)
        intent = self.detect_intent(text)
        timestamp = datetime.now().isoformat()

        clean_summary = text[:200].replace('\n', ' ')

        self.memory.log_entry(
            source=file_path,
            data_type="PDF",
            sender="Unknown",
            intent=intent,
            extracted_fields={"raw_text": clean_summary + "..."}
        )

        return {
            "intent": intent,
            "summary": clean_summary + "..."
        }


    def detect_intent(self, text):
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
