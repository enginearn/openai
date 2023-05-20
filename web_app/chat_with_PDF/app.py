#!/usr/bin/env python3

import os
from dotenv import load_dotenv
import streamlit as st
import pypdf

def main() -> None:
    load_dotenv()
    st.set_page_config(page_title='Chat with PDF', layout='centered', initial_sidebar_state='auto')
    st.header('Chat with PDF 🕸')
    st.write('This is a web app to chat with PDFs.')

    # Upload PDF
    st.subheader('Upload PDF')
    pdf_file = st.file_uploader('Upload PDF', type=['pdf'])

    # Extract PDF to text
    if pdf_file is not None:
        st.subheader('PDF to text')
        pdf_reader = pypdf.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            text = page.extract_text()
            st.write(text)


if __name__ == '__main__':
    main()
