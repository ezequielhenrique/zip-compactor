from PyQt5 import QtWidgets
from zip_compactor_design import Ui_MainWindow
from tools import getOpenFilesAndDirs, Message
from zipfile import ZipFile, ZIP_DEFLATED


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
        import os
        path_save = QtWidgets.QFileDialog.getSaveFileName(filter='*.zip')
        files_to_compact = list()
        for index in range(self.ui.list_view.count()):
            files_to_compact.append(self.ui.list_view.item(index).text())

        with ZipFile(path_save[0], 'w', ZIP_DEFLATED) as zipObj:
            for file in files_to_compact:
                zipObj.write(os.path.split(file)[1])

        #with ZipFile(path_save[0], 'w') as zipObj:
        #    for folder_name, sub_folders, filenames in os.walk(self.files):
        #        print(filenames)
        #        for filename in filenames:
        #            print(filename)
        #            file_path = os.path.join(folder_name, filename)
        #            zipObj.write(file_path, os.path.basename(file_path))
        msg = Message(self, 'Arquivo criado com sucesso!', type_m='info')
        msg.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())
