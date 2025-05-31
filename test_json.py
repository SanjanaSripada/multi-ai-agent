from agents.json_agent import JSONAgent

# Simulated JSON payload
json_payload = {
    "sender": "vendor@example.com",
    "intent": "Invoice",
    "data": {
        "amount": 5000,
        "due_date": "2025-06-10"
    }
}

agent = JSONAgent()
result = agent.process_json(json_payload)

print("JSON Agent Result:")
print(result)
