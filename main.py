import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()


def main():
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )
    message = input("What do you wanna ask?: ")
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    print(chat_completion.choices[0].message.content)


if __name__ == "__main__":
    main()
