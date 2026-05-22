import math
import sys  
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QRadioButton, QComboBox, QLineEdit, QPushButton, QLabel, QButtonGroup)
from PyQt5.QtCore import Qt


class MinimalistCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Calculator Functii Speciale")
        self.setFixedSize(350, 380)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(25, 25, 25, 25)
        
        cat_layout = QHBoxLayout()
        self.radio_trig = QRadioButton("Trigonometrie")
        self.radio_log = QRadioButton("Logaritmi")
        self.radio_trig.setChecked(True)
        
        self.btn_group = QButtonGroup()
        self.btn_group.addButton(self.radio_trig)
        
        self.btn_group.addButton(self.radio_log)
        cat_layout.addWidget(self.radio_trig)
        cat_layout.addWidget(self.radio_log)
        cat_layout.setAlignment(self.radio_log, Qt.AlignRight)
        self.radio_trig.toggled.connect(self.update_functions)
        
        self.func_combo = QComboBox()
        self.func_combo.addItems(["sin(x)", "cos(x)", "tan(x)", "cot(x)"])
        self.func_combo.currentIndexChanged.connect(self.update_placeholderText)
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Introduceți valoarea x ...")    
        self.input_field.setAlignment(Qt.AlignCenter)
        self.input_field.returnPressed.connect(self.calculate)
        self.calc_button = QPushButton("Calculează")
        self.calc_button.clicked.connect(self.calculate)
        self.clear_button = QPushButton("Resetează")
        self.clear_button.clicked.connect(self.clear_form)
        self.result_label = QLabel("Rezultat: ")
        self.result_label.setObjectName("resultLabel")
        self.result_label.setAlignment(Qt.AlignCenter)
        
        main_layout.addLayout(cat_layout)
        main_layout.addWidget(self.func_combo)  
        main_layout.addWidget(self.input_field)
        main_layout.addStretch()
        main_layout.addWidget(self.calc_button)
        main_layout.addWidget(self.clear_button)
        main_layout.addWidget(self.result_label)
        self.setLayout(main_layout)
        self.apply_stylesheet()
        

    def update_functions(self):
        if self.radio_trig.isChecked():
            self.func_combo.clear()
            self.func_combo.addItems(["sin(x)", "cos(x)", "tan(x)", "cot(x)"])
            self.update_placeholderText()
        else:
            self.func_combo.clear()
            self.func_combo.addItems(["log10(x)", "ln(x)", "log2(x)"])
        self.update_placeholderText()    

    def clear_form(self):
        self.input_field.clear()
        self.result_label.setText("")
        self.result_label.setStyleSheet("") 
    
    def _set_error(self, message: str):
        self.result_label.setText(f"Eroare: {message}")
        self.result_label.setStyleSheet("color: red;")    

    def calculate(self):
        text_value = self.input_field.text().strip()
        try:
            x = float(text_value)
            func = self.func_combo.currentText()
            result = 0.0
          
            if func in ["sin(x)", "cos(x)", "tan(x)", "cot(x)"]:
                radians = math.radians(x)
                if func == "sin(x)":
                    result = math.sin(radians)
                elif func == "cos(x)":
                    result = math.cos(radians)
                elif func == "tan(x)":
                    if math.cos(radians) == 0:
                        raise ZeroDivisionError("Tangenta nu este definită pentru acest unghi.")
                    result = math.tan(radians)
                elif func == "cot(x)":
                    if math.tan(radians) == 0:
                        raise ZeroDivisionError("Cotangenta nu este definită pentru acest unghi.")
                    result = 1 / math.tan(radians)
            else:
                if x <= 0:
                    raise ValueError("Logaritmul nu este definit pentru x<0.")
                if func == "log10(x)":
                    result = math.log10(x)
                elif func == "ln(x)":
                    result = math.log(x)
                elif func == "log2(x)":
                    result = math.log2(x)
            self.result_label.setText(f"Rezultat: {result:.4f}")
            self.result_label.setStyleSheet("color: blue;")
        except ValueError as ve:
            if "could not convert" in str(ve) or "invalid literal" in str(ve):
                self._set_error("Introduceți o valoare numerică validă.")
            else:
                self._set_error(str(ve))
        except ZeroDivisionError as e:
            self._set_error(str(e))

        except Exception as e:
            self._set_error(f"A apărut o problemă neașteptată: {e}")
            
    def update_placeholderText(self):
        if self.radio_trig.isChecked():
            self.input_field.setPlaceholderText("Introduceti valoarea x in grade...")
        else:
            self.input_field.setPlaceholderText("Introduceti valoarea x...")
            
    def apply_stylesheet(self):
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                font-family: Segoe UI, sans-serif;
                color: #cdd6f4;
            }
            QLabel {
                font-size: 14px;
                color: #cdd6f4;
            }
            QRadioButton {
                font-size: 14px;
                color: #cdd6f4;
            }
            QComboBox, QLineEdit {
                background-color: #313244;
                border: 1px solid #45475a;
                border-radius: 6px;
                padding: 10px;
                color: #cdd6f4;
            }
            QComboBox::drop-down {
                border: none;
            }
            QPushButton {
                font-size: 14px;
                padding: 10px;
                background-color: #1565c0;
                color: white;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0d47a1;
            }
            QPushButton:pressed {
                background-color: #082b6b;
            }
            QLabel#resultLabel {
                font-size: 15px;
                border-radius: 6px;
                padding: 4px 0;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
            }
            QRadioButton::indicator:unchecked {
                border: 2px solid #45475a;
                border-radius: 9px;
                background-color: #1e1e1e;
            }
            QRadioButton::indicator:checked {
                border: 2px solid #1565c0;
                border-radius: 9px;
                background-color: #1565c0;
            }
        """)     
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = MinimalistCalculator()
    calc.show()
    sys.exit(app.exec_())
                