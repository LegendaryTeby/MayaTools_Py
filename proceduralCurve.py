import maya.cmds as maya
from PySide2 import QtWidgets as qw
from PySide2.QtCore import Qt

from enum import Enum

#["polySphere", "polyCube", "polyCylinder", "polyCone", "polyTorus"]
class PolyType(Enum):
    PolySphere = 0
    PolyCube = 1
    PolyCone = 2
    PolyCylinder = 3
    PolyTorus = 4

#UI dev
def ui_create_slider(min: int = 0, max: int = 100, defaultValue: int = 1, orientation: Qt.Orientation = Qt.Horizontal):
    slider = qw.QSlider(orientation)
    slider.setMinimum(min)
    slider.setMaximum(max)
    slider.setValue(defaultValue)
    return slider
def ui_create_label(width = 100, height = 15, text = "None"):
    label = qw.QLabel(text)
    label.setFixedWidth(width)
    label.setFixedHeight(height)
    return label

class WidgetSphere(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.draw_ui()
        self.bind_ui()
        
    def draw_ui(self):
        self.layout = qw.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        label = qw.QLabel("SPHERE")
        label.setAlignment(Qt.AlignCenter)        
        
        self.label_radius = ui_create_label(text = "Radius : ")
        self.slider_radius = ui_create_slider(1, 100 * 100, 1)
        layout_radius = qw.QFormLayout()
        layout_radius.addRow(self.label_radius, self.slider_radius)

        self.label_subdiv_x = ui_create_label(text = "Sub Division X : *")
        self.slider_subdiv_x = ui_create_slider(3, 50, 20)
        layout_subdiv_x = qw.QFormLayout()
        layout_subdiv_x.addRow(self.label_subdiv_x, self.slider_subdiv_x)

        self.label_subdiv_y = ui_create_label(text = "Sub Division Y : *")
        self.slider_subdiv_y = ui_create_slider(3, 50, 20)
        layout_subdiv_y = qw.QFormLayout()
        layout_subdiv_y.addRow(self.label_subdiv_y, self.slider_subdiv_y)

        self.layout.addWidget(label)
        self.layout.addLayout(layout_radius)
        self.layout.addLayout(layout_subdiv_x)
        self.layout.addLayout(layout_subdiv_y)

    def bind_ui(self):
        self.slider_radius.valueChanged.connect(self.set_radius_label)
        self.slider_subdiv_x.valueChanged.connect(self.set_subdiv_x_label)
        self.slider_subdiv_y.valueChanged.connect(self.set_subdiv_y_label)

        self.set_radius_label()
        self.set_subdiv_x_label()
        self.set_subdiv_y_label()

    def set_radius_label(self):
        self.label_radius.setText("Radius : {0}".format(self.get_radius()))
    def set_subdiv_x_label(self):
        self.label_subdiv_x.setText("Sub Division X : {0}".format(self.slider_subdiv_x.value()))
    def set_subdiv_y_label(self):
        self.label_subdiv_y.setText("Sub Division Y : {0}".format(self.slider_subdiv_y.value()))

    def get_subdiv(self):
        x = self.slider_subdiv_x.value()
        y = self.slider_subdiv_y.value()
        return x, y
    def get_radius(self):
        return self.slider_radius.value()

class WidgetCube(qw.QWidget):

    def __init__(self):
        super().__init__()
        self.draw_ui()
        self.bind_ui()

    def draw_ui(self):
        self.layout = qw.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        label = qw.QLabel("CUBE")
        label.setAlignment(Qt.AlignCenter)

        #Global
        self.label_global = ui_create_label(text = "Global : ")
        self.slider_global = ui_create_slider(1, 100, 1)
        globalLayout = qw.QFormLayout()
        globalLayout.addRow(self.label_global, self.slider_global)
        
        #Width
        self.label_width = ui_create_label(text = "Width : *")
        self.slider_width = ui_create_slider(1, 100, 1)
        widthLayout = qw.QFormLayout()
        widthLayout.addRow(self.label_width, self.slider_width)
        #Height
        self.label_height = ui_create_label(text = "Height : *")
        self.slider_height = ui_create_slider(1, 100, 1)
        heightLayout = qw.QFormLayout()
        heightLayout.addRow(self.label_height, self.slider_height)
        #Depth
        self.label_depth = ui_create_label(text = "Depth : *")
        self.slider_depth = ui_create_slider(1, 100, 1)
        depthLayout = qw.QFormLayout()
        depthLayout.addRow(self.label_depth, self.slider_depth)

        #Subdiv Global
        self.label_subdiv_global = ui_create_label(text = "Division Global : ")
        self.slider_subdiv_global = ui_create_slider(1, 50, 1)
        subdivGLayout = qw.QFormLayout()
        subdivGLayout.addRow(self.label_subdiv_global, self.slider_subdiv_global)
        #Subdiv Height
        self.label_subdiv_height = ui_create_label(text = "Division Height : *")
        self.slider_subdiv_height = ui_create_slider(1, 50, 1)
        subdivHLayout = qw.QFormLayout()
        subdivHLayout.addRow(self.label_subdiv_height, self.slider_subdiv_height)
        #Subdiv Width
        self.label_subdiv_width = ui_create_label(text = "Division Width : *")
        self.slider_subdiv_width = ui_create_slider(1, 50, 1)
        subdivWLayout = qw.QFormLayout()
        subdivWLayout.addRow(self.label_subdiv_width, self.slider_subdiv_width)
        #Subdiv Depth
        self.label_subdiv_depth = ui_create_label(text = "Division Depth : *")
        self.slider_subdiv_depth = ui_create_slider(1, 50, 1)
        subdivDLayout = qw.QFormLayout()
        subdivDLayout.addRow(self.label_subdiv_depth, self.slider_subdiv_depth)

        self.layout.addWidget(label)
        self.layout.addLayout(globalLayout)
        self.layout.addLayout(widthLayout)
        self.layout.addLayout(heightLayout)
        self.layout.addLayout(depthLayout)
        self.layout.addWidget(qw.QLabel("SubDivision"))
        self.layout.addLayout(subdivGLayout)
        self.layout.addLayout(subdivWLayout)
        self.layout.addLayout(subdivHLayout)
        self.layout.addLayout(subdivDLayout)

    def bind_ui(self):
        self.slider_global.valueChanged.connect(self.update_global)
        self.slider_height.valueChanged.connect(self.set_height_label)
        self.slider_width.valueChanged.connect(self.set_width_label)
        self.slider_depth.valueChanged.connect(self.set_depth_label)

        self.slider_subdiv_global.valueChanged.connect(self.update_subdiv_global)
        self.slider_subdiv_height.valueChanged.connect(self.set_subdiv_height_label)
        self.slider_subdiv_width.valueChanged.connect(self.set_subdiv_width_label)
        self.slider_subdiv_depth.valueChanged.connect(self.set_subdiv_depth_label)

        self.set_height_label()
        self.set_width_label()
        self.set_depth_label()

        self.set_subdiv_height_label()
        self.set_subdiv_width_label()
        self.set_subdiv_depth_label()

    def update_global(self):
        value = self.slider_global.value()
        self.slider_height.setValue(value)
        self.slider_width.setValue(value)
        self.slider_depth.setValue(value)

    def update_subdiv_global(self):
        value = self.slider_subdiv_global.value()
        self.slider_subdiv_height.setValue(value)
        self.slider_subdiv_width.setValue(value)
        self.slider_subdiv_depth.setValue(value)

    #Labels
    def set_height_label(self):
        self.label_height.setText("Height : {0}".format(self.slider_height.value()))
    def set_width_label(self):
        self.label_width.setText("Width : {0}".format(self.slider_width.value()))
    def set_depth_label(self):
        self.label_depth.setText("Depth : {0}".format(self.slider_depth.value()))
    def set_subdiv_height_label(self):
        self.label_subdiv_height.setText("Division Height : {0}".format(self.slider_subdiv_height.value()))
    def set_subdiv_width_label(self):
        self.label_subdiv_width.setText("Division Width : {0}".format(self.slider_subdiv_width.value()))
    def set_subdiv_depth_label(self):
        self.label_subdiv_depth.setText("Division Depth : {0}".format(self.slider_subdiv_depth.value()))


    def get_height(self):
        return self.slider_height.value()
    def get_width(self):
        return self.slider_width.value()
    def get_depth(self):
        return self.slider_depth.value()
    
    def get_subdiv_height(self):
        return self.slider_subdiv_height.value()
    def get_subdiv_width(self):
        return self.slider_subdiv_width.value()
    def get_subdiv_depth(self):
        return self.slider_subdiv_depth.value()

class WidgetCone(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.draw_ui()
        self.bind_ui()

    def draw_ui(self):
        self.layout = qw.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        label = qw.QLabel("CONE")
        label.setAlignment(Qt.AlignCenter)

        #Radius
        self.label_radius = ui_create_label(text = "Radius : *")
        self.slider_radius = ui_create_slider(1, 100, 1)
        radiusLayout = qw.QFormLayout()
        radiusLayout.addRow(self.label_radius, self.slider_radius)
        #Height
        self.label_height = ui_create_label(text = "Height : *")
        self.slider_height = ui_create_slider(1, 100, 2)
        heightLayout = qw.QFormLayout()
        heightLayout.addRow(self.label_height, self.slider_height)
        #Subdiv Axis
        self.label_subdiv_axis = ui_create_label(text = "Division Axis : *")
        self.slider_subdiv_axis = ui_create_slider(3, 50, 20)
        subdivALayout = qw.QFormLayout()
        subdivALayout.addRow(self.label_subdiv_axis, self.slider_subdiv_axis)
        #Subdiv Height
        self.label_subdiv_height = ui_create_label(text = "Division Height : *")
        self.slider_subdiv_height = ui_create_slider(1, 50, 1)
        subdivHLayout = qw.QFormLayout()
        subdivHLayout.addRow(self.label_subdiv_height, self.slider_subdiv_height)
        #Subdiv Cap
        self.label_subdiv_cap = ui_create_label(text = "Division Cap : *")
        self.slider_subdiv_cap = ui_create_slider(0, 50, 0)
        subdivCLayout = qw.QFormLayout()
        subdivCLayout.addRow(self.label_subdiv_cap, self.slider_subdiv_cap)

        self.layout.addWidget(label)
        self.layout.addLayout(radiusLayout)
        self.layout.addLayout(heightLayout)
        self.layout.addWidget(qw.QLabel("Sub Division"))
        self.layout.addLayout(subdivALayout)
        self.layout.addLayout(subdivHLayout)
        self.layout.addLayout(subdivCLayout)
        
    def bind_ui(self):
        self.slider_radius.valueChanged.connect(self.set_radius_label)
        self.slider_height.valueChanged.connect(self.set_height_label)

        self.set_radius_label()
        self.set_height_label()

        self.slider_subdiv_axis.valueChanged.connect(self.set_subdiv_axis)
        self.slider_subdiv_height.valueChanged.connect(self.set_subdiv_height)
        self.slider_subdiv_cap.valueChanged.connect(self.set_subdiv_cap)

        self.set_subdiv_axis()
        self.set_subdiv_height()
        self.set_subdiv_cap()

    #Labels
    def set_radius_label(self):
        self.label_radius.setText("Radius : {0}".format(self.slider_radius.value()))
    def set_height_label(self):
        self.label_height.setText("Height : {0}".format(self.slider_height.value()))
    def set_subdiv_axis(self):
        self.label_subdiv_axis.setText("Division Axis : {0}".format(self.slider_subdiv_axis.value()))
    def set_subdiv_height(self):
        self.label_subdiv_height.setText("Division Height : {0}".format(self.slider_subdiv_height.value()))
    def set_subdiv_cap(self):
        self.label_subdiv_cap.setText("Division Cap : {0}".format(self.slider_subdiv_cap.value()))

    def get_radius(self):
        return self.slider_radius.value()
    def get_height(self):
        return self.slider_height.value()
    def get_subdiv_axis(self):
        return self.slider_subdiv_axis.value()
    def get_subdiv_height(self):
        return self.slider_subdiv_height.value()
    def get_subdiv_cap(self):
        return self.slider_subdiv_cap.value()

class widgetCylinder(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.draw_ui()
        self.bind_ui()

    def draw_ui(self):
        self.layout = qw.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        label = qw.QLabel("CYLINDER")
        label.setAlignment(Qt.AlignCenter)

        #Radius
        self.label_radius = ui_create_label(text = "Radius : *")
        self.slider_radius = ui_create_slider(1, 100, 1)
        radiusLayout = qw.QFormLayout()
        radiusLayout.addRow(self.label_radius, self.slider_radius)
        #Height
        self.label_height = ui_create_label(text = "Height : *")
        self.slider_height = ui_create_slider(1, 100, 2)
        heightLayout = qw.QFormLayout()
        heightLayout.addRow(self.label_height, self.slider_height)
        #Subdiv Axis
        self.label_subdiv_axis = ui_create_label(text = "Division Axis : *")
        self.slider_subdiv_axis = ui_create_slider(3, 50, 20)
        subdivALayout = qw.QFormLayout()
        subdivALayout.addRow(self.label_subdiv_axis, self.slider_subdiv_axis)
        #Subdiv Height
        self.label_subdiv_height = ui_create_label(text = "Division Height : *")
        self.slider_subdiv_height = ui_create_slider(1, 50, 1)
        subdivHLayout = qw.QFormLayout()
        subdivHLayout.addRow(self.label_subdiv_height, self.slider_subdiv_height)
        #Subdiv Caps
        self.label_subdiv_caps = ui_create_label(text = "Division Caps : *")
        self.slider_subdiv_caps = ui_create_slider(0, 50, 1)
        subdivCLayout = qw.QFormLayout()
        subdivCLayout.addRow(self.label_subdiv_caps, self.slider_subdiv_caps)
        #Round Cap
        self.check_round_caps = qw.QCheckBox()
        rndCapLayout = qw.QFormLayout()
        rndCapLayout.addRow(qw.QLabel("Round Caps : "), self.check_round_caps)

        self.layout.addWidget(label)
        self.layout.addLayout(radiusLayout)
        self.layout.addLayout(heightLayout)
        self.layout.addLayout(rndCapLayout)
        self.layout.addWidget(qw.QLabel("Sub Division"))
        self.layout.addLayout(subdivALayout)
        self.layout.addLayout(subdivHLayout)
        self.layout.addLayout(subdivCLayout)

    def bind_ui(self):
        self.slider_radius.valueChanged.connect(self.set_label_radius)
        self.slider_height.valueChanged.connect(self.set_label_height)

        self.set_label_radius()
        self.set_label_height()

        self.slider_subdiv_axis.valueChanged.connect(self.set_label_subdiv_axis)
        self.slider_subdiv_height.valueChanged.connect(self.set_label_subdiv_height)
        self.slider_subdiv_caps.valueChanged.connect(self.set_label_subdiv_caps)

        self.set_label_subdiv_axis()
        self.set_label_subdiv_height()
        self.set_label_subdiv_caps()

    #Labels
    def set_label_radius(self):
        self.label_radius.setText("Radius : {0}".format(self.get_radius()))
    def set_label_height(self):
        self.label_height.setText("Height : {0}".format(self.get_height()))
    def set_label_subdiv_axis(self):
        self.label_subdiv_axis.setText("Division Axis : {0}".format(self.get_subdiv_axis()))
    def set_label_subdiv_height(self):
        self.label_subdiv_height.setText("Division Height : {0}".format(self.get_subdiv_height()))
    def set_label_subdiv_caps(self):
        self.label_subdiv_caps.setText("Division Caps : {0}".format(self.get_subdiv_caps()))

    def get_radius(self):
        return self.slider_radius.value()
    def get_height(self):
        return self.slider_height.value()
    def get_round_caps(self):
        return self.check_round_caps.isChecked()
    def get_subdiv_axis(self):
        return self.slider_subdiv_axis.value()
    def get_subdiv_height(self):
        return self.slider_subdiv_height.value()
    def get_subdiv_caps(self):
        return self.slider_subdiv_caps.value()


class WidgetTorus(qw.QWidget):
    def __init__(self):
        super().__init__()
        self.draw_ui()
        self.bind_ui()

    def draw_ui(self):
        self.layout = qw.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        label = qw.QLabel("TORUS")
        label.setAlignment(Qt.AlignCenter)

        #Radius
        self.label_radius = ui_create_label(text = "Radius : *")
        self.slider_radius = ui_create_slider(2, 100, 1)
        radiusLayout = qw.QFormLayout()
        radiusLayout.addRow(self.label_radius, self.slider_radius)
        #Section Radius
        self.label_section_radius = ui_create_label(text = "Section Radius : *")
        self.slider_section_radius = ui_create_slider(1, 100, 1)
        sectionRLayout = qw.QFormLayout()
        sectionRLayout.addRow(self.label_section_radius, self.slider_section_radius)
        #Twist
        self.label_twist = ui_create_label(text = "Twist : *")
        self.slider_twist = ui_create_slider(0, 6, 0)
        twistLayout = qw.QFormLayout()
        twistLayout.addRow(self.label_twist, self.slider_twist)
        #Subdiv Axis
        self.label_subdiv_axis = ui_create_label(text = "Division Axis : *")
        self.slider_subdiv_axis = ui_create_slider(3, 50, 20)
        subdivALayout = qw.QFormLayout()
        subdivALayout.addRow(self.label_subdiv_axis, self.slider_subdiv_axis)
        #Subdiv Height
        self.label_subdiv_height = ui_create_label(text = "Division Height : *")
        self.slider_subdiv_height = ui_create_slider(3, 50, 20)
        subdivHLayout = qw.QFormLayout()
        subdivHLayout.addRow(self.label_subdiv_height, self.slider_subdiv_height)

        self.layout.addWidget(label)
        self.layout.addLayout(radiusLayout)
        self.layout.addLayout(sectionRLayout)
        self.layout.addLayout(twistLayout)
        self.layout.addWidget(qw.QLabel("Sub Division"))
        self.layout.addLayout(subdivALayout)
        self.layout.addLayout(subdivHLayout)

    def bind_ui(self):
        self.slider_radius.valueChanged.connect(self.set_label_radius)
        self.slider_section_radius.valueChanged.connect(self.set_label_section_radius)
        self.slider_twist.valueChanged.connect(self.set_label_twist)

        self.set_label_radius()
        self.set_label_section_radius()
        self.set_label_twist()

        self.slider_subdiv_axis.valueChanged.connect(self.set_label_subdiv_axis)
        self.slider_subdiv_height.valueChanged.connect(self.set_label_subdiv_height)

        self.set_label_subdiv_axis()
        self.set_label_subdiv_height()

    #Labels
    def set_label_radius(self):
        self.label_radius.setText("Radius : {0}".format(self.get_radius()))
    def set_label_section_radius(self):
        self.label_section_radius.setText("Section Radius : {0}".format(self.get_section_radius()))
    def set_label_twist(self):
        self.label_twist.setText("Twist : {0}".format(self.get_twist()))
    def set_label_subdiv_axis(self):
        self.label_subdiv_axis.setText("Division Axis : {0}".format(self.get_subdiv_axis()))
    def set_label_subdiv_height(self):
        self.label_subdiv_height.setText("Division Height: {0}".format(self.get_subdiv_height()))

    def get_radius(self):
        return self.slider_radius.value()
    def get_section_radius(self):
        return self.slider_section_radius.value()
    def get_twist(self):
        return self.slider_twist.value()
    def get_subdiv_axis(self):
        return self.slider_subdiv_axis.value()
    def get_subdiv_height(self):
        return self.slider_subdiv_height.value()

class WidgetError(qw.QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Error !")
        self.setIcon(qw.QMessageBox.Warning)

    def set_error_label(self, label):
        self.setText(label)

class curvetool(qw.QWidget):
    widget_sphere = WidgetSphere()
    widget_cube = WidgetCube()
    widget_cone = WidgetCone()
    widget_cylinder = widgetCylinder()
    widget_torus = WidgetTorus()
    widget_layout = qw.QStackedLayout()

    widget_error = WidgetError()

    def __init__(self):
        super().__init__()
        self.draw_ui()
        self.bind_ui()

    def closeEvent(self, event):
        self.widget_error.close()

    def draw_ui(self):
        self.setFixedSize(350, 500)
        self.layout = qw.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)

        #Poly Selection
        self.choice_object = qw.QComboBox()
        self.choice_object.addItems([PolyType.PolySphere.name, PolyType.PolyCube.name, PolyType.PolyCone.name, PolyType.PolyCylinder.name, PolyType.PolyTorus.name])
        label_type = ui_create_label(text = "Type : ")
        typeLayout = qw.QFormLayout()
        typeLayout.addRow(label_type, self.choice_object)

        #Curve
        self.curvename = qw.QLineEdit()
        self.curvename.setText("curve1")
        label_curve = ui_create_label(text = "Curve : ")
        curveLayout = qw.QFormLayout()
        curveLayout.addRow(label_curve, self.curvename)

        #Object
        self.objectname = qw.QLineEdit()
        self.objectname.setText("object")
        label_object = ui_create_label(text = "Objects name : ")
        objectLayout = qw.QFormLayout()
        objectLayout.addRow(label_object, self.objectname)

        #Group
        self.groupname = qw.QLineEdit()
        self.groupname.setText("group")
        label_group = ui_create_label(text = "Group name : ")
        groupLayout = qw.QFormLayout()
        groupLayout.addRow(label_group, self.groupname)

        self.btn_generate = qw.QPushButton("Generate Group")
        self.btn_clear = qw.QPushButton("Clear Group")

        qtyLayout = qw.QFormLayout()
        self.label_qty = ui_create_label(text = "Quantity : *")
        self.slider_qty = ui_create_slider(0, 100, 1, Qt.Horizontal)
        qtyLayout.addRow(self.label_qty, self.slider_qty)

        #Poly Widgets
        self.widget_layout.addWidget(self.widget_sphere)
        self.widget_layout.addWidget(self.widget_cube)
        self.widget_layout.addWidget(self.widget_cone)
        self.widget_layout.addWidget(self.widget_cylinder)
        self.widget_layout.addWidget(self.widget_torus)

        #Layout
        self.layout.addLayout(typeLayout)
        self.layout.addLayout(curveLayout)
        self.layout.addLayout(objectLayout)
        self.layout.addLayout(groupLayout)
        self.layout.addLayout(qtyLayout)
        self.layout.addWidget(self.btn_generate)
        self.layout.addWidget(self.btn_clear)
        self.layout.addLayout(self.widget_layout)
        
        
    def bind_ui(self):
        self.btn_generate.clicked.connect(self.generate_curve)
        self.btn_clear.clicked.connect(self.clear_group)
        self.choice_object.currentIndexChanged.connect(self.set_polytype)
        
        self.slider_qty.valueChanged.connect(self.set_qty_label)

        self.set_qty_label()
        self.set_polytype()

        self.choice_object.setCurrentIndex(0)

#UI 
    def set_qty_label(self):
        self.set_label(self.label_qty, "Quantity : {0}".format(self.slider_qty.value()))

    def set_label(self, label, text):
        label.setText(text)

    def set_polytype(self):
        self.widget_layout.setCurrentIndex(self.choice_object.currentIndex())

#Maya
    def clear_group(self):
        name = self.groupname.text()
        if maya.objExists(name):
            maya.delete(name)

    def is_valid_object_name(self):
        return not maya.objExists("{0}_{1}".format(self.objectname.text(), 0))
    def is_valid_curve_name(self):
        return maya.objExists(self.curvename.text())

#Spawn
    def spawn_object(self, name):
        type = self.choice_object.currentIndex()
        if type == PolyType.PolySphere.value:
            self.spawn_polysphere(name)
        elif type == PolyType.PolyCube.value:
            self.spawn_polycube(name)
        elif type == PolyType.PolyCone.value:
            self.spawn_polycone(name)
        elif type == PolyType.PolyCylinder.value:
            self.spawn_polycylinder(name)
        elif type == PolyType.PolyTorus.value:
            self.spawn_polytorus(name)

    def spawn_polysphere(self, name):
        radius = self.widget_sphere.get_radius()
        x, y = self.widget_sphere.get_subdiv()
        maya.polySphere(n = name, r = radius, sx = x, sy = y)

    def spawn_polycube(self, name):
        h = self.widget_cube.get_height()
        w = self.widget_cube.get_width()
        d = self.widget_cube.get_depth()

        sh = self.widget_cube.get_subdiv_height()
        sw = self.widget_cube.get_subdiv_width()
        sd = self.widget_cube.get_subdiv_depth()

        maya.polyCube(n = name, h = h, w = w, d = d, sh = sh, sw = sw, sd = sd)
    
    def spawn_polycone(self, name):
        r = self.widget_cone.get_radius()
        h = self.widget_cone.get_height()
        sa = self.widget_cone.get_subdiv_axis()
        sh = self.widget_cone.get_subdiv_height()    
        sc = self.widget_cone.get_subdiv_cap()
        maya.polyCone(n = name, r = r, h = h, sa = sa, sh = sh, sc = sc)

    def spawn_polycylinder(self, name):
        r = self.widget_cylinder.get_radius()
        h = self.widget_cylinder.get_height()
        sa = self.widget_cylinder.get_subdiv_axis()
        sh = self.widget_cylinder.get_subdiv_height()
        sc = self.widget_cylinder.get_subdiv_caps()
        rndc = self.widget_cylinder.get_round_caps()
        maya.polyCylinder(n = name, r = r, h = h, sa = sa, sh = sh, sc = sc, rcp = rndc)
    def spawn_polytorus(self, name):
        r = self.widget_torus.get_radius()
        sr = self.widget_torus.get_section_radius()
        t = self.widget_torus.get_twist()
        sa = self.widget_torus.get_subdiv_axis()
        sh = self.widget_torus.get_subdiv_height()
        maya.polyTorus(n = name, r = r, sr = sr, tw = t, sa = sa, sh = sh)

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
