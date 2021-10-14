# -*- coding: utf-8 -*-
#mtr.py

import pyxel
import numpy as np
from random import randint

class APP:
  def __init__(self):
      self.x = 0
      self.y = -40
      self.pos_x = np.random.randint(5, 15, (30, 1))
      self.pos_y = np.random.randint(0, 40, (30, 1))
      self.num = np.random.randint(0, 9, (20, 30))
      
      pyxel.init(128, 128, caption="mtr",scale=6)
      
      pyxel.load('assets/mtr.pyxres')
      
      pyxel.mouse(False)
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      pass

  def draw(self):
      pyxel.cls(0)
     
      for i in range(30):
          for ii in range(20):
              c1 = randint(1, 30)
              c2 = randint(1, 30)
              if c1 == c2:
                  c = 11
              else:
                  c = 3
              
              pyxel.text(self.x+self.pos_x[i]*i, self.y+self.pos_y[i]-6*(ii), 
                     str(self.num[ii][i]), c)
          
      
      self.y += 1
      if self.y > 260:
          self.y = -40
          self.pos_x = np.random.randint(5, 15, (30, 1))

                  
APP()