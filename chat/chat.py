#!/usr/bin/env python3

import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("OPENAI_API_KEY")

# 料金の概算を計算するための関数を定義する
def calculate_cost(total_tokens) -> float:
    cost = total_tokens * 0.002  # 1トークンあたり0.002ドル
    return round(cost, 3)


def give_a_role() -> str:
    res = input("Something specify the role for assistant?[y/N]: ").lower()
    if res in ["y", "yes"]:
        role_text = input("Specify the role for assistant: ")
    else:
        role_text = ""
    return role_text

# ChatGPTを使って質問する関数を定義する
def ask_ChatGPT(question: str, model="gpt-3.5-turbo", temperature=0.9, role_text="") -> str:
    response = openai.ChatCompletion.create(
        model=model,
        temperature=temperature,
        messages=[
            {"role": "system", "content": f"{role_text}"},
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
