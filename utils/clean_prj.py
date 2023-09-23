import os
import shutil

# home directory
home_directory = os.path.expanduser("~")

# remove all Pipenv virtual environments
pipenv_envs_directory = os.path.join(home_directory, ".local/share/virtualenvs")

if os.path.exists(pipenv_envs_directory) and os.path.isdir(pipenv_envs_directory):
    virtual_envs = [
        d
        for d in os.listdir(pipenv_envs_directory)
        if os.path.isdir(os.path.join(pipenv_envs_directory, d))
    ]

    if virtual_envs:
        print("Removing Pipenv virtual environments:")
        for env in virtual_envs:
            env_path = os.path.join(pipenv_envs_directory, env)
            try:
                shutil.rmtree(env_path)
                print(f"  - {env}")
            except Exception as e:
                print(f"  - Failed to remove {env}: {e}")
        print("All Pipenv virtual environments have been removed.")
    else:
        print("No Pipenv virtual environments found.")
else:
    print("Pipenv virtual environments directory not found.")

# remove Pipfile.lock file from root directory
os.remove("Pipfile.lock")
