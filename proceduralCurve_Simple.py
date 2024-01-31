
import maya.cmds as maya
from PySide2 import QtWidgets as qw
from PySide2.QtCore import Qt

class errorwidget(qw.QMessageBox):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Error !")
        self.setIcon(qw.QMessageBox.Warning)

    def set_error_label(self, label):
        self.setText(label)

class curvetool(qw.QWidget):

    widget_error = errorwidget()

    width = 80

    def __init__(self):
        super().__init__()
        self.draw_ui()
        self.bind_ui()
        

    def closeEvent(self, event):
        self.widget_error.close()

    def draw_ui(self):
        self.setFixedSize(300, 500)
        self.layout = qw.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)

        self.choice_object = qw.QComboBox()
        self.choice_object.addItems(["polySphere", "polyCube", "polyCylinder", "polyCone", "polyTorus", "polyPlane"])
        label_type = self.ui_create_label("Type : ")
        typeLayout = qw.QFormLayout()
        typeLayout.addRow(label_type, self.choice_object)

        self.curvename = qw.QLineEdit()
        self.curvename.setText("curve1")
        label_curve = self.ui_create_label("Curve : ")
        curveLayout = qw.QFormLayout()
        curveLayout.addRow(label_curve, self.curvename)

        self.objectname = qw.QLineEdit()
        self.objectname.setText("object")
        label_object = self.ui_create_label("Objects name : ")
        objectLayout = qw.QFormLayout()
        objectLayout.addRow(label_object, self.objectname)

        self.groupname = qw.QLineEdit()
        self.groupname.setText("group")
        label_group = self.ui_create_label("Group name : ")
        groupLayout = qw.QFormLayout()
        groupLayout.addRow(label_group, self.groupname)

        self.btn_generate = qw.QPushButton("Generate Group")
        self.btn_clear = qw.QPushButton("Clear Group")

        divLayout = qw.QFormLayout()
        self.label_div = self.ui_create_label("Quantity : *")
        
        self.slider_qty = self.ui_create_slider(0, 100, 1, Qt.Horizontal)
        divLayout.addRow(self.label_div, self.slider_qty)

        self.layout.addLayout(typeLayout)
        self.layout.addLayout(curveLayout)
        self.layout.addLayout(objectLayout)
        self.layout.addLayout(groupLayout)
        self.layout.addLayout(divLayout)
        self.layout.addWidget(self.btn_generate)
        self.layout.addWidget(self.btn_clear)
        
    def bind_ui(self):
        self.btn_generate.clicked.connect(self.generate_curve)
        self.btn_clear.clicked.connect(self.clear_group)

        self.slider_qty.valueChanged.connect(self.set_qty_label)

        self.set_qty_label()

#UI 
    def set_qty_label(self):
        self.set_label(self.label_div, "Quantity : {0}".format(self.slider_qty.value()))

    def set_label(self, label, text):
        label.setText(text)

#UI dev
    def ui_create_label(self, defaultText):
        label = qw.QLabel(defaultText)
        label.setFixedWidth(self.width)
        return label

    def ui_create_slider(self, min: int = 1, max: int = 100, defaultValue: int = 1, orientation: Qt.Orientation = Qt.Horizontal):
        slider = qw.QSlider(orientation)
        slider.setMinimum(min)
        slider.setMaximum(max)
        slider.setValue(defaultValue)
        return slider

#Maya
    def clear_group(self):
        name = self.groupname.text()
        if maya.objExists(name):
            maya.delete(name)

    def is_valid_object_name(self):
        return not maya.objExists("{0}_{1}".format(self.objectname.text(), 0))
    def is_valid_curve_name(self):
        return maya.objExists(self.curvename.text())

    def spawn_object(self, name):
        typecmd = self.choice_object.currentText()
        exec("maya.{0}(name = name)".format(typecmd))
        

    def generate_curve(self):
        if not self.is_valid_curve_name():
            self.show_error_widget("Error: Curve name '{0}' invalid (doesn't exist)".format(self.curvename.text()))    
            return
        
        self.clear_group()
        if not self.is_valid_object_name():
            self.show_error_widget("Error: Objects name '{0}' invalid (already taken)".format(self.objectname.text()))
            return
        curve = self.curvename.text()
        if maya.objExists(curve):
            qty = self.slider_qty.value() + 1
            step = 1 / (qty)
            index = 0
            tab = []
            while index <= qty:
                name = "{0}_{1}".format(self.objectname.text(), index)
                x, y, z = maya.pointOnCurve(curve, pr = step * index, top = True)
                self.spawn_object(name)
                maya.move(x, y, z)
                index += 1
                tab.append(name)
            
            maya.group(tab, n = self.groupname.text())

        else:
            self.show_error_widget("Error : Curve '{0}' not found (invalid name)".format(name))
        
#Feedback
    def show_error_widget(self, label):
        self.widget_error.set_error_label(label)
        self.widget_error.show()

app = curvetool()
app.show()
