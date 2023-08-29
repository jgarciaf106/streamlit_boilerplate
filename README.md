# Streamlit Boilerplate

[![GitHub stars](https://img.shields.io/github/stars/andresgarcia106/streamlit_boilerplate.svg?style=social&label=Star)](https://github.com/andresgarcia106/streamlit_boilerplate)
[![GitHub forks](https://img.shields.io/github/forks/andresgarcia106/streamlit_boilerplate.svg?style=social&label=Fork)](https://github.com/andresgarcia106/streamlit_boilerplate/fork)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![made-with-streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://docs.streamlit.io/)

A Streamlit boilerplate project for kickstarting your data-driven web applications. This project provides a basic structure and best practices to help you get started quickly with Streamlit.

## Features
- Multipage App 
- Create new views easily.

## Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/andresgarcia106/streamlit_boilerplate.git your-repo-name
cd your-repo-name
pipenv run init
```

## Development

### Create a new view
```bash
pipenv run view
```

This command will prompt for the view name and will create a view inside app/views/ with a boilerplate code and register the new view under the main app, just need to add your streamlit code inside the content function.

### Run the app
```bash
pipenv run start
```
This command will launch your application locally.

# Streamlit deployment
- Push changes to your github repository.
- When deploying in streamlit use main.py as entrypoint.
