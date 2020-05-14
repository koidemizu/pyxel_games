# -*- coding: utf-8 -*-
"""
Program_Name:Q_Shooter

"""

from random import randint
import pyxel

class APP:
  def __init__(self):
      self.player = Player()
      self.p_shots = []
      self.enemys = []
      self.rects = []
      self.effects = []
      
      self.stage_start = False
      
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
      if move_y - 2 < 178:
          move_y = 180
      if move_y < 0:
          move_y = 0          
      self.player.update(move_x, move_y)
      
      #Attack
      if (pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 5, 15) and
         (len(self.p_shots) < 1)):
          new_shot = P_Shot(self.player.player_x + 0.5, self.player.player_y)
          self.p_shots.append(new_shot)
          
      #p_shots update
      r = len(self.rects)
      i = len(self.p_shots)
      e = len(self.enemys)
      for i in range(i):
          self.p_shots[i].update(self.p_shots[i].pos_x, 
                                 self.p_shots[i].pos_y - 3)
          for r in range(r):
              if ((self.rects[r].pos_x < self.p_shots[i].pos_x < 
                  (self.rects[r].pos_x + self.rects[r].pos_x2))and
                  (self.rects[r].pos_y < self.p_shots[i].pos_y < 
                  (self.rects[r].pos_y + self.rects[r].pos_y2))):
                  self.p_shots[i].exist = False
          for e in range(e):
              if ((self.enemys[e].enemy_x <= self.p_shots[i].pos_x <= 
                  (self.enemys[e].enemy_x + 3))and
                  (self.enemys[e].enemy_y <= self.p_shots[i].pos_y <= 
                  (self.enemys[e].enemy_y + 3))and
                  (self.p_shots[i].exist == True)):
                  self.p_shots[i].exist = False
                  for n in range(10):
                      x = randint(-3, 3)
                      y = randint(-3, 3)
                      x = x * 0.1
                      y = y * 0.1
                      new_effect = Effect(self.enemys[e].enemy_x,
                                          self.enemys[e].enemy_y,
                                          x, y ,self.enemys[e].color,30)
                      self.effects.append(new_effect)
                  del self.enemys[e]
              break
          if self.p_shots[i].pos_y < 0:
              self.p_shots[i].exist = False
          if self.p_shots[i].exist == False:
              del self.p_shots[i]
              break
        
      #Effect update
      f = len(self.effects)
      for f in range(f):
          self.effects[f].update()
          if self.effects[f].time2 == self.effects[f].time:
              del self.effects[f]
              break
          
      #Rects create
      new_rect = Rect(10, 10, 50, 50, 3)
      self.rects.append(new_rect)
      for n in range(6, 50, 15):
          for m in range(6, 50, 12):
              new_rect = Rect(10+m, 10+n, 5, 6, 3)
              self.rects.append(new_rect)
      
      #Enemys create
      if self.stage_start == False:
          new_enemy = Enemy(70, 60)
          self.enemys.append(new_enemy)
          self.stage_start = True
              
                            
              
  def draw(self):
      pyxel.cls(0)
      
      pyxel.line(0, 178, 150, 178, 2)
      
      pyxel.rect(self.player.player_x, self.player.player_y, 3, 3, 
                 self.player.color)
      for i in self.p_shots:
          pyxel.rect(i.pos_x, i.pos_y, 2, 2, i.color)
          
      for e in self.enemys:
          pyxel.rect(e.enemy_x, e.enemy_y, 3, 3, e.color)
    
      for r in self.rects:
          pyxel.rectb(r.pos_x, r.pos_y, r.pos_x2, r.pos_y2, r.color)
        
      for f in self.effects:
          pyxel.rect(f.pos_x, f.pos_y, 1, 1, f.color)
      
      
class Player:   
  def __init__(self):
      self.player_x = 70
      self.player_y = 105
      self.color = 12 # 0~15
  
  def update(self, x, y):
      self.player_x = x
      self.player_y = y

class Enemy:   
  def __init__(self, x, y):
      self.enemy_x = x
      self.enemy_y = y
      self.enemy_x2 = 0
      self.enemy_y2 = 0
      self.color = 8 # 0~15
  
  def update(self, x, y):
      self.player_x = x
      self.player_y = y

class P_Shot:
  def __init__(self, x, y):
      self.pos_x = x
      self.pos_y = y
      self.color = 12 # 0~15
      self.exist = True
  def update(self, x, y):
      self.pos_x = x
      self.pos_y = y
    
class Rect:
  def __init__(self, x, y, x2, y2, c):
      self.pos_x = x
      self.pos_y = y
      self.pos_x2 = x2
      self.pos_y2 = y2      
      self.color = c # 0~15
  def update(self, x, y):
      self.pos_x = x
      self.pos_y = y

class Effect:
  def __init__(self, x, y, x2, y2, c, t):
      self.pos_x = x
      self.pos_y = y
      self.pos_x2 = x2
      self.pos_y2 = y2      
      self.color = c # 0~15
      self.time = t
      self.time2 = 0
  def update(self):
      self.pos_x = self.pos_x - self.pos_x2
      self.pos_y = self.pos_y - self.pos_y2
      self.time2 = self.time2 + 1
      
APP()





