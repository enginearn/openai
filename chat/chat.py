#!/usr/bin/env python3

import os
import datetime
import pandas as pd
import polars as pl
from rich import print
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")


def ask_ChatGPT(question: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question},
        ],
    )
    # print(response)
    answer = (
        f"{response.choices[0].message.role}: {response.choices[0].message.content}"
    )
    return answer


def create_save_path(ext="txt") -> str:
    user_ext = input("Save as .csv or .txt? [csv/txt]: ")
    if user_ext == "":
        pass
    elif user_ext in ["csv", "txt"]:
        ext = user_ext
    save_dir = "conversations"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    dt = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"conversation_{dt}.{ext}"
    file = os.path.join(os.path.abspath(save_dir), file_name)
    # print(f"Saving conversation to {file}.")
    return file


def save_conversation(conversation: list) -> None:
    file = create_save_path()
    file, ext = os.path.splitext(file)
    match ext:
        case ".csv":
            data = [conversation[i : i + 2] for i in range(0, len(conversation), 2)]
            df = pd.DataFrame(data, columns=["text", "timestamp"])
            df.to_csv(file + ext, index=False)
        case ".txt":
            with open(file + ext, "w") as f:
                for line in conversation:
                    f.write(line + "\n")
        case _:
            "not matching..."

    print(f"Conversation saved to {file + ext}.")


# Start the chatbot
print("Welcome to the chatbot. Type 'q' or 'exit' to quit.")
conversation = []
while True:
    question = input("You: ")
    if question == "":
        continue

    conversation.append(f"You: {question}")
    conversation.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if question in ["q", "exit"]:
        # remove last two lines as one conversation is two lines
        save_conversation(conversation[:-2])
        break
    elif len(conversation) > 0:
        answer = ask_ChatGPT(question)
        print(answer)
        conversation.append(f"{answer}")
        conversation.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
