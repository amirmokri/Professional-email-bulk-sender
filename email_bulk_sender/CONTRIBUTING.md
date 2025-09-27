# Contributing to Email Bulk Sender

Thank you for your interest in contributing to Email Bulk Sender! This document provides guidelines and information for contributors.

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/your-username/email_bulk_sender.git
   cd email_bulk_sender
   ```
3. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🛠️ Development Setup

### Prerequisites
- Python 3.9+
- Git
- Windows 10/11 (for Outlook testing)
- Microsoft Outlook (for Outlook mode testing)

### Testing Your Changes
1. **Test with drafts first**:
   ```bash
   python main.py --mode outlook --contacts examples/contacts.csv --message examples/message.txt --subject "Test" --outlook-draft
   ```
2. **Verify functionality** with both Outlook and SMTP modes
3. **Check for errors** in the console output

## 📝 How to Contribute

### Reporting Issues
- Use the GitHub issue tracker
- Include:
  - Python version
  - Operating system
  - Error messages
  - Steps to reproduce
  - Expected vs actual behavior

### Suggesting Features
- Open an issue with the "enhancement" label
- Describe the use case and benefits
- Consider implementation complexity

### Code Contributions

#### Pull Request Process
1. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** following the coding standards
3. **Test thoroughly** on Windows with Outlook
4. **Update documentation** if needed
5. **Commit with clear messages**:
   ```bash
   git commit -m "Add feature: brief description"
   ```
6. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open a Pull Request** with a clear description

#### Coding Standards
- **Follow PEP 8** for Python code
- **Use type hints** where appropriate
- **Add docstrings** for functions and classes
- **Keep functions small** and focused
- **Handle errors gracefully** with proper logging

#### Code Style
```python
def example_function(param1: str, param2: int) -> bool:
    """
    Brief description of what the function does.
    
    Args:
        param1: Description of parameter
        param2: Description of parameter
        
    Returns:
        Description of return value
        
    Raises:
        ValueError: When something goes wrong
    """
    try:
        # Implementation here
        return True
    except Exception as e:
        logger.error("Error in example_function: %s", e)
        raise
```

## 🧪 Testing Guidelines

### Test Cases to Cover
- **Contact file parsing** (CSV, Excel, various formats)
- **Message template processing** (text, HTML, placeholders)
- **Outlook integration** (account selection, attachments, drafts)
- **SMTP delivery** (authentication, error handling)
- **Error scenarios** (missing files, invalid data, network issues)

### Testing Checklist
- [ ] Test with sample data from `examples/` folder
- [ ] Test with `--outlook-draft` flag first
- [ ] Verify attachments work correctly
- [ ] Test HTML message detection
- [ ] Test placeholder replacement
- [ ] Test error handling and logging

## 📚 Documentation

### When to Update Documentation
- Adding new features
- Changing command-line arguments
- Modifying file formats
- Adding new dependencies

### Documentation Files
- `README.md` - Main documentation
- `CONTRIBUTING.md` - This file
- `CHANGELOG.md` - Version history
- Code comments and docstrings

## 🏷️ Release Process

### Version Numbering
We use [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Release Checklist
- [ ] Update version in `setup.py`
- [ ] Update `CHANGELOG.md`
- [ ] Test on clean environment
- [ ] Create GitHub release
- [ ] Tag the release

## 🤝 Community Guidelines

### Code of Conduct
- Be respectful and inclusive
- Focus on constructive feedback
- Help others learn and grow
- Follow the golden rule

### Communication
- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and general discussion
- **Pull Requests**: Code contributions and reviews

## 🎯 Areas for Contribution

### High Priority
- **Error handling improvements**
- **Additional email providers** (Yahoo, AOL, etc.)
- **Batch processing optimizations**
- **Configuration file support**
- **Email template validation**

### Medium Priority
- **GUI interface**
- **Scheduling capabilities**
- **Email tracking**
- **Unsubscribe management**
- **Analytics and reporting**

### Low Priority
- **Mobile app**
- **Web interface**
- **API endpoints**
- **Database integration**

## 📞 Getting Help

- **Read the documentation** first
- **Search existing issues** for similar problems
- **Ask questions** in GitHub Discussions
- **Join the community** and help others

## 🏆 Recognition

Contributors will be:
- Listed in the README
- Mentioned in release notes
- Credited in the changelog
- Appreciated by the community!

Thank you for contributing to Email Bulk Sender! 🎉
