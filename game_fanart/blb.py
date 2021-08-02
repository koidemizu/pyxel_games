# -*- coding: utf-8 -*-
#blb.py

import pyxel

class APP:
  def __init__(self):
      pyxel.init(128, 128, caption="BLB",scale=6)
      
      pyxel.load('assets/blb.pyxres')
      
      pyxel.mouse(False)
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      pass

  def draw(self):
      pyxel.cls(0)
      
      pyxel.bltm(0,0,0,0,0,128,128)
      
      pyxel.rect(0, 100, 128, 63, 0)
      pyxel.rect(0, 82, 18, 20, 0)
      pyxel.rect(18, 90, 110, 10, 0)
      pyxel.blt(2,84,2,0,240,16,16,14)
      pyxel.blt(20,92,0,0,0,64,8,14)
      pyxel.blt(5,105,0,0,8,72,8,14)
      pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)

                  
APP()