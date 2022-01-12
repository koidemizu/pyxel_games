# -*- coding: utf-8 -*-

import pyxel

class APP:
  def __init__(self):
      pyxel.init(128, 128, title="pyxel")
      
      self.list1  = [10, 20, 30, 40]
      self.list2  = ["A", "B", "C", "D"]
      self.list3  = ["A", 2, [1,2], ("a","b")]
      
      self.tuple = (10, 20, 30, 40)
      
      self.dic    = {"TANAKA": "TARO", "SUZUKI": "HANAKO",}
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      pass

  def draw(self):
      pyxel.cls(0)
      pyxel.text(1, 10, str(self.list1), 6)
      pyxel.text(1, 20, str(self.list1[0]), 6)
      pyxel.text(1, 30, str(self.list1[3]), 6)      
      
      pyxel.text(1, 40, str(self.list2), 10)
      pyxel.text(1, 50, self.list2[1], 10)
      pyxel.text(1, 60, self.list2[2], 10)      

      pyxel.text(1, 70, str(self.list3), 5)
      pyxel.text(1, 80, self.list3[0], 5)
      pyxel.text(1, 90, str(self.list3[1]), 5)      
      
      pyxel.text(1, 100, str(self.tuple), 9)
      
      pyxel.text(1, 110, str(self.dic), 7)
      pyxel.text(1, 120, str(self.dic["TANAKA"]), 7)      
      
      
APP()