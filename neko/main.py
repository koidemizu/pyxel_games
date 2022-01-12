# -*- coding: utf-8 -*-
#Neko

import pyxel

class APP:
  def __init__(self):
      self.player = Player()
      
      pyxel.init(128, 128, caption="TEST", scale=5,)
      
      pyxel.load('assets/assets.pyxres')
      
      pyxel.mouse(False)
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      #Move UP
      if pyxel.btn(pyxel.KEY_UP):
          self.player.p_m = 1
          self.player.p_c += 1
          a = self.check_move(1)
          if a == 1:
              self.player.p_y -= 1
 
      #Move DOWN
      elif pyxel.btn(pyxel.KEY_DOWN):
          self.player.p_m = 3
          self.player.p_c += 1
          a = self.check_move(3)
          if a == 1:
              self.player.p_y += 1

      #Move RIGHT
      elif pyxel.btn(pyxel.KEY_RIGHT):
          self.player.p_m = 2
          self.player.p_c += 1
          a = self.check_move(2)
          if a == 1:
              self.player.p_x += 1

      #Move LEFT       
      elif pyxel.btn(pyxel.KEY_LEFT):
          self.player.p_m = 4
          self.player.p_c += 1
          a = self.check_move(4)
          if a == 1:
              self.player.p_x -= 1

      else:
          self.player.p_m = 0
          self.player.p_c = 0
          self.player.p_m2 = 0

  def draw(self):
      pyxel.cls(0)
      
      #Draw tilemap
      pyxel.bltm(0,0,0,0,0,16,16)
      
      #Player draw//////////////////////////////
      x = self.player.p_x
      y = self.player.p_y

      if self.player.p_m == 1:
          if self.player.p_c % 15 == 0:
              self.player.p_m2 += 1
          if self.player.p_m2 % 2 == 0:
              pyxel.blt(x,y,0,16,24,8,8,2)
          else:
              pyxel.blt(x,y,0,8,24,8,8,2)
      elif self.player.p_m == 2:
          if self.player.p_c % 15 == 0:
              self.player.p_m2 += 1
          if self.player.p_m2 % 2 == 0:
              pyxel.blt(x,y,0,0,8,8,8,2)
          else:
              pyxel.blt(x,y,0,8,8,8,8,2)
      elif self.player.p_m == 3:
          if self.player.p_c % 15 == 0:
              self.player.p_m2 += 1
          if self.player.p_m2 % 2 == 0:
              pyxel.blt(x,y,0,16,0,8,8,2)
          else:
              pyxel.blt(x,y,0,8,0,8,8,2)              
      elif self.player.p_m == 4:
          if self.player.p_c % 15 == 0:
              self.player.p_m2 += 1
          if self.player.p_m2 % 2 == 0:
              pyxel.blt(x,y,0,0,16,8,8,2)
          else:
              pyxel.blt(x,y,0,8,16,8,8,2)
      elif self.player.p_m == 0:
          pyxel.blt(x,y,0,0,0,8,8,2)
          
      #/////////////////////////////////////////
      #pyxel.rectb(self.player.p_x, self.player.p_y, 8, 8, 8)       
          
  def check_move(self, x):
      """
      Player coordinates
           
      """
      px = int((self.player.p_x - 1) / 8)
      py = int((self.player.p_y) / 8)
      px2 = int((self.player.p_x + 8) / 8)
      py2 = int((self.player.p_y + 8) / 8)
      px3 = int((self.player.p_x + 6) / 8)
      py3 = int((self.player.p_y + 6) / 8)
      px4 = int((self.player.p_x) / 8)
      py4 = int((self.player.p_y + 2) / 8)
      
      pm = pyxel.tilemap(0).get(px3, py)
      pm2 = pyxel.tilemap(0).get(px4, py)
      pm3 = pyxel.tilemap(0).get(px3, py2)
      pm4 = pyxel.tilemap(0).get(px4, py2)
      
      pm5 = pyxel.tilemap(0).get(px, py3)
      pm6 = pyxel.tilemap(0).get(px2, py3)
      pm7 = pyxel.tilemap(0).get(px, py4)
      pm8 = pyxel.tilemap(0).get(px2, py4)
      
      #Move UP
      if x == 1:
          if pm < 160 and pm2 < 160:
              return 1
      #Move DOWN
      elif x == 3:
          if pm3 < 160 and  pm4 < 160:
              return 1

      #Move RIGHT
      elif x == 2:
          if pm6 < 160 and pm8 < 160:
              return 1
      #Move LEFT
      elif x == 4:
          if pm5 < 160 and pm7 < 160:
              return 1
      else:
          return 0

class Player:
    def __init__(self):
        self.p_x = 8
        self.p_y = 8
        self.p_m = 0
        self.p_m2 = 0
        self.p_c = 0
                
APP()

