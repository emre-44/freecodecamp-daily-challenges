"""
Given a CSS rgb(r, g, b) color string, return its hexadecimal equivalent.

Here are some example outputs for a given input:

Input	Output
"rgb(255, 255, 255)"	"#ffffff"
"rgb(1, 2, 3)"	"#010203"
Make any letters lowercase.
Return a # followed by six characters. Don't use any shorthand values.
"""

def rgb_to_hex(rgb):
    """
    Generate hexadecimal code from user RGB format string
    
    Args:
        rgb(str): RGB format input
        
    Returns:
        hex_color(str): Hex color code
    """
    hex_codes = rgb.replace("rgb(","").replace(")","").split(", ")
    r, g, b = int(hex_codes[0]),int(hex_codes[1]),int(hex_codes[2])
    hex_color = f"#{r:02x}{g:02x}{b:02x}"

    return hex_color

#Test Stage
print(rgb_to_hex("rgb(255, 255, 255)"))
