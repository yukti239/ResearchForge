# 🔬 ResearchForge - AI Research Paper Explainer

An intelligent tool that analyzes research papers using Google's Gemini AI to provide summaries, explanations, answer questions, and generate project ideas.

## ✨ Features

- **📝 Paper Summarization**: Get comprehensive summaries with key findings and limitations
- **🧠 Simplified Explanations**: Understand complex papers in simple language
- **❓ Q&A System**: Ask specific questions about the research paper
- **💡 Project Ideas**: Generate implementation ideas based on research concepts

## 🚀 Deployment

**Live App**: https://researchforge-czqwrqljbrnunrcna6fcbo.streamlit.app/

**GitHub Repo**: https://github.com/yukti239/ResearchForge

## 📋 Prerequisites

- Python 3.8+
- Google Gemini API Key ([Get it here](https://ai.google.dev))

## 🔧 Setup Instructions

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/yukti239/ResearchForge.git
   cd AI-Research-Paper-Explainer
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Add your Gemini API key:
   - Create a `.streamlit/secrets.toml` file
   - Add: `GEMINI_API_KEY = "your-api-key-here"`

5. Run the app:
   ```bash
   streamlit run app.py
   ```

### Streamlit Cloud Deployment

1. Go to your app on Streamlit Cloud: https://share.streamlit.io/
2. Click the menu (⋮) on your ResearchForge app
3. Select **Settings**
4. Go to **Secrets**
5. Add your API key:
   ```toml
   GEMINI_API_KEY = "your-gemini-api-key"
   ```
6. Save - your app will automatically restart!

## 📦 Project Structure

```
AI-Research-Paper-Explainer/
├── app.py              # Main Streamlit application
├── analyzer.py         # AI analysis functions
├── pdf_reader.py       # PDF extraction utilities
├── requirements.txt    # Python dependencies
└── .streamlit/
    └── secrets.toml    # Local API key (not committed)
```

## 🛠️ Technologies Used

- **Streamlit**: Web framework for data apps
- **Google Generative AI**: Gemini API for paper analysis
- **PyPDF**: PDF text extraction
- **Python-dotenv**: Environment variable management

## 📝 License

MIT License - feel free to use and modify!

## 🤝 Contributing

Contributions are welcome! Feel free to open issues and submit pull requests.

---

Made with ❤️ for researchers and students
