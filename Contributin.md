# Contributing to Jarvis Code Analyzer

First off, thank you for considering contributing to NOVA Code Analyzer! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)
- [Testing Guidelines](#testing-guidelines)

## 📜 Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow:

- **Be respectful** and considerate in your communication
- **Be collaborative** and open to feedback
- **Be inclusive** and welcoming to newcomers
- **Focus on what's best** for the community and project

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**When filing a bug report, include:**

- **Clear title** and description
- **Python version**: `python --version`
- **OS and version**: e.g., Ubuntu 22.04, macOS 13.1, Windows 11
- **Steps to reproduce** the issue
- **Expected behavior** vs. actual behavior
- **Error messages** (full traceback if applicable)
- **Code samples** that trigger the bug

**Example Bug Report:**

```markdown
## Bug: Analyzer crashes on files with Unicode docstrings

**Environment:**
- Python: 3.9.5
- OS: Ubuntu 20.04
- Version: 1.0.0

**Steps to Reproduce:**
1. Create a file with Unicode characters in docstring
2. Run: `python code_analyzer_demo.py`
3. Select option 1 and enter the filename

**Expected:** Analysis completes successfully
**Actual:** UnicodeDecodeError is raised

**Error Message:**
```
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff
```

**Sample Code:**
```python
# test_unicode.py
"""
This is a test file with émojis 🚀
"""
```
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues.

**When suggesting an enhancement, include:**

- **Clear title** describing the enhancement
- **Detailed description** of the proposed feature
- **Use case**: Why would this be useful?
- **Examples**: How would it work?
- **Implementation ideas**: Optional, if you have thoughts

**Example Enhancement:**

```markdown
## Feature Request: Export analysis to HTML report

**Description:**
Add ability to export code analysis results as an HTML report with charts and graphs.

**Use Case:**
Developers want to share analysis results with their team via email or documentation.

**Proposed API:**
```python
from code_analyzer_demo import analyze_python_file, export_html

analysis = analyze_python_file('mycode.py')
export_html(analysis, output_file='report.html')
```

**Implementation Ideas:**
- Use Jinja2 for HTML templating
- Include Chart.js for visualization
- Add CSS styling for professional look
```

### Your First Code Contribution

Unsure where to begin? Look for issues labeled:

- `good first issue` - Simple issues for newcomers
- `help wanted` - Issues where we need community help
- `documentation` - Documentation improvements

## 🛠️ Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub first, then:
git clone https://github.com/YOUR_USERNAME/jarvis-code-analyzer.git
cd jarvis-code-analyzer
```

### 2. Create a Virtual Environment

```bash
# Python 3.7+
python -m venv venv

# Activate (Linux/macOS)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Install in development mode
pip install -r requirements.txt

# Install development dependencies (optional)
pip install pytest black flake8 mypy
```

### 4. Create a Branch

```bash
git checkout -b feature/your-feature-name
# or
git checkout -b bugfix/issue-number-description
```

**Branch Naming Convention:**
- `feature/add-html-export` - New features
- `bugfix/fix-unicode-error` - Bug fixes
- `docs/update-readme` - Documentation
- `refactor/improve-ast-parser` - Code refactoring
- `test/add-unit-tests` - Adding tests

## 🔄 Pull Request Process

### 1. Make Your Changes

- Write clean, readable code
- Follow the style guidelines below
- Add comments for complex logic
- Update documentation if needed

### 2. Test Your Changes

```bash
# Run the analyzer
python code_analyzer_demo.py

# Test on various Python files
python code_analyzer_demo.py <<EOF
1
test_sample.py
4
EOF

# If you added tests, run them
pytest tests/
```

### 3. Commit Your Changes

```bash
git add .
git commit -m "Add feature: HTML export for analysis reports"
```

**Commit Message Guidelines:**

- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Fix bug" not "Fixes bug"
- First line: Brief summary (50 chars or less)
- Add blank line, then detailed description if needed

**Examples:**

✅ Good:
```
Add HTML export functionality

- Implement export_html() function
- Add Jinja2 template for reports
- Include Chart.js for visualizations
- Add tests for HTML generation
```

❌ Bad:
```
updated some files
```

### 4. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

### 5. Create Pull Request

- Go to the original repository on GitHub
- Click "New Pull Request"
- Select your fork and branch
- Fill in the PR template
- Link related issues (e.g., "Closes #123")

**PR Template:**

```markdown
## Description
Brief description of what this PR does.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
Describe how you tested your changes.

## Checklist
- [ ] My code follows the style guidelines
- [ ] I have commented my code where necessary
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix/feature works
- [ ] New and existing unit tests pass locally

## Screenshots (if applicable)
Add screenshots or GIFs if your changes affect the UI.

## Related Issues
Closes #123
```

### 6. Address Review Feedback

- Be responsive to reviewer comments
- Make requested changes promptly
- Push updates to the same branch
- Mark conversations as resolved when addressed

## 📐 Style Guidelines

### Python Style

Follow **PEP 8** with these specifics:

#### Formatting

```python
# Use 4 spaces for indentation
def my_function(param1, param2):
    """Function docstring."""
    return param1 + param2

# Maximum line length: 88 characters (Black default)
# Use Black for auto-formatting:
black code_analyzer_demo.py
```

#### Naming Conventions

```python
# Functions and variables: snake_case
def calculate_complexity(node):
    pass

# Classes: PascalCase
class CodeAnalyzer:
    pass

# Constants: UPPER_SNAKE_CASE
MAX_COMPLEXITY = 100

# Private methods: _leading_underscore
def _internal_helper(self):
    pass
```

#### Type Hints

Always use type hints for function parameters and return values:

```python
from typing import List, Dict, Optional

def analyze_file(filepath: str) -> Dict[str, any]:
    """Analyze a Python file."""
    pass

def process_data(items: List[str], count: Optional[int] = None) -> List[str]:
    """Process list of items."""
    pass
```

#### Docstrings

Use Google-style docstrings:

```python
def complex_function(param1: str, param2: int) -> Dict[str, float]:
    """
    Brief description of what the function does.
    
    Longer description if needed. Explain the purpose,
    algorithm, or important details here.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Dictionary containing result metrics with keys:
        - 'score': Calculated score value
        - 'confidence': Confidence level
        
    Raises:
        ValueError: If param2 is negative
        FileNotFoundError: If file doesn't exist
        
    Example:
        >>> result = complex_function("test", 42)
        >>> print(result['score'])
        85.5
    """
    pass
```

#### Imports

Organize imports in this order:

```python
# Standard library imports
import os
import sys
from typing import List, Dict

# Third-party imports
import numpy as np
from flask import Flask

# Local application imports
from .utils import helper_function
from .models import DataModel
```

### Code Quality Tools

Run these before submitting:

```bash
# Format code
black code_analyzer_demo.py

# Check style
flake8 code_analyzer_demo.py

# Type checking
mypy code_analyzer_demo.py

# Remove unused imports
autoflake --remove-all-unused-imports -i code_analyzer_demo.py
```

## 🧪 Testing Guidelines

### Writing Tests

Create test files in the `tests/` directory:

```python
# tests/test_analyzer.py
import pytest
from code_analyzer_demo import analyze_python_file, CodeAnalyzer


def test_analyze_simple_function():
    """Test analysis of a simple function."""
    code = """
def hello(name):
    return f"Hello {name}"
"""
    # Create temporary file
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        filepath = f.name
    
    analysis = analyze_python_file(filepath)
    
    assert len(analysis['functions']) == 1
    assert analysis['functions'][0]['name'] == 'hello'
    assert analysis['complexity'] > 0


def test_analyze_class_with_methods():
    """Test analysis of class with methods."""
    code = """
class MyClass:
    def __init__(self):
        pass
    
    def method1(self):
        pass
"""
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(code)
        filepath = f.name
    
    analysis = analyze_python_file(filepath)
    
    assert len(analysis['classes']) == 1
    assert analysis['classes'][0]['name'] == 'MyClass'
    assert len(analysis['classes'][0]['methods']) == 2


def test_complexity_calculation():
    """Test complexity metric calculation."""
    analyzer = CodeAnalyzer()
    # Add complexity calculation tests
    pass
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=code_analyzer_demo

# Run specific test file
pytest tests/test_analyzer.py

# Run specific test
pytest tests/test_analyzer.py::test_analyze_simple_function
```

### Test Coverage

Aim for at least 80% code coverage for new features:

```bash
pytest --cov=code_analyzer_demo --cov-report=html
# Open htmlcov/index.html in browser
```

## 📝 Documentation

### Code Documentation

- Add docstrings to all public functions and classes
- Include usage examples in docstrings
- Document complex algorithms
- Add inline comments for non-obvious code

### README Updates

If you add features, update:
- Feature list
- Installation instructions (if needed)
- Usage examples
- Configuration options

### Changelog

Add your changes to `CHANGELOG.md`:

```markdown
## [Unreleased]

### Added
- HTML export functionality for analysis reports
- New command-line flags for batch processing

### Changed
- Improved AST parsing performance by 30%
- Updated complexity calculation algorithm

### Fixed
- Fixed Unicode handling in docstring extraction
- Resolved memory leak in batch analysis mode
```

## 🏆 Recognition

Contributors are recognized in:
- `CONTRIBUTORS.md` file
- GitHub Contributors page
- Release notes for major contributions

## ❓ Questions?

- Open a [Discussion](https://github.com/yourusername/jarvis-code-analyzer/discussions)
- Ask in the issue comments
- Contact maintainers

## 🎉 Thank You!

Your contributions make this project better for everyone. Thank you for taking the time to contribute! 🚀

---

**Happy Contributing!** 💻✨