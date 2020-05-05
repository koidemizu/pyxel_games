# -*- coding: utf-8 -*-
"""
Program_Name:Pyxel_Invaders

@author: T.Koshiba
"""

from random import randint, randrange
import pyxel

WINDOW_H = 120
WINDOW_W = 160
PIC_H = 16
PIC_W = 16

class APP:
  def __init__(self):
      self.game_start = False
      self.game_over = False
      self.game_end = False
      self.boss = Boss()
      self.boss_enemys = []
      self.boss_flug = False
      self.boss_scr = 0
      self.boss_count = 1
      self.boss_color = 0
      self.score = 0
      self.shots = []
      self.enemys = []
      self.enemys_shots = []
      self.boss_hp = 50
      self.bombs = []
      self.p_ship = Ship()
      
      pyxel.init(WINDOW_W, WINDOW_H, caption="Pyxel Invaders")
      # Road image file
      pyxel.load("assets/inve.pyxres")
      
      pyxel.mouse(False)
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      # System controll
      if pyxel.btnp(pyxel.KEY_Q):
          pyxel.quit()
      if pyxel.btnp(pyxel.KEY_R):
          self.game_start = False
      if pyxel.btnp(pyxel.KEY_S):
          self.game_start = True
          self.retry()
          
      # Player update
      if self.game_over == False:
          self.ship_move()

                  
      if self.game_end == False:
          self.hit_chk()
          self.ene_create()
          self.ene_move()
          self.boss_move()
          eshots_len = len(self.enemys_shots)
          for e in range(eshots_len):
            self.enemys_shots[e].update()
        
      self.bomb_del()
      # Bomb dalete logic
      if len(self.bombs) > 3:
          del self.bombs[0]  
                  
              
  def draw(self):
      if self.boss_count == 7:
          pyxel.cls(7)
      else:
          pyxel.cls(0)
             
      #Game over logic
      if self.game_over:
          if self.boss_count == 7:
              pyxel.cls(7)
              pyxel.text(100, 60, "GAME OVER!! ", 0)
              pyxel.text(100, 80, "R = RETRY ", 0)
              pyxel.text(100, 90, "Q = QUIT ", 0)
          else:
              pyxel.cls(0)
              pyxel.text(100, 60, "GAME OVER!! ", pyxel.frame_count % 16)
              pyxel.text(100, 80, "R = RETRY ", pyxel.frame_count % 16)
              pyxel.text(100, 90, "Q = QUIT ", pyxel.frame_count % 16)
      # Score count
      if self.boss_count == 7:
          pyxel.text(1, 2, "SCORE:" + str(self.score), 0)
          if self.boss_flug == True:
              pyxel.text(120, 2, "BOSS:" + str(self.boss.boss_h), 0)
          else:
              pyxel.text(120, 2, "LEVEL:" + str(self.boss_count), 0)
      else:
          pyxel.text(1, 2, "SCORE:" + str(self.score), 7)
          if self.boss_flug == True:
              pyxel.text(120, 2, "BOSS:" + str(self.boss.boss_h), 7)
          else:
              pyxel.text(120, 2, "LEVEL:" + str(self.boss_count), 7)
      
      # Player draw
      if self.game_over == False:
          if self.boss_count == 7:
              pyxel.blt(self.p_ship.ship_x, self.p_ship.ship_y, 0, 144, 0, 
                    -PIC_W, PIC_H, 6)
          else:
              pyxel.blt(self.p_ship.ship_x, self.p_ship.ship_y, 0, 96, 0, 
                    -PIC_W, PIC_H, 6)
      else:
          pyxel.blt(self.p_ship.ship_x, self.p_ship.ship_y, 0, 128, 
                              0,-PIC_W, PIC_H, 6)      
      
      #Blits draw
      if self.boss_count == 7:
          for i in self.shots:
              if i.exists == True:
                  pyxel.rect(i.pos_x+7, i.pos_y-3,
                             2, 2, 0)
      else:
          for i in self.shots:
              if i.exists == True:
                  pyxel.rect(i.pos_x+7, i.pos_y-3,
                             2, 2, 12)
          
       # Enemy draw
      for i in self.enemys:
          if self.boss_flug == False:
              if self.boss_count == 7:
                  if i.ene_f == 0:
                      pyxel.blt(i.ene_x, i.ene_y, 0, 0, i.ene_c * 32, 
                                    -PIC_W, PIC_H, 6)
                  else:
                      pyxel.blt(i.ene_x, i.ene_y, 0, 16, i.ene_c * 32, 
                                    -PIC_W, PIC_H, 6)
              else:
                  if i.ene_v == 1:
                      if i.ene_f == 0:
                          pyxel.blt(i.ene_x, i.ene_y, 0, 0, i.ene_c * 32, 
                                    -PIC_W, PIC_H, 6)
                      else:
                          pyxel.blt(i.ene_x, i.ene_y, 0, 16, i.ene_c * 32, 
                                    -PIC_W, PIC_H, 6)
                  elif i.ene_v == 2:
                      if i.ene_f == 0:
                          pyxel.blt(i.ene_x, i.ene_y, 0, 32, i.ene_c * 32, 
                                    -PIC_W, PIC_H, 6)
                      else:
                          pyxel.blt(i.ene_x, i.ene_y, 0, 48, i.ene_c * 32, 
                                    -PIC_W, PIC_H, 6)
                  else:
                      if i.ene_f == 0:
                          pyxel.blt(i.ene_x, i.ene_y, 0, 64, i.ene_c * 32, 
                                    -PIC_W, PIC_H, 6)
                      else:
                          pyxel.blt(i.ene_x, i.ene_y, 0, 80, i.ene_c * 32, 
                                    -PIC_W, PIC_H, 6)
                  
       # Boss draw          
      if self.boss_flug == True:
          if self.boss_count == 6:
              pyxel.blt(self.boss.boss_x, self.boss.boss_y,
                        0, 64, 16, 16, 16, 6)
              pyxel.text(35, 60, "DESTROY THEIR PLANET!! ", 7)
          elif self.boss_count == 7:
              pyxel.blt(self.boss.boss_x, self.boss.boss_y,
                        0, 16, 128, 16, 16, 6)
          else:
              pyxel.blt(self.boss.boss_x, self.boss.boss_y,
                        0, 0, 16 * self.boss.boss_c, 48, 16, 6)
          
      # Bomb draw
      for i in self.bombs:
          if i.bomb_t < 15:
              pyxel.blt(i.bomb_x, i.bomb_y, 0, 128, 0, 
                        -PIC_W, PIC_H, 6)      
      # Enemy_shot draw
      for i in self.enemys_shots:
          pyxel.rect(i.e_shot_x, i.e_shot_y, 2, 2, i.e_shot_c)
          
      # Game Start draw
      if self.game_start == False:
           pyxel.cls(0)
           pyxel.text(20, 30, "PYXEL INVADERS", 10)
           pyxel.text(100, 60, "READY? ", pyxel.frame_count % 16)
           pyxel.text(100, 70, "S = START ", pyxel.frame_count % 16)
           pyxel.text(100, 80, "Q = QUIT ", pyxel.frame_count % 16)
    
      # Game end draw
      if self.game_end == True:
           pyxel.cls(0)
           pyxel.text(20, 30, "PYXEL INVADERS", 10)
           pyxel.text(100, 60, "GAME CLEAR!", pyxel.frame_count % 16)
        
  def retry(self): #Retry 
      self.game_over = False
      self.game_end = False
      self.boss_flug = False
      self.boss_count = 1
      self.boss_color = 0
      self.score = 0
      self.shots = []
      self.enemys = []
      self.enemys_shots = []
      self.boss_enemys = []
      self.boss_hp = 50
      self.bombs = []
      self.p_ship = Ship()
      
  def ship_move(self): # Player controll
      #if pyxel.btn(pyxel.KEY_RIGHT):
       #   if self.p_ship.ship_x < 145:
        #      self.p_ship.update(self.p_ship.ship_x + 2, self.p_ship.ship_y)
      #if pyxel.btn(pyxel.KEY_LEFT):
       #   if self.p_ship.ship_x > 0:
        #      self.p_ship.update(self.p_ship.ship_x - 2, self.p_ship.ship_y)
      #if pyxel.btn(pyxel.KEY_UP):
       #   if self.p_ship.ship_y > 1:
        #      self.p_ship.update(self.p_ship.ship_x, self.p_ship.ship_y-2)
      #if pyxel.btn(pyxel.KEY_DOWN):
       #   if self.p_ship.ship_y < 105:
        #      self.p_ship.update(self.p_ship.ship_x, self.p_ship.ship_y+2)
      # Attack if push Key-Space
      #if pyxel.btnp(pyxel.KEY_SPACE, 5, 15):
       #   if len(self.shots) < 11:
        #      new_shot = Shot()
         #     new_shot.update(self.p_ship.ship_x, self.p_ship.ship_y, 8)
          #    self.shots.append(new_shot)
      
      #Player move by mouse.        
      move_x = pyxel.mouse_x
      move_y = pyxel.mouse_y
      if move_x > 145:
          move_x = 145
      if move_x < 0:
          move_x = 0          
      if move_y > 105:
          move_y = 105
      if move_y < 0:
          move_y = 0          
      self.p_ship.update(move_x, move_y)
      #Auto attack
      if len(self.shots) < 11 and pyxel.frame_count % 8 == 0:
          new_shot = Shot()
          new_shot.update(self.p_ship.ship_x, self.p_ship.ship_y, 8)
          self.shots.append(new_shot)
 
  def ene_create(self): # Enemy creation
      # Nomal attack
      if self.boss_flug == False:
          if pyxel.frame_count % 40 == 0:
              if self.boss_count == 1:
                  new_enemy = Enemy(1)
                  new_enemy.ene_x = randrange(30, 65, 16)
                  self.enemys.append(new_enemy)
                  new_enemy = Enemy2(1)
                  new_enemy.ene_x = randrange(70, 125, 16)
                  self.enemys.append(new_enemy)
              elif self.boss_count == 2:
                  enemy_v = randint(1, 2)
                  new_enemy = Enemy(enemy_v)
                  new_enemy.ene_x = randrange(30, 65, 16)
                  self.enemys.append(new_enemy)
                  enemy_v = randint(1, 2)
                  new_enemy = Enemy2(enemy_v)
                  new_enemy.ene_x = randrange(70, 125, 16)
                  self.enemys.append(new_enemy)
              else:
                  enemy_v = randint(1, 3)
                  new_enemy = Enemy(enemy_v)
                  new_enemy.ene_x = randrange(30, 65, 16)
                  self.enemys.append(new_enemy)
                  enemy_v = randint(2, 3)
                  new_enemy = Enemy2(enemy_v)
                  new_enemy.ene_x = randrange(70, 125, 16)
                  self.enemys.append(new_enemy)                    
                 
  def ene_move(self): # Enemy controll      
      enemy_count = len(self.enemys)
      for e in range (enemy_count):
          enemy_vec1 = randint(0, 7)
          enemy_vec2 = enemy_vec1 % 2
          if self.enemys[e].ene_y < 115:
              ene_chk =self.e_move_chk(e, self.enemys[e].ene_x, 
                                           self.p_ship.ship_y)
              # Enemy y
              if self.enemys[e].ene_v == 1:   # No.1 Enemy move 
                  self.enemys[e].ene_y = self.enemys[e].ene_y + 1.0
                  
                  # Enemy shot
                  f = randint(1, 3)
                  if ((pyxel.frame_count % 100 == 0) and (f == 1)): 
                      self.e_shot_ctr(self.enemys[e].ene_x + 8,
                                      self.enemys[e].ene_y + 4,
                                      self.enemys[e].ene_v,
                                      self.enemys[e].ene_c,
                                      0, 1.8)                       
                  
              elif self.enemys[e].ene_v == 2:  # No.2 Enemy move
                  self.enemys[e].ene_y = self.enemys[e].ene_y + 1.2
                  
                  # Enemy shot
                  f = randint(1, 2)
                  if ((pyxel.frame_count % 90 == 0) and (f == 1)): 
                      self.e_shot_ctr(self.enemys[e].ene_x + 8,
                                      self.enemys[e].ene_y + 4,
                                      self.enemys[e].ene_v,
                                      self.enemys[e].ene_c,
                                      -0.5, 1.8)                 
                      self.e_shot_ctr(self.enemys[e].ene_x + 8,
                                      self.enemys[e].ene_y + 4,
                                      self.enemys[e].ene_v,
                                      self.enemys[e].ene_c,
                                      0, 1.8)                 
                      self.e_shot_ctr(self.enemys[e].ene_x + 8,
                                      self.enemys[e].ene_y + 4,
                                      self.enemys[e].ene_v,
                                      self.enemys[e].ene_c,
                                      0.5, 1.8)                 
                  if ene_chk == 0:
                      if self.enemys[e].ene_x > self.p_ship.ship_x:
                          self.enemys[e].ene_x=self.enemys[e].ene_x - 0.25
                      else:
                          self.enemys[e].ene_x=self.enemys[e].ene_x + 0.25
                          
              elif self.enemys[e].ene_v == 3:   # No.3 enemy move
                  # Enemy shot
                  f = randint(1, 1)
                  if ((pyxel.frame_count % 80 == 0) and (f == 1)): 
                      self.e_shot_ctr(self.enemys[e].ene_x + 8,
                                      self.enemys[e].ene_y + 4,
                                      self.enemys[e].ene_v,
                                      self.enemys[e].ene_c,
                                      -1, 1.8)                        
                      self.e_shot_ctr(self.enemys[e].ene_x + 8,
                                      self.enemys[e].ene_y + 4,
                                      self.enemys[e].ene_v,
                                      self.enemys[e].ene_c,
                                      1, 1.8)                 
                      self.e_shot_ctr(self.enemys[e].ene_x + 8,
                                      self.enemys[e].ene_y + 4,
                                      self.enemys[e].ene_v,
                                      self.enemys[e].ene_c,
                                      -1, -1.8)                        
                      self.e_shot_ctr(self.enemys[e].ene_x + 8,
                                      self.enemys[e].ene_y + 4,
                                      self.enemys[e].ene_v,
                                      self.enemys[e].ene_c,
                                      1, -1.8)                 
                  if self.enemys[e].ene_f == 0:
                      self.enemys[e].ene_y = self.enemys[e].ene_y + 1.4
                      if self.enemys[e].ene_y > self.p_ship.ship_y - 2:
                          self.enemys[e].ene_f = 1
                  else:
                      self.enemys[e].ene_y = self.enemys[e].ene_y - 1.2
                      if self.enemys[e].ene_x < self.p_ship.ship_x:
                          if ene_chk == 0:
                              self.enemys[e].ene_x=self.enemys[e].ene_x + 0.25
                      else:
                          if ene_chk == 0:
                              self.enemys[e].ene_x=self.enemys[e].ene_x - 0.25
                      if self.enemys[e].ene_y < self.p_ship.ship_y - 40:
                          if self.boss_count != 7 and self.boss_flug == False:
                              self.enemys[e].ene_f = 0
                          elif self.enemys[e].ene_y < 0:
                               del self.enemys[e]
                               break
              elif self.enemys[e].ene_v == 9:
                  if self.boss_count == 5:
                      self.enemys[e].ene_y = (self.enemys[e].ene_y + 2.0)
                  else:
                      self.enemys[e].ene_y = (self.enemys[e].ene_y + 1.0)
              
              if pyxel.frame_count % 50 == 0 and ene_chk == 0:
                  if self.boss_flug == False or self.boss_count == 7:
                      # Enemy x
                      if self.enemys[e].ene_v == 1:
                          if enemy_vec2 > 0:
                              self.enemys[e].ene_x = self.enemys[e].ene_x + 4
                              if self.enemys[e].ene_f == 0:
                                  self.enemys[e].ene_f = 1
                              else:
                                  self.enemys[e].ene_f = 0
                          else:
                              self.enemys[e].ene_x = self.enemys[e].ene_x - 4
                              if self.enemys[e].ene_f == 0:
                                  self.enemys[e].ene_f = 1
                              else:
                                  self.enemys[e].ene_f = 0
                      elif self.enemys[e].ene_v == 2:
                          if self.enemys[e].ene_x < self.p_ship.ship_x:
                              if self.enemys[e].ene_f == 0:
                                  self.enemys[e].ene_f = 1
                              else:
                                  self.enemys[e].ene_f = 0
                          else:
                              if self.enemys[e].ene_f == 0:
                                  self.enemys[e].ene_f = 1
                              else:
                                  self.enemys[e].ene_f = 0
                      else:
                          continue
                  else:
                      continue
          else:
              del self.enemys[e]
              break
          
  def e_shot_ctr(self, x, y, v, c, mx, my):
      # Enemy shot
      new_e_shot = Ene_shot(x, y, v, c, mx, my)
      self.enemys_shots.append(new_e_shot)
      
  def b_shot_ctr(self, x, y, v, c, mx, my):
      # Boss shot
      new_b_shot = [Ene_shot(x, y, v, c, mx, my),
                    Ene_shot(x+24, y, v, c, mx, my),
                    Ene_shot(x+48, y, v, c, mx, my)]
      for b in new_b_shot:
          self.enemys_shots.append(b)
      
  def e_move_chk(self, me, x, y):
      enemy_hit = len(self.enemys)
      for e in range(enemy_hit):
          if e == me:
             break
          if ((self.enemys[e].ene_x - 8 <= x + 16) and
              (self.enemys[e].ene_x + 8 <= x -16 )and
              (self.enemys[e].ene_y - 8 <= y + 8)):
                 result = 1
                 return result
          else:
              result = 0
              return result
          
  def hit_chk(self): # Hit check
      # Enemy_shots-Player
      enemy_shots = len(self.enemys_shots)
      for e in range (enemy_shots):
          if ((self.enemys_shots[e].e_shot_y > 160) or 
              (self.enemys_shots[e].e_shot_y < 0)):
              del self.enemys_shots[e]
              break
          if ((self.p_ship.ship_x + 2 <= self.enemys_shots[e].e_shot_x 
             <= self.p_ship.ship_x + 14) and (self.p_ship.ship_y + 4 <= 
             self.enemys_shots[e].e_shot_y <= self.p_ship.ship_y + 13)):
            self.game_over = True
      
      shot_count = len(self.shots)
      # Blits delete
      for j in range (shot_count):
          if self.shots[j].pos_y > 10:
              self.shots[j].pos_y = self.shots[j].pos_y - 3
          else:
              del self.shots[j]
              break
      # Enemy-Blits
      shot_hit = len(self.shots)
      if self.boss_flug == False:
         for h in range (shot_hit):
              enemy_hit = len(self.enemys)
              for e in range (enemy_hit):
                  if ((self.enemys[e].ene_x - 8 <= self.shots[h].pos_x 
                       <= self.enemys[e].ene_x + 8)and
                       (self.enemys[e].ene_y - 7 <= self.shots[h].pos_y <= 
                        self.enemys[e].ene_y + 15)and
                       (self.shots[h].exists == True)):
                      # If hit enemy make bomb instance
                      new_bomb = Bomb(self.enemys[e].ene_x, 
                                      self.enemys[e].ene_y)
                      self.bombs.append(new_bomb)
                      del self.enemys[e]
                      self.shots[h].shot_del()
                      if self.boss_flug == False:
                          self.score = self.score + 100
                          self.boss_scr = self.boss_scr + 1
                          break # If hit enemy break
                  else:
                      continue
                  break
      else:
          for h in range (shot_hit):
              if self.boss_count == 6 or self.boss_count == 7:
                  hitbox_x = 15
                  hitbox_y = 15
              else:
                  hitbox_x = 40
                  hitbox_y = 10
              if ((self.boss.boss_x - 8 <= self.shots[h].pos_x 
                       <= self.boss.boss_x + hitbox_x) and
                      (self.boss.boss_y <= self.shots[h].pos_y 
                       <= self.boss.boss_y + hitbox_y)):
                          self.shots[h].shot_del()
                          self.boss.boss_h = self.boss.boss_h - 1
                          new_bomb = Bomb(self.shots[h].pos_x, 
                                          self.shots[h].pos_y)
                          self.bombs.append(new_bomb)    
              else:
                  continue
              break
      # Enemy-Player
      enemy_atk = len(self.enemys)
      for e in range (enemy_atk):
          if self.boss_flug == False:
              # Hit check on 4 points
              #1
              if (((self.enemys[e].ene_x + 3 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 3 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y <= self.p_ship.ship_y + 14))or
              #2
                   (self.enemys[e].ene_x + 12 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 12 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y <= self.p_ship.ship_y + 14)or
              #3
                   (self.enemys[e].ene_x + 3 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 3 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y + 6 >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y + 6 <= self.p_ship.ship_y + 14)or
              #4
                   ((self.enemys[e].ene_x + 12 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 12 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y + 6 >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y + 6 <= self.p_ship.ship_y + 14))):
                    self.game_over = True
          elif self.boss_count != 7:
              # Hit check on 2 points
              #1
              if (((self.enemys[e].ene_x + 8 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 8 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y <= self.p_ship.ship_y + 14))or
              #2
                   ((self.enemys[e].ene_x + 8 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 8 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y + 4 >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y + 4 <= self.p_ship.ship_y + 14))):
                    self.game_over = True
          else:
              # Hit check on 4 points
              #1
              if (((self.enemys[e].ene_x + 3 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 3 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y <= self.p_ship.ship_y + 14))or
              #2
                   (self.enemys[e].ene_x + 12 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 12 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y <= self.p_ship.ship_y + 14)or
              #3
                   (self.enemys[e].ene_x + 3 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 3 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y + 6 >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y + 6 <= self.p_ship.ship_y + 14)or
              #4
                   ((self.enemys[e].ene_x + 12 >= self.p_ship.ship_x + 2) and
                   (self.enemys[e].ene_x + 12 <= self.p_ship.ship_x + 14) and
                   (self.enemys[e].ene_y + 6 >= self.p_ship.ship_y) and
                   (self.enemys[e].ene_y + 6 <= self.p_ship.ship_y + 14))):
                    self.game_over = True
                    
  def boss_move(self):
      # Boss flug    
      if self.boss_flug == False: 
          if self.score != 0:     
              #boss_chk = 15 * self.boss_count
              boss_chk = 15 * self.boss_count
              if boss_chk > 100:
                  boss_chk = 100
              if self.boss_scr % boss_chk == 0:
                  if self.game_end == False: 
                      if self.boss_count == 5:
                          self.boss_flug = True
                          self.enemys.clear()
                          self.boss_hp = 50 * self.boss_count
                          self.boss_color = 6
                          self.boss.update(50, 10, self.boss_hp, 
                                           self.boss_color)
                      elif self.boss_count == 6:
                          self.boss_flug = True
                          self.enemys.clear()
                          self.boss_hp = 500
                          #self.boss_hp = 50 * self.boss_count
                          self.boss_color = randrange(1, 6, 2)
                          self.boss.update(70, 0, self.boss_hp, 
                                           self.boss_color)           
                      elif self.boss_count == 7:
                          self.boss_flug = True
                          self.enemys.clear()
                          self.boss_hp = 50 * self.boss_count
                          #self.boss_hp = 50 * self.boss_count
                          self.boss_color = 8
                          self.boss.update(70, -5, self.boss_hp, 
                                           self.boss_color)     
                      else:
                          self.boss_flug = True
                          self.enemys.clear()
                          self.boss_hp = 50 * self.boss_count
                          #self.boss_hp = 50 * self.boss_count
                          self.boss_color = randrange(1, 6, 2)
                          self.boss.update(50, 10, self.boss_hp, 
                                           self.boss_color)
                      
      # Boss move and hit check
      if self.boss_flug == True:
          #Boss shot
          if pyxel.frame_count % 40 == 0:          
                  self.b_shot_ctr(self.boss.boss_x,
                                       self.boss.boss_y + 4,
                                       99,
                                       self.boss.boss_c,
                                       0, 1.8)          
          if self.boss_count == 5:
               if self.boss.boss_m == 0:
                 if self.boss.boss_x > self.p_ship.ship_x - 8:
                     self.boss.move(self.boss.boss_x - 1, self.boss.boss_y)
                 elif self.boss.boss_x == self.p_ship.ship_x - 8:
                     self.boss.boss_m = 1
                 else:
                     self.boss.move(self.boss.boss_x + 1, self.boss.boss_y)
               elif self.boss.boss_m == 1:
                 if self.boss.boss_y > self.p_ship.ship_y - 40:
                     self.boss.boss_m = 2
                 else:
                     self.boss.move(self.boss.boss_x, self.boss.boss_y + 1)
               else:
                   self.boss.move(self.boss.boss_x, self.boss.boss_y - 1)
                   if self.boss.boss_y < 10:
                     self.boss.boss_m = 0
          elif self.boss_count == 6 or self.boss_count == 7:
               if self.boss.boss_y < 150:
                   self.boss.move(self.boss.boss_x, self.boss.boss_y + 0.1)
                   if self.boss.boss_y > 100:
                       self.game_over == True
          else:    
               if self.boss.boss_m == 0:
                 if self.boss.boss_x > 0:
                     self.boss.move(self.boss.boss_x - 1, self.boss.boss_y)
                 else:
                     self.boss.boss_m = 1
               else:
                 if self.boss.boss_x < 115:
                     self.boss.move(self.boss.boss_x + 1, self.boss.boss_y)
                 else:
                    self.boss.boss_m = 0
                    
 #         shot_hit = len(self.shots)        
  #        for h in range (shot_hit):
   #           if self.boss_count == 6 or self.boss_count == 7:
    #              hitbox_x = 15
     #             hitbox_y = 15
      #        else:
       #           hitbox_x = 40
        #          hitbox_y = 10
         #     if ((self.boss.boss_x - 8 <= self.shots[h].pos_x 
          #         <= self.boss.boss_x + hitbox_x) and
           #       (self.boss.boss_y <= self.shots[h].pos_y 
            #       <= self.boss.boss_y + hitbox_y)):
             #     self.shots[h].shot_del()
              #    self.boss.boss_h = self.boss.boss_h - 1
               #   new_bomb = Bomb(self.shots[h].pos_x, self.shots[h].pos_y)
                #  self.bombs.append(new_bomb)    
                    
      # Boss delete
      if self.boss.boss_h <= 0:
          if self.boss_flug == True:
              self.score = self.score + 5000
              pyxel.cls(0)
              self.boss_flug = False
              self.enemys.clear()
              #self.game_end = True
              self.boss_count = self.boss_count + 1
              self.boss_scr = 1            
              if self.boss_count == 7:
                  self.game_end = True
  
  def bomb_del(self):
      for b in self.bombs:
          b.bomb_t = b.bomb_t + 1
      
class Ship:   
  def __init__(self):
      self.ship_x = 70
      self.ship_y = 105
  
  def update(self, x, y):
      self.ship_x = x
      self.ship_y = y
      
class Shot:
  def __init__(self):
      self.pos_x = 0
      self.pos_y = 0
      self.color = 8 # 0~15
      self.exists = True
  def update(self, x, y, color):
      self.pos_x = x
      self.pos_y = y
      self.color = color
  def shot_del(self):
      self.exists = False
      
class Enemy:
  def __init__(self, v):
      self.ene_x = 0
      self.ene_y = 0
      self.ene_f = 0
      self.ene_c = randint(0, 2)
      self.ene_v = v
      self.ene_h = 4
  def update(self, x, y):
      self.ene_x = x  
      self.ene_y = y
  def ene_del(self):
      self.exists = False
      
class Enemy2:
  def __init__(self, v):
      self.ene_x = randint(20, 125)
      self.ene_y = 10
      self.ene_f = 0
      self.ene_c = randint(0, 2)
      self.ene_v = v
  def update(self, x, y):
      self.ene_x = x
      self.ene_y = y
      
class Ene_shot:
  def __init__(self, x, y, v, c, mx, my):
      self.e_shot_x = x
      self.e_shot_y = y
      self.e_shot_mx = mx
      self.e_shot_my = my
      if v == 1:
          if c == 0:
              self.e_shot_c = 11
          elif c == 1:
              self.e_shot_c = 9
          else:
              self.e_shot_c = 8           
      elif v == 2:
          if c == 0:
              self.e_shot_c = 11
          elif c == 1:
              self.e_shot_c = 9
          else:
              self.e_shot_c = 8         
      elif v == 3:
          if c == 0:
              self.e_shot_c = 2
          elif c == 1:
              self.e_shot_c = 7
          else:
              self.e_shot_c = 13     
      else:
          if c == 1:
              self.e_shot_c = 8
          elif c == 3:
              self.e_shot_c = 11
          else:
              self.e_shot_c = 7
  def update(self):
      self.e_shot_x = self.e_shot_x + self.e_shot_mx
      self.e_shot_y = self.e_shot_y + self.e_shot_my
        
      
class Bomb:
  def __init__(self, x, y):
      self.bomb_x = x
      self.bomb_y = y
      self.bomb_t = 0       
      
class Boss:
  def __init__(self):
      self.boss_x = 0
      self.boss_y = 0  
      self.boss_h = 0        
      self.boss_c = 0
      self.boss_m = 0
  def update(self, x, y, h, c):
      self.boss_x = x
      self.boss_y = y  
      self.boss_h = h        
      self.boss_c = c
  def move(self, x, y):
      self.boss_x = x
      self.boss_y = y  
                  
APP()




