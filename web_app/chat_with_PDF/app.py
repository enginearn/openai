#!/usr/bin/env python3

from dotenv import load_dotenv
import streamlit as st
import pypdf

from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def main() -> None:
    load_dotenv()
    st.set_page_config(
        page_title="Chat with PDF", layout="centered", initial_sidebar_state="auto"
    )
    st.header("Chat with PDF 🕸")
    st.write("This is a web app to chat with PDFs.")

    # Upload PDF
    st.subheader("Upload PDF")
    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

    # Extract PDF to text
    if pdf_file is not None:
        pdf_reader = pypdf.PdfReader(pdf_file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # split text
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=500,
            chunk_overlap=150,
            length_function=len,
        )
        chunks = text_splitter.split_text(text)

        # Embedding
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Chat
        st.subheader("Chat")
        user_input = st.text_input("You", "")
        # while True:
        try:
            user_input = user_input.strip()
            if user_input != "":
                with st.spinner(text="In progress..."):
                    response = knowledge_base.similarity_search(user_input)
                    llm = OpenAI()
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
            print(e)


if __name__ == "__main__":
    main()
