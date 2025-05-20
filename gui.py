from main import create_dir
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QWidget,
    QMainWindow,
    QLineEdit,
    QCheckBox,
    QComboBox,
    QFileDialog,
    QMessageBox,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPalette, QColor
import os


app = QApplication([])

app.setStyle("Fusion")

palette = QPalette()
palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)

app.setPalette(palette)

window = QMainWindow()
window.setWindowTitle("Project Creator")
window.resize(700, 520)

window.setStyleSheet(
    """
    QMainWindow {
        background-color: #353535;
    }
    QLabel {
        color: white;
        font-size: 14px;
        margin: 5px;
    }
    QLineEdit {
        padding: 8px;
        border: 2px solid #2a82da;
        border-radius: 5px;
        background-color: #191919;
        color: white;
        font-size: 14px;
        margin: 5px;
        min-width: 300px;
    }
    QLineEdit:focus {
        border: 2px solid #42a2da;
    }
    QPushButton {
        background-color: #2a82da;
        color: white;
        border: none;
        padding: 10px;
        border-radius: 5px;
        font-size: 14px;
        margin: 10px;
    }
    QPushButton:hover {
        background-color: #42a2da;
    }
    QPushButton:pressed {
        background-color: #1a72ca;
    }
    QComboBox {
        padding: 8px;
        border: 2px solid #2a82da;
        border-radius: 5px;
        background-color: #191919;
        color: white;
        font-size: 14px;
        margin: 5px;
        min-width: 300px;
    }
    QComboBox::drop-down {
        border: none;
    }
    QComboBox::down-arrow {
        image: none;
        border: none;
    }
    QCheckBox {
        color: white;
        font-size: 14px;
        margin: 5px;
    }
    QCheckBox::indicator {
        width: 18px;
        height: 18px;
    }
    QCheckBox::indicator:unchecked {
        border: 2px solid #2a82da;
        background-color: #191919;
        border-radius: 3px;
    }
    QCheckBox::indicator:checked {
        background-color: #2a82da;
        border: 2px solid #2a82da;
        border-radius: 3px;
    }
"""
)

central_widget = QWidget()
window.setCentralWidget(central_widget)

main_layout = QVBoxLayout(central_widget)
main_layout.setContentsMargins(40, 40, 40, 40)
main_layout.setSpacing(20)

# --- Выбор директории ---
dir_layout = QHBoxLayout()
dir_label = QLabel("Папка для проекта:")
dir_label.setFixedWidth(180)
dir_path_field = QLineEdit()
dir_path_field.setReadOnly(True)
dir_path_field.setPlaceholderText("Не выбрана...")
dir_button = QPushButton("Выбрать папку")
dir_layout.addWidget(dir_label)
dir_layout.addWidget(dir_path_field)
dir_layout.addWidget(dir_button)

# --- Название проекта ---
project_layout = QHBoxLayout()
project_label = QLabel("Название проекта:")
project_label.setFixedWidth(180)
input_field = QLineEdit()
input_field.setPlaceholderText("Введите название вашего проекта")
project_layout.addWidget(project_label)
project_layout.addWidget(input_field)

# --- Архитектура ---
arch_layout = QHBoxLayout()
arch_label = QLabel("Архитектура:")
arch_label.setFixedWidth(180)
arch_combo = QComboBox()
arch_combo.addItem("Чистая архитектура")
arch_layout.addWidget(arch_label)
arch_layout.addWidget(arch_combo)

# --- Чекбокс Redis ---
redis_checkbox = QCheckBox("Использовать Redis")

# --- Чекбокс Docker ---
docker_checkbox = QCheckBox("Использовать Docker")

# --- Кнопка ---
button = QPushButton("Создать проект")

main_layout.addLayout(dir_layout)
main_layout.addLayout(project_layout)
main_layout.addLayout(arch_layout)
main_layout.addWidget(redis_checkbox)
main_layout.addWidget(docker_checkbox)
main_layout.addWidget(button)
main_layout.addStretch()


# --- Логика выбора папки ---
def choose_directory():
    dir_path = QFileDialog.getExistingDirectory(
        window, "Выберите папку для проекта", os.path.expanduser("~")
    )
    if dir_path:
        dir_path_field.setText(dir_path)


dir_button.clicked.connect(choose_directory)


def on_button_click():
    project_name = input_field.text()
    base_path = dir_path_field.text()
    if not project_name or not base_path:
        QMessageBox.warning(
            window, "Ошибка", "Пожалуйста, введите название проекта и выберите папку."
        )
        return
    try:
        create_dir(
            project_name,
            path=base_path,
            is_have_redis=redis_checkbox.isChecked(),
            is_have_docker=docker_checkbox.isChecked(),
        )
        QMessageBox.information(
            window, "Успех", f"Проект '{project_name}' успешно создан!"
        )
    except Exception as e:
        QMessageBox.critical(
            window, "Ошибка", f"Произошла ошибка при создании проекта:\n{e}"
        )


button.clicked.connect(on_button_click)

window.show()
app.exec()
