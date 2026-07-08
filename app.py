import streamlit as st

try:
    from code_reviewer import review_code
except ModuleNotFoundError:
    def review_code(code):
        return (
            "Error: 'code_reviewer.py' was not found.\n\n"
            "Create a file named 'code_reviewer.py' in the project folder "
            "and define a function:\n\n"
            "def review_code(code):\n"
            "    return 'Your review here'"
        )

st.title("AI Code Reviewer")

code = st.text_area("Paste your code here")

if st.button("Review Code"):
    if code.strip():
        st.write(review_code(code))
    else:
        st.warning("Please enter some code.")