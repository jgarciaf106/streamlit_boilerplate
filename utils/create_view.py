import os

# Ask for the view name
view_name = input("Enter the view name: ")

# Generate the Python file name
file_name = f"{view_name}.py"

# Define the content of the Python file
file_content = f'''import streamlit as st
from app.utils.page import Page

# define the content of the view inside the content function
def content():
    st.write("This is the content of the page.")

# create a view object and pass the content function
render = Page("{view_name} Page", content)
'''

# Write the content to the new Python file
with open(f"./app/views/{file_name}", 'w') as file:
    file.write(file_content)

print("\n*******************************************")
print(f"\nView created at: ./app/views/{file_name}")
print("\nRemember to register the view in main.py by:")
print(f"\n - Importing the view with: from app.views import {view_name}")
print(f"\n - Adding it to the view object with: view.add_view('{view_name}', {view_name}.render)")
print("\n*******************************************\n")
