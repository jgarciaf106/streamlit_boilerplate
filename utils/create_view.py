import os
import ast
import astor
import textwrap
import subprocess

# Ask for the view name
view_name = input("Enter the view name: ")
icon_name = input("Enter the boostrap icon name: ")


def create_view():
    file_content = f"""
import streamlit as st
from app.utils.page import Page

# define the content of the view inside the content function
def content():
    st.write("This is the content of the page.")

# create a view object and pass the content function
render = Page("{(view_name.capitalize())} Page", content)
"""

    # Strip the initial indentation
    stripped_content = textwrap.dedent(file_content)

    # Write the content to the new Python file with the correct indentation
    with open(f"./app/views/{view_name}.py", "w") as file:
        file.write(stripped_content)


def parse_view():
    with open("./main.py", "r") as file:
        main_code = file.read()

        # Parse the Python code and extract the syntax tree
        parsed_tree = ast.parse(main_code)

        # Find the assignment statement for the 'view' variable
        for node in parsed_tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id == "views":
                        # Assuming view is a list of dictionaries
                        new_dict = {
                            "title": f"{(view_name.capitalize())}",
                            "function": f"{(view_name)}.render",
                            "args": None,
                            "icon": f"{icon_name}",
                        }

                        # Create a new dictionary node
                        new_dict_node = ast.Dict(
                            keys=[ast.Str(s=key) for key in new_dict.keys()],
                            values=[
                                ast.Str(s=str(value)) for value in new_dict.values()
                            ],
                        )

                        # Insert the new dictionary before the last dictionary in the list
                        node.value.elts.insert(-1, new_dict_node)

        # Convert the updated AST back to a string
        updated_code = astor.to_source(parsed_tree)

        # Write the updated content back to the main.py file
        with open("./main.py", "w") as file:
            file.write(updated_code)


def register_view():
    # Read the content of main.py
    with open("./main.py", "r") as file:
        lines = file.readlines()

    # Find the line "from app.views import" and append the view name separated by a comma
    for i, line in enumerate(lines):
        if "from app.views import" in line:
            lines[i] = line.replace("\n", f", {view_name}\n")

    # Write the updated content back to main.py
    with open("./main.py", "w") as file:
        file.writelines(lines)

    parse_view()

    print("*" * 50)
    print(f"View '{view_name}' created and registered successfully.")
    print("*" * 50)


def autoformat_with_black(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                subprocess.run(["black", filepath])


# Specify the directory to start formatting from
starting_directory = "./path_to_your_directory"

if __name__ == "__main__":
    create_view()
    register_view()
    autoformat_with_black("./")
