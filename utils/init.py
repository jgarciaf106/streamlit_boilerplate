import subprocess
import configparser

# Update the .gitignore file to ignore the utils folder
with open(".gitignore", "a") as gitignore:
    gitignore.write("\n# Ignore utils folder\nutils/")
print("utils/ folder has been added to .gitignore.")

# Define the configuration details
config_data = {
    "deploy": {
        "repo_user": "github_username",
        "repo_name": "github_repository_name",
        "repo_branch": "deploying_branch",
        "entry_point": ".py_file_entry_point",
    }
}

# Run pipenv install
try:
    subprocess.run(["pipenv", "install"])
except subprocess.CalledProcessError:
    print("Error: pipenv install command failed.")
    exit(1)

# Create and write the config.ini file
config = configparser.ConfigParser()
config.read_dict(config_data)

with open("config.ini", "w") as configfile:
    config.write(configfile)

print("Configuration file 'config.ini' has been created.")

# create .streamlit folder and  streamlite files
try:
    subprocess.run(["mkdir", ".streamlit"])
    # create config.toml file
    with open(".streamlit/config.toml", "w") as configfile:
        configfile.write(
            """[theme]
                base="dark"
                primaryColor="#F63366"
                backgroundColor="#FFFFFF"
                secondaryBackgroundColor="#F0F2F6"
                textColor="#262730"
                font="sans serif"
            """)
        
    print("Configuration file '.streamlit/config.toml' has been created.")

    # create .streamlit/secrets.toml file
    with open(".streamlit/secrets.toml", "w") as configfile:
        configfile.write('jwt_key = "123456"')

    print("Configuration file '.streamlit/secrets.toml' has been created.")
        
except subprocess.CalledProcessError:
    print("Error: mkdir .streamlit command failed.")
    exit(1)
    
