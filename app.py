from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "You are a depressed robot. And yes, the answer is 42!"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Please tell a little about yourself."
        }
      ]
    },
  ],
  response_format={
    "type": "text"
  }
)

print(response.choices[0].message.content)