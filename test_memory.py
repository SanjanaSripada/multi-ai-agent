from memory.memory_manager import MemoryManager

memory = MemoryManager()

# Log a test entry
memory.log(
    source="test_input",
    data_type="Email",
    sender="test@example.com",
    intent="RFQ",
    extracted_fields={"urgent": True}
)

# Show all logs
for row in memory.fetch_all():
    print(row)
