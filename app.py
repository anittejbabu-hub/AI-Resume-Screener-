import streamlit as st
from model import calculate_similarity

st.set_page_config(page_title="AI Resume Screener", page_icon="🤖")

st.title("🤖 AI Resume Screening System")
st.markdown("Compare Resume with Job Description using AI")

job_desc = st.text_area("📄 Job Description", height=200)
resume = st.text_area("📄 Resume Text", height=200)

if st.button("🔍 Check Match"):
    if job_desc.strip() != "" and resume.strip() != "":
        score = calculate_similarity(job_desc, resume)

        st.subheader("Result:")
        st.success(f"Similarity Score: {score}%")

        if score > 75:
            st.write("✅ Strong Match")
        elif score > 50:
            st.write("⚡ Moderate Match")
        else:
            st.write("❌ Low Match")

    else:
        st.warning("Please fill both fields before checking.")