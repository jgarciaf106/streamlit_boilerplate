import os
import textwrap

# Ask for the view name
view_name = input("Enter the view name: ")

def create_view():
    file_content = f'''
import streamlit as st
from app.utils.page import Page

# define the content of the view inside the content function
def content():
    st.write("This is the content of the page.")

# create a view object and pass the content function
render = Page("{(view_name.capitalize())} Page", content)
'''

    # Strip the initial indentation
    stripped_content = textwrap.dedent(file_content)

    # Write the content to the new Python file with the correct indentation
    with open(f"./app/views/{view_name}.py", 'w') as file:
        file.write(stripped_content)

def register_view():
    # Read the content of main.py
    with open("./main.py", 'r') as file:
        lines = file.readlines()

    # Find the line "from app.views import" and append the view name separated by a comma
    for i, line in enumerate(lines):
        if "from app.views import" in line:
            lines[i] = line.replace("\n", f", {view_name}\n")

    # Find the last line that starts with "view.add_view" and register the view
    for i, line in enumerate(reversed(lines)):
        if line.startswith("view.add_view"):
            lines[len(lines) - i - 1] = line.replace("\n", f"\nview.add_view('{view_name.capitalize()}', {view_name}.render)\n")
            break

    # Write the updated content back to main.py
    with open("./main.py", 'w') as file:
        file.writelines(lines)
    
    print("*" * 50)
    print(f"View '{view_name}' created and registered successfully.")
    print("*" * 50)
    

if __name__ == "__main__":
    create_view()
    register_view()