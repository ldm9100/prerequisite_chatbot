import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    content = input("User: ")

    response = openai.Completion.create(
        model="davinci:ft-personal-2023-06-10-11-29-28",
        prompt= "\n\nUser: " + content + "\nAI: ",
        temperature=1.0,
        max_tokens=50,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )

    chat_response = response.choices[0].text.strip()
    print(f"AI: {chat_response}")
