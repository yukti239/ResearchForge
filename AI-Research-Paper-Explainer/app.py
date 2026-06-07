import streamlit as st

from pdf_reader import (
    extract_text,
    get_page_count,
    get_word_count
)

from analyzer import (
    summarize_paper,
    explain_simple,
    ask_question,
    generate_project_ideas
)

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="ResearchForge",
    page_icon="⚒️",
    layout="wide"
)

# ------------------------------------------------
# CUSTOM CSS
# ------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:1.5rem;
    max-width:1300px;
}

/* Hero */

.hero-title{
    font-size:72px;
    font-weight:700;
    text-align:center;
    margin-bottom:5px;
}

.hero-tagline{
    font-size:22px;
    color:#C27C48;
    text-align:center;
    margin-bottom:15px;
}

.hero-desc{
    font-size:18px;
    color:#9CA3AF;
    text-align:center;
    margin-bottom:35px;
}

/* Cards */

.feature-box{
    background:#141414;
    border:1px solid #2A2A2A;
    border-radius:16px;
    padding:25px;
    min-height:220px;
}

.feature-box h3{
    color:#F5F5F5;
}

.feature-box p{
    color:#B0B0B0;
}

.feature-box:hover{
    border:1px solid #C27C48;
}

/* Metrics */

div[data-testid="stMetric"]{
    background:#141414;
    border:1px solid #2A2A2A;
    padding:15px;
    border-radius:12px;
}

/* Buttons */

.stButton > button{
    width:100%;
    height:55px;
    border-radius:12px;
    font-weight:600;
}

/* Upload Box */

section[data-testid="stFileUploader"]{
    border:1px dashed #3A3A3A;
    border-radius:16px;
    padding:15px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------
# SIDEBAR
# ------------------------------------------------

with st.sidebar:

    st.title("⚒️ ResearchForge")

    st.markdown("---")

    st.write("Turn research papers into:")

    st.write("📄 AI Insights")
    st.write("🎓 Simplified Explanations")
    st.write("💡 Project Ideas")
    st.write("💬 Interactive Q&A")

    st.markdown("---")

    st.caption("Version 1.0")

# ------------------------------------------------
# HERO
# ------------------------------------------------

st.markdown("""
<div class="hero-title">
⚒️ ResearchForge
</div>

<div class="hero-tagline">
Forging Projects from Research
</div>

<div class="hero-desc">
Upload any research paper and transform it into insights,
project ideas, explanations and research Q&A.
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------
# FEATURE CARDS
# ------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-box">
    <h3>📄 AI Insights</h3>
    <p>
    Get AI-powered analysis and key takeaways
    from your research paper.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    <h3>🎓 Simplify</h3>
    <p>
    Understand complex concepts in
    simple easy-to-grasp language.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
    <h3>💬 Research Q&A</h3>
    <p>
    Ask anything about your paper
    and receive accurate answers.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-box">
    <h3>💡 Project Ideas</h3>
    <p>
    Discover implementation ideas
    inspired by the research.
    </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ------------------------------------------------
# FILE UPLOAD
# ------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload Research Paper (PDF)",
    type=["pdf"]
)

# ------------------------------------------------
# AFTER UPLOAD
# ------------------------------------------------

if uploaded_file:

    text = extract_text(uploaded_file)

    pages = get_page_count(uploaded_file)

    words = get_word_count(text)

    st.success("Research Paper Uploaded Successfully")

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Pages", pages)

    with m2:
        st.metric("Words", f"{words:,}")

    with m3:
        st.metric("Model", "Gemini")

    st.markdown("---")

    b1, b2, b3 = st.columns(3)

    analyze = b1.button("📄 Analyze Paper")
    explain = b2.button("🎓 Explain Simply")
    ideas = b3.button("💡 Generate Ideas")

    if analyze:

        with st.spinner("Analyzing..."):

            result = summarize_paper(text)

        st.markdown("## 📄 Analysis")

        st.write(result)

    if explain:

        with st.spinner("Generating Explanation..."):

            result = explain_simple(text)

        st.markdown("## 🎓 Explanation")

        st.write(result)

    if ideas:

        with st.spinner("Generating Ideas..."):

            result = generate_project_ideas(text)

        st.markdown("## 💡 Project Ideas")

        st.write(result)

    st.markdown("---")

    st.markdown("## 💬 Research Assistant")

    question = st.text_input(
        "Ask a question about this paper"
    )

    if question:

        with st.spinner("Thinking..."):

            answer = ask_question(
                text,
                question
            )

        st.write(answer)