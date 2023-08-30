# Streamlit Boilerplate

[![GitHub stars](https://img.shields.io/github/stars/andresgarcia106/streamlit_boilerplate.svg?style=social&label=Star)](https://github.com/andresgarcia106/streamlit_boilerplate)
[![GitHub forks](https://img.shields.io/github/forks/andresgarcia106/streamlit_boilerplate.svg?style=social&label=Fork)](https://github.com/andresgarcia106/streamlit_boilerplate/fork)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://docs.streamlit.io/)

A Streamlit boilerplate project for kickstarting your data-driven web applications. This project provides a basic structure and best practices to help you get started quickly with Streamlit.

## Features
- Multipage App 
- Create new views easily.
- Pipenv commands:
    - init: initialize your app project
    - view: create and register new views on the app.
    - start: launch locally your app.
    - deploy: launch streamlit portal with the app details for easy app deployment.
    - deps: keep your app depencies always up to date.
    - clean: troubleshooting and virtual env reset.    

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/andresgarcia106/streamlit_boilerplate.git your-app-name &&
cd your-app-name && 
pipenv run init
```

## Development

### Create a new view
```bash
pipenv run view
```

This command will prompt for the view name and will create a view inside app/views/ with a boilerplate code and register the new view under the main app, just need to add your streamlit code inside the content function.

## Testing
```bash
pipenv run start
```
This command will launch your application locally, so you can test your application.

## Deployment
- Push changes to your github repository.

```bash
pipenv run deploy
```

This command will launch streamlit deploy page with the required details to start deploying your app.
Make sure you update the config.ini in your root directory with the following details.

```ini
[deploy]
repo_user=github_username
repo_name=github_repository_name
repo_branch=deploying_brach
entry_point=.py_file_entry_point
```

#### Streamlit Config

For custom settings deployment, update the config.toml file in the directory .streamlit.
For additional details review the Streamlit documentation.
[![made-with-streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://docs.streamlit.io/library/advanced-features/configuration)


Notes:
- You might get prompt to login into streamlit cloud and authorization prompts from github.
- You'll need to manually update the "App URL (Optional)" with your app url name.

## Troubleshooting

```bash
pipenv run clean
```
This command will remove the virtual enviroment and the Pipfile.lock and will serve as troubleshooting if you encounter any issues in your app.
