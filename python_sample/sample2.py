# -*- coding: utf-8 -*-

import pyxel

class APP:
  def __init__(self):
      pyxel.init(128, 128, caption="pyxel")
      
      self.number1 = 1
      self.number2 = 2
      self.number3 = 3      
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      pass

  def draw(self):
      pyxel.cls(0)
      pyxel.text(20, 20, str(self.number1), 7)
      pyxel.text(20, 30, str(self.number2), 7)
      pyxel.text(20, 40, str(self.number3), 7)      
      
      pyxel.text(20, 50, str(self.number1 + 10), 8)
      pyxel.text(20, 60, str(self.number2 - 10), 8)
      pyxel.text(20, 70, str(self.number3 * 10), 8)      

      pyxel.text(20, 80, str(self.number1 + self.number2), 9)
      pyxel.text(20, 90, str(self.number2 - self.number1), 9)
      pyxel.text(20, 100, str(self.number3 / self.number2), 9)      
      
APP()