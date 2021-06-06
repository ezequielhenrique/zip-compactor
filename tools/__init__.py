from PyQt5 import QtWidgets, QtGui
from zipfile import ZipFile, ZIP_DEFLATED
import os


class Message(QtWidgets.QMessageBox):
    def __init__(self, parent, text, type_m='error'):
        QtWidgets.QMessageBox.__init__(self, parent)
        self.setParent(parent)
        self.setStyleSheet("QPushButton {background-color: rgb(166, 166, 166); color: rgb(64, 64, 64); "
                           "border-style: solid; font:bold; font-size: 12px; border-width: 2px; border-radius: 10px; "
                           "border-color: rgb(115, 115, 115); border-style: solid; padding: 2px 30px 2px 30px;}")
        if type_m.lower() == 'error':
            self.setIcon(QtWidgets.QMessageBox.Critical)
            self.setText('Erro:')
            self.setWindowTitle('Error')
        elif type_m.lower() == 'info':
            self.setIcon(QtWidgets.QMessageBox.Information)
            self.setText('Info:')
            self.setWindowTitle('Information')
        self.setInformativeText(text)


def getOpenFilesAndDirs(parent=None, caption='', directory='', filters='', initial_filter='', options=None):
    def updateText():
        # update the contents of the line edit widget with the selected files
        selected = []
        for index in view.selectionModel().selectedRows():
            selected.append('"{}"'.format(index.data()))
        lineEdit.setText(' '.join(selected))

    # dialog = QtWidgets.QFileDialog(parent, windowTitle=caption)
    dialog = QtWidgets.QFileDialog()
    dialog.setFileMode(dialog.ExistingFiles)

    directory = os.path.dirname(os.path.realpath(__file__))
    parent_directory = os.path.split(directory)[0] + '/images'
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(f"{parent_directory}/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    dialog.setWindowIcon(icon)

    if options:
        dialog.setOptions(options)
    dialog.setOption(dialog.DontUseNativeDialog, True)
    if directory:
        dialog.setDirectory(directory)
    if filters:
        dialog.setNameFilter(filters)
        if initial_filter:
            dialog.selectNameFilter(initial_filter)

    # by default, if a directory is opened in file listing mode,
    # QFileDialog.accept() shows the contents of that directory, but we
    # need to be able to "open" directories as we can do with files, so we
    # just override accept() with the default QDialog implementation which
    # will just return exec_()
    dialog.accept = lambda: QtWidgets.QDialog.accept(dialog)

    # there are many item views in a non-native dialog, but the ones displaying
    # the actual contents are created inside a QStackedWidget; they are a
    # QTreeView and a QListView, and the tree is only used when the
    # viewMode is set to QFileDialog.Details, which is not this case
    stackedWidget = dialog.findChild(QtWidgets.QStackedWidget)
    view = stackedWidget.findChild(QtWidgets.QListView)
    view.selectionModel().selectionChanged.connect(updateText)

    lineEdit = dialog.findChild(QtWidgets.QLineEdit)
    # clear the line edit contents whenever the current directory changes
    dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

    dialog.exec_()
    folders_in(dialog.selectedFiles())
    # print list(folders_in(dialog.selectedFiles()))
    return dialog.selectedFiles()


def folders_in(path_to_parent):
    for file_name in os.listdir(path_to_parent):
        if os.path.isdir(os.path.join(path_to_parent, file_name)):
            yield os.path.join(path_to_parent, file_name)


def create_zip(path, list_files, zip_dir):
    with ZipFile(path, 'w', ZIP_DEFLATED) as zipObj:
        for file in list_files:
            if os.path.isdir(file):
                folder = os.path.basename(file)
                for folder_name, sub_folders, filenames in os.walk(file):
                    for filename in filenames:
                        file_path = os.path.join(folder_name, filename)
                        file_zip = os.path.join(folder, filename)
                        zipObj.write(file_path, os.path.join(zip_dir, file_zip), ZIP_DEFLATED)
            elif os.path.isfile(file):
                zipObj.write(file, os.path.join(zip_dir, os.path.split(file)[1]), ZIP_DEFLATED)
