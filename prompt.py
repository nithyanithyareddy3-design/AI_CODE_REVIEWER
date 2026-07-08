from langchain_core.prompts import PromptTemplate
review_prompt=PromptTemplat(
    input_variable=["language","review_type","code"],
    template="""
    You are a senior software Engineer,
    review this {language} code
    review Type: {review_type}
    provide:
1. Summary
2. syntax Errors
3. Logic Errors
4. Performance improvements
5. Security Issues 
6. Best Practices
7. Improved Code
8. Explanation
Code:
'''{language}
{code}
'''
Return Markdown

""")