import os
import json # storing as JSON files

DEFAULT_FILE_NAME = f"%USERPROFILE%/.cleangpt.json"


DEFAULT_REPLACEMENTS = {
    "\u2014": ", ",
    "\u2019": "'",
    "\u201c": "\"",
    "\u201d": "\""
}

class Memo:
    def __init__(self, loc):
        self.loc = os.path.expandvars(loc)

        if not os.path.exists(self.loc):
            with open(self.loc, "w") as file:
                file.write("{}")

        with open(self.loc, "r") as file:
            self.data = json.load(file)

        # loading the default replacement characters
        self.data |= DEFAULT_REPLACEMENTS
        

    def contains(self, key):
        return key in self.data

    def update(self, key, value):
        self.data[key] = value

    def iter(self):
        return self.data.items()

    def save(self):
        with open(self.loc, "w") as file:
            return file.write(json.dumps(self.data, indent=4))
