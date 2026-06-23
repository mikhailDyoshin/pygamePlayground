from ollama import chat

TEMPERATURE = 1.0
messages = []

while True:
    user_input = input("Chat with history: ")
    response = chat(
        model="qwen3.5",
        messages=[*messages, {"role": "user", "content": user_input}],
        think=False,
        # keep_alive="5m",
        options={"temperature": TEMPERATURE},
    )

    # Add the response to the messages to maintain the history
    messages += [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": response.message.content},
    ]
    print(response.message.content + "\n")
