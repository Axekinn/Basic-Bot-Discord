# Security Policy

## Supported Versions

This project maintains security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| Latest  | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **DO NOT** open a public issue
2. Email the maintainer directly (if personal project) or use GitHub's private vulnerability reporting
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

## Security Best Practices for Users

### Environment Variables
- Never commit `.env` files
- Regenerate tokens if accidentally exposed
- Use strong, unique tokens

### Bot Permissions
- Use minimal required permissions
- Regularly audit bot permissions
- Remove unused permissions

### Dependencies
- Keep dependencies updated
- Monitor for security advisories
- Use `pip audit` to check for vulnerabilities

## Security Features

This bot template includes:
- Environment variable configuration
- Secure token handling
- Input validation in commands
- Error handling to prevent information leakage

## Contact

For security concerns, please contact [your-email@example.com] or create a private security advisory on GitHub.
