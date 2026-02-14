# Basic function
def greet_client(name):
    return f"Welcome to Synaptic Clarity, {name}!"

# Function with default parameter
def create_prompt(task, tone="professional", language="English"):
    return f"Please {task}. Usa a {tone} tone. Respond in {language}."

# Using the function
prompt = create_prompt("summarize the document", tone="formal")

# Function with variable number of arguments - *args and **kwargs
def build_worklow(*steps, **config):
    """
    Build a workfloe from variable steps and configuration.
    
    Args:
        *steps: A variable number of steps in the workflow.
        **config: Keyword arguments for configuration options.
    """
    workflow = {
        "steps": list(steps),
        "config": config
    }
    return workflow

# Example usage
my_workflow = build_worklow(
    "Data Collection", "Data Cleaning", "Model Training", 
    timeout=300, retries=2
)