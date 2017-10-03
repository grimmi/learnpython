'''
In this kata you parse RGB colors represented by strings.
The formats are primarily used in HTML and CSS.
Your task is to implement a function which takes a color as a
string and returns the parsed color as a map (see Examples).
Input:

The input string represents one of the following:

    6-digit hexadecimal - "#RRGGBB"
    e.g. "#012345", "#789abc", "#FFA077"
    Each pair of digits represents a value of the channel in hexadecimal: 00 to FF

    3-digit hexadecimal - "#RGB"
    e.g. "#012", "#aaa", "#F5A"
    Each digit represents a value 0 to F which translates to 2-digit hexadecimal: 0->00, 1->11, 2->22, and so on.

    Preset color name
    e.g. "red", "BLUE", "LimeGreen"
    You have to use the predefined map PRESET_COLORS (JavaScript, Python, Ruby),
    presetColors (Java, C#, Haskell), or preset-colors (Clojure).
    The keys are the names of preset colors in lower-case and the
    values are the corresponding colors in 6-digit hexadecimal (same as 1. "#RRGGBB").

Examples:

parse_html_color('#80FFA0')   # => {'r': 128, 'g': 255, 'b': 160}
parse_html_color('#3B7')      # => {'r': 51,  'g': 187, 'b': 119}
parse_html_color('LimeGreen') # => {'r': 50,  'g': 205, 'b': 50 }

taken from: https://www.codewars.com/kata/58b57ae2724e3c63df000006/train/python
'''
PRESET_COLORS = {'limegreen' : '#ff5599'}

def parse_html_color(color):
    def make_map(red_string, green_string, blue_string):
        return { 'r': int(red_string, 16), 'g': int(green_string, 16), 'b': int(blue_string, 16) }

    if not color.startswith('#'):
        color = PRESET_COLORS[color.lower()]

    if(len(color) == 7):
        return make_map(color[1] + color[2], color[3] + color[4], color[5] + color[6])
    elif len(color) == 4:
        return make_map(color[1] * 2, color[2] * 2, color[3] * 2)

print(parse_html_color("LimeGreen"))
