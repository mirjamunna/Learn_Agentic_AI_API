# Lists - ordered, mutable, allows duplicate elements
tasks = ["analyze document", "extract data", "generate report"]
tasks.append("send notification")  # Add new task to the list
first_task = tasks[0]  # Access first task

# Dictionaries - key-value pairs, unordered, mutable
client_info = {
    "name": "Acme Corp",
    "industry": "Manufacturing",
    "location": "New York",
    "active": True
}
print(client_info["name"])  # Access value by key

# Nested data structures - combining lists and dictionaries
# Common in API responses and complex data representations
workflow = {
    "id": "wf_001",
    "steps": [
        {"name": "input", "type": "document"},
        {"name": "process", "type": "llm"},
        {"name": "output", "type": "email"}
    ],
    "metadata": {
        "created_by": "Mir Shah",
        "version": 1.0
    }
}

# Accessing nested data
first_step = workflow["steps"][0]["name"]  # "input"
created_by = workflow["metadata"]["created_by"]  # "Mir Shah"

print(first_step + " " + created_by)