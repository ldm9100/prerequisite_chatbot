import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

head = """The following is a conversation with an AI assistant. The assistant is clever, especially helpful for recommending subjects to help User's study. 
If the User wants to study something, the assistant recommend a prerequisite to study that subject. 
For example, if the User wants to study about 2d tree, the assistant can say 'You need to study linked list first.'\n\nUser: """

while True:
    content = input("User: ")

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= head + content + "\nAI: ",
        temperature=1.0,
        max_tokens=100,
        top_p=0.9,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )

    chat_response = response.choices[0].text.strip()
    print(f"AI: {chat_response}")
