from granite_client import generate_response

prompt = """
Job Role: AI Engineer

Experience: Fresher

Skills:
Python
Machine Learning
SQL

Generate 3 interview questions.
"""

print(generate_response(prompt))