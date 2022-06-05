from PyQt5 import QtWidgets, QtGui
from designs.main_window_design import Ui_MainWindow
from tools import get_files_and_dirs, Message, create_zip


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.button_select.clicked.connect(self.select_paste)
        self.ui.button_converter.clicked.connect(self.compact_to_zip)
        self.ui.button_extract.clicked.connect(self.extract_files)

        self.files = None

    def select_paste(self):
        try:
            self.files = get_files_and_dirs(self, caption='Select files and dirs')

            if len(self.files) > 0:
                self.ui.list_view.clear()
                for i in range(len(self.files)):
                    item = QtWidgets.QListWidgetItem()
                    if i % 2 == 0:
                        item.setBackground(QtGui.QColor("#3C3C3C"))
                    item.setText(str(self.files[i]))
                    self.ui.list_view.addItem(item)

        except Exception as error:
            msg = Message(self, str(error))
            msg.show()

    def compact_to_zip(self):
        try:
            if self.ui.list_view.count() > 0:

                path_save = QtWidgets.QFileDialog.getSaveFileName(filter='*.zip')
                files_to_compact = list()

                for index in range(self.ui.list_view.count()):
                    files_to_compact.append(self.ui.list_view.item(index).text())

                zip_filename = path_save[0]
                create_zip(zip_filename, files_to_compact)

                msg = Message(self, 'Successfully created file!', type_m='info')
                msg.show()
                self.ui.list_view.clear()
            else:
                msg_add = Message(self, 'Select files to compress', type_m='info')
                msg_add.show()
        except FileNotFoundError:
            pass
        except Exception as error:
            msg = Message(self, str(error))
            msg.show()

    def extract_files(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec_())
