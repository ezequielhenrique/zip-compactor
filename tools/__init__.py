import zipfile

from PyQt5 import QtWidgets, QtGui
from zipfile import ZipFile
import shutil
import os


class Message(QtWidgets.QMessageBox):
    def __init__(self, parent, text, type_m='error'):
        QtWidgets.QMessageBox.__init__(self, parent)
        self.setParent(parent)
        self.setStyleSheet("QPushButton {background-color: rgb(64, 66, 67); color: rgb(242, 242, 242); "
                           "border-style: solid; font:bold; font-size: 12px; border-width: 1px; border-radius: 10px; "
                           "border-color: rgb(160, 160, 160); border-style: solid; padding: 2px 30px 2px 30px;}")
        if type_m.lower() == 'error':
            self.setIcon(QtWidgets.QMessageBox.Critical)
            self.setText('Erro:')
            self.setWindowTitle('Error')
        elif type_m.lower() == 'info':
            self.setIcon(QtWidgets.QMessageBox.Information)
            self.setText('Info:')
            self.setWindowTitle('Information')
        self.setInformativeText(text)


def get_files_and_dirs(parent=None, caption='', directory='', filters='', initial_filter='', options=None):
    def update_text():
        # update the contents of the line edit widget with the selected files
        selected = []
        for index in view.selectionModel().selectedRows():
            selected.append('"{}"'.format(index.data()))
        lineEdit.setText(' '.join(selected))

    def folders_in(path_to_parent):
        for file_name in os.listdir(path_to_parent):
            if os.path.isdir(os.path.join(path_to_parent, file_name)):
                yield os.path.join(path_to_parent, file_name)

    dialog = QtWidgets.QFileDialog(parent)
    dialog.setWindowTitle(caption)
    dialog.setFileMode(dialog.ExistingFiles)
    dialog.setStyleSheet("border-color: rgb(160, 160, 160);\n"
                         "border-width: 1px;\n"
                         "border-style: solid;")

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
    view.selectionModel().selectionChanged.connect(update_text)

    lineEdit = dialog.findChild(QtWidgets.QLineEdit)
    # clear the line edit contents whenever the current directory changes
    dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

    dialog.exec_()
    folders_in(dialog.selectedFiles())

    return dialog.selectedFiles()


def create_zip(filename_save, file_paths):
    with ZipFile(filename_save, 'w', zipfile.ZIP_DEFLATED) as zip_file:  # writing files to a zipfile
        for path in file_paths:
            if os.path.isfile(path):                # if path is a file
                path = os.path.basename(path)
                zip_file.write(path)            # add file in a zip

            if os.path.isdir(path):                 # if path is a directory
                dir_name = os.path.basename(path)
                for root, directories, files in os.walk(path):      # walk through the full directory
                    for filename in files:
                        complete_path = os.path.normpath(os.path.join(root, filename))
                        list_path = complete_path.split(os.sep)     # convert the path in a list

                        while list_path[0] != dir_name:     # delete the super directory
                            list_path.pop(0)

                        resume_path = os.path.join(*list_path)      # convert the list in a path
                        zip_file.write(complete_path, resume_path)
