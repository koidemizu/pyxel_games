# -*- coding: utf-8 -*-
"""
Program_Name:Q_Shooter

"""

from random import randint, randrange
import pyxel

class APP:
  def __init__(self):
      self.player = Player()
      self.p_shots = []
      
      pyxel.init(150, 200, caption="Q_Shooter")
      
      pyxel.mouse(False)
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      #Player move by mouse.        
      move_x = pyxel.mouse_x
      move_y = pyxel.mouse_y
      if move_x + 2 > 150:
          move_x = 145
      if move_x < 0:
          move_x = 0          
      if move_y + 2 > 200:
          move_y = 197
      if move_y < 0:
          move_y = 0          
      self.player.update(move_x, move_y)
      #Auto attack
      if len(self.p_shots) < 15 and pyxel.frame_count % 6 == 0:
          new_shot = P_Shot(self.player.player_x, self.player.player_y)
          self.p_shots.append(new_shot)
      #p_shots update
      i = len(self.p_shots)
      for i in range(i):
          self.p_shots[i].update(self.p_shots[i].pos_x, 
                                 self.p_shots[i].pos_y - 3)
          if self.p_shots[i].pos_y < 0:
              del self.p_shots[i]
              break
              
                            
              
  def draw(self):
      pyxel.cls(0)
      pyxel.rect(self.player.player_x, self.player.player_y, 3, 3, 
                 self.player.color)
      for i in self.p_shots:
          pyxel.rect(i.pos_x, i.pos_y, 2, 2, i.color)
      
      
class Player:   
  def __init__(self):
      self.player_x = 70
      self.player_y = 105
      self.color = 8 # 0~15
  
  def update(self, x, y):
      self.player_x = x
      self.player_y = y

class P_Shot:
  def __init__(self, x, y):
      self.pos_x = x
      self.pos_y = y
      self.color = 8 # 0~15
  def update(self, x, y):
      self.pos_x = x
      self.pos_y = y
      
APP()





