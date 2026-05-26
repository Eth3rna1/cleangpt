# CleanGPT

A text cleaning utility with a GUI that intelligently removes and replaces invalid characters from text. CleanGPT learns your character replacement preferences and caches them for future use.

## Features

- **Interactive GUI** - Paste text into a simple, user-friendly window
- **Invalid Character Detection** - Identifies characters outside standard ASCII, digits, punctuation, and whitespace
- **Smart Replacement System** - Prompts you to replace or remove invalid characters as they're encountered
- **Persistent Caching** - Learns your replacement preferences and stores them locally, so you're never asked the same question twice
- **Default Replacements** - Comes with common Unicode character replacements pre-loaded:
  - Em dash (—) → comma-space (, )
  - Right single quotation mark (') → apostrophe (')
  - Left double quotation mark (") → regular quote (")
  - Right double quotation mark (") → regular quote (")
- **Space Normalization** - Automatically collapses multiple consecutive spaces into single spaces

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd cleangpt
```

2. Ensure you have Python 3.x installed

3. No external dependencies required - uses only Python's standard library (tkinter, json, string)

## Usage

Run the application:
```bash
python -m cleangpt
```

This will:
1. Open a GUI window where you can paste text
2. Click the "Clean" button to start processing
3. For any unrecognized invalid characters, you'll be prompted in the terminal to specify a replacement
   - Press Enter with no input to remove the character entirely
4. The cleaned text will be printed to the terminal
5. Your replacements are cached in `~/.cleangpt.json` for future use

## Project Structure

```
cleangpt/
├── __main__.py          # Entry point - orchestrates the cleaning workflow
├── src.py               # Core cleaning logic
├── gui/
│   ├── __init__.py
│   └── src.py           # Tkinter GUI implementation
├── memo/
│   ├── __init__.py
│   └── src.py           # Caching system for character replacements
└── README.md
```

## Configuration

Your character replacement cache is stored at: `~/.cleangpt.json`

The file contains a JSON mapping of invalid characters to their replacements:
```json
{
    "—": ", ",
    "'": "'",
    """: "\"",
    """: "\"",
    "…": "..."
}
```

You can manually edit this file to add, remove, or modify replacements.

## How It Works

1. **Text Input** - User pastes text via the GUI and clicks "Clean"
2. **Validation** - The cleaner scans through each character
3. **Character Classification** - Valid characters include:
   - ASCII letters (a-z, A-Z)
   - Digits (0-9)
   - Punctuation marks
   - Whitespace (space, tab, newline)
4. **User Interaction** - For each invalid character not in cache:
   - Shows the character with surrounding context
   - Prompts for a replacement
5. **Replacement** - All identified characters are replaced according to the cache
6. **Normalization** - Extra spaces are collapsed
7. **Output** - Cleaned text is printed to terminal

## Author

Gabriel Mendieta Hernandez

## License

MIT
