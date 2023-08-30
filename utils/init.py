import subprocess
import configparser

# Define the configuration details
config_data = {
    'deploy': {
        'repo_user': 'github_username',
        'repo_name': 'github_repository_name',
        'repo_branch': 'deploying_branch',
        'entry_point': '.py_file_entry_point',
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

with open('config.ini', 'w') as configfile:
    config.write(configfile)

print("Configuration file 'config.ini' has been created.")