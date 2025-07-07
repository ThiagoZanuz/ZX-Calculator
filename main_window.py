from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)
        self.setWindowTitle('Calculator GUI')

    def adjust_fixed_size(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())

    def add_widget_to_v_layout(self, widget: QWidget):
        self.v_layout.addWidget(widget)