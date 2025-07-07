from variables import ConfigStyles

from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget

class Button(QPushButton):
    def __init__(self, text: str, parent: QWidget | None = None, *args, **kwargs):
        super().__init__(text, parent, *args, **kwargs)
        self.config_style()

    def config_style(self):
        self.setStyleSheet(f'font-size: {ConfigStyles.MEDIUM_FONT_SIZE}px;')
        self.setMinimumSize(65, 65)

class ButtonsGrid(QGridLayout):
    def __init__(self, display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.display = display

        self._OPERATORS = ['^', '*', '/', '+', '-']
        self._EQUALS = '='
        self._CLEAR = 'C'
        self._BACKSPACE = '←'

        self._grid_mask = [
            [self._CLEAR, self._BACKSPACE, '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '+'],
            ['1', '2', '3', '-'],
            ['', '0', '.', self._EQUALS]
        ]

        self._make_grid()

    def _make_grid(self):
        for row_number, row in enumerate(self._grid_mask):
            for column_number, button_text in enumerate(row):
                button = Button(button_text)
                self.addWidget(button, row_number, column_number)
                button.clicked.connect(lambda _, b=button: self._insert_button_to_display(b))

    def _insert_button_to_display(self, button):
        button_text = button.text()
        current_text = self.display.text()

        if button_text == self._CLEAR:
            self.display.setText('')
            return
        
        if button_text == self._BACKSPACE:
            new_text = self.display.text()[:-1]
            self.display.setText(new_text)
            return
        
        if not current_text and button_text in self._OPERATORS:
            return

        if current_text and current_text[-1] in self._OPERATORS and \
           button_text in self._OPERATORS:
            self.display.setText(current_text[:-1] + button_text)
            return
        
        if button_text == self._EQUALS:
            if not current_text:
                return
            try:
                math_expression = current_text.replace('^', '**')
                result = eval(math_expression)
                self.display.setText(str(result))

            except Exception:
                self.display.setText('Err')
            return
        
        if current_text == 'Err':
            self.display.setText('')

        new_text = self.display.text() + button_text
        self.display.setText(new_text)