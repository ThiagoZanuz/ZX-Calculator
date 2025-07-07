from main_window import MainWindow
from display import Display
from variables import FoldersPaths
from buttons import ButtonsGrid

import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()

    icon = QIcon(str(FoldersPaths.WINDOW_ICON_PATH))
    app.setWindowIcon(icon)
    window.setWindowIcon(icon)

    display = Display()
    window.add_widget_to_v_layout(display)

    buttons_grid = ButtonsGrid(display)
    window.v_layout.addLayout(buttons_grid)

    window.adjust_fixed_size()
    window.show()
    app.exec()