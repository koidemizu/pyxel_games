import math
import pyxel

import random
from module import pycocam

class App:
    points = ()
    c = pycocam.Pycocam(200, 150)

    def __init__(self):
        pyxel.init(200, 150, caption='Pyxel pycocam demo')

        # In order to have a better view for this demo
        self.c.z = -4.5

        for i in range(1, 100):
            self.points = self.points + ((random.uniform(-2, 2),
                random.uniform(-2, 2),
                random.uniform(-2, 2)), )
        pyxel.run(self.update, self.draw)

    def draw(self):
        pyxel.cls(0)
        for i in range(0, len(self.points)):
            self.c.point(self.points[i], (i % 15) + 1)

        for i in range(-20, 20, 3):
           self.c.line((1,  i/10,  1), (1,  i/10, -1), 7)
           self.c.line((1,  i/10, -1), (-1, i/10, -1), 7)
           self.c.line((-1, i/10, -1), (-1, i/10,  1), 7)
           self.c.line((-1, i/10,  1), (1,  i/10,  1), 7)

    def update(self):
        if pyxel.btn(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btn(pyxel.KEY_UP):
            self.c.z += 0.01
        if pyxel.btn(pyxel.KEY_DOWN):
            self.c.z -= 0.01
        if pyxel.btn(pyxel.KEY_LEFT):
            self.c.theta += 0.01
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.c.theta -= 0.01

App()