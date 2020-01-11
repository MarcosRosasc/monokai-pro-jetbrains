
import os
import re

COLORS = {
    "Spectrum": {
        # from iterm:
        "2d2a2e": "222222", # black
        "ff6188": "fc618d", # red
        "a9dc76": "7bd88f", # green
        "ffd866": "fce566", # yellow
        "fc9867": "fd9353", # blue (orange)
        "ab9df2": "948ae3", # magenta
        "78dce8": "5ad4e6", # cyan
        "fcfcfa": "f7f1ff", # white
        "5b595c": "525053", # grey (selection)
        "727072": "69676c", # grey (bright black)
        # from sublime:
        "221F22": "191919", # sidebar
        "373438": "2c2c2c", # caret row
        "403E41": "363537", # command bg
        "939293": "8b888f", # inactive icons
    }
}

for name, colors in COLORS.items():
    with open("src/Monokai Pro.theme.json", "r") as f:
        theme = f.read()

    with open("resources/colors/Monokai Pro.xml", "r") as f:
        scheme = f.read()

    for k,v in colors.items():
        color = re.compile(re.escape(k), re.IGNORECASE)
        theme = color.sub(v, theme)
        scheme = color.sub(v, scheme)

    theme = theme.replace("Monokai Pro.xml", "Monokai Pro {name}.xml".format(name=name))
    theme = theme.replace("\"Monokai Pro\"", "\"Monokai Pro (Filter {name})\"".format(name=name))
    scheme = scheme.replace("Monokai Pro", "Monokai Pro (Filter {name})".format(name=name))

    with open("src/Monokai Pro {name}.theme.json".format(name=name), "w") as f:
        f.write(theme)

    with open("resources/colors/Monokai Pro {name}.xml".format(name=name), "w") as f:
        f.write(scheme)
