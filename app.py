from openai import OpenAI

client = OpenAI()

while True:
    user_input = input("Enter a message: ")

    response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": user_input
            }
        ]
        },
    ]
    )

    print(response.choices[0].message.content)