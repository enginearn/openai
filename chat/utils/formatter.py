#!/usr/bin/env python3

import os
import datetime

# ファイル形式を選択する関数を定義する
def create_save_path(ext="") -> str:
    print("If you do not save, the conversation will be lost.")
    user_ext = input("Save as .csv or .txt? [csv/txt/NO(default: not saved)]: ").lower()
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
