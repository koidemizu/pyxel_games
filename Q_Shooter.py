# -*- coding: utf-8 -*-
"""
Program_Name:Q_Shooter

"""

from random import randint
from random import randrange
import pyxel

class APP:
  def __init__(self):
      self.player = Player()
      self.p_shots = []
      self.blits = 5
      #self.enemys = []
      self.new_rects = []
      self.rects = []
      self.effects = []
      
      self.Game_time = 0
      
      self.stage_ctr = 99
      self.stage_count = 0
      self.move_count = 0
      self.game_over = False
      self.update_type = 0
      self.update_chk = False
      
      #self.enemy_pos = {
       #   "1":[70, 65],
        #  "2":[35, 70],
         # "3":[50, 100],
          #"4":[80, 70],
          #"5":[45, 80],
          #}
      self.rects_pos = {
          "1":[[10, 10, 50, 50, 3, 0],[30, 30, 70, 30, 12, 0],
               [80, 90, 40, 20, 12, 1]],
          "2":[[10, 10, 50, 50, 3, 0],[30, 30, 70, 30, 12, 0],
               [80, 90, 40, 20, 12, 1]],
          "3":[[10, 10, 50, 50, 3, 0],[30, 30, 70, 30, 12, 0],
               [80, 90, 40, 20, 12, 1]],
          "4":[[10, 10, 50, 50, 3, 0],[30, 30, 70, 30, 12, 0],
               [80, 90, 40, 20, 12, 1]],
          "5":[[10, 10, 50, 50, 3, 0],[30, 30, 70, 30, 12, 0],
               [80, 90, 40, 20, 12, 1]],
          }
      
      pyxel.init(150, 200, caption="Q_Shooter")
      
      pyxel.mouse(False)
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      if self.stage_ctr == 1:
          self.Player_ctr()
          self.Shot_ctr()
          self.Rect_ctr()
          self.Effect_upd()
          
          if len(self.rects) <= 0:
              
              if self.update_chk == False:
                  if self.Game_time % 3 == 0:
                      self.update_type = 1
                  elif self.Game_time % 4 == 0:
                      self.update_type = 2
                  elif self.Game_time % 5 == 0:
                      self.update_type = 3   
                  else:
                      self.update_type = 4
                  self.update_chk = True
                  
              self.move_count = self.move_count + 1
              if self.move_count >= 150:
                  self.stage_ctr = 0
                  self.move_count = 0
                  self.blits = 5
                 # self.enemys = []
                  self.new_rects = []
                  self.rects = []
                  self.effects = []
                  self.update_chk = False
                  self.player.p_up(self.update_type)
                  self.update_type = 0
          else:
             self.Time_count()
             
                  
      elif self.stage_ctr == 99:
          if pyxel.btnp(pyxel.KEY_S):
              self.stage_ctr = 0
              
      elif self.stage_ctr == 0:
          self.stage_ctr = 1
          self.stage_count = self.stage_count + 1
          
          if self.stage_count > 99:
              #new_enemy = Enemy(self.enemy_pos[str(self.stage_count)][0], 
               #                 self.enemy_pos[str(self.stage_count)][1])
              #self.enemys.append(new_enemy)
          
              self.new_rects = []
          
              self.new_rects = self.rects_pos[str(self.stage_count)]
              for n in self.new_rects:
                  new_rect = Rect(n[0], n[1], n[2], n[3], n[4], n[5])
                  self.rects.append(new_rect)
          else:
              #new_enemy = Enemy(randint(10, 140),randint(10, 110))
              #self.enemys.append(new_enemy)
              
              for i in range(self.stage_count):
                  self.new_rects = []
                  c = randint(1,14)
                  if c == 6:
                      c = 8
                  new_rect = Rect(randint(15,135),randint(15,100),
                                  randint(10,60),
                                  randint(10,60),c,randint(0,4), 
                                  randrange(50,101,10))
                  self.rects.append(new_rect)
                  
              self.player.player_x = 75
              self.player.player_y = 180
              
      elif self.stage_ctr == 98:
          self.Effect_upd()
          if pyxel.btnp(pyxel.KEY_R):
              self.Restart()
          if pyxel.btnp(pyxel.KEY_C):
              self.Continue()
              
  def draw(self):
      pyxel.cls(0)
      
      if self.stage_ctr == 1 or self.stage_ctr == 98:
          
          pyxel.text(2, 190, "TIME:" + str(self.Game_time), 8)
      
          #pyxel.line(0, 178, 150, 178, 2)
          if self.stage_ctr == 1:
              pyxel.rect(self.player.player_x, self.player.player_y, 3, 3, 
                         self.player.color)
          for i in self.p_shots:
              pyxel.rect(i.pos_x, i.pos_y, 2, 2, i.color)
          
          #for e in self.enemys:
           #   pyxel.rect(e.enemy_x, e.enemy_y, 3, 3, e.color)
    
          for r in self.rects:
              pyxel.rectb(r.pos_x, r.pos_y, r.pos_x2, r.pos_y2, r.color)
        
          for f in self.effects:
              pyxel.rect(f.pos_x, f.pos_y, 1, 1, f.color)
        
          m_x = pyxel.mouse_x
          m_y = pyxel.mouse_y
          pyxel.tri(m_x, m_y, m_x - 1, m_y + 1, m_x + 1, m_y + 1, 7)
        
          if len(self.rects) <= 0:
              pyxel.text(2, 50, "STAGE CLEAR", 8)
              pyxel.text(2, 60, "UPDATE_TYPE = " + str(self.update_type), 8)
        
          if self.stage_ctr == 98:
              pyxel.text(2, 50, "---GameOver---", 8)
              pyxel.text(2, 60, "R:ReStart", 8)
              pyxel.text(2, 70, "C:Continue", 8)
              
      elif self.stage_ctr == 99:
          pyxel.text(2, 50, "Q_Shooter", 8)
          pyxel.text(2, 60, "S:Start", 8)
          
  def Restart(self):
      self.player = Player()
      self.p_shots = []
      self.blits = 5
      #self.enemys = []
      self.new_rects = []
      self.rects = []
      self.effects = []
      
      self.Game_time = 0
      
      self.stage_ctr = 99
      self.stage_count = 0
      self.move_count = 0
      self.game_over = False
      
  def Continue(self):
      self.player = Player()
      self.p_shots = []
      self.blits = 5
      #self.enemys = []
      self.new_rects = []
      self.rects = []
      self.effects = []
      
      self.Game_time = 0
      
      self.stage_ctr = 0
      self.stage_count = self.stage_count - 1
      self.move_count = 0
      self.game_over = False
      
  def Player_ctr(self):
      #Player move by mouse.        
      move_x = pyxel.mouse_x
      move_y = pyxel.mouse_y
   #   if move_x + 2 > 150:
    #      move_x = 145
     # if move_x < 0:
      #    move_x = 0          
      #if move_y + 2 > 200:
       #   move_y = 197
      #if move_y - 2 < 2:
       #   move_y = 2
      #if move_y < 0:
       #   move_y = 0          
      self.player.update(move_x, move_y)
      
      r = len(self.rects)
      for r in range(r):
          x = self.Hit_chk_PR(r)
          if x == 1:
              self.game_over = True
              self.stage_ctr = 98
              self.Effect_make(self.player.player_x, 
                                   self.player.player_y, 
                                   self.player.color)
              
      #Attack
      if (pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON, 5, 15) and
         (len(self.p_shots) < self.player.rof) and (self.blits > 0)):
          new_shot = P_Shot(self.player.player_x + 0.5, self.player.player_y)
          self.p_shots.append(new_shot)
          #self.blits = self.blits - 1
  
  def Rect_ctr(self):
      r = len(self.rects)
      for i in range(r):
          if ((pyxel.frame_count % int(self.rects[i].attack_time) == 0) and
          (self.rects[i].mode1 < 90)):
              n = randint(97, 99)
              x = self.rects[i].attack(n)
              self.rects.append(x)
          if ((self.rects[i].pos_y > 220) or (self.rects[i].pos_x > 160) or
             (self.rects[i].pos_x < -10)):
              del self.rects[i]
              break
          if self.rects[i].hp <= 0:
              del self.rects[i]
              break
          
          self.rects[i].update()
          
  def Shot_ctr(self):
      #p_shots update
      r = len(self.rects)
      i = len(self.p_shots)
  #    e = len(self.enemys)
      for i in range(i):
          self.p_shots[i].update(self.p_shots[i].pos_x, 
                                 self.p_shots[i].pos_y - self.player.spd)
          for r in range(r):
              x = self.Hit_chk_SR(r, i)
              if x == 1:
                  self.p_shots[i].exist = False
                  self.Effect_make(self.p_shots[i].pos_x, 
                                   self.p_shots[i].pos_y,
                                   self.rects[r].color)
                  if self.rects[r].hp <= 0:
                      del self.rects[r]
                  break
         # for e in range(e):
          #    x = self.Hit_chk_SE(e, i)
           #   if x == 1:
           #       self.p_shots[i].exist = False
            #      self.Effect_make(self.enemys[e].enemy_x, 
             #                      self.enemys[e].enemy_y,
              #                     self.enemys[e].color)
               #   del self.enemys[e]
              #break
          if self.p_shots[i].pos_y < 0:
              self.p_shots[i].exist = False
          if self.p_shots[i].exist == False:
              del self.p_shots[i]
              break
      
  def Hit_chk_SR(self, r, i):
      if ((self.rects[r].pos_x < self.p_shots[i].pos_x < 
          (self.rects[r].pos_x + self.rects[r].pos_x2))and
          (self.rects[r].pos_y < self.p_shots[i].pos_y < 
          (self.rects[r].pos_y + self.rects[r].pos_y2))):
          if self.rects[r].mode1 == 4:
              m = 0
          elif self.rects[r].mode1 == 99:
              m = 97
          else:
              m = self.rects[r].mode1 + 1
          self.rects[r].mode_cng(m)
          self.rects[r].hp = self.rects[r].hp - self.player.atk
          return 1
      else:
          return 0
      
  def Hit_chk_PR(self, r):
      if ((self.rects[r].pos_x < self.player.player_x < 
          (self.rects[r].pos_x + self.rects[r].pos_x2))and
          (self.rects[r].pos_y < self.player.player_y < 
          (self.rects[r].pos_y + self.rects[r].pos_y2))):
          return 1
      else:
          return 0
      
  #def Hit_chk_SE(self, e, i):
   #   if ((self.enemys[e].enemy_x <= self.p_shots[i].pos_x <= 
    #      (self.enemys[e].enemy_x + 3))and
     #     (self.enemys[e].enemy_y <= self.p_shots[i].pos_y <= 
      #    (self.enemys[e].enemy_y + 3))and
       #   (self.p_shots[i].exist == True)):
        #  return 1
      #else:
       #   return 0
     
  def Effect_make(self, a, b, c):
      for n in range(10):
          x = randint(-3, 3)
          y = randint(-3, 3)
          x = x * 0.1
          y = y * 0.1
          new_effect = Effect(a, b, x, y, c, 30)
          self.effects.append(new_effect)
      
  def Effect_upd(self):
      #Effect update
      f = len(self.effects)
      for f in range(f):
          self.effects[f].update()
          if self.effects[f].time2 == self.effects[f].time:
              del self.effects[f]
              break
     
  def Time_count(self):
      self.Game_time = self.Game_time + 1
      
        
class Player:   
  def __init__(self):
      self.player_x = 70
      self.player_y = 105
      self.color = 12 # 0~15
      self.atk = 1
      self.spd = 3
      self.rof = 1
      self.mv_s = 1
  
  def update(self, x, y):
      if self.player_x < x:
          self.player_x = self.player_x + self.mv_s
      elif self.player_x > x:
          self.player_x = self.player_x - self.mv_s
      if self.player_y < y:
          self.player_y = self.player_y + self.mv_s
      elif self.player_y > y:
          self.player_y = self.player_y - self.mv_s
  def p_up(self, x):
      if x == 1:
          self.atk = self.atk + 0.2
      elif x == 2:
          self.spd = self.spd + 0.2
      elif x == 3:
          self.rof = self.rof + 1
      elif x == 4:
          self.mv_s = self.mv_s + 1

class Enemy:   
  def __init__(self, x, y):
      self.enemy_x = x
      self.enemy_y = y
      self.enemy_x2 = 0
      self.enemy_y2 = 0
      self.color = 8 # 0~15
      self.mode = 0
  

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
  def __init__(self, x, y, x2, y2, c, m, a):
      self.pos_x = x
      self.pos_y = y
      self.pos_x2 = x2
      self.pos_y2 = y2      
      self.color = c # 0~15
      self.mode1 = m
      self.mode2 = 0
      self.hp = 5
      self.attack_time = a
  def mode_cng(self, m):
      self.mode1 = m
  def update(self):
      if self.mode1 == 1:
          if self.pos_x < 2:
              self.mode2 = 1
          elif self.pos_x + self.pos_x2 > 148:
              self.mode2 = 0
          if self.mode2 == 0:    
              self.pos_x = self.pos_x - 1
          elif self.mode2 == 1:
              self.pos_x = self.pos_x + 1
      elif self.mode1 == 2:
          if self.pos_y < 2:
              self.mode2 = 1
          elif self.pos_y + self.pos_y2 > 200:
              self.mode2 = 0
          if self.mode2 == 0:    
              self.pos_y = self.pos_y - 1
          elif self.mode2 == 1:
              self.pos_y = self.pos_y + 1
      elif self.mode1 == 3:
          if ((self.pos_y < 2) or (self.pos_x < 2)):
              self.mode2 = 1
          elif ((self.pos_x + self.pos_x2 > 148) or 
              (self.pos_y + self.pos_y2 > 200)):
              self.mode2 = 0
          if self.mode2 == 0:    
              self.pos_x = self.pos_x - 1
              self.pos_y = self.pos_y - 1
          elif self.mode2 == 1:
              self.pos_x = self.pos_x + 1
              self.pos_y = self.pos_y + 1
      elif self.mode1 == 4:
          if ((self.pos_y + self.pos_y2 > 200) or (self.pos_x < 2)):
              self.mode2 = 1
          elif ((self.pos_x + self.pos_x2 > 148) or 
              (self.pos_y < 2)):
              self.mode2 = 0
          if self.mode2 == 0:    
              self.pos_y = self.pos_y + 1
              self.pos_x = self.pos_x - 1
          elif self.mode2 == 1:
              self.pos_y = self.pos_y - 1
              self.pos_x = self.pos_x + 1
      elif self.mode1 == 97:
          self.pos_y = self.pos_y + 1.5
          self.pos_x = self.pos_x + 1
      elif self.mode1 == 98:
          self.pos_y = self.pos_y + 1.5
          self.pos_x = self.pos_x - 1
      elif self.mode1 == 99:
          self.pos_y = self.pos_y + 1.5
  def attack(self,n):
      new_rect = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+(self.pos_y2/2),
                      6,6,self.color,n,10)
      return new_rect

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





