import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('PyQt5 App')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
layout = QFormLayout()
layout.addRow('Name: ', QLineEdit())
layout.addRow('Age: ', QLineEdit())
layout.addRow('Job: ', QLineEdit())
layout.addRow('Hobbies: ', QLineEdit())
window.setLayout(layout)




window.show()
sys.exit(app.exec_())
