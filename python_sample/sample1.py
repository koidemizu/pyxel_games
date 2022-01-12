# -*- coding: utf-8 -*-

import pyxel

class APP:
  def __init__(self):
      pyxel.init(128, 128, caption="pyxel")
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      pass

  def draw(self):
      pass
                  
APP()