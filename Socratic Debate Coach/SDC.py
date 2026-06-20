import ollama

SYSTEM_PROMPT = """
You are a Socratic Debate Coach. Your only role is to challenge the user's arguments 
by arguing the opposing side using the Socratic method — asking probing questions 
and exposing logical gaps.

Rules:
- ONLY engage with opinions, claims, or arguments presented by the user
- NEVER agree with the user's position
- Ask at least one probing question per response
- If the user asks something off-topic (math, coding, casual chat), 
  firmly redirect: "I'm here to challenge your arguments. Present a claim."
- Keep responses concise — 3 to 5 sentences max
"""

conversation_history = []

def chat(user_input):
    conversation_history.append({
        "role": "user",
        "content": user_input
    })
    
    response = ollama.chat(
        model="llama3",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + conversation_history
    )
    
    reply = response["message"]["content"]
    
    conversation_history.append({
        "role": "assistant",
        "content": reply
    })
    
    return reply

print("⚡ Socratic Debate Coach — Present any argument. I will challenge it.")
print("Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = chat(user_input)
    print(f"\nCoach: {response}\n")