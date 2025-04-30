import streamlit as st

# Set page config
st.set_page_config(
    page_title="Muhammad Waheed - Portfolio",
    page_icon="👨‍💻",
    layout="centered",
)

# Global CSS styling
st.markdown("""
    <style>
    html, body, [class*="css"] {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f5f7fa;
        color: #333;
    }
    .stButton>button {
        border-radius: 8px;
        padding: 0.5em 1.5em;
        font-weight: 600;
        font-size: 1rem;
        margin: 0.25em;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 14px rgba(0,0,0,0.15);
    }
    .page-title {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.title("📁 Portfolio")
page = st.sidebar.radio("Go to", ["Home", "Skills", "Projects", "Learning Journey", "Contact"])

# Home Page
if page == "Home":
    st.markdown("""
        <div style="background-color: white; padding: 2rem; border-radius: 1.5rem; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05); max-width: 800px; margin: auto;">
            <h1 style="text-align: center; font-size: 2.5rem; color: #2c3e50;">👨‍💻 Muhammad Waheed</h1>
            <p style="text-align: center; font-size: 1.25rem; color: #7f8c8d; margin-top: -10px;">
                Accelerating AI innovation with modern, type-safe Python.
            </p>
            <hr style="margin: 2rem 0; border-top: 1px solid #ecf0f1;" />
            <p style="font-size: 1.1rem; line-height: 1.7; text-align: justify;">
                I’m an <strong>AI engineer</strong> in the Certified Agentic & Robotic AI Engineer program, focused on building robust intelligent systems using <strong>Modern Python</strong> — including <code>static typing</code>, <code>OOP</code>, and <code>async</code> features.
                <br/><br/>
                I leverage AI-assisted coding to build scalable, production-ready web apps and I’m passionate about pioneering solutions in the emerging field of <strong>Agentic AI</strong>.
                <br/><br/>
                This portfolio highlights my projects, skills, and learning journey as I continuously evolve in the world of intelligent systems.
            </p>
        </div>
    """, unsafe_allow_html=True)

# Skills Page
elif page == "Skills":
    st.markdown('<div class="page-title">🧠 Skills</div>', unsafe_allow_html=True)

    st.subheader("Programming Languages")
    st.write("Python, TypeScript")

    st.subheader("Tools & Libraries")
    st.write("""
    - Python (with type hints & mypy)  
    - Pandas & NumPy  
    - Streamlit  
    - asyncio (async/await)  
    - Git & GitHub   
    - Google Colab  
    """)

    st.subheader("Soft Skills")
    st.write("""
    - Problem Solving  
    - Debugging & Troubleshooting  
    - Clear Communication  
    - Collaboration & Teamwork  
    - Adaptability  
    - Time Management  
    - Critical Thinking  
    - Continuous Learning  
    """)

# Projects Page
elif page == "Projects":
    st.markdown('<div class="page-title">🚀 Projects</div>', unsafe_allow_html=True)

    st.subheader("Streamlit Web Apps")
    st.write("""
    - **StreamSweep** – Data cleaner & visualizer ([GitHub](https://github.com/muhammadwaheedairi/Data-Sweeper-App.git) / [Live](https://streamsweep.streamlit.app/))  
    - **Unit Converter Pro** – Conversion tool ([GitHub](https://github.com/muhammadwaheedairi/Unit-Converter.git) / [Live](https://unitconverterpro.streamlit.app/))  
    - **Secure Data Encryption System** – Encryption app ([GitHub](https://github.com/muhammadwaheedairi/Secure-Data-Encryption-System.git) / [Live](https://datalockr.streamlit.app/))  
    - **BMI Calculator** – ([Live](https://check-my-bmi.streamlit.app/))  
    """)

    st.subheader("CLI Tool")
    st.write("""
    - **Personal Library Manager** – ([PyPI](https://pypi.org/project/personal-library-manager/) / [GitHub](https://github.com/muhammadwaheedairi/personal-library-manager.git))  
    """)

    st.subheader("Practice Games (Google Colab)")
    st.markdown("""
    - [Mad Libs](https://colab.research.google.com/drive/1msz-mYt7oQ9dynzqHplM3VrcgDJd2Y3P?usp=drive_link)  
    - [Guess Number (Computer)](https://colab.research.google.com/drive/1mmk3Fh9Y103tII9WETJHAkKY3Twm9sEQ?usp=drive_link)  
    - [Guess Number (User)](https://colab.research.google.com/drive/1EE5ahLlDcuHh5nMVBbDJ5ereBskpVYtp?usp=drive_link)  
    - [Rock/Paper/Scissors](https://colab.research.google.com/drive/1oBFjzVQYcruLTwoEkGZmlSpvZ0p7kdpv?usp=drive_link)  
    - [Hangman](https://colab.research.google.com/drive/1q6qgXeEEsE52UlXv5TX4DLIYeNjYgNah?usp=drive_link)  
    - [Countdown Timer](https://colab.research.google.com/drive/1W5yOdz9lvTHTUTmGc4QAguQJMQg_ll4P?usp=drive_link)  
    - [Password Generator](https://colab.research.google.com/drive/1nPSY-kbE_l--aZaXEgV-_TfTdvXs5kPn?usp=drive_link)  
    """, unsafe_allow_html=True)

# Learning Journey Page
elif page == "Learning Journey":
    st.markdown('<div class="page-title">📘 Learning Journey</div>', unsafe_allow_html=True)
    st.write("""
    - **Why Python:** Its simplicity and rich AI ecosystem made it my go-to for prototyping intelligent systems.  
    - **Key Challenges:** Embracing static typing, async patterns, and solid OOP design.  
    - **Driven By:** Turning ideas into real tools and continuous learning.  
    - **Next Up:** Deepening ML/agentic AI skills, plus backend APIs and cloud deployment.  
    """)

# Contact Page
elif page == "Contact":
    st.markdown("""
        <div style="background-color: white; padding: 2rem 2.5rem; border-radius: 1.5rem; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05); max-width: 750px; margin: auto;">
            <h2 style="text-align: center; font-size: 2rem; color: #2c3e50;">📬 Get in Touch</h2>
            <p style="text-align: center; font-size: 1.1rem; color: #7f8c8d;">
                Feel free to reach out if you’d like to collaborate, have questions, or just want to connect!
            </p>
            <div style="margin-top: 2rem; display: flex; justify-content: center; gap: 2rem; flex-wrap: wrap;">
                <a href="mailto:muhammadwaheedairi@gmail.com" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #3498db; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 10px; font-size: 1rem; cursor: pointer;">
                        📧 Email
                    </button>
                </a>
                <a href="https://github.com/Muhammadwaheedairi" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #2c3e50; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 10px; font-size: 1rem; cursor: pointer;">
                        💻 GitHub
                    </button>
                </a>
                <a href="https://www.linkedin.com/in/muhammadwaheedairi/" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #0e76a8; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 10px; font-size: 1rem; cursor: pointer;">
                        🔗 LinkedIn
                    </button>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)
