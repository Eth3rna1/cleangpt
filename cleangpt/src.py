import string

VALID_CHARACTERS = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + " \n\t"

DEFAULT_CHARACTER_WINDOW = 15

def get_char_window(text, i, window_size):
    low = i - window_size if i - window_size >= 0 else 0
    high = i + window_size if i + window_size < len(text) else len(text) - 1
    return text[low: high]

def collapse_extra_spaces(text):
    return "".join(text.split(" "))

def clean_text(text: str, memo, char_win=DEFAULT_CHARACTER_WINDOW) -> str:
    n = len(text)

    for i in range(n):
        char = text[i]
        if char not in VALID_CHARACTERS and not memo.contains(char):
            print(f"\"{char}\" - \"{get_char_window(text, i, char_win)}\"")
            # invalid_chars.append(char)
            memo.update(char, "")
            new_char = input(f"Replacement for \"{char}\": ")
            memo.update(char, new_char)

    for char, new_char in memo.iter():
        text = text.replace(char, new_char)

    text = collapse_extra_spaces(text)

    return text
