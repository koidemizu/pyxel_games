# -*- coding: utf-8 -*-
#blb.py

import pyxel
from random import randint

class APP:
  def __init__(self):
      pyxel.init(128, 128,capture_sec=30)
      
      pyxel.load('assets/hrp.pyxres')
      
      pyxel.mouse(False)
      
      self.game_status = 0
      self.player = [3, 7]
      self.player_move = 0
      self.enemys = [
          [2, 2, randint(0, 5), randint(0, 1)],
          [4, 4, randint(0, 5), randint(0, 1)],
          [5, 0, randint(0, 5), randint(0, 1)],
          [0, 4, randint(0, 5), randint(0, 1)],         
          [6, 3, randint(0, 5), randint(0, 1)],
          [6, 6, randint(0, 5), randint(0, 1)],    
          ]
      self.bang = []
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      if pyxel.btnp(pyxel.KEY_S) and self.game_status == 0:
          self.game_status = 1
          
      if pyxel.btnp(pyxel.KEY_UP) and self.player[1] > 0:
          if self.player_move == 0:
              self.player[1] = self.player[1] - 1
              self.player_move = 1
      elif pyxel.btnp(pyxel.KEY_DOWN) and self.player[1] < 7:
          if self.player_move == 0:
              self.player[1] = self.player[1] + 1
              self.player_move = 1
      elif pyxel.btnp(pyxel.KEY_RIGHT) and self.player[0] < 7:
          if self.player_move == 0:
              self.player[0] = self.player[0] + 1
              self.player_move = 1
      elif pyxel.btnp(pyxel.KEY_LEFT) and self.player[0] > 0:    
          if self.player_move == 0:
              self.player[0] = self.player[0] - 1
              self.player_move = 1
          
      if self.player_move == 1 and self.game_status == 1:
          #self.bang = []
          for i in self.enemys:
              x = abs(i[0] - self.player[0])
              y = abs(i[1] - self.player[1])
              x2 = i[0] - self.player[0]
              y2 = i[1] - self.player[1]
              if x > y:
                  if x2 > 0:
                      i[0] = i[0] - 1
                  else:
                      i[0] = i[0] + 1
              else:
                  if y2 > 0:
                      i[1] = i[1] -1
                  else:
                      i[1] = i[1] + 1
              if i[0] == self.player[0] and i[1] == self.player[1]:
                  self.game_status = 99
                    
             
              for i2 in self.enemys:
                  if i == i2:
                      pass
                  else:                      
                      if i[0] == i2[0] and i[1] == i2[1]:                          
                          self.bang.append([i2[0], i2[1]])
                          self.bang.append([i[0], i[1]])
                          print(self.bang)
                          i[0] = 50
                          i2[0] = 50
                     
                    
          for i3 in range(len(self.enemys)):
              if self.enemys[i3][0] > 20:
                  del self.enemys[i3]
              break
          
          if len(self.enemys) < 2:              
              self.enemys = []
          
          self.player_move = 0          
          

  def draw(self):
      pyxel.cls(0)
      
      if self.game_status == 0:
          pyxel.blt(0,0,0,0,0,128,128)
      elif self.game_status == 1:
          pyxel.bltm(0,0,0,0,0,128,128)
          pyxel.blt(self.player[0]*16,self.player[1]*16,1,0,40,16,16,14)
          for b in self.bang:
              print(b)
              pyxel.blt(b[0]*16,b[1]*16,1,16,40,16,16,14)          
          for i in self.enemys:
              pyxel.blt(i[0]*16,i[1]*16,1,0+i[2]*16,8+i[3]*16,16,16,14)
      elif self.game_status == 99:
          pyxel.bltm(0,0,0,0,0,128,128)
          pyxel.blt(self.player[0]*16,self.player[1]*16,1,0,40,16,16,14)
          for i in self.enemys:
              pyxel.blt(i[0]*16,i[1]*16,1,0+i[2]*16,8+i[3]*16,16,16,14)                        
          pyxel.text(48, 48, "GAME OVER!!", pyxel.frame_count % 16)
      
      
      

                  
APP()