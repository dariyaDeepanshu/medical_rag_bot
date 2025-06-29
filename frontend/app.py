import streamlit as st
import requests

st.set_page_config(page_title="🧠 Medical RAG Bot", layout="wide")
st.title("🧠 Medical Q&A Bot")
st.caption("Built with WHO, CDC, and India Dengue Guidelines")

st.markdown("""
<style>
.chat-container {
    padding: 20px;
    border-radius: 12px;
    background-color: #f9f9f9;
    margin-top: 10px;
    margin-bottom: 20px;
    box-shadow: 0 0 8px rgba(0, 0, 0, 0.08);
}
.answer-box {
    background-color: #f0f8ff;
    border-left: 6px solid #007ACC;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
}
.source-box {
    font-size: 0.9em;
    color: #555;
    padding: 10px;
    background-color: #fafafa;
    border: 1px dashed #ccc;
    margin-top: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

query = st.text_input("💬 Ask your medical question:")

if st.button("Ask"):
    if not query.strip():
        st.warning("❗ Please enter a valid question.")
    else:
        with st.spinner("🧠 Thinking..."):
            try:
                response = requests.post(
                    "http://localhost:8000/query", json={"query": query})
                if response.status_code == 200:
                    data = response.json()
                    st.markdown('<div class="answer-box">',
                                unsafe_allow_html=True)
                    st.markdown(f"**🧾 Answer:**  \n{data['answer']}")
                    st.markdown('</div>', unsafe_allow_html=True)

                    if data.get("sources"):
                        st.markdown("### 📚 Source References")
                        for i, src in enumerate(data["sources"], 1):
                            st.markdown(
                                f'<div class="source-box">🔹 **Source {i}:** {src}</div>', unsafe_allow_html=True)
                    else:
                        st.info("No source documents found.")

                else:
                    st.error("❌ API returned an error.")

            except Exception as e:
                st.error(f"❌ Connection error: {e}")
