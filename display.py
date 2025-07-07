from variables import ConfigStyles

from PySide6.QtWidgets import QLineEdit
from PySide6.QtCore import Qt

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        margins = [ConfigStyles.TEXT_MARGIN for _ in range(4)]
        self.setStyleSheet(f'font-size: {ConfigStyles.BIG_FONT_SIZE}px;')
        self.setMinimumHeight(ConfigStyles.BIG_FONT_SIZE * 2)
        self.setMinimumWidth(ConfigStyles.MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)