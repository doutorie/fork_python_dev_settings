# VS Code Python Setup: Poetry

## 📚 Poetry Version

### 1. Poetry Installation

```bash
# Install Poetry (Linux/macOS/WSL)
curl -sSL https://install.python-poetry.org | python3 -

# Windows PowerShell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -

# Alternative: via pip (not recommended but works)
pip install poetry

# Verify installation
poetry --version
```

### 2. Poetry Configuration

```bash
# Configure Poetry to create venv in project directory
poetry config virtualenvs.in-project true

# Show current configuration
poetry config --list

# Set Python version preference
poetry config virtualenvs.prefer-active-python true
```

### 3. Project Setup with Poetry

```bash
# Create new project
poetry new my_project
cd my_project

# Or initialize in existing directory
mkdir my_project && cd my_project
poetry init
```

### 4. Poetry pyproject.toml Configuration

```toml
[tool.poetry]
name = "my_project"
version = "0.1.0"
description = "My awesome Python project"
authors = ["Your Name <your.email@example.com>"]
readme = "README.md"
packages = [{include = "my_project", from = "src"}]

[tool.poetry.dependencies]
python = "^3.9"
fastapi = "^0.108.0"
uvicorn = "^0.25.0"
pandas = "^2.1.0"
numpy = "^1.26.0"
requests = "^2.31.0"
python-dotenv = "^1.0.0"

[tool.poetry.group.dev.dependencies]
black = "^23.12.0"
isort = "^5.13.0"
flake8 = "^7.0.0"
pylint = "^3.0.0"
mypy = "^1.8.0"
ruff = "^0.1.9"
pycodestyle = "^2.11.0"
autopep8 = "^2.0.0"
pytest = "^7.4.0"
pytest-cov = "^4.1.0"
pytest-mock = "^3.12.0"
pydocstyle = "^6.3.0"
typing-extensions = "^4.9.0"

[tool.poetry.group.jupyter.dependencies]
jupyter = "^1.0.0"
ipykernel = "^6.27.0"
matplotlib = "^3.8.0"
seaborn = "^0.13.0"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

# Black configuration
[tool.black]
line-length = 88
target-version = ['py39']
include = '\.pyi?$'
exclude = '''
/(
    \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | _build
  | buck-out
  | build
  | dist
)/
'''

# isort configuration
[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["my_project"]

# MyPy configuration
[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
show_error_codes = true

# Pylint configuration
[tool.pylint.messages_control]
disable = [
    "C0103",  # invalid-name
    "C0114",  # missing-module-docstring
    "R0903",  # too-few-public-methods
]

[tool.pylint.format]
max-line-length = 88

# Ruff configuration
[tool.ruff]
line-length = 88
target-version = "py39"
select = [
    "E",   # pycodestyle errors
    "W",   # pycodestyle warnings
    "F",   # pyflakes
    "I",   # isort
    "B",   # flake8-bugbear
    "C4",  # flake8-comprehensions
    "UP",  # pyupgrade
]
ignore = [
    "E501",  # line too long, handled by black
    "B008",  # do not perform function calls in argument defaults
]

[tool.ruff.per-file-ignores]
"__init__.py" = ["F401"]

# Pytest configuration
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--cov=src",
    "--cov-report=html",
    "--cov-report=term-missing",
]
```

### 5. Poetry Commands

```bash
# Install dependencies
poetry install

# Install only production dependencies
poetry install --only=main

# Install development dependencies
poetry install --with=dev

# Add new dependency
poetry add requests
poetry add pytest --group=dev
poetry add jupyter --group=jupyter

# Remove dependency
poetry remove requests

# Update dependencies
poetry update

# Show installed packages
poetry show

# Show dependency tree
poetry show --tree

# Activate virtual environment
poetry shell

# Run commands in virtual environment
poetry run python main.py
poetry run pytest
poetry run black .
poetry run mypy src/

# Export requirements.txt (if needed)
poetry export -f requirements.txt --output requirements.txt
poetry export -f requirements.txt --dev --output requirements-dev.txt
```

### 6. VS Code Settings for Poetry

```json
{
    // Python interpreter (Poetry automatically creates venv in .venv/)
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "python.terminal.activateEnvironment": true,
    
    // Poetry integration
    "python.poetryPath": "poetry",
    
    // Linting
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.linting.flake8Enabled": true,
    "python.linting.pycodestyleEnabled": true,
    "python.linting.mypyEnabled": true,
    "python.linting.lintOnSave": true,
    
    // Formatting
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--line-length", "88"],
    "python.sortImports.args": ["--profile", "black"],
    
    // Auto-format on save
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    
    // Ruff
    "ruff.lint.enable": true,
    "ruff.format.enable": true,
    
    // Docstring generation
    "autoDocstring.docstringFormat": "google",
    "autoDocstring.startOnNewLine": true,
    
    // Testing
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    
    // Files to exclude
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true,
        "**/.mypy_cache": true,
        "**/.venv": true
    }
}
```

---


## 🚀 Quick Setup Scripts

### Poetry Setup Script

```python
#!/usr/bin/env python3
"""Poetry project setup script."""

import subprocess
import sys
from pathlib import Path

def setup_poetry_project():
    """Setup Poetry project with all configurations."""
    print("🎭 Setting up Poetry project...")
    
    # Initialize Poetry project
    subprocess.run(["poetry", "init", "--no-interaction"], check=True)
    
    # Configure Poetry
    subprocess.run(["poetry", "config", "virtualenvs.in-project", "true"], check=True)
    
    # Add development dependencies
    dev_deps = [
        "black", "isort", "flake8", "pylint", "mypy", "ruff",
        "pytest", "pytest-cov", "pytest-mock", "pydocstyle"
    ]
    
    for dep in dev_deps:
        subprocess.run(["poetry", "add", "--group", "dev", dep], check=True)
    
    # Install dependencies
    subprocess.run(["poetry", "install"], check=True)
    
    # Create project structure
    create_project_structure()
    
    print("✅ Poetry project setup complete!")
    print("Run: poetry shell")

def create_project_structure():
    """Create basic project structure."""
    dirs = ["src", "tests", "docs"]
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
    
    (Path("src") / "__init__.py").touch()
    (Path("tests") / "__init__.py").touch()

if __name__ == "__main__":
    setup_poetry_project()
```

