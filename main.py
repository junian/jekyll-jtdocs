from pygments.formatters import HtmlFormatter

# WCAG 2.1 - AAA compliant themes
aaa_themes = [
    "a11y-dark",
    "a11y-high-contrast-dark",
    "pitaya-smoothie",
    "github-light",
    "github-dark",
    "github-light-colorblind",
    "github-dark-colorblind",
    "github-light-high-contrast",
    "github-dark-high-contrast",
    "gotthard-dark",
]

# WCAG 2.1 - AA compliant themes
aa_themes = [
    "a11y-light",
    "a11y-high-contrast-light",
    "gotthard-light",
    "blinds-light",
    "blinds-dark",
    "greative",
]

# Combine all themes
themes = aaa_themes + aa_themes

for style in themes:
    formatter = HtmlFormatter(style=style)
    css = formatter.get_style_defs(".highlight")
    with open(f"_sass/vendor/accessible-pygments/{style}.scss", "w") as f:
        f.write(css)
    print(f"Generated: {style}.scss")