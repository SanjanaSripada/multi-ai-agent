from memory.memory_manager import MemoryManager
import json 

class JSONAgent:
    REQUIRED_FIELDS = ["sender", "intent", "data"]

    def __init__(self):
        self.memory = MemoryManager()

    def process_json(self, payload):
        missing_fields = [field for field in self.REQUIRED_FIELDS if field not in payload]

        if missing_fields:
            result = {
                "status": "error",
                "message": f"Missing fields: {', '.join(missing_fields)}",
                "original_payload": payload
            }
        else:
            reformatted = {
                "from": payload["sender"],
                "intent": payload["intent"],
                "content": payload["data"]
            }

            # Log to memory
            self.memory.log_entry(
                source="json_agent",
                data_type="JSON",
                sender=payload["sender"],
                intent=payload["intent"],
                extracted_fields=reformatted
            )

            result = {
                "status": "success",
                "formatted_data": reformatted
            }

        return result
