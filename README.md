# VS Code Python Development Setup Guide

## VS Code Extensions

```json
{
    "mandatory": [
        "ms-python.python",
        "charliermarsh.ruff",
        "njpwerner.autodocstring",
        "psioniq.psi-header"
    ],
    "git": [
        "waderyan.gitblame",
        "mhutchie.git-graph",
        "donjayamanne.githistory",
        "github.vscode-pull-request-github"
    ]
}
```

## Project Structure

```
project_name/
│
├── src/                    # Source code
│   └── project_name/      # Main package
│       └── __init__.py
│
├── tests/                 # Test files
│   ├── __init__.py
│   ├── project_name/
│       └── unit/
│       │    └──test_function_a.│py            
│       └── integration/  
├── docs/                  # Documentation
│   ├── api/              # API documentation
│   ├── guides/           # User guides
│   └── examples/         # Code examples
│
├── .venv/                # Virtual environment (git ignored)
├── .vscode/settings.json              # VS Code settings
├── .git/                 # Git repository
├── .gitignore           # Git ignore file
├── pyproject.toml       # Project configuration
├── README.md            # Project documentation
└── pytest.ini          # Pytest configuration
```

## Tool Configuration

### Using uv for Dependencies

```bash
# Install uv
pip install uv

# Create new project
uv venv
uv venv activate

# Add dependencies
uv pip install ruff pandas pytest
uv pip install --editable .

# Generate requirements
uv pip freeze > requirements.txt
```


### Ruff Configuration
```
Ruff is configured for:
- Line length: 80 characters
- Code formatting
- Import sorting
- Type checking
- Style enforcement
- Docstring validation
```

### pytest Configuration (optional)

*Add only if used in the project* into -> `pyproject.toml`

````
[tool.pytest.ini_options]
minversion = "6.0"
addopts = "-ra -q --doctest-modules"
testpaths = [
    "tests",
]
python_files = ["test_*.py", "*_test.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
markers = [
    "unit: Unit tests",
    "integration: Integration tests",
    "e2e: End-to-end tests",
    "slow: Tests that take longer to run"
]
````