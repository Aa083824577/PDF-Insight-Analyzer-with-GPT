# main.py: This is a Streamlit application that allows users to upload PDF files.
#  It uses parser.py to extract text from the PDF and then sends that text
#  (or a truncated version of it) to insights.py to generate insights using an LLM.
#  It displays the extracted text and the generated insights.


import streamlit as st 
import os 
import pandas as pd
from parser import parser_pdf
from insights import get_llm_insights

st.set_page_config(page_title="file analyser", layout="wide")
st.title("file analysis system with llm ")

uploaded_file =  st.file_uploader("uplodad your pdf , csv or excel file", type=["pdf"] )


if uploaded_file: 
    file_path = os.path.join("assets/uploads", uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    pdf_text = parser_pdf(file_path)
    print(len(pdf_text))
    st.subheader("PDF content")
    st.text_area("text extracted from PDF", pdf_text , height=300)

    if st.button("generate insights from pdf"):
        with st.spinner("thinking..."):
            try:
                insight = get_llm_insights(pdf_text[:8000])
                st.success("insight:")
                st.write(insight)
                print(insight)
            except Exception as e:
                st.error(f"Error generating insights: {e}")
    # st.stop()
