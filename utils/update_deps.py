import json
import os
import configparser

# generate pipenv_graph.json
os.system("pipenv graph --json > pipenv_graph.json")

# Load the Pipfile
config = configparser.ConfigParser()
config.read("Pipfile")

# Check if [packages] section exists
if "packages" in config:
    # Get the packages listed under [packages]
    packages = config["packages"]

    # Extract package names
    required_packages = [key for key in packages.keys() if key != "pipfile"]
else:
    print("No [packages] section found in Pipfile")


with open("pipenv_graph.json", "r") as file:
    data = json.load(file)

main_packages = set()

for entry in data:
    # Check if the entry has a 'package' key and 'package_name' inside it.
    if "package" in entry and "package_name" in entry["package"]:
        package_name = entry["package"]["package_name"]
        version = entry["package"].get(
            "installed_version"
        )  # Get the version if available

        # Check if this package is in the required_packages set
        if package_name in required_packages:
            if version:
                package_name = f"{package_name}=={version}"
            main_packages.add(package_name)

with open("requirements.txt", "w") as file:
    for package in main_packages:
        file.write(f"{package}\n")

# Remove the temporary pipenv_graph.json file.
os.remove("pipenv_graph.json")

# install updated dependencies
os.system("pipenv install -r requirements.txt")

# remove requirements.txt
os.remove("requirements.txt")
