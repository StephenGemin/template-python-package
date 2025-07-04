import subprocess


def initialize():
    """Initialize repo"""
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "-A", "."], check=True)
    subprocess.run(["git","commit","-m","commit template"], check=True)


if __name__ == "__main__":
    if "{{ cookiecutter.initilize_git_repo }}" in ["y", "Y"]:
        initialize()
