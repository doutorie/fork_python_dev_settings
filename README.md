# VS Code Python Development Setup Guide

## 1. Initial Setup

### Install Required Software
```bash
# Python (if not installed)
# Download from python.org or use package manager

# VS Code
# Download from code.visualstudio.com

# Git (optional but recommended)
# Download from git-scm.com
```

## 2. Essential VS Code Extensions

### Core Python Extensions
```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "ms-python.pylint",
        "ms-python.flake8",
        "ms-python.black-formatter",
        "ms-python.isort",
        "ms-toolsai.jupyter",
        "njpwerner.autodocstring",
        "ms-python.mypy-type-checker",
        "charliermarsh.ruff",
        "ms-vscode.live-server",
        "ms-vscode.vscode-json"
    ]
}
```

### Install Extensions via Command Palette
```
Ctrl+Shift+P → Extensions: Install Extensions
```

Or install via command line:
```bash
# Core Python support
code --install-extension ms-python.python
code --install-extension ms-python.vscode-pylance

# Linting and formatting
code --install-extension ms-python.pylint
code --install-extension ms-python.flake8
code --install-extension ms-python.black-formatter
code --install-extension ms-python.isort
code --install-extension charliermarsh.ruff

# Documentation
code --install-extension njpwerner.autodocstring

# Type checking
code --install-extension ms-python.mypy-type-checker

# Jupyter support
code --install-extension ms-toolsai.jupyter
```

## 3. Virtual Environment Creation

### Method 1: Using venv (Recommended)
```bash
# Create virtual environment
python -m venv myproject_env

# Activate virtual environment
# Windows
myproject_env\Scripts\activate

# Linux/macOS
source myproject_env/bin/activate

# Verify activation
which python
python --version
```

### Method 2: Using conda
```bash
# Create environment
conda create -n myproject python=3.11

# Activate environment
conda activate myproject

# List environments
conda env list
```

### Method 3: VS Code Integrated
```bash
# Open VS Code in project folder
code .

# Ctrl+Shift+P → Python: Create Environment
# Select venv → Select Python interpreter
```

## 4. Essential Python Libraries

### Development Libraries
```bash
# Install in your activated virtual environment

# Core development tools
pip install --upgrade pip
pip install wheel setuptools

# Code formatting and linting
pip install black isort flake8 pylint mypy

# PEP 8 specific checker
pip install pycodestyle autopep8

# Advanced linter (faster alternative)
pip install ruff

# Documentation
pip install pydocstyle

# Testing
pip install pytest pytest-cov pytest-mock

# Type hints
pip install typing-extensions

# Environment management
pip install python-dotenv

# Common data science libraries
pip install pandas numpy matplotlib seaborn jupyter

# Web development
pip install fastapi uvicorn requests httpx

# Database
pip install sqlalchemy psycopg2-binary

# Async support
pip install asyncio aiofiles aiohttp
```

### Create requirements.txt
```bash
# Generate requirements file
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt
```

### Example requirements.txt
```txt
# PEP 8 and formatting
black==23.12.1
isort==5.13.2
flake8==7.0.0
pycodestyle==2.11.1
autopep8==2.0.4
pylint==3.0.3
mypy==1.8.0
ruff==0.1.9

# Testing
pytest==7.4.4
pytest-cov==4.1.0
pytest-mock==3.12.0

# Documentation
pydocstyle==6.3.0

# Type hints
typing-extensions==4.9.0

# Environment
python-dotenv==1.0.0

# Data science
pandas==2.1.4
numpy==1.26.3
matplotlib==3.8.2
seaborn==0.13.0

# Web
fastapi==0.108.0
uvicorn==0.25.0
requests==2.31.0
httpx==0.26.0

# Database
sqlalchemy==2.0.25
```

## 5. VS Code Settings Configuration

### settings.json
```json
{
    // Python interpreter
    "python.defaultInterpreterPath": "./venv/bin/python",
    
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
    "python.formatting.autopep8Args": ["--max-line-length", "88"],
    "python.sortImports.args": ["--profile", "black"],
    
    // Auto-format on save
    "editor.formatOnSave": true,
    "editor.formatOnType": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    },
    
    // Ruff (alternative to flake8/pylint)
    "ruff.lint.enable": true,
    "ruff.format.enable": true,
    
    // Docstring generation
    "autoDocstring.docstringFormat": "google",
    "autoDocstring.startOnNewLine": true,
    "autoDocstring.includeExtendedSummary": true,
    
    // Type checking
    "python.analysis.typeCheckingMode": "basic",
    "python.analysis.autoImportCompletions": true,
    
    // Jupyter
    "jupyter.askForKernelRestart": false,
    "jupyter.interactiveWindow.creationMode": "perFile",
    
    // Editor
    "editor.rulers": [88, 120],
    "editor.wordWrap": "on",
    "editor.minimap.enabled": true,
    "editor.bracketPairColorization.enabled": true,
    
    // File associations
    "files.associations": {
        "*.py": "python",
        ".env": "plaintext"
    },
    
    // Git
    "git.autofetch": true,
    "git.confirmSync": false
}
```

## 6. Workspace Settings

### .vscode/settings.json (Project-specific)
```json
{
    "python.defaultInterpreterPath": "./venv/bin/python",
    "python.terminal.activateEnvironment": true,
    "python.testing.pytestEnabled": true,
    "python.testing.pytestArgs": ["tests"],
    "python.testing.unittestEnabled": false,
    "python.testing.nosetestsEnabled": false,
    
    "files.exclude": {
        "**/__pycache__": true,
        "**/.pytest_cache": true,
        "**/.mypy_cache": true,
        "**/venv": true,
        "**/.venv": true
    }
}
```

### .vscode/launch.json (Debugging)
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": ["main:app", "--reload", "--port", "8000"],
            "console": "integratedTerminal",
            "justMyCode": true
        },
        {
            "name": "Python: Pytest",
            "type": "python",
            "request": "launch",
            "module": "pytest",
            "args": ["tests/"],
            "console": "integratedTerminal",
            "justMyCode": true
        }
    ]
}
```

## 7. Auto-Docstring Configuration

### Google Style Docstrings (Recommended)
```python
def example_function(param1: str, param2: int = 10) -> bool:
    """Summary line describing the function.
    
    Extended description of the function (optional).
    
    Args:
        param1: Description of param1.
        param2: Description of param2. Defaults to 10.
    
    Returns:
        Description of return value.
    
    Raises:
        ValueError: If param1 is empty.
        TypeError: If param2 is not an integer.
    
    Examples:
        >>> example_function("hello", 5)
        True
    """
    if not param1:
        raise ValueError("param1 cannot be empty")
    return len(param1) > param2
```

### Keyboard Shortcuts for Docstrings
```json
// keybindings.json
[
    {
        "key": "ctrl+shift+2",
        "command": "autoDocstring.generateDocstring",
        "when": "editorTextFocus && editorLangId == python"
    }
]
```

## 8. Code Quality Configuration Files

### .pycodestyle
```ini
[pycodestyle]
max-line-length = 88
ignore = E203, E501, W503
exclude = 
    .git,
    __pycache__,
    venv,
    .venv,
    build,
    dist,
    *.egg-info
```

### .flake8
```ini
[flake8]
max-line-length = 88
extend-ignore = E203, E501, W503
exclude = 
    .git,
    __pycache__,
    venv,
    .venv,
    build,
    dist,
    *.egg-info
```

### pyproject.toml (Modern Python configuration)
```toml
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

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["your_package_name"]

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

[tool.pylint.messages_control]
disable = [
    "C0103",  # invalid-name
    "C0114",  # missing-module-docstring
    "R0903",  # too-few-public-methods
]

[tool.pylint.format]
max-line-length = 88

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
"__init__.py" = ["F401"]  # ignore unused imports in __init__.py

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

## 9. Project Structure Template

```
my_project/
├── .vscode/
│   ├── settings.json
│   ├── launch.json
│   └── extensions.json
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   └── conftest.py
├── docs/
│   └── README.md
├── venv/
├── .env
├── .gitignore
├── .flake8
├── pyproject.toml
├── requirements.txt
└── README.md
```

## 10. Quick Setup Script

### setup_project.py
```python
#!/usr/bin/env python3
"""Quick project setup script."""

import os
import subprocess
import sys
from pathlib import Path

def create_venv():
    """Create virtual environment."""
    print("Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"], check=True)
    print("✓ Virtual environment created")

def install_packages():
    """Install required packages."""
    print("Installing packages...")
    
    # Determine pip path
    if os.name == 'nt':  # Windows
        pip_path = "venv\\Scripts\\pip.exe"
    else:  # Unix/Linux/macOS
        pip_path = "venv/bin/pip"
    
    packages = [
        "black", "isort", "flake8", "pylint", "mypy", "ruff",
        "pycodestyle", "autopep8",
        "pytest", "pytest-cov", "pytest-mock",
        "pydocstyle", "typing-extensions", "python-dotenv"
    ]
    
    subprocess.run([pip_path, "install", "--upgrade", "pip"], check=True)
    subprocess.run([pip_path, "install"] + packages, check=True)
    print("✓ Packages installed")

def create_structure():
    """Create project structure."""
    print("Creating project structure...")
    
    dirs = ["src", "tests", "docs", ".vscode"]
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
    
    # Create __init__.py files
    (Path("src") / "__init__.py").touch()
    (Path("tests") / "__init__.py").touch()
    
    print("✓ Project structure created")

def create_config_files():
    """Create configuration files."""
    print("Creating configuration files...")
    
    # .gitignore
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
.venv/
env/
ENV/

# IDE
.vscode/settings.json
.idea/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/

# MyPy
.mypy_cache/
.dmypy.json
dmypy.json

# Environment variables
.env
.env.local
.env.*.local

# OS
.DS_Store
Thumbs.db
""".strip()
    
    with open(".gitignore", "w") as f:
        f.write(gitignore_content)
    
    print("✓ Configuration files created")

if __name__ == "__main__":
    print("Setting up Python project...")
    create_venv()
    install_packages()
    create_structure()
    create_config_files()
    print("\n🎉 Project setup complete!")
    print("\nNext steps:")
    print("1. Activate virtual environment:")
    if os.name == 'nt':
        print("   venv\\Scripts\\activate")
    else:
        print("   source venv/bin/activate")
    print("2. Install VS Code extensions")
    print("3. Open VS Code: code .")
```

## 11. Usage Instructions

### Step-by-Step Setup
1. **Create project folder**
   ```bash
   mkdir my_project && cd my_project
   ```

2. **Run setup script**
   ```bash
   python setup_project.py
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/macOS
   source venv/bin/activate
   ```

4. **Open VS Code**
   ```bash
   code .
   ```

5. **Install extensions** (use the extensions.json file)

6. **Select Python interpreter** (Ctrl+Shift+P → Python: Select Interpreter)

### Testing Auto-Docstring
```python
def test_function(name: str, age: int = 25) -> str:
    # Place cursor after the function definition
    # Press Ctrl+Shift+2 (or your configured shortcut)
    # Docstring will be auto-generated!
    pass
```

## 12. Keyboard Shortcuts Summary

| Shortcut | Action |
|----------|--------|
| `Ctrl+Shift+P` | Command Palette |
| `Ctrl+Shift+2` | Generate Docstring |
| `Shift+Alt+F` | Format Document |
| `Ctrl+K Ctrl+F` | Format Selection |
| `F12` | Go to Definition |
| `Shift+F12` | Go to References |
| `Ctrl+.` | Quick Fix |
| `F5` | Start Debugging |
| `Ctrl+F5` | Run Without Debugging |
| `Ctrl+Shift+\`` | New Terminal |

This setup provides a complete professional Python development environment with automatic formatting, linting, type checking, and documentation generation!