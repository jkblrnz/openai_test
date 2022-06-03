import os
from dotenv import load_dotenv
import openai
import json

def main():
    load_dotenv()
    openai.api_key = os.getenv('openai_key')

    question = input("Enter your question: ")

    try:
        with open("query.txt", "r") as textFile:
            query = textFile.read()
            textFile.close()
    except IOError:
        print("failed to open query.txt")
        sys.exit(1)

    response = openai.Completion.create(
        engine = "text-davinci-002",
        prompt = query + question,
        temperature = 0,
        max_tokens = 500,
        top_p = 1,
        frequency_penalty = 0.0,
        presence_penalty = 0.0,
    )

    print(response["choices"][0]["text"].strip())

if __name__ == '__main__':
    main()
