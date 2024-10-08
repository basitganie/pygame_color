# pygame_colors.py
colors = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "cyan": (0, 255, 255),
    "magenta": (255, 0, 255),
    "gray": (128, 128, 128),
    "grey": (128, 128, 128),  # Both spellings
    "darkgray": (64, 64, 64),
    "darkgrey": (64, 64, 64),
    "lightgray": (211, 211, 211),
    "lightgrey": (211, 211, 211),
    "brown": (165, 42, 42),
    "orange": (255, 165, 0),
    "pink": (255, 192, 203),
    "purple": (128, 0, 128),
    "violet": (238, 130, 238),
    "indigo": (75, 0, 130),
    "gold": (255, 215, 0),
    "silver": (192, 192, 192),
    "bronze": (205, 127, 50),
    "lime": (0, 255, 0),
    "olive": (128, 128, 0),
    "maroon": (128, 0, 0),
    "navy": (0, 0, 128),
    "teal": (0, 128, 128),
    "aqua": (0, 255, 255),
    "turquoise": (64, 224, 208),
    "coral": (255, 127, 80),
    "salmon": (250, 128, 114),
    "chocolate": (210, 105, 30),
    "crimson": (220, 20, 60),
    "beige": (245, 245, 220),
    "khaki": (240, 230, 140),
    "lavender": (230, 230, 250),
    "plum": (221, 160, 221),
    "orchid": (218, 112, 214),
    "periwinkle": (204, 204, 255),
    "chartreuse": (127, 255, 0),
    "mint": (189, 252, 201),
    "peach": (255, 218, 185),
    "apricot": (251, 206, 177),
    "mustard": (255, 219, 88),
    "skyblue": (135, 206, 235),
    "lightblue": (173, 216, 230),
    "darkblue": (0, 0, 139),
    "midnightblue": (25, 25, 112),
    "lightgreen": (144, 238, 144),
    "darkgreen": (0, 100, 0),
    "forestgreen": (34, 139, 34),
    "seagreen": (46, 139, 87),
    "limegreen": (50, 205, 50),
    "palegreen": (152, 251, 152),
    "lightpink": (255, 182, 193),
    "hotpink": (255, 105, 180),
    "deeppink": (255, 20, 147),
    "lightcoral": (240, 128, 128),
    "slategray": (112, 128, 144),
    "slategrey": (112, 128, 144),
    "lightslategray": (119, 136, 153),
    "lightslategrey": (119, 136, 153),
    "darkslategray": (47, 79, 79),
    "darkslategrey": (47, 79, 79),
    "rosybrown": (188, 143, 143),
    "saddlebrown": (139, 69, 19),
    "sienna": (160, 82, 45),
    "snow": (255, 250, 250),
    "seashell": (255, 245, 238),
    "ivory": (255, 255, 240),
    "honeydew": (240, 255, 240),
    "lavenderblush": (255, 240, 245),
    "mistyrose": (255, 228, 225),
    "slateblue": (106, 90, 205),
    "mediumslateblue": (123, 104, 238),
    "royalblue": (65, 105, 225),
    "dodgerblue": (30, 144, 255),
    "steelblue": (70, 130, 180),
    "deepskyblue": (0, 191, 255),
    "powderblue": (176, 224, 230),
    "cornflowerblue": (100, 149, 237),
    "firebrick": (178, 34, 34),
    "darkred": (139, 0, 0),
    "darkorange": (255, 140, 0),
    "orangered": (255, 69, 0),
    "goldenrod": (218, 165, 32),
    "mediumseagreen": (60, 179, 113),
    "mediumturquoise": (72, 209, 204),
    "lightseagreen": (32, 178, 170),
    "palevioletred": (219, 112, 147),
    "springgreen": (0, 255, 127),
    "mediumspringgreen": (0, 250, 154),
    "darkviolet": (148, 0, 211),
    "darkorchid": (153, 50, 204),
    "mediumorchid": (186, 85, 211),
    "darkmagenta": (139, 0, 139),
    "mediumpurple": (147, 112, 219),
}

def get_color(color_name):
    """Returns the RGB tuple of the color by name."""
    return colors.get(color_name.lower(), (255, 255, 255))  # Default to white if color is not found

def lighten(color, factor=1.2):
    """Returns a lighter version of the given color."""
    return tuple(min(int(c * factor), 255) for c in color)

def darken(color, factor=0.8):
    """Returns a darker version of the given color."""
    return tuple(max(int(c * factor), 0) for c in color)
    