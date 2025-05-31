from agents.email_agent import EmailAgent

email_text = """From: client@company.com
Subject: Request for Quote - Urgent

Hello,

We urgently need a quote for 500 units of your product. Please respond ASAP.

Regards,
Client Team
"""

agent = EmailAgent()
result = agent.extract_email_fields(email_text)

print("Extracted Email Info:")
for key, value in result.items():
    print(f"{key}: {value}")
