# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions workflow for CI/CD
- Comprehensive test suite
- Configuration file support
- Email template validation

### Changed
- Improved error messages
- Enhanced logging system

### Fixed
- Memory usage optimization for large contact lists
- Attachment handling edge cases

## [1.0.0] - 2024-01-XX

### Added
- Initial release of Email Bulk Sender
- **Outlook Integration**: Full support for Microsoft Outlook desktop application
  - Account selection for multiple Outlook accounts
  - HTML email detection and formatting
  - Attachment support
  - Draft mode for safe testing
  - Recipient resolution and validation
- **SMTP Support**: Universal SMTP delivery
  - Support for Gmail, Office 365, and custom SMTP servers
  - TLS/SSL encryption
  - Retry mechanism with exponential backoff
  - Rate limiting and throttling protection
- **Contact Management**: Smart contact file processing
  - Auto-detection of email columns in CSV/Excel files
  - Support for multiple file formats (.csv, .xlsx, .xls)
  - Flexible column naming (email, email_address, e-mail, etc.)
- **Message Personalization**: Dynamic content generation
  - Placeholder replacement using contact data
  - Support for any column as a placeholder
  - Graceful handling of missing data
- **Advanced Features**:
  - Multiple attachment support
  - HTML and plain text message formats
  - Comprehensive error handling and logging
  - Progress tracking with tqdm
  - Command-line interface with extensive options
- **Safety Features**:
  - Draft mode for testing before sending
  - Preflight checks for Outlook availability
  - Attachment validation
  - Error recovery and continuation
- **Documentation**:
  - Comprehensive README with examples
  - Troubleshooting guide
  - Security and compliance guidelines
  - Performance optimization tips

### Technical Details
- **Python 3.9+** compatibility
- **Dependencies**: pandas, openpyxl, tqdm, tenacity, pywin32 (Windows)
- **Architecture**: Modular design with separate SMTP and Outlook modules
- **Error Handling**: Comprehensive exception handling with detailed logging
- **Performance**: Optimized for large contact lists with memory efficiency

### Security
- No hardcoded credentials
- Secure SMTP authentication
- Input validation and sanitization
- Safe file handling
- Compliance with email marketing best practices

## [0.9.0] - 2024-01-XX (Pre-release)

### Added
- Basic Outlook integration
- SMTP delivery functionality
- Contact file parsing
- Message template system
- Command-line interface

### Changed
- Initial project structure
- Basic error handling

### Fixed
- Initial bug fixes and stability improvements

---

## Version History Summary

- **v1.0.0**: Production-ready release with full feature set
- **v0.9.0**: Beta release with core functionality

## Future Roadmap

### v1.1.0 (Planned)
- Configuration file support
- Email template validation
- Enhanced error recovery
- Performance optimizations

### v1.2.0 (Planned)
- GUI interface
- Scheduling capabilities
- Email tracking
- Analytics dashboard

### v2.0.0 (Planned)
- Web interface
- API endpoints
- Database integration
- Multi-user support

## Migration Guide

### From v0.9.0 to v1.0.0
- No breaking changes
- New `--outlook-draft` flag available
- Enhanced error messages
- Improved attachment handling

## Support

For questions about specific versions or migration help:
- Check the [README.md](README.md) for current documentation
- Open an issue on GitHub for version-specific problems
- Review the [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines
