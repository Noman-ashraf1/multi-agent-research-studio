from app.agents.llm.llm import llm

print("Calling LLM...")

response = llm.invoke("Say hello in one sentence.")

print("Response received:")
print(response.content)