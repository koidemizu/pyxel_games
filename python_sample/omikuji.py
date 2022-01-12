# -*- coding: utf-8 -*-

import pyxel

class APP:
  def __init__(self):
      pyxel.init(128, 128, caption="pyxel")
      
      self.txt = ["DAIKICHI","CHUKICHI","SYOKITI","KYOU"]
      self.num = 0
      self.start_flag = False
      
      
      pyxel.run(self.update, self.draw)
     
  def update(self):      
      if pyxel.btnp(pyxel.KEY_SPACE):
          if self.start_flag == False:
              self.start_flag = True
          else:
              self.start_flag = False

      if self.start_flag == True:
          self.num = self.num + 1
          
      if self.num > 3:
          self.num = 0
          

  def draw(self):
      pyxel.cls(0)
      pyxel.text(45, 50, self.txt[self.num], 7)
      
      
APP()