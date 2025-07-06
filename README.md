 Open source, github hosted, pure Python package template


![Build Status](https://github.com/StephenGemin/template-python-package/workflows/Build/badge.svg)


## Quickstart
* Requires [`uv`](https://docs.astral.sh/uv/) if initializing new repo
```bash
pipx install cookiecutter
cookiecutter git@github.com:StephenGemin/template-python-package.git
# OR
cookiecutter https://github.com/StephenGemin/template-python-package.git
```
* create remote repo
* `git remote add origin git@github.com/StephenGemin/example_python_project.git`
* `git push -u origin`
* If publishing, add PyPI secrets

## Contributing
First, setup development environment with the following commands:
```bash
uv venv && uv pip sync requirements.txt && uv run pre-commit install
```
