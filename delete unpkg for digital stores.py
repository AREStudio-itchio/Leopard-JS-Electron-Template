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

            # ruta relativa desde este archivo a /lib/leopard.js
            rel = os.path.relpath(lib, dirpath)

            # formato web
            rel = rel.replace("\\", "/")

            # asegurar ./ cuando no sube directorios
            if not rel.startswith("."):
                rel = "./" + rel

            # reemplazo SOLO de esa URL concreta
            new_txt = re.sub(pattern, rel, txt)

            if new_txt != txt:
                with open(path, "w", encoding="utf-8") as fp:
                    fp.write(new_txt)