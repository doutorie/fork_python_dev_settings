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