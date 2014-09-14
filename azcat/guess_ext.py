import os

def guess_ext_by_filename (filename):
    FILENAMES = {
                  "Makefile":  "mak",
                }

    ext = os.path.splitext(filename)[1].lstrip(".")
    if ext == "":
        for k,v in FILENAMES.items():
            if filename.startswith(k):
                return v
        return ""
    else:
        return ext


def guess_ext_by_contents (s):
    INTERPRETERS = {
                     "python": "py",
                     "ruby":   "rb",
                     "perl":   "pl",
                     "php":    "php",
                     "bash":   "sh",
                     "zsh":    "sh",
                     "sh":     "sh",
                   }

    if not s.startswith("#!"):
        return ""

    shebang = s.split("\n", 1)[0]
    try:
        interpreter = shebang.split("env ")[1]
    except IndexError:
        interpreter = os.path.basename(shebang[2:])

    for k,v in INTERPRETERS.items():
        if interpreter.startswith(k):
            return v
    return ""