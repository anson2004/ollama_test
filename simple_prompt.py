import ollama

messages=[
  {
    'role': 'user',
    'content': 'Hello world',
  },
]
# Streaming chat completion with a model
for chunk in ollama.chat('llama2', messages=messages, stream=True):
  print(chunk['message']['content'], end='', flush=True)