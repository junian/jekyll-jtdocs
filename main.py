from pygments.formatters import HtmlFormatter
from pygments.styles import get_all_styles
import os

# Ensure output directories exist
base_dir = "_sass/vendor/pygments-styles"
accessible_dir = f"{base_dir}/accessible-pygments"
os.makedirs(base_dir, exist_ok=True)
os.makedirs(accessible_dir, exist_ok=True)

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

# Combine accessible-pygments themes
accessible_themes = aaa_themes + aa_themes

# Get all official Pygments themes
official_themes = list(get_all_styles())

# Remove accessible themes from official list to avoid duplicates
official_themes = [t for t in official_themes if t not in accessible_themes]

print(f"Generating {len(accessible_themes)} accessible-pygments themes...\n")

# Generate accessible-pygments themes
for style in accessible_themes:
    try:
        formatter = HtmlFormatter(style=style)
        css = formatter.get_style_defs(".highlight")
        with open(f"{accessible_dir}/{style}.scss", "w") as f:
            f.write(css)
        print(f"✓ Generated: accessible-pygments/{style}.scss")
    except Exception as e:
        print(f"✗ Failed to generate accessible-pygments/{style}.scss: {e}")

print(f"\nGenerating {len(official_themes)} official Pygments themes...\n")

# Generate official Pygments themes
for style in official_themes:
    try:
        formatter = HtmlFormatter(style=style)
        css = formatter.get_style_defs(".highlight")
        with open(f"{base_dir}/{style}.scss", "w") as f:
            f.write(css)
        print(f"✓ Generated: {style}.scss")
    except Exception as e:
        print(f"✗ Failed to generate {style}.scss: {e}")

print(f"\n{'='*60}")
print(f"Total accessible-pygments themes: {len(accessible_themes)}")
print(f"Total official Pygments themes: {len(official_themes)}")
print(f"Total themes generated: {len(accessible_themes) + len(official_themes)}")
print(f"{'='*60}")
print(f"Accessible themes directory: {accessible_dir}")
print(f"Official themes directory: {base_dir}")