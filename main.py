from PyQt5 import QtWidgets
from zip_compactor_design import Ui_MainWindow
from tools import getOpenFilesAndDirs, Message
from zipfile import ZipFile, ZIP_DEFLATED
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
        self.ui.list_view.clear()

        self.files = getOpenFilesAndDirs()
        for path in self.files:
            self.ui.list_view.addItem(str(path))

    def compact_to_zip(self):
        try:
            path_save = QtWidgets.QFileDialog.getSaveFileName(filter='*.zip')
            zip_dir = pathlib.Path(os.path.split(path_save[0])[1]).stem
            files_to_compact = list()
            for index in range(self.ui.list_view.count()):
                files_to_compact.append(self.ui.list_view.item(index).text())

            with ZipFile(path_save[0], 'w', ZIP_DEFLATED) as zipObj:
                for file in files_to_compact:
                    if os.path.isdir(file):
                        folder = os.path.basename(file)
                        for folder_name, sub_folders, filenames in os.walk(file):
                            for filename in filenames:
                                file_path = os.path.join(folder_name, filename)
                                file_zip = os.path.join(folder, filename)
                                zipObj.write(file_path, os.path.join(zip_dir, file_zip), ZIP_DEFLATED)
                    elif os.path.isfile(file):
                        zipObj.write(file, os.path.join(zip_dir, os.path.split(file)[1]), ZIP_DEFLATED)

            msg = Message(self, 'Arquivo criado com sucesso!', type_m='info')
            msg.show()
        except Exception as error:
            print(error)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())
