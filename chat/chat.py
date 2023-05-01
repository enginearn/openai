#!/usr/bin/env python3

import os
import datetime
import tiktoken
import math
import pandas as pd
import polars as pl
from rich import print
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

# 料金の概算を計算するための関数を定義する
def calculate_cost(total_tokens) -> float:
    cost = math.floor(total_tokens * 0.002)  # 1トークンあたり0.002ドル
    return round(cost, 2)  # 小数点以下2桁で四捨五入して返す


# ChatGPTを使って質問する関数を定義する
def ask_ChatGPT(question: str, model="gpt-3.5-turbo") -> str:
    response = openai.ChatCompletion.create(
        model=model,
        temperature=0.9,
        messages=[
            {"role": "user", "content": question},
        ],
    )
    # print(response)
    answer = (
        f"{response.choices[0].message.role}: {response.choices[0].message.content}"
    )
    # print(f"total tokens: {response.choices[0].total_logprobs.tokens}")
    # print(f"response: {response.keys()}")
    completion_tokens = response.usage.completion_tokens
    prompt_tokens = response.usage.prompt_tokens
    total_tokens = response.usage.total_tokens
    return answer, completion_tokens, prompt_tokens, total_tokens


# ファイル形式を選択する関数を定義する
def create_save_path(ext="txt") -> str:
    print("If not saved, the conversation will be lost.")
    user_ext = input("Save as .csv or .txt? [csv/txt/no(default: not saved)]: ").lower()
    if user_ext in ["q", "exit", "quit", "bye", "no", ""]:
        print("Bye!")
        exit()
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


# 会話を保存する関数を定義する
def save_conversation(conversation: list) -> None:
    file = create_save_path()
    file, ext = os.path.splitext(file)
    match ext:
        case ".csv":
            # data = [conversation[i : i + 2] for i in range(0, len(conversation), 2)] # 2行を1行へ (timestamp, message)
            data = [
                conversation[i : i + 7] for i in range(0, len(conversation), 7)
            ]  # 7行を1行へ (timestamp, message, comp_tokens, prompt_tokens, total_tokens, cost)
            columns = [
                "timestamp",
                "user",
                "message",
                "comp_tokens",
                "prompt_tokens",
                "total_tokens",
                "cost",
            ]
            df = pd.DataFrame(data, columns=columns)
            df.to_csv(file + ext, index=False)
        case ".txt":
            with open(file + ext, "w") as f:
                for line in conversation:
                    f.write(str(line) + "\n")
        case _:
            "not matching..."

    print(f"Conversation saved to {file + ext}.")


# 会話開始
print("Welcome to the chatbot. Type 'q' or 'exit' to quit.")
conversation = []
while True:
    try:
        question = input("user: ")
        if question == "":
            continue
    except KeyboardInterrupt:
        print("Bye!")
        exit()

    conversation.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    conversation.extend(["user", question])
    conversation.extend(["-", "-", "-", "-"])

    if question in ["q", "exit"]:
        # remove last 7 lines
        save_conversation(conversation[:-7])
        break
    elif len(conversation) > 0:
        results = ask_ChatGPT(question)
        assistant = results[0].split(":")[0]
        answer = results[0].split(":")[1]
        comp_tokens = results[1]
        prompt_tokens = results[2]
        total_tokens = results[3]
        cost = calculate_cost(total_tokens)

        print(f"{assistant}: {answer}")

        conversation.append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        conversation.extend([assistant, answer])
        conversation.extend([comp_tokens, prompt_tokens, total_tokens, str(cost)])
