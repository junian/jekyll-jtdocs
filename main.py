from pygments.formatters import HtmlFormatter
from pygments.styles import get_all_styles

# WCAG 2.1 - AAA compliant themes (accessible-pygments)
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

# WCAG 2.1 - AA compliant themes (accessible-pygments)
aa_themes = [
    "a11y-light",
    "a11y-high-contrast-light",
    "gotthard-light",
    "blinds-light",
    "blinds-dark",
    "greative",
]

# Get all official Pygments themes
official_themes = list(get_all_styles())

# Combine all themes (accessible-pygments + official Pygments)
themes = aaa_themes + aa_themes + official_themes

# Remove duplicates while preserving order
seen = set()
unique_themes = []
for theme in themes:
    if theme not in seen:
        seen.add(theme)
        unique_themes.append(theme)

print(f"Generating {len(unique_themes)} syntax highlighting themes...\n")

for style in unique_themes:
    try:
        formatter = HtmlFormatter(style=style)
        css = formatter.get_style_defs(".highlight")
        with open(f"_sass/vendor/accessible-pygments/{style}.scss", "w") as f:
            f.write(css)
        print(f"✓ Generated: {style}.scss")
    except Exception as e:
        print(f"✗ Failed to generate {style}.scss: {e}")

print(f"\nTotal themes generated: {len(unique_themes)}")