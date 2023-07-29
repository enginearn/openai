# chat-lang-chain-zenn

## Description

## Setup

``` PowerShell
# Path: Python\openai\chat_lang_chain_zenn
rye init
success: Initialized project in C:\Users\path\to\Development\Python\openai\chat_lang_chain_zenn\.
  Run `rye sync` to get started
rye show
project: chat-lang-chain-zenn
path: C:\Users\path\to\Development\Python\openai\chat_lang_chain_zenn
venv: C:\Users\path\to\Development\Python\openai\chat_lang_chain_zenn\.venv
target python: 3.8
venv python: cpython@3.11.3
rye pin 3.11
pinned 3.11.3 in C:\Users\path\to\Development\Python\openai\chat_lang_chain_zenn\.python-version
ls

    Directory: C:\Users\path\to\Development\Python\openai\chat_lang_chain_zenn

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d----          2023/07/29    13:49                src
-a---          2023/07/29    13:53              7 .python-version
-a---          2023/07/29    13:49            419 pyproject.toml
-a---          2023/07/29    13:49             52 README.md
rye sync
.\.venv\Scripts\activate
rye add openai langchain tiktoken streamlit mypy pylint black
rye sync
$env:openai_api_key = "YOUR_API_KEY"
```
