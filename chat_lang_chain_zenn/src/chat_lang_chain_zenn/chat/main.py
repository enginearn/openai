#!/usr/bin/env python3

import streamlit as st
from langchain.chat_models import ChatOpenAI
from chat_utils import init_chat, init_messages, select_model, handle_user_input, display_messages, display_cost

def main() -> None:
    init_chat()
    init_messages()
    model, temperature = select_model()
    llm = ChatOpenAI(model=model, temperature=temperature)
    handle_user_input(llm)
    display_messages()
    display_cost()

if __name__ == "__main__":
    main()
