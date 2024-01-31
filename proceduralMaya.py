from maya import cmds as maya
from PySide2 import QtWidgets as qw
from PySide2.QtCore import Qt
import random as rnd

class proceduralMaya(qw.QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Maya tool")
        self.setFixedHeight(500)
        self.setFixedWidth(500)
        self.draw_ui()

        self.set_sphere_radius()
        self.set_sphere_subdiv()
        self.set_cube_qty()
        self.set_sphere_qty()

        self.bind_ui()

    def draw_ui(self):
        self.layout = qw.QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignTop)
        self.layout.addWidget(qw.QLabel("Create Sphere"))
        self.draw_sphere_ui()
        self.layout.addWidget(qw.QLabel("Create Cube"))
        self.draw_cube_ui()

    def draw_sphere_ui(self):
        radiusLayout = qw.QFormLayout(self)
        self.sphere_radius_label = qw.QLabel()
        radiusLayout.addRow(qw.QLabel("Sphere Radius : "), self.sphere_radius_label)
        self.layout.addLayout(radiusLayout)

        self.sphere_radius_slider = self.ui_create_slider(1, 20)
        self.layout.addWidget(self.sphere_radius_slider)

        subdivLayout = qw.QFormLayout(self)
        self.sphere_subdiv_label = qw.QLabel()
        subdivLayout.addRow(qw.QLabel("Sphere Sub division : "), self.sphere_subdiv_label)
        self.layout.addLayout(subdivLayout)

        self.sphere_subdiv_slider = self.ui_create_slider(3, 50)
        self.layout.addWidget(self.sphere_subdiv_slider)

        self.btn_sphere = qw.QPushButton("Make Sphere")
        self.layout.addWidget(self.btn_sphere)

        sphereQtyLayout = qw.QFormLayout(self)
        self.sphere_qty_slider = self.ui_create_slider(1, 1000)
        self.sphere_qty_label = qw.QLabel()
        sphereQtyLayout.addRow(qw.QLabel("Sphere Quantity : "), self.sphere_qty_label)
        self.btn_multi_sphere = qw.QPushButton("Make Multi Sphere")
        self.btn_delete_sphere = qw.QPushButton("Delete Sphere")
        self.layout.addLayout(sphereQtyLayout)
        self.layout.addWidget(self.sphere_qty_slider)
        self.layout.addWidget(self.btn_multi_sphere)
        self.layout.addWidget(self.btn_delete_sphere)

    def draw_cube_ui(self):
        cubeQtyLayout = qw.QFormLayout(self)
        self.cube_qty_label = qw.QLabel()
        self.cube_qty_slider = self.ui_create_slider(1, 1000)
        cubeQtyLayout.addRow(qw.QLabel("Cubes Quantity : "), self.cube_qty_label)
        self.btn_multi_cubes = qw.QPushButton("Make Multi Cubes")
        self.btn_delete_cubes = qw.QPushButton("Delete Cubes")
        self.layout.addLayout(cubeQtyLayout)
        self.layout.addWidget(self.cube_qty_slider)
        self.layout.addWidget(self.btn_multi_cubes)
        self.layout.addWidget(self.btn_delete_cubes)

    def ui_create_slider(self, min: int, max: int):
        slider = qw.QSlider(Qt.Horizontal)
        slider.setMinimum(min)
        slider.setMaximum(max)
        return slider

    def bind_ui(self):
        self.sphere_radius_slider.valueChanged.connect(self.set_sphere_radius)
        self.sphere_subdiv_slider.valueChanged.connect(self.set_sphere_subdiv)
        self.sphere_qty_slider.valueChanged.connect(self.set_sphere_qty)
        self.btn_sphere.clicked.connect(self.create_sphere)
        self.btn_multi_sphere.clicked.connect(self.create_multi_sphere)
        self.btn_delete_sphere.clicked.connect(self.delete_multi_spheres)

        self.cube_qty_slider.valueChanged.connect(self.set_cube_qty)
        self.btn_multi_cubes.clicked.connect(self.create_multi_cubes)
        self.btn_delete_cubes.clicked.connect(self.delete_multi_cubes)

    def set_sphere_radius(self):
        self.sphere_radius_label.setText("{0}".format(self.sphere_radius_slider.value()))
    def set_sphere_subdiv(self):
        self.sphere_subdiv_label.setText("{0}".format(self.sphere_subdiv_slider.value()))
    def set_sphere_qty(self):
        self.sphere_qty_label.setText("{0}".format(self.sphere_qty_slider.value()))
    
    def set_cube_qty(self):
        self.cube_qty_label.setText("{0}".format(self.cube_qty_slider.value()))

    def create_sphere(self):
        r = self.sphere_radius_slider.value()
        subdiv = self.sphere_subdiv_slider.value()
        maya.polySphere(n="Sphere", sx = subdiv, sy = subdiv)

    def create_multi_sphere(self):
        self.delete_multi_spheres()
        rad = rnd.randrange(2, 20)
        subdiv = rnd.randrange(3, 20)
        index = 0
        tab = []
        for sp in range(self.cube_qty_slider.value()):
            x, y, z = self.get_random3(-100, 100)
            index += 1
            name = "Sphere_{0}".format(index)
            maya.polySphere(n = name, sx = subdiv, sy = subdiv, r = rad)
            maya.move(x, y, z)
            tab.append(name)
        maya.group(tab, n = "Spheres")

    def create_multi_cubes(self):
        self.delete_multi_cubes()
        size = rnd.randrange(1, 20)
        index = 0
        tab = []
        for cb in range(self.cube_qty_slider.value()):
            x, y, z = self.get_random3(-100, 100)
            rY, rX, rZ = self.get_random3(0, 360)
            index += 1
            name = "Cube_{0}".format(index)
            maya.polyCube(n = name, h = size, w = size, d = size, ax = [rY, rX, rZ])
            maya.move(x, y, z)
            tab.append(name)
        maya.group(tab, n = "Cubes")

    def delete_multi_spheres(self):
        if maya.objExists("Spheres"):
            maya.delete("Spheres")

    def delete_multi_cubes(self):
        if maya.objExists("Cubes"):
            maya.delete("Cubes")

    def get_random3(self, min, max):
        x = rnd.randrange(min, max)
        y = rnd.randrange(min, max)
        z = rnd.randrange(min, max)
        return x, y, z

###

app = proceduralMaya()
app.show()