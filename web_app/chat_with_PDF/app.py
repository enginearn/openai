#!/usr/bin/env python3

import streamlit as st
import pypdf

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def validate_api_key(api_key):
    # Add your own validation logic here
    expected_length = 51
    if not api_key or len(api_key) != expected_length:
        st.error("Invalid API key. Please check and try again.")
    else:
        st.session_state["api_key"] = api_key
        return True

def setup_streamlit():
    st.set_page_config(
        page_title="Chat with PDF", layout="centered", initial_sidebar_state="auto"
    )
    st.header("Chat with PDF 🕸")
    st.write("This is a web app to chat with PDFs.")
    api_key = st.text_input("Enter your OpenAI API Key", type='password')
    if st.button('Submit'):
        if validate_api_key(api_key):
            st.success("API key validated successfully!")
        else:
            st.error("Invalid API key. Please check and try again.")


def upload_pdf():
    st.subheader("Upload PDF")
    return st.file_uploader("Upload PDF", type=["pdf"])


def pdf_to_text(pdf_file) -> str:
    pdf_reader = pypdf.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        page = page.extract_text()
        if page is None:
            continue
        text += page
    return text


def text_to_chunks(text) -> list[str]:
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=150,
        length_function=len,
    )
    return text_splitter.split_text(text)


def chat(knowledge_base, user_input):
    try:
        user_input = user_input.strip()
        if user_input != "":
            with st.spinner(text="In progress..."):
                response = knowledge_base.similarity_search(user_input)
                llm = OpenAI(openai_api_key=st.session_state["api_key"])  # Use the API key from the session state
                chain = load_qa_chain(llm, chain_type="stuff")
                with get_openai_callback() as cb:
                    response = chain.run(
                        input_documents=response, question=user_input, top_k=1
                    )
                    st.text_area("Chatbot", response, height=200)
                    st.write(
                        f"Total Tokens: {cb.total_tokens} Prompt Tokens: {cb.prompt_tokens} Completion Tokens: {cb.completion_tokens} Total Cost (USD): ${cb.total_cost:.5f}"
                    )
    except Exception as e:
        st.error(e)# Display the error message in the Streamlit interface


def main() -> None:
    setup_streamlit()
    pdf_file = upload_pdf()

    # Extract PDF to text
    if pdf_file is not None:
        text = pdf_to_text(pdf_file)

        # split text
        chunks = text_to_chunks(text)

        # Embedding
        embeddings = OpenAIEmbeddings(openai_api_key=st.session_state["api_key"])
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Chat
        st.subheader("Chat")
        user_input = st.text_input("You", "")
        chat(knowledge_base, user_input)


if __name__ == "__main__":
    main()
