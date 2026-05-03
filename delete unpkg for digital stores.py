import os, re

root = os.getcwd()
lib = os.path.join(root, "lib", "leopard.js")

pattern = r'https://unpkg\.com/leopard@\^?1/dist/index\.esm\.js'

for dirpath, _, files in os.walk(root):
    for f in files:
        if f.endswith((".js", ".html")):
            path = os.path.join(dirpath, f)

            with open(path, encoding="utf-8") as fp:
                txt = fp.read()

            rel = os.path.relpath(lib, dirpath)
            
            rel = rel.replace("\\", "/")

            if not rel.startswith("."):
                rel = "./" + rel

            new_txt = re.sub(pattern, rel, txt)

            if new_txt != txt:
                with open(path, "w", encoding="utf-8") as fp:
                    fp.write(new_txt)
