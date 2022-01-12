# -*- coding: utf-8 -*-

import pyxel

class APP:
  def __init__(self):
      pyxel.init(128, 128, caption="pyxel")
      
      self.number1 = 0
      self.number2 = 0
      self.number3 = 0
      self.number1_stop = False
      self.number2_stop = False
      self.number3_stop = False
      
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      if pyxel.btnp(pyxel.KEY_1):
          self.number1_stop = True
      if pyxel.btnp(pyxel.KEY_2):
          self.number2_stop = True
      if pyxel.btnp(pyxel.KEY_3):
          self.number3_stop = True
      if pyxel.btnp(pyxel.KEY_SPACE):
          self.number1_stop = False
          self.number2_stop = False
          self.number3_stop = False     
          
      if self.number1_stop == False:
          self.number1 = pyxel.frame_count % 9
      if self.number2_stop == False:
          self.number2 = pyxel.frame_count % 9
      if self.number3_stop == False:          
          self.number3 = pyxel.frame_count % 9

  def draw(self):
      pyxel.cls(0)
      pyxel.text(20, 50, str(self.number1), 7)
      pyxel.text(40, 50, str(self.number2), 7)
      pyxel.text(60, 50, str(self.number3), 7)      
      
      pyxel.rectb(15, 45, 15, 15, pyxel.frame_count % 16)
      pyxel.rectb(35, 45, 15, 15, pyxel.frame_count % 16)
      pyxel.rectb(55, 45, 15, 15, pyxel.frame_count % 16)
      pyxel.rectb(10, 40, 65, 40, 7)            
      
APP()