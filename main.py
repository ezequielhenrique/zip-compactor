from PyQt5 import QtWidgets
from designs.window_design import Ui_MainWindow
from tools import getOpenFilesAndDirs, Message, create_zip
import os
import pathlib


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_select.clicked.connect(self.select_paste)
        self.ui.button_converter.clicked.connect(self.compact_to_zip)

        self.files = None

    def select_paste(self):
        try:
            self.ui.list_view.clear()

            self.files = getOpenFilesAndDirs()
            for path in self.files:
                self.ui.list_view.addItem(str(path))
        except Exception as error:
            msg = Message(self, str(error))
            msg.show()

    def compact_to_zip(self):
        try:
            if self.ui.list_view.count() != 0:

                path_save = QtWidgets.QFileDialog.getSaveFileName(filter='*.zip')
                zip_dir = pathlib.Path(os.path.split(path_save[0])[1]).stem
                files_to_compact = list()

                for index in range(self.ui.list_view.count()):
                    files_to_compact.append(self.ui.list_view.item(index).text())

                part_progress = 100 / len(files_to_compact)

                # function create zip
                create_zip(path_save[0], files_to_compact, zip_dir)

                self.ui.progress_bar.setValue(100)
                msg = Message(self, 'Successfully created file!', type_m='info')
                msg.show()
                self.ui.progress_bar.setValue(0)
                self.ui.list_view.clear()
            else:
                msg_add = Message(self, 'Select files to compress', type_m='info')
                msg_add.show()
        except FileNotFoundError:
            pass
        except Exception as error:
            msg = Message(self, str(error))
            msg.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())
