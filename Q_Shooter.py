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
      self.rectsb = []
      self.effects = []
      
      self.Game_time = 0
      self.uc3 = 0
      
      self.stage_ctr = 99
      self.stage_count = 9
      self.move_count = 0
      self.game_over = False
      self.game_clear = False
      self.update_type = 0
      self.update_chk = False
      self.sp_flug = False
      self.sp_count = 0
      
      self.demo_flug = False
      
      #self.enemy_pos = {
       #   "1":[70, 65],
        #  "2":[35, 70],
         # "3":[50, 100],
          #"4":[80, 70],
          #"5":[45, 80],
          #}
      self.rects_pos = {
          "5":[[50, 10, 20, 60, 7, 1, 70, 0],[100, 10, 20, 60, 7, 1, 60, 0],
               [51, 20, 25, 25, 7, 1, 50, 0],[96, 20, 25, 25, 7, 1, 40, 0],
               [67, 20, 40, 35, 7, 1, 50, 0],
               [54, 14, 10, 10, 8, 1, 70, 2], [104, 14, 10, 10, 8, 1, 70, 2],
               [54, 54, 10, 10, 8, 1, 75, 2], [104, 54, 10, 10, 8, 1, 75, 2],
               [80, 30, 10, 10, 8, 1, 120, 11],],
          "10":[[2, 1, 20, 70, 7, 0, 70, 0],[130, 1, 20, 70, 7, 0, 60, 0],
               [2, 10, 148, 25, 7, 0, 50, 0],[60, 20, 35, 35, 7, 0, 40, 0],
               [52, 50, 50, 10, 7, 0, 50, 0],[42, 57, 72, 20, 7, 0, 50, 0],
               [52, 60, 50, 10, 7, 0, 50, 0],[38, 77, 80, 10, 7, 0, 50, 0],
               [52, 1, 50, 35, 7, 0, 50, 0],[38, 1, 80, 35, 7, 0, 50, 0],
               [10, 14, 10, 10, 5, 0, 135, 3], [132, 14, 10, 10, 5, 0, 135, 3],
               [7, 55, 10, 10, 5, 0, 120, 3], [135, 55, 10, 10, 5, 0, 120, 3],
               [39, 5, 5, 5, 2, 0, 50, 1], [110, 5, 5, 5, 2, 0, 50, 1],
               [46, 5, 5, 5, 2, 0, 55, 1], [103, 5, 5, 5, 2, 0, 55, 1],
               [53, 5, 5, 5, 2, 0, 60, 1], [96, 5, 5, 5, 2, 0, 60, 1],
               [60, 5, 5, 5, 2, 0, 65, 1], [89, 5, 5, 5, 2, 0, 65, 1],
               [73, 38, 10, 10, 8, 0, 120, 12],],
          "15":[[10, 10, 50, 50, 3, 0],[30, 30, 70, 30, 12, 0],
               [80, 90, 40, 20, 12, 1]],
          "20":[[10, 10, 50, 50, 3, 0],[30, 30, 70, 30, 12, 0],
               [80, 90, 40, 20, 12, 1]],
          "25":[[10, 10, 50, 50, 3, 0],[30, 30, 70, 30, 12, 0],
               [80, 90, 40, 20, 12, 1]],
          }
      
      pyxel.init(150, 200, caption="Q_Shooter")
      
      pyxel.mouse(False)
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      if self.stage_ctr == 1:
          self.Player_ctr()
          self.Shot_ctr()
          if self.stage_count % 5 == 0:
              x = self.stage_count
              if self.sp_flug == True:
                  self.sp_count = self.sp_count + 1
              if self.sp_count > 25:
                  self.sp_flug = False
                  self.sp_count = 0
              self.Rect_ctr_B(x)
          else:
              self.Rect_ctr()
          self.Effect_upd()
          
          if len(self.rects) <= 0:
              if self.stage_count == 25:
                  self.game_clear = False
              #uc1 = len(str(self.Game_time))
              #uc2 = str(self.Game_time)[-1*uc1]
              #uc3 = int(uc2)
              if self.update_chk == False:
                  if self.uc3 % 3 == 0:
                      self.update_type = 1
                  elif self.uc3 % 2 == 0:
                      self.update_type = 2
                  elif self.uc3 % 5 == 0:
                      self.update_type = 3   
                  else:
                      self.update_type = 0
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
                  self.sp_flug = False
                  self.sp_count = 0
                  self.player.p_up(self.update_type)
                  self.update_type = 0
          else:
             self.Time_count()
             
                  
      elif self.stage_ctr == 99:
          if pyxel.btnp(pyxel.KEY_S):
              self.stage_ctr = 0
              self.rects = []
          if self.demo_flug == True:
              pass
          else:
              for i in range(5):
                  c = randint(1,14)
                  if c == 8:
                      c = 6
                  new_rect = Rect(randint(15,135),randint(15,100),
                                  randint(10,60),
                                  randint(10,60),c,randint(0,4), 
                                  randrange(50,101,10),0,1)
                  self.rects.append(new_rect)
              self.demo_flug = True
          self.Rect_ctr()
              
      elif self.stage_ctr == 0:
          self.stage_ctr = 1
          self.stage_count = self.stage_count + 1
          hp_b = self.stage_count * 0.1
          
          if self.stage_count % 5 == 0:
              
              self.new_rects = []
          
              self.new_rects = self.rects_pos[str(self.stage_count)]
              for n in self.new_rects:
                  new_rect = Rect(n[0], n[1], n[2], n[3], n[4], n[5], 
                                  n[6], n[7], hp_b)
                  self.rects.append(new_rect)
          else:
              #new_enemy = Enemy(randint(10, 140),randint(10, 110))
              #self.enemys.append(new_enemy)
              st_c = self.stage_count
              if st_c > 10:
                  st_c = 10
              for i in range(st_c):
                  self.new_rects = []
                  c = randint(1,14)
                  if c == 8:
                      c = 6
                  v = self.stage_count
                  if v > 10:
                      v = 10
                  a = randint(1, v)
                  new_rect = Rect(randint(15,135),randint(15,100),
                                  randint(10,60),
                                  randint(10,60),c,randint(0,4), 
                                  randrange(50,101,10),a,hp_b)
                  self.rects.append(new_rect)
                  
              self.player.player_x = 75
              self.player.player_y = 180
              
      elif self.stage_ctr == 98:
          if self.stage_count % 5 == 0:
              x = self.stage_count
              if self.sp_flug == True:
                  self.sp_count = self.sp_count + 1
              if self.sp_count > 25:
                  self.sp_flug = False
                  self.sp_count = 0
              self.Rect_ctr_B(x)
          else:
              self.Rect_ctr()
          self.Effect_upd()
          if pyxel.btnp(pyxel.KEY_R):
              self.Restart()
          if pyxel.btnp(pyxel.KEY_C):
              self.Continue()
              
  def draw(self):
      pyxel.cls(0)
      
      if self.stage_ctr == 1 or self.stage_ctr == 98:
          
          uc1 = len(str(self.Game_time))
          uc2 = str(self.Game_time)[-1*uc1]
          self.uc3 = int(uc2)
          if self.uc3 % 3 == 0:
              t_c = 10
          elif self.uc3 % 2 == 0:
              t_c = 11
          elif self.uc3 % 5 == 0:
              t_c = 7
          else:
              t_c = 8
          pyxel.text(2, 190, "TIME:" + str(self.Game_time), t_c)
          pyxel.text(45, 190, "Atk: " + str(round(self.player.atk, 1)) +
                              "  RoF:" + str(round(self.player.rof, 1)) +
                              "  Spd:" + str(round(self.player.spd, 1)) , 8)
      
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
              #if r.mode1 >= 100:
               #   pyxel.rect(r.pos_x, r.pos_y, r.pos_x2, r.pos_y2, r.color)
              #elif self.sp_flug == False or r.mode1 >= 90:
               #   pyxel.rectb(r.pos_x, r.pos_y, r.pos_x2, r.pos_y2, r.color)             
              #else:
               #   pyxel.rect(r.pos_x, r.pos_y, r.pos_x2, r.pos_y2, r.color)
          for f in self.effects:
              pyxel.rect(f.pos_x, f.pos_y, 1, 1, f.color)
        
          m_x = pyxel.mouse_x
          m_y = pyxel.mouse_y
          pyxel.trib(m_x, m_y, m_x - 1, m_y + 1, m_x + 1, m_y + 1, 7)
        
          if len(self.rects) <= 0:
              pyxel.text(2, 50, "STAGE CLEAR", 8)
              pyxel.text(2, 60, "UPDATE_TYPE = " + str(self.update_type), t_c)
        
          if self.stage_ctr == 98:
              pyxel.text(2, 50, "---GameOver---", 8)
              pyxel.text(2, 60, "R:ReStart", 8)
              pyxel.text(2, 70, "C:Continue", 8)
              #pyxel.text(2, 49, "---GameOver---", 1)
              #pyxel.text(2, 59, "R:ReStart", 1)
              #pyxel.text(2, 69, "C:Continue", 1)
              
         # if self.stage_count == 5 and  self.sp_flug == True:
          #    msg_posx = 0
           #   msg_posy = 0
            #  for r in self.rects:
             #     msg_posx = msg_posx + (r.pos_x + (r.pos_x2 / 2))
              #    msg_posy = msg_posy + (r.pos_y + (r.pos_y2 / 2))
               #   break
              #pyxel.text(msg_posx-12, msg_posy, "FIRE!!", 0)
              
      elif self.stage_ctr == 99:
          pyxel.text(2, 50, "Q_Shooter", 8)
          pyxel.text(2, 60, "S:Start", 8)
          for r in self.rects:
              pyxel.rectb(r.pos_x, r.pos_y, r.pos_x2, r.pos_y2, r.color)   
          
          
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
      self.rectsb = []
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
      px = self.player.player_x
      py = self.player.player_y
      r = len(self.rects)
      for i in range(r):
          if ((pyxel.frame_count % int(self.rects[i].attack_time) == 0) and
          (self.rects[i].mode1 < 90)):
              n = self.rects[i].shot_type
              x = self.rects[i].attack(n)
              n_len = len(x)
              for r in range(n_len):
                  self.rects.append(x[r])
          if ((self.rects[i].pos_y > 220) or (self.rects[i].pos_x > 160) or
             (self.rects[i].pos_x < -10)):
              del self.rects[i]
              break
          if self.rects[i].hp <= 0:
              del self.rects[i]
              break
          
          self.rects[i].update(px, py)
          
  def Rect_ctr_B(self, sp_a):
      px = self.player.player_x
      py = self.player.player_y
      r = len(self.rects)
      b_h = 0
      for b in range(r):
          if self.rects[b].mode1 < 90:
              b_h = b_h + 1
      for i in range(r):
          if ((pyxel.frame_count % int(self.rects[i].attack_time) == 0) and
          (self.rects[i].mode1 < 90)):
              n = self.rects[i].shot_type
              x = self.rects[i].attack(n)
              n_len = len(x)
              for r in range(n_len):
                  self.rects.append(x[r])
          if self.rects[i].hp <= 0:
              del self.rects[i]
              break
          
          m1 = self.rects[i].mode2
          
          self.rects[i].update(px, py)
          
          m2 = self.rects[i].mode2
          
          if m1 == m2 or self.rects[i].mode1 >= 90 :
              pass
          else:
              for i in range(r):
                  self.rects[i].mode2 = m2
                  
      r = len(self.rects)
      for q in range(r):
          if ((self.rects[q].pos_y > 220) or (self.rects[q].pos_x > 160) or
             (self.rects[q].pos_x < -10)):
              del self.rects[q]
              break
          
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
      if ((self.rects[r].pos_x-1 < self.p_shots[i].pos_x < 
          (self.rects[r].pos_x + self.rects[r].pos_x2 + 1))and
          (self.rects[r].pos_y-1 < self.p_shots[i].pos_y < 
          (self.rects[r].pos_y + self.rects[r].pos_y2 + 1))):
          if ((self.stage_count % 5 == 0) and (self.rects[r].mode1 < 90)):
              m = self.rects[r].mode1
          else:
              if self.rects[r].mode1 == 4:
                  m = 0
              elif self.rects[r].mode1 == 99:
                  m = 95
              elif self.rects[r].mode1 >= 100:
                  m = 95
              else:
                  m = self.rects[r].mode1 + 1
          self.rects[r].mode_cng(m)
          self.rects[r].hp = self.rects[r].hp - self.player.atk
          return 1
      else:
          return 0
      
  def Hit_chk_PR(self, r):
      if ((self.rects[r].pos_x < self.player.player_x + 1.5 < 
          (self.rects[r].pos_x + self.rects[r].pos_x2))and
          (self.rects[r].pos_y < self.player.player_y + 1.5 < 
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
      self.player_y = 180
      self.color = 12 # 0~15
      self.atk = 1
      self.spd = 3
      self.rof = 1
      self.mv_s = 1
  
  def update(self, x, y):
      if self.player_x < x:
          if self.player_x + 1 < 148:
              self.player_x = self.player_x + self.mv_s
      elif self.player_x > x:
          if self.player_x - 1 > 0:
              self.player_x = self.player_x - self.mv_s
      if self.player_y < y:
          if self.player_y + 1 < 198:
              self.player_y = self.player_y + self.mv_s
      elif self.player_y > y:
          if self.player_y - 1 > 0:
              self.player_y = self.player_y - self.mv_s
  def p_up(self, x):
      if x == 1:
          self.atk = self.atk + 0.2
      elif x == 2:
          self.spd = self.spd + 0.2
      elif x == 3:
          self.rof = self.rof + 1
      elif x == 4:
          self.mv_s = self.mv_s + 0.2

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

class Rectb:
  def __init__(self, x, y, x2, y2, c, m):
      self.pos_x = x
      self.pos_y = y
      self.pos_x2 = x2
      self.pos_y2 = y2      
      self.color = c # 0~15
      self.mode1 = m
      self.mode2 = 0
    
class Rect:
  def __init__(self, x, y, x2, y2, c, m, a, s, b):
      self.pos_x = x
      self.pos_y = y
      self.pos_x2 = x2
      self.pos_y2 = y2      
      self.color = c # 0~15
      self.mode1 = m
      self.mode2 = 0
      self.hp = 5 + b
      self.attack_time = a
      self.shot_type = s
  def mode_cng(self, m):
      self.mode1 = m
  def update(self, px, py):
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
      elif self.mode1 == 92:
          self.pos_y = self.pos_y + 1.7
      elif self.mode1 == 93:
          self.pos_y = self.pos_y + 1.2
      elif self.mode1 == 94:
          self.pos_y = self.pos_y + 0.7
      elif self.mode1 == 95:
          self.pos_y = self.pos_y + 1.5
          self.pos_x = self.pos_x + 0.5
      elif self.mode1 == 96:
          self.pos_y = self.pos_y + 1.5
          self.pos_x = self.pos_x - 0.5
      elif self.mode1 == 97:
          self.pos_y = self.pos_y + 1.5
          self.pos_x = self.pos_x + 1
      elif self.mode1 == 98:
          self.pos_y = self.pos_y + 1.5
          self.pos_x = self.pos_x - 1
      elif self.mode1 == 99:
          self.pos_y = self.pos_y + 1.5
      elif self.mode1 == 100:
          if px >= self.pos_x+1:              
              self.pos_y = self.pos_y + 1 + self.mode2 * 0.1
              self.pos_x = self.pos_x + 0.2
          else:
              self.pos_y = self.pos_y + 1 + self.mode2 * 0.1
              self.pos_x = self.pos_x - 0.2
              
  def attack(self,n):
      new_rects = []
      if n == 1:
          new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+(self.pos_y2/2),
                          6,6,self.color,99,10,0,1)
          new_rects.append(new_r)
      elif n == 2:
          for i in range(2):
              new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+
                           (self.pos_y2/2),6,6,self.color,95+i,10,0,1)
              new_rects.append(new_r)
      elif n == 3:
          for i in range(3):
              new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+
                           (self.pos_y2/2),6,6,self.color,97+i,10,0,1)
              new_rects.append(new_r)
      elif n == 4:
          for i in range(3):
              new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+
                           (self.pos_y2/2),6,6,self.color,92+i,10,0,1)
              new_rects.append(new_r)
      elif n == 5:
          new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+(self.pos_y2/2),
                          6,6,self.color,99,10,0,1)
          new_rects.append(new_r)
      elif n == 6:
          new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+(self.pos_y2/2),
                          6,6,self.color,99,10,0,1)
          new_rects.append(new_r)
      elif n == 7:
          new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+(self.pos_y2/2),
                          6,6,self.color,99,10,0,1)
          new_rects.append(new_r)
      elif n == 8:
          new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+(self.pos_y2/2),
                          6,6,self.color,99,10,0,1)
          new_rects.append(new_r)
      elif n == 9:
          new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+(self.pos_y2/2),
                          6,6,self.color,99,10,0,1)
          new_rects.append(new_r)
      elif n == 10:
          new_r = Rect(self.pos_x+(self.pos_x2/2),self.pos_y+(self.pos_y2/2),
                          6,6,self.color,99,10,0,1)
          new_rects.append(new_r)
      elif n == 11:
          for i in range(5) :
              new_r = Rect(self.pos_x+(self.pos_x2/2),
                           self.pos_y+(self.pos_y2/2),
                           6,6,self.color,92+i,10,0,1)
              new_rects.append(new_r)
      elif n == 12:
          for i in range(3) :
              new_r = Rect(self.pos_x+(self.pos_x2/2)+i*2,
                           self.pos_y+(self.pos_y2/2),
                           6,6,self.color,92+i,10,0,1)
              new_rects.append(new_r)
          for i in range(3) :
              new_r = Rect(self.pos_x+(self.pos_x2/2)-i*2-4,
                           self.pos_y+(self.pos_y2/2),
                           6,6,self.color,92+i,10,0,1)
              new_rects.append(new_r)
      else:
          pass
      return new_rects

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





