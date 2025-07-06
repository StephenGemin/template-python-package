import subprocess
import shutil


def initialize():
    """Initialize repo"""
    if not shutil.which("uv"):
        raise FileNotFoundError("Must install uv to initialize repository")
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["uv", "sync"], check=True)
    subprocess.run(["git", "add", "-A", "."], check=True)
    subprocess.run(["git", "commit", "-m", "commit template"], check=True)
    subprocess.run(["uv", "run", "pre-commit", "install"], check=True)


if __name__ == "__main__":
    if "{{ cookiecutter.initilize_git_repo }}" in ["y", "Y"]:
        initialize()
