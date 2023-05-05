#!/usr/bin/env python3

import datetime

from rich import print

from chat import ask_ChatGPT, give_a_role, calculate_cost
from utils.save_data import save_conversation


def main() -> None:
    # 会話開始
    print("Welcome to the chatbot. Type 'q' or 'exit' to quit.")
    give_a_role() # ユーザーがシステムの役割を指定する
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

        if question.lower() in ["q", "quit", "exit", "bye"]:
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


if __name__ == "__main__":
    main()
