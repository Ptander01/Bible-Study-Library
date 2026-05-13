import os

HTML_PATH = "holy-spirit-study.html"
JS_PATH   = "app.compiled.js"

with open(HTML_PATH, "r") as f:
    html = f.read()

with open(JS_PATH, "r") as f:
    compiled_js = f.read()

script_open  = html.index("<script>")
script_close = html.index("</script>", script_open) + len("</script>")
new_html     = html[:script_open] + "<script>\n" + compiled_js + "\n</script>" + html[script_close:]

with open(HTML_PATH, "w") as f:
    f.write(new_html)

print(f"Rebuilt {HTML_PATH} ({len(new_html) // 1024} KB)")
