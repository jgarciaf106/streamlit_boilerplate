import json
import os
import configparser
import subprocess


try:
    # generate requirements.txt
    
    # generate pipenv_graph.json
    os.system('pipenv graph --json > pipenv_graph.json')

    # Load the Pipfile
    config = configparser.ConfigParser()
    config.read('Pipfile')

    # Check if [packages] section exists
    if 'packages' in config:
        # Get the packages listed under [packages]
        packages = config['packages']

        # Extract package names
        required_packages = [key for key in packages.keys() if key != 'pipfile']
    else:
        print("No [packages] section found in Pipfile")

    with open('pipenv_graph.json', 'r') as file:
        data = json.load(file)

    main_packages = set()

    for entry in data:
        # Check if the entry has a 'package' key and 'package_name' inside it.
        if 'package' in entry and 'package_name' in entry['package']:
            package_name = entry['package']['package_name']
            version = entry['package'].get('installed_version')  # Get the version if available
            
            # Check if this package is in the required_packages set
            if package_name in required_packages:
                if version:
                    package_name = f"{package_name}=={version}"
                main_packages.add(package_name)
                
    with open('requirements.txt', 'w') as file:
        for package in main_packages:
            file.write(f"{package}\n")
            
    # run docker build
    
    # check if Dockerfile exists
    if os.path.isfile("Dockerfile"):
        # ask for image name
        image_name = input("Enter image name: ")
        
        # ask for image tag
        image_tag = input("Enter image tag: ")
        
        # check if image name and tag are provided
        if image_name and image_tag:
            subprocess.run(["docker", "build", "-f", "Dockerfile", "-t", f"{image_name}:{image_tag}", "."])
        else:
            print("Error: Image name and tag are required")
            exit(1)
    else:
        print("Error: Dockerfile not found")
        exit(1)
    
    # delete requirements.txt and pipenv_graph.json    
    os.remove("requirements.txt")
    os.remove("pipenv_graph.json")
    
except subprocess.CalledProcessError:
    print("Error: Docker build failed")
    exit(1)

    

