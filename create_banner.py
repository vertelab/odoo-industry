#!/usr/bin/env python3
from io import StringIO
import cairosvg
import sys
import os
import xml.sax.saxutils as saxutils

# sudo apt-get install fonts-ubuntu
# fc-cache -fv

template_svg = "banner_template.svg"

def adjust_font_size(text, max_width_px, base_font_size=10.5833, avg_char_width=6):    
    """
    text: the text string to insert in SVG
    max_width_px: maximum allowed width in pixels for the text
    base_font_size: the default font size used when the text length fits within max_width_px
    avg_char_width: estimated average width of a single character at base_font_size
    
    Returns:
        a font size (float) that ensures the text fits within max_width_px by scaling down proportionally
    """
    
    text_width = len(text) * avg_char_width
    if text_width <= max_width_px:
        return f"{base_font_size}px"
    else:
        # Calculate scaling factor to reduce font size so text fits max width
        scale = max_width_px / text_width
        new_font_size = base_font_size * scale
        min_font_size = 5   # Don't reduce font size below this threshold
        return f"{max(new_font_size, min_font_size)}px"

def svg_replace_and_convert(svg_template_path, replacement_text, output_png_path):
    with open(svg_template_path, 'r', encoding='utf-8') as f:
        svg_content = f.read()
    replacement_text = saxutils.escape(replacement_text)
    svg_content = svg_content.replace('[REPLACEME]', replacement_text)
    svg_content = svg_content.replace('[REPLACEFONTSIZE]', adjust_font_size(replacement_text,120))
    svg_stream = StringIO(svg_content)
    cairosvg.svg2png(bytestring=svg_stream.getvalue().encode('utf-8'), write_to=output_png_path)

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} [modules]")
    sys.exit(1)

modules = sys.argv[1:]

for module in modules:
    if os.path.isdir(module):
        with open(f"{module}/__manifest__.py", "r", encoding="utf-8") as f:
            code = f.read()

        manifest_dict = eval(code, {"__builtins__": None}, {})
        os.makedirs(f'{module}/images', exist_ok=True)
        svg_replace_and_convert(template_svg, manifest_dict['name'], f'{module}/images/main.png')
        print(f"{module} Done...")
