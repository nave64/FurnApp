# Contributing to Mobland

Thank you for your interest in contributing to the Mobland Django e-commerce platform! This document provides guidelines for contributing to the project.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Git
- Virtual environment (recommended)

### Development Setup

1. **Fork the repository**
   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/yourusername/mobland.git
   cd mobland
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv env
   # Windows
   env\Scripts\activate
   # macOS/Linux
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

## 📝 Development Guidelines

### Code Style
- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Add docstrings to functions and classes
- Keep functions small and focused

### Django Best Practices
- Use Django's built-in features when possible
- Follow Django's model, view, and template patterns
- Use Django's form handling
- Implement proper error handling

### Database Changes
- Always create migrations for model changes
- Test migrations on a copy of production data
- Use descriptive migration names

### Frontend Guidelines
- Use semantic HTML
- Follow responsive design principles
- Use CSS classes consistently
- Test on multiple browsers

## 🔧 Development Workflow

### 1. Create a Feature Branch
```bash
git checkout -b feature/your-feature-name
```

### 2. Make Changes
- Write clean, readable code
- Add tests for new functionality
- Update documentation if needed

### 3. Test Your Changes
```bash
# Run tests
python manage.py test

# Check code style
flake8 .

# Run migrations
python manage.py makemigrations
python manage.py migrate
```

### 4. Commit Changes
```bash
git add .
git commit -m "Add: Brief description of changes"
```

### 5. Push and Create Pull Request
```bash
git push origin feature/your-feature-name
```

## 📋 Pull Request Guidelines

### Before Submitting
- [ ] Code follows project style guidelines
- [ ] All tests pass
- [ ] New features have tests
- [ ] Documentation is updated
- [ ] No merge conflicts

### Pull Request Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added for new features
- [ ] Manual testing completed

## Screenshots (if applicable)
Add screenshots to help explain your changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No merge conflicts
```

## 🐛 Bug Reports

When reporting bugs, please include:

1. **Description**: Clear description of the bug
2. **Steps to Reproduce**: Detailed steps to reproduce the issue
3. **Expected Behavior**: What should happen
4. **Actual Behavior**: What actually happens
5. **Environment**: Python version, Django version, OS
6. **Screenshots**: If applicable

## 💡 Feature Requests

When requesting features, please include:

1. **Description**: Clear description of the feature
2. **Use Case**: Why this feature would be useful
3. **Proposed Solution**: How you think it should work
4. **Alternatives**: Other solutions you've considered

## 🏗️ Project Structure

```
mobland/
├── mobland/              # Main Django project
├── account_module/       # User authentication
├── home_module/          # Homepage
├── product_module/       # Product management
├── order_module/         # Orders and payments
├── user_panel_module/    # User dashboard
├── blogs/               # Blog system
├── contact_us/          # Contact forms
├── site_module/         # Site settings
├── polls/               # Utilities and template tags
├── templates/           # HTML templates
├── static/              # Static files
└── uploads/             # User uploads
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test product_module

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

### Writing Tests
- Write tests for new features
- Test edge cases
- Use descriptive test names
- Follow AAA pattern (Arrange, Act, Assert)

## 📚 Documentation

### Code Documentation
- Add docstrings to functions and classes
- Use clear, descriptive comments
- Document complex logic

### API Documentation
- Document API endpoints
- Include request/response examples
- Document authentication requirements

## 🔒 Security

### Security Guidelines
- Never commit sensitive information
- Use environment variables for secrets
- Validate all user input
- Use Django's built-in security features
- Keep dependencies updated

### Reporting Security Issues
- Email security issues to the maintainers
- Do not create public issues for security problems
- Include detailed information about the vulnerability

## 📞 Getting Help

- Check existing issues and pull requests
- Read the documentation
- Ask questions in discussions
- Contact maintainers directly for urgent issues

## 📄 License

This project is private and proprietary. By contributing, you agree that your contributions will be licensed under the same terms as the project.

---

Thank you for contributing to Mobland! 🎉
