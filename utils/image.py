import subprocess

# run docker image

try:
    # ask for image name
    image_name = input("Enter image name: ")
    
    subprocess.run(["docker", "run", "-p", "8501:8501", f"{image_name}"])
except Exception as e:
    print(e)
    exit(1)
    