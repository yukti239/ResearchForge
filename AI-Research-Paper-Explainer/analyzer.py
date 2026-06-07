import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-2.5-flash")
else:
    model = None


def safe_generate(prompt):
    if model is None:
        return "⚠️ API Key Not Configured: Please add your GEMINI_API_KEY to Streamlit Cloud Secrets. Go to your app settings → Secrets and add: GEMINI_API_KEY=your_key_here"
    
    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"⚠️ Error: {str(e)}"


def summarize_paper(text):

    prompt = f"""
    Analyze this research paper.

    Provide:

    # Paper Title

    # Simple Summary

    # Problem Statement

    # Methodology

    # Key Findings

    # Limitations

    # Future Scope

    Research Paper:
    {text[:5000]}
    """

    return safe_generate(prompt)


def explain_simple(text):

    prompt = f"""
    Explain this research paper to a 15-year-old student.

    Use very simple language.
    Give examples.

    Research Paper:
    {text[:5000]}
    """

    return safe_generate(prompt)


def ask_question(text, question):

    prompt = f"""
    Research Paper:

    {text[:5000]}

    User Question:
    {question}

    Answer only using information from the paper.
    """

    return safe_generate(prompt)


def generate_project_ideas(text):

    prompt = f"""
    Based on this research paper,

    Suggest 5 unique project ideas.

    For each project provide:
    - Project Name
    - Difficulty
    - Short Description

    Research Paper:
    {text[:5000]}
    """

    return safe_generate(prompt)