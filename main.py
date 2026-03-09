from pygments.formatters import HtmlFormatter

themes = ["github-light", "github-dark"]

for style in themes:
    formatter = HtmlFormatter(style=style)
    css = formatter.get_style_defs(".highlight")
    with open(f"_sass/vendor/accessible-pygments/{style}.scss", "w") as f:
        f.write(css)