import openai

# OpenAI APIキーを設定
openai.api_key = 'sk-proj-ZFzo4bjoVEjIT0XUT8GNT3BlbkFJ1hszuUnELOZITpoqPluD'

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.Create(
        model="gpt-4.0",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)