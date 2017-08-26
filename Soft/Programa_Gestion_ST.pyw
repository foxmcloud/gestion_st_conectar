#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
from MenuPrincipal import MenuPrincipal
#from PyQt4 import QtGui
#import Modulos.ST.Escribir_Parque
#from Forms.MenuPrincipalST import *
from PyQt4 import QtGui#from Login import *

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    QtGui.QApplication.addLibraryPath('C:\Python34\Lib\site-packages\PyQt4\plugins')
    myapp = MenuPrincipal()
    myapp.show()
    sys.exit(app.exec_())
