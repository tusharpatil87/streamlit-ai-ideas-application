import streamlit as st
from utils.topic_suggester import suggest_topics

def main():
    st.title("Generative AI Topic Suggester")
    
    st.header("Select a Subject Area")
    subject_area = st.selectbox("Choose a subject area:", ["Technology", "Healthcare", "Education", "Finance", "Art", "Science"])
    
    if st.button("Suggest Topics"):
        topics = suggest_topics(str.lower(subject_area))
        if topics:
            st.subheader("Suggested Topics:")
            for topic in topics:
                st.write(f"- {topic}")
        else:
            st.write("No topics found for the selected subject area.")

if __name__ == "__main__":
    main()