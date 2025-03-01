import sys
import math
import PyQt5.QtWidgets as pyqt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QValidator, QIcon, QDoubleValidator
from engine import on_click , on_converter 



app = pyqt.QApplication(sys.argv)

window = pyqt.QMainWindow()
window.setWindowTitle("anCoder Calculator with Python pyQt")
window.setGeometry(100,100,450,550)
window.setMaximumSize(700,600)
window.setWindowIcon(QIcon('icon.png'))

widget = pyqt.QWidget()
window.setCentralWidget(widget)

main_layout = pyqt.QHBoxLayout()

left_layout = pyqt.QVBoxLayout()
# left_layout.setAlignment(Qt.AlignTop)
right_layout = pyqt.QVBoxLayout()

main_layout.addLayout(left_layout,3)
main_layout.addLayout(right_layout,2)

widget.setLayout(main_layout)


# Right side seciton ------------------------
history = []

history_display = pyqt.QTextEdit("You Previos All History ›")
history_display.hide()


clear_history = pyqt.QPushButton('Clear History')
clear_history.setFixedSize(70, 20)
clear_history.hide()
clear_history.clicked.connect(lambda checked, v='RESET': on_click(v, display, result_label, history_display, history))
clear_history.setStyleSheet(
        """
        QPushButton{ 
            color:#000;
            border-radius:5px; 
            margin-right:0px;
        }
        QPushButton:hover{
            background-color: #D2D0CF;
         }
         QPushButton:pressed{
            background-color:#E1DFDE;
         }
        """
    )
right_layout.addWidget(clear_history)
right_layout.addWidget(history_display)

# left side seciton ------------------------

# Converter Buttons and History toggle button
converter_layout = pyqt.QHBoxLayout()
converter_layout.setAlignment(Qt.AlignTop)
converter_buttons = ['Dec-Bin','Bin-Dec','Dec-Oct','Oct-Dec','Dec-Hex','Hex-Dec','History']
for text in converter_buttons:
    btn = pyqt.QPushButton(text)
    btn.setFont(QFont('Arial', 8))
    btn.setFixedSize(50, 20)
    btn.clicked.connect(lambda checked, v=text: on_converter(v, display, result_label, history_display, history,window,clear_history))
    btn.setStyleSheet(
        """
        QPushButton{ 
            color:#000;
            border-radius:5px; 
        }
        QPushButton:hover{
            background-color: #D2D0CF;
         }
         QPushButton:pressed{
            background-color:#E1DFDE;
         }
        """
    )
    converter_layout.addWidget(btn)

left_layout.addLayout(converter_layout)

# Entry Field Box 
display = pyqt.QLineEdit(window)
display.setAlignment(Qt.AlignTop)
display.setReadOnly(False)
valdation = QDoubleValidator()
valdation.setNotation(QDoubleValidator.StandardNotation)
# valdidation.setNotation(Qt.VQValidator.StandardNotation)
# valdidation.setNotation(Qt.QV)
display.setValidator(valdation)
 
left_layout.addWidget(display)

# Result Live show seciton
result_label = pyqt.QLabel('=')
result_label.setAlignment(Qt.AlignRight)
left_layout.addWidget(result_label)



# Calculator Keyboard section
keyboard_layout = pyqt.QGridLayout()
keyboard_layout.setAlignment(Qt.AlignBottom)
left_layout.addLayout(keyboard_layout)
 

buttons = [
    ('(', ')', '⇄', 'AC', '⌫'),  # Trigonometry and clear functions
    ('sin', 'cos', 'tan', 'mod', '!'),  # Parentheses, Pi, modulo, and factorial
    ('log', '7', '8', '9', '÷'),  # Logarithm, numbers, and division
    ('⌃', '4', '5', '6', '×'),  # Power function and multiplication
    ('√', '1', '2', '3', '-'),  # Square root and subtraction
    ('π', '0', '.', '=', '+'),  # Reset, numbers, decimal, equals, and addition
     # Fraction Converter (<> changed to ⇄ for clarity)
]


def create_keyboard(buttons, layout):
    for row, values in enumerate(buttons):
        for col, value in enumerate(values):
            btn = pyqt.QPushButton(value)
            btn.setFont(QFont('Arial', 12))
            btn.setFixedSize(80, 40)
            btn.clicked.connect(lambda checked, v=value: on_click(v, display, result_label, history_display, history))
            btn.setStyleSheet(
                """
                QPushButton{ 
                    background-color:#D2D0CF;
                    color:#000;
                    border-radius:8px; 
                    border: 1px solid #6b6a68;
                }
                QPushButton:hover{
                    background-color: #acaca9;
                }
                QPushButton:pressed{
                    background-color:#acaca9;
                }
                """
            )
            layout.addWidget(btn, row + 1, col)

 
# Apply styles
def apply_styles():
    window.setStyleSheet("background-color: #F8FAFF;")  
    display.setStyleSheet("background-color: #F8FAFF; border: 1px solid #888; height:80px ; border-radius: 5px; font-size: 18px; padding:5px")
    result_label.setStyleSheet("color: #333; font-size: 14px;")
    history_display.setStyleSheet("background-color: transparent; border: 1px solid #bdc3c7; padding:5px; border-radius:5px")


#  Calling the keybard
create_keyboard(buttons,keyboard_layout)
# calling the to style the layout keyboad and entry filedn and window and result labal
apply_styles()





window.show()
sys.exit(app.exec_())