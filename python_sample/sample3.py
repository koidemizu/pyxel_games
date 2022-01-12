# -*- coding: utf-8 -*-

import pyxel

class APP:
  def __init__(self):
      pyxel.init(128, 128, caption="pyxel")
      
      self.str1 = "HELLO"
      self.str2 = "World"
      self.str3 = "pyxel"      
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      pass

  def draw(self):
      pyxel.cls(0)
      pyxel.text(20, 20, self.str1, 6)
      pyxel.text(20, 30, self.str2, 6)
      pyxel.text(20, 40, self.str3, 6)      
      
      pyxel.text(20, 50, self.str1 + " " + self.str2, 11)      
      pyxel.text(20, 60, self.str1 + " " + self.str3, 11)      
      
      pyxel.text(20, 70, self.str1[0], 14)      
      pyxel.text(30, 70, self.str1[1], 14)      
      pyxel.text(40, 70, self.str1[2], 14)      
      pyxel.text(50, 70, self.str1[3], 14)      
      pyxel.text(60, 70, self.str1[4], 14)      
      
      pyxel.text(20, 80, self.str1.lower(), 13)      
      pyxel.text(20, 90, self.str3.upper(), 13)      
      
APP()