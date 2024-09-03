import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model name and parameters
model_name = "llama3.1"  # or whatever the exact name of the model is

# Define a prompt for the model
prompt = "Translate the following English text to French: Hello, how are you?"

# Generate a response from the model
response = client.generate(model=model_name, prompt=prompt)

print("Prompt:", prompt)
print("Response:", response)
