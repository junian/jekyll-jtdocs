from pygments.formatters import HtmlFormatter

# choose any accessible-pygments style
STYLE = "a11y-dark"

# generate CSS scoped to `.highlight`
formatter = HtmlFormatter(style=STYLE)

css = formatter.get_style_defs(".highlight")

# write to Jekyll sass directory
with open("_sass/_pygments.scss", "w") as f:
    f.write(css)

print("Generated _sass/_pygments.scss")