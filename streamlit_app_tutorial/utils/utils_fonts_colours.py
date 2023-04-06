import matplotlib.pylab as plt
import matplotlib.colors as pltcol
import altair as alt

# Fonts and colours
FONT = "Averta"
TITLE_FONT = "Averta"
FONTSIZE_TITLE = 16
FONTSIZE_SUBTITLE = 13
FONTSIZE_NORMAL = 13

NESTA_COLOURS = [
    "#0000FF",
    "#18A48C",
    "#9A1BBE",
    "#EB003B",
    "#FF6E47",
    "#646363",
    "#0F294A",
    "#97D9E3",
    "#A59BEE",
    "#F6A4B7",
    "#FDB633",
    "#D2C9C0",
    "#FFFFFF",
    "#000000",
]


def nestafont():
    """Define Nesta fonts"""
    return {
        "config": {
            "title": {"font": TITLE_FONT, "anchor": "start"},
            "axis": {"labelFont": FONT, "titleFont": FONT},
            "header": {"labelFont": FONT, "titleFont": FONT},
            "legend": {"labelFont": FONT, "titleFont": FONT},
            "range": {
                "category": NESTA_COLOURS,
                "ordinal": {
                    "scheme": NESTA_COLOURS
                },
            },
        }
    }

# Colour pallette for the altair choropleth maps
# As we are looking at the deciles, we will have 10 colour codes.
summer_palette = [ 
    "#f94144","#f3722c","#f8961e","#f9844a","#f9c74f","#90be6d","#43aa8b","#4d908e","#577590","#277da1"
]
winter_palette = [ 
    "#7400b8","#6930c3","#5e60ce","#5390d9","#4ea8de","#48bfe3","#56cfe1","#64dfdf","#72efdd","#80ffdb"
]
domain = [i + 1 for i in range(10)]
colour_palettes = {
    'Spring' : alt.Scale(domain=domain,scheme='yellowgreenblue',reverse=False),
    'Summer' : alt.Scale(domain=domain,range=summer_palette),
    'Autumn' : alt.Scale(domain=domain,scheme='plasma',reverse=True),
    'Winter' : alt.Scale(domain=domain,range=winter_palette,reverse=True)
}