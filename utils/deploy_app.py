import webbrowser
import configparser

def streamlit_deploy():
    # load the config file
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    # check if deploy section exists
    if 'deploy' in config:
        # get the deploy section
        deploy = config['deploy']
        
        # Check if the required values exist in the configuration file
        if 'repo_user' not in deploy:
            print("Error: 'repo_user' is missing in config.ini")
        if 'repo_name' not in deploy:
            print("Error: 'repo_name' is missing in config.ini")
        if 'repo_branch' not in deploy:
            print("Error: 'repo_branch' is missing in config.ini")
        if 'entry_point' not in deploy:
            print("Error: 'entry_point' is missing in config.ini")
        else:
            # build the url
            url = f"https://share.streamlit.io/deploy?repository={deploy['repo_user']}%2F{deploy['repo_name']}&branch={deploy['repo_branch']}&"\
                  f"mainModule={deploy['entry_point']}"
        
    webbrowser.open(url)

if __name__ == "__main__":
    streamlit_deploy()
