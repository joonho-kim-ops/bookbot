# BookBot AI Agent Instructions

## Project Overview
BookBot is a Python-based text analysis tool developed as part of the Boot.dev curriculum. The project focuses on processing and analyzing text files, specifically books, to perform various text analytics operations.

## Project Structure
```
bookbot/
├── main.py          # Main application logic
├── books/          
│   └── frankenstein.txt  # Sample book for analysis
└── README.md
```

## Key Components
- `main.py`: Contains core text processing functions
  - `get_book_text()`: Reads and loads book content from files in the `books/` directory
- `books/`: Directory containing text files for analysis

## Development Patterns
1. **File Processing**
   - Text files are stored in the `books/` directory
   - Files are processed using standard Python file operations with context managers (`with` statements)

2. **Function Design**
   - Functions are focused on single responsibilities
   - Use descriptive names that indicate their purpose (e.g., `get_book_text`)

## Development Environment
- Python-based project
- No external dependencies required (uses standard library)
- No build process needed - run directly with Python

## Getting Started
1. Ensure Python is installed
2. Run scripts directly: `python main.py`
3. Text files for analysis should be placed in the `books/` directory

## Common Tasks
- Reading book content: Use the `get_book_text()` function
- Adding new features: Add new functions to `main.py`
- Testing changes: Run the script with sample text files from the `books/` directory

## Best Practices
- Keep functions focused on single tasks
- Use appropriate error handling for file operations
- Maintain consistent Python code style