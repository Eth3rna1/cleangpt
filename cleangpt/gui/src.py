import tkinter as tk
from tkinter import scrolledtext


def get_text_from_gui():
    result = {"text": None}

    def on_clean():
        # Get all text from the text box
        result["text"] = text_area.get("1.0", tk.END).strip()
        root.destroy()

    # Create main window
    root = tk.Tk()
    root.title("Paste Your Text")
    root.geometry("700x500")

    # Label
    label = tk.Label(root, text="Paste your text below:")
    label.pack(pady=10)

    # Large text area with scrollbar
    text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
    text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    # Clean button
    clean_button = tk.Button(root, text="Clean", command=on_clean)
    clean_button.pack(pady=10)

    # Run GUI loop
    root.mainloop()

    return result["text"]
