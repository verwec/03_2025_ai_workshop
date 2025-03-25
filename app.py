from openai import OpenAI

client = OpenAI()

user_history = []

while True:
    user_input = input("Enter a message: ")
    user_history.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=user_history,
    )

    print(response.choices[0].message.content)
    user_history.append({"role": "assistant", "content": response.choices[0].message.content})