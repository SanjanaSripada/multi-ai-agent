from agents.classifier_agent import ClassifierAgent

classifier = ClassifierAgent()

# Test Email Input
email_text = """From: client@company.com
Subject: Request for Quote

Hi Team, please send us a quote for 1000 units. It’s urgent.

Thanks,
Client
"""

# Test JSON Input
json_payload = {
    "sender": "vendor@example.com",
    "intent": "Invoice",
    "data": {
        "amount": 7500,
        "due_date": "2025-06-15"
    }
}

print("\n--- Email Input ---")
email_result = classifier.route_input(email_text)
print(email_result)

print("\n--- JSON Input ---")
json_result = classifier.route_input(json_payload)
print(json_result)
