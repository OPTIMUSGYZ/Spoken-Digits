import os

path = os.path.abspath(__file__)
path = path[:-23]
path = path.replace(' ', '\ ')
os.system('pyside6-uic ' + path + 'Qt_GUI/form.ui > MainUI.py')
