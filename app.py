from openai import OpenAI
from vectorstore_example import get_context

client = OpenAI()

user_history = []

def chat(query):
    context = get_context(query)

    prompt_with_context = f"""
        Context:
        {context}

        Question:
        {query}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", 
             "content": prompt_with_context
             }
        ]  
    )

    return response.choices[0].message.content
