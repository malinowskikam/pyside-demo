from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QLabel, QVBoxLayout, QLayout, QWidget, QMessageBox


class MainWidget(QMainWindow):
    _path: Path | None

    _select_button: QPushButton
    _clear_button: QPushButton
    _run_button: QPushButton
    _path_label: QLabel
    _layout: QLayout
    _layout_widget: QWidget

    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(400, 300))
        self.setWindowTitle("PySide Demo")

        self._path = None

        self._select_button = QPushButton("Select")
        self._select_button.clicked.connect(self._on_select_clicked)

        self._clear_button = QPushButton("Clear")
        self._clear_button.clicked.connect(self._on_clear_clicked)

        self._run_button = QPushButton("Run")
        self._run_button.clicked.connect(self._on_run_clicked)

        self._path_label = QLabel()
        self._set_path_to_label()

        self._layout_widget = QWidget()
        self._layout = QVBoxLayout()
        self._layout.addWidget(self._select_button)
        self._layout.addWidget(self._clear_button)
        self._layout.addWidget(self._path_label)
        self._layout.addWidget(self._run_button)
        self._layout_widget.setLayout(self._layout)

        self.setCentralWidget(self._layout_widget)

    def _on_select_clicked(self):
        selected_path = QFileDialog.getExistingDirectory(None, "Select Directory")
        if selected_path:
            self._path = Path(selected_path)
            self._set_path_to_label()

    def _on_clear_clicked(self):
        self._path = None
        self._set_path_to_label()

    def _on_run_clicked(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Run dialog")
        if self._path:
            dialog.setText(f"Running in path: {self._path}")
            dialog.setIcon(QMessageBox.Icon.Information)
        else:
            dialog.setText("No path selected")
            dialog.setIcon(QMessageBox.Icon.Warning)
        _ = dialog.exec()

    def _set_path_to_label(self):
        if self._path:
            self._path_label.setText(str(self._path))
        else:
            self._path_label.setText("Not Selected")
