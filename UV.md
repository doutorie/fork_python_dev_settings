# VS Code Python Setup: UV


## ⚡ UV Version (Astral-sh)

### 1. UV Installation

```bash
# Install UV (Linux/macOS)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Via pip
pip install uv

# Via homebrew (macOS)
brew install uv

# Verify installation
uv --version
```

### 2. UV Project Setup

```bash
# Create new project
uv init my_project
cd my_project

# Initialize in existing directory
mkdir my_project && cd my_project
uv init
```

### 3. UV pyproject.toml Configuration

```toml
[project]
name = "my_project"
version = "0.1.0"
description = "My awesome Python project with UV"
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
readme = "README.md"
license = {text = "MIT"}
requires-python = ">=3.9"
keywords = ["python", "project"]
classifiers = [
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

dependencies = [
    "fastapi>=0.108.0",
    "uvicorn>=0.25.0",
    "pandas>=2.1.0",
    "numpy>=1.26.0",
    "requests>=2.31.0",
    "python-dotenv>=1.0.0",
]

[project.optional-dependencies]
dev = [
    "black>=23.12.0",
    "isort>=5.13.0",
    "flake8>=7.0.0",
    "pylint>=3.0.0",
    "mypy>=1.8.0",
    "ruff>=0.1.9",
    "pycodestyle>=2.11.0",
    "autopep8>=2.0.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "pytest-mock>=3.12.0",
    "pydocstyle>=6.3.0",
    "typing-extensions>=4.9.0",
]

jupyter = [
    "jupyter>=1.0.0",
    "ipykernel>=6.27.0",
    "matplotlib>=3.8.0",
    "seaborn>=0.13.0",
]

[project.urls]
Homepage = "https://github.com/yourusername/my_project"
Repository = "https://github.com/yourusername/my_project"
Documentation = "https://my_project.readthedocs.io"
Issues = "https://github.com/yourusername/my_project/issues"

[project.scripts]
my-project = "my_project.main:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

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

# UV specific configuration
[tool.uv]
dev-dependencies = [
    "black>=23.12.0",
    "isort>=5.13.0",
    "ruff>=0.1.9",
    "mypy>=1.8.0",
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
]
```

### 4. UV Commands

```bash
# Create virtual environment and install dependencies
uv sync

# Install dependencies only
uv pip install -r pyproject.toml

# Add new dependency
uv add requests
uv add pytest --dev
uv add "fastapi>=0.100.0"

# Remove dependency
uv remove requests

# Update dependencies
uv lock --upgrade
uv sync

# Install from lock file
uv sync --frozen

# Run commands
uv run python main.py
uv run pytest
uv run black .
uv run mypy src/

# Install development dependencies
uv sync --group dev

# Install specific groups
uv sync --extra jupyter

# Show installed packages
uv pip list

# Create lock file
uv lock

# Export requirements
uv export --format requirements-txt --output-file requirements.txt
uv export --format requirements-txt --extra dev --output-file requirements-dev.txt

# Activate virtual environment
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Or use uv shell (if available)
uv shell
```

### 5. VS Code Settings for UV

```json
{
    // Python interpreter (UV creates .venv in project root)
    "python.defaultInterpreterPath": "./.venv/bin/python",
    "python.terminal.activateEnvironment": true,
    
    // UV integration
    "python.packageManager": "uv",
    
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
    
    // Ruff (UV's recommended linter)
    "ruff.lint.enable": true,
    "ruff.format.enable": true,
    "ruff.showNotifications": "always",
    
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
        "**/.venv": true,
        "**/uv.lock": false  # Show UV lock file
    }
}
```

## 🚀 Quick Setup Scripts

### UV Setup Script

```python
#!/usr/bin/env python3
"""UV project setup script."""

import subprocess
import sys
from pathlib import Path

def setup_uv_project():
    """Setup UV project with all configurations."""
    print("⚡ Setting up UV project...")
    
    # Initialize UV project
    subprocess.run(["uv", "init"], check=True)
    
    # Add development dependencies
    dev_deps = [
        "black>=23.12.0", "isort>=5.13.0", "ruff>=0.1.9", 
        "mypy>=1.8.0", "pytest>=7.4.0", "pytest-cov>=4.1.0"
    ]
    
    for dep in dev_deps:
        subprocess.run(["uv", "add", "--dev", dep], check=True)
    
    # Sync dependencies
    subprocess.run(["uv", "sync"], check=True)
    
    # Create project structure
    create_project_structure()
    
    print("✅ UV project setup complete!")
    print("Run: source .venv/bin/activate")

def create_project_structure():
    """Create basic project structure."""
    dirs = ["src", "tests", "docs"]
    for dir_name in dirs:
        Path(dir_name).mkdir(exist_ok=True)
    
    (Path("src") / "__init__.py").touch()
    (Path("tests") / "__init__.py").touch()

if __name__ == "__main__":
    setup_uv_project()
```

