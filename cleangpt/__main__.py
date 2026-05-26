from cleangpt import clean_text
from cleangpt.gui import get_text_from_gui
from cleangpt.memo import Memo, DEFAULT_FILE_NAME


if __name__ == "__main__":
    memo = Memo(DEFAULT_FILE_NAME)
    text = get_text_from_gui()
    clean_text = clean_text(text, memo)
    memo.save()
    print(clean_text)
