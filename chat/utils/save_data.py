#!/usr/bin/env python3

import os
import pandas as pd

from .formatter import create_save_path

# 会話を保存する関数を定義する
def save_conversation(conversation: list) -> None:
    file = create_save_path()
    file, ext = os.path.splitext(file)
    match ext:
        case ".csv":
            columns = [
                "timestamp",
                "user",
                "message",
                "comp_tokens",
                "prompt_tokens",
                "total_tokens",
                "cost",
            ]
            cols = len(columns)
            # data = [conversation[i : i + cols] for i in range(0, len(conversation), cols)] # 3行を1行へ (timestamp, user, message)
            data = [
                conversation[i : i + cols] for i in range(0, len(conversation), cols)
            ]  # 7行を1行へ (timestamp, user, message, comp_tokens, prompt_tokens, total_tokens, cost)
            df = pd.DataFrame(data, columns=columns)
            df.to_csv(file + ext, index=False)
        case ".txt":
            with open(file + ext, "w") as f:
                for line in conversation:
                    f.write(str(line) + "\n")
        case _:
            "not matching..."

    print(f"Conversation saved to {file + ext}.")
