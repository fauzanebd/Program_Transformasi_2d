# -*- coding: utf-8 -*-

"""
Kode Main Window untuk program transformasi 2D
Fauzan Abdillah
19/444049/TK/49245
Teknologi Informasi
"""


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import matplotlib
matplotlib.use('Qt5Agg')
from functools import partial

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import dialogTranslasi
import dialogRotasi
import dialogScaling
import dialogShearingX
import dialogShearingY
import numpy as np

from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt


class Ui_MainWindow(object):

    # inisialisasi variable variable
    numberOfNodes = 0
    dictOfNodes = {}
    savedStep = []
    savedTransform = []
    textContent = []
    sc = None

    # fungsi ui mainwindow
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Program Transformasi Bangun 2D - Fauzan Abdillah")
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(667, 467)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #canvas baruuu
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, MainWindow)
        self.plotLayout = QVBoxLayout()
        self.plotLayout.addWidget(self.toolbar)
        self.plotLayout.addWidget(self.canvas)

        # widget untuk gambar
        self.PlotWidget = QtWidgets.QWidget(self.centralwidget)
        self.PlotWidget.setGeometry(QtCore.QRect(270, 60, 371, 331))
        self.PlotWidget.setObjectName("PlotWidget")
        self.PlotWidget.setLayout(self.plotLayout)

        # setting button untuk menampilkan gambar
        self.btnTampilGambar = QtWidgets.QPushButton(self.centralwidget)
        self.btnTampilGambar.setGeometry(QtCore.QRect(130, 240, 121, 23))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.btnTampilGambar.setFont(font)
        self.btnTampilGambar.setObjectName("btnTampilGambar")

        # setting button horizontal: hapus gambar sama hapus transformasi
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(270, 410, 371, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.btHapusGambar = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.btHapusGambar.setFont(font)
        self.btHapusGambar.setObjectName("btHapusGambar")
        self.horizontalLayout.addWidget(self.btHapusGambar)
        self.btHapusGambar.clicked.connect(self.HapusBangun)

        self.btHapusTransformasi = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.btHapusTransformasi.setFont(font)
        self.btHapusTransformasi.setObjectName("btHapusTransformasi")
        self.horizontalLayout.addWidget(self.btHapusTransformasi)
        self.btHapusTransformasi.clicked.connect(self.HapusTransformasi)

        # GroupBox button transformasi
        self.TransformGB = QtWidgets.QGroupBox(self.centralwidget)
        self.TransformGB.setGeometry(QtCore.QRect(30, 270, 221, 171))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.TransformGB.setFont(font)
        self.TransformGB.setObjectName("TransformGB")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.TransformGB)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 20, 221, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # setting button translasi
        self.btTranslasi = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.btTranslasi.setFont(font)
        self.btTranslasi.setObjectName("btTranslasi")
        self.verticalLayout_2.addWidget(self.btTranslasi)
        self.btTranslasi.clicked.connect(self.TranslasiDialog)

        #setting button rotasi
        self.btRotasi = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.btRotasi.setFont(font)
        self.btRotasi.setObjectName("btRotasi")
        self.verticalLayout_2.addWidget(self.btRotasi)
        self.btRotasi.clicked.connect(self.RotasiDialog)

        #setting button scaling
        self.btScaling = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.btScaling.setFont(font)
        self.btScaling.setObjectName("btScaling")
        self.verticalLayout_2.addWidget(self.btScaling)
        self.btScaling.clicked.connect(self.ScalingDialog)

        #setting button shearing x
        self.btShearingX = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.btShearingX.setFont(font)
        self.btShearingX.setObjectName("btShearingX")
        self.verticalLayout_2.addWidget(self.btShearingX)
        self.btShearingX.clicked.connect(self.ShearingXDialog)

        #setting button shearing y
        self.btShearingY = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.btShearingY.setFont(font)
        self.btShearingY.setObjectName("btShearingY")
        self.verticalLayout_2.addWidget(self.btShearingY)
        self.btShearingY.clicked.connect(self.ShearingYDialog)

        # label2 judul dkk
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(390, 20, 251, 21))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        # text instruksi
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 60, 221, 91))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        # input plaintext
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(30, 180, 221, 51))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnTampilGambar.clicked.connect(self.gambarAwal)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnTampilGambar.setText(_translate("MainWindow", "Tampilkan Gambar"))
        self.btHapusGambar.setText(_translate("MainWindow", "Hapus Bangun"))
        self.btHapusTransformasi.setText(_translate("MainWindow", "Hapus Transformasi"))
        self.TransformGB.setTitle(_translate("MainWindow", "Pilih Jenis Transformasi"))
        self.btTranslasi.setText(_translate("MainWindow", "Translasi"))
        self.btRotasi.setText(_translate("MainWindow", "Rotasi"))
        self.btScaling.setText(_translate("MainWindow", "Scaling"))
        self.btShearingX.setText(_translate("MainWindow", "Shearing X"))
        self.btShearingY.setText(_translate("MainWindow", "Shearing Y"))
        self.label.setText(_translate("MainWindow", "Program Transformasi 2D"))
        self.label_2.setText(_translate("MainWindow", "Fauzan Abdillah (19/444049/TK/49245)"))
        self.label_3.setText(_translate("MainWindow", "Input di sini"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei UI\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">INSTRUKSI</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Masukkan posisi titik-titik bangun pada bidang koordinat dengan ketentuan sebagai berikut:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Satu titik di dalam satu tanda kurung</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Pisahkan x dan y dengan tanda koma</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">- Pisahkan antar titik dengan spasi</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Contoh:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">segitiga yang terletak pada</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">A(2,3), B(5,5), dan C(3,4) diinputkan sebagai berikut:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">(2,3) (5,5) (3,4)</span></p></body></html>"))

    # fungsi untuk mendapatkan titik titik koordinat dari input plainTextEdit
    def getCoordinate(self):
        self.textContent = []
        self.textContent.append(self.plainTextEdit.toPlainText())
        allNodes = self.plainTextEdit.toPlainText().split()

        # dictOfNodes adalah variable untuk menyimpan titik awal bangun
        self.dictOfNodes = {'x': [],
                            'y': []}
        for i in range(len(allNodes)):
            allNodes[i] = allNodes[i].translate({ord(c): None for c in '( )'})
        for i in allNodes:
            try:
                x,y = i.split(',')
                self.dictOfNodes['x'].append(int(x))
                self.dictOfNodes['y'].append(int(y))
            except:
                import errorInputDialog
                errorDialog = QtWidgets.QDialog()
                errorDialog.setWindowTitle("Error!")
                error_ui = errorInputDialog.Ui_Dialog()
                error_ui.setupUi(errorDialog)
                error_ui.pushButton.clicked.connect(errorDialog.close)
                errorDialog.exec_()
                break

    # fungsi untuk menggambar bangun di awal (belum ditransformasi)
    def gambarAwal(self):
        if len(self.savedStep) < 2:
            self.savedTransform = []
            self.getCoordinate()
            self.figure.clear()
            ax = self.figure.add_subplot(111)
            ax.fill(self.dictOfNodes['x'], self.dictOfNodes['y'])
            self.canvas.draw()
            self.savedTransform.append(self.dictOfNodes)
            self.savedStep.append('inisiasi bangun 2D awal')
            self.plainTextEdit.setReadOnly(False)
        else:
            pass

    # fungsi untuk menggambar bangun hasil transformasi
    def gambarTransformasi(self, title):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        self.figure.suptitle(title, fontsize=6)
        ax.fill(self.savedTransform[-1]['x'], self.savedTransform[-1]['y'])
        self.canvas.draw()
        self.plainTextEdit.setReadOnly(True)
        self.textContent.append(self.savedStep[-1])
        result = []
        for i in range(len(self.savedTransform[-1]['x'])):
            a = self.savedTransform[-1]['x'][i]
            b = self.savedTransform[-1]['y'][i]
            result.append("({},{})".format(a,b))
        self.textContent.append("result: {}".format(" ".join(result)))
        self.plainTextEdit.setPlainText('\n'.join(self.textContent))

    #fungsi untuk merubah bentuk data titik koordinat jadi array of matrix
    def dict_to_matrix(self, dict):
        nodes_matrix = []
        for i in range(len(dict['x'])):
            nodes_matrix.append(
                np.array([[dict['x'][i]], [dict['y'][i]]])
            )
        return nodes_matrix

    #fungsi untuk ui dialog translasi
    def TranslasiDialog(self):

        self.translasiDialog = QtWidgets.QDialog()
        self.translasiDialog.setWindowTitle("Translasi")
        self.translasiDialog.setObjectName("Translasi")
        self.translasi_ui = dialogTranslasi.Ui_Dialog()
        self.translasi_ui.setupUi(self.translasiDialog)

        self.translasi_ui.buttonBox.accepted.connect(self.translasiDialog.close)
        self.translasi_ui.buttonBox.accepted.connect(self.Translasi)
        self.translasi_ui.buttonBox.rejected.connect(self.translasiDialog.close)
        self.translasiDialog.exec_()

    #fungsi translasi
    def Translasi(self):
        try:
            # jarak x dan y didapatakan dari input
            jarakX = int(self.translasi_ui.inputJarakX.text())
            jarakY = int(self.translasi_ui.inputJarakY.text())
            at_x = jarakX
            at_y = jarakY
            nodes = self.savedTransform[-1]

            # matriks transformasi untuk trnaslasi
            trans_matrix = np.array([[at_x], [at_y]])
            nodes_matrix = self.dict_to_matrix(nodes)

            # matriks transformasi ditambah matriks titik pada bangun
            result = nodes_matrix + trans_matrix
            result_dict = {'x': [],
                           'y': []}
            for i in result:
                result_dict['x'].append(i[0][0])
                result_dict['y'].append(i[1][0])
            self.savedTransform.append(result_dict)
            self.savedStep.append("transformasi {} satuan ke arah X dan {} satuan ke arah Y".format(jarakX, jarakY))
            self.gambarTransformasi(
                "Posisi bangun 2D setelah ditranslasi\n{} satuan ke arah X dan {} satuan ke arah Y".format(jarakX, jarakY))
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Input bukan angka')
            error_dialog.exec_()


    def RotasiDialog(self):

        self.rotasiDialog = QtWidgets.QDialog()
        self.rotasiDialog.setWindowTitle("Rotasi")
        self.rotasiDialog.setObjectName("Rotasi")
        self.rotasi_ui = dialogRotasi.Ui_Dialog()
        self.rotasi_ui.setupUi(self.rotasiDialog)

        self.rotasi_ui.buttonBox.accepted.connect(self.rotasiDialog.close)
        self.rotasi_ui.buttonBox.accepted.connect(self.Rotasi)
        self.rotasi_ui.buttonBox.rejected.connect(self.rotasiDialog.close)
        self.rotasiDialog.exec_()

    # fungsi untuk rotasi
    def Rotasi(self):
        try:
            # nilai derajat dan titik putar diambil dari input dari dialog rotasi
            degree = int(self.rotasi_ui.inputSudut.text())
            origin = (int(self.rotasi_ui.inputPusatX.text()), int(self.rotasi_ui.inputPusatY.text()))

            # penghitungan cos dan sin menggunakan library numpy
            e1 = np.cos(np.deg2rad(degree))
            e2 = np.sin(np.deg2rad(degree))

            # matrix trig adalah matrix untuk transformasi rotasi
            trig = np.array([[e1, -e2], [e2, e1]])

            # point_matrix adalah matrix kumpulan titik yang dimiliki bangun
            point_matrix = self.dict_to_matrix(self.savedTransform[-1])
            first = []

            # dilakukan perkalian dot product, menggunakan library numpy
            # tidak lupa dikurangi terlebih dahulu oleh titik asal
            for i in point_matrix:
                first.append(np.dot(trig, i - np.array([[origin[0]], [origin[1]]])))
            result = first + np.array([[origin[0]], [origin[1]]])
            result_dict = {'x':[],
                           'y':[]}
            for i in result:
                result_dict['x'].append(i[0][0])
                result_dict['y'].append(i[1][0])
            self.savedTransform.append(result_dict)
            self.savedStep.append("rotasi dengan sudut {} derajat dengan titik putar di ({},{})".format(degree, origin[0], origin[1]))
            self.gambarTransformasi(
                "Posisi bangun 2D setelah dirotasi dengan sudut {} derajat\ndengan titik putar di ({},{})".format(degree, origin[0], origin[1]))
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Input bukan angka')
            error_dialog.exec_()

    def ScalingDialog(self):

        self.scalingDialog = QtWidgets.QDialog()
        self.scalingDialog.setWindowTitle("Scaling")
        self.scalingDialog.setObjectName("Scaling")
        self.scaling_ui = dialogScaling.Ui_Dialog()
        self.scaling_ui.setupUi(self.scalingDialog)

        self.scaling_ui.buttonBox.accepted.connect(self.scalingDialog.close)
        self.scaling_ui.buttonBox.accepted.connect(self.Scaling)
        self.scaling_ui.buttonBox.rejected.connect(self.scalingDialog.close)
        self.scalingDialog.exec_()

    # fungsi untuk scaling
    def Scaling(self):

        try:
            # nilai faktor scaling didapatkan dari lineedit pada dialog scaling
            factor = int(self.scaling_ui.inputFaktorScaling.text())
            result = self.dict_to_matrix(self.savedTransform[-1])

            # elemen matrix titik dikalikan sesuai faktor scaling
            for i in range(len(result)):
                result[i] = factor * result[i]
            result_dict = {'x': [],
                           'y': []}
            for i in result:
                result_dict['x'].append(i[0][0])
                result_dict['y'].append(i[1][0])
            self.savedTransform.append(result_dict)
            self.savedStep.append("scaling dengan faktor {}".format(factor))
            self.gambarTransformasi(
                "Posisi bangun 2D setelah discaling dengan\nfaktor scaling sebesar {}".format(factor))
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Input bukan angka')
            error_dialog.exec_()


    def ShearingXDialog(self):

        self.shearingXDialog = QtWidgets.QDialog()
        self.shearingXDialog.setWindowTitle("Shearing X")
        self.shearingXDialog.setObjectName("Shearing X")
        self.shearingX_ui = dialogShearingX.Ui_Dialog()
        self.shearingX_ui.setupUi(self.shearingXDialog)

        self.shearingX_ui.buttonBox.accepted.connect(self.shearingXDialog.close)
        self.shearingX_ui.buttonBox.accepted.connect(self.ShearingX)
        self.shearingX_ui.buttonBox.rejected.connect(self.shearingXDialog.close)
        self.shearingXDialog.exec_()

    # fungsi untuk shearing ke arah X
    def ShearingX(self):

        try:

            # val adalah nilai shearing, didapat dari lineEdit pada dialog shearingX
            val = int(self.shearingX_ui.inputNilaiShearing.text())

            # dibuat matriks transformasi shearing X
            shear_mat = np.array([[1, val],
                                  [0, 1]])

            # dilakukan dot product antara matriks transformasi shearing x dan matriks titik
            result = []
            for i in range(len(self.savedTransform[-1]['x'])):
                result.append(np.dot(shear_mat, self.dict_to_matrix(self.savedTransform[-1])[i]))
            result_dict = {'x':[],
                           'y':[]}
            for i in result:
                result_dict['x'].append(i[0][0])
                result_dict['y'].append(i[1][0])
            self.savedTransform.append(result_dict)
            self.savedStep.append("shearing ke arah x sejauh {} satuan".format(val))
            self.gambarTransformasi(
                "Posisi bangun 2D setelah dishearing ke arah X\nsejauh {} satuan".format(val))
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Input bukan angka')
            error_dialog.exec_()


    def ShearingYDialog(self):

        self.shearingYDialog = QtWidgets.QDialog()
        self.shearingYDialog.setWindowTitle("Shearing Y")
        self.shearingYDialog.setObjectName("Shearing Y")
        self.shearingY_ui = dialogShearingY.Ui_Dialog()
        self.shearingY_ui.setupUi(self.shearingYDialog)

        self.shearingY_ui.buttonBox.accepted.connect(self.shearingYDialog.close)
        self.shearingY_ui.buttonBox.accepted.connect(self.ShearingY)
        self.shearingY_ui.buttonBox.rejected.connect(self.shearingYDialog.close)
        self.shearingYDialog.exec_()

    # fungsi untuk shearing ke arah Y
    def ShearingY(self):

        try:

            # val adalah nilai shearing, didapat dari lineEdit pada dialog shearingX
            val = int(self.shearingY_ui.inputNilaiShearingY.text())

            # dibuat matriks transformasi shearing X
            shear_mat = np.array([[1, 0],
                                  [val, 1]])

            # dilakukan dot product antara matriks transformasi shearing x dan matriks titik
            result = []
            for i in range(len(self.savedTransform[-1]['x'])):
                result.append(np.dot(shear_mat, self.dict_to_matrix(self.savedTransform[-1])[i]))
            result_dict = {'x':[],
                           'y':[]}
            for i in result:
                result_dict['x'].append(i[0][0])
                result_dict['y'].append(i[1][0])
            self.savedTransform.append(result_dict)
            self.savedStep.append("shearing ke arah Y sejauh {} satuan".format(val))
            self.gambarTransformasi(
                "Posisi bangun 2D setelah dishearing ke arah Y\nsejauh {} satuan".format(val))
        except:
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Input bukan angka')
            error_dialog.exec_()

    # fungsi untuk menghapus bangun yang dimasukkan pengguna
    def HapusBangun(self):
        self.savedTransform = []
        self.savedStep = []
        self.textContent = []
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setReadOnly(False)
        self.gambarAwal()

    # fungsi untuk menghapus transformasi-transformasi yang dilakukan
    def HapusTransformasi(self):
        if len(self.savedTransform) > 1:
            self.savedTransform = self.savedTransform[:1]

            print(self.savedTransform[0]['x'])
            result = []
            for i in range(len(self.savedTransform[0]['x'])):
                a = self.savedTransform[0]['x'][i]
                b = self.savedTransform[0]['y'][i]
                result.append("({},{})".format(a, b))
            self.textContent = "{}".format(" ".join(result))
            self.plainTextEdit.setPlainText(self.textContent)
            self.savedStep = []
            self.gambarAwal()
            self.plainTextEdit.setReadOnly(True)

        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
