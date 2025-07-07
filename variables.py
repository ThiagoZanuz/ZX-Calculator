from pathlib import Path

class FoldersPaths():
    ROOT_FOLDER = Path(__file__).parent
    WINDOW_ICON_PATH = ROOT_FOLDER / 'zx_icon.png'

class ConfigStyles():
    BIG_FONT_SIZE = 40
    MEDIUM_FONT_SIZE = 24
    SMALL_FONT_SIZE = 18
    TEXT_MARGIN = 15
    MINIMUM_WIDTH = 400

class InterColors():
    PRIMARY_COLOR = ''
    DARKER_PRIMARY_COLOR = ''
    DARKEST_PRIMARY_COLOR = ''