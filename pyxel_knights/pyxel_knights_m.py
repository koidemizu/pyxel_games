# -*- coding: utf-8 -*-

import pyxel
from random import randint
import csv
from module import Fontlist, Text_list, Npc_pos, Enemy_pos

class App:
 def __init__(self):
     #Font set
     self.font_list = Fontlist.text_j()
     
     #Text list set
     self.text_list = Text_list.text_get()
     
     #Player status
     self.Player = Player(8, 56)
     self.player_move = 0    
     self.atc_flug = False   
     self.atc_count = 0      
     self.p_atc_x = 0        
     self.p_atc_y = 0        
     
     #Map status
     self.stage_flug = 1     
     self.map_count_x = 1    
     self.map_count_y = 1    
     self.map_x = 0
     self.map_y = 0
     self.map_move = 0

     #NPC status
     self.npcs = []
     self.npc_move = 0
     self.npc_pos_x = Npc_pos.npc_posx()
     self.npc_pos_y = Npc_pos.npc_posy()

     #Enemy status
     self.enemys = []
     self.enemy_pos_x = Enemy_pos.enemy_posx()
     self.enemy_pos_y = Enemy_pos.enemy_posy()
     
     #System status
     self.game_start = False 
     self.game_over = False 
     self.movie_flug = False 
     self.movie_count = 0
     self.music_flug = True
     self.shop1 = Shop(1)
     self.items = [0,0,0,0,0,0,0,0,]
     self.items_t = Text_list.item_get_t()
     self.gate_flug_1 = 0
     self.save_st = 0
     self.load_st = 0
     
     pyxel.init(128,128, caption="pyxel_knights", scale=5)

     #Image read
     pyxel.load('assets/pknights.pyxres')
     
     pyxel.run(self.update, self.draw)
     
 def update(self):

     if pyxel.btnp(pyxel.KEY_S) and self.game_start == False:
       self.game_start = True
       self.movie_flug = True
       self.movie_count = 1
       self.music_flug = False
     if pyxel.btnp(pyxel.KEY_L) and self.game_start == False:
       self.game_start = True
       self.movie_flug = True
       self.movie_count = 253
       self.music_flug = False
       self.Load_data()
     if pyxel.btnp(pyxel.KEY_R) and self.game_over == True:
       self.Retry()
     if pyxel.btnp(pyxel.KEY_Q):
         pyxel.quit()
     
     if self.movie_flug == False:
         #Player controll
         self.Player_ctr()
         #NPC controll
         self.NPC_ctr()
         #Enemy controll
         self.Enemy_ctr()
         #Enemy Hit-check
         self.Hit_chk()
         #Player Damage-check
         self.Dmg_chk()
     
     #Enemy & NPC creation
     if self.map_move == 1:
        self.npcs.clear()
        self.enemys.clear()
        tgt_map_x = int(self.map_x / 16)
        tgt_map_y = int(self.map_y / 16)
        xy_key = str(tgt_map_x) + "-" + str(tgt_map_y)
        
        #Enemy creation
        enemy_x_1 = self.enemy_pos_x[xy_key]
        enemy_y_1 = self.enemy_pos_y[xy_key]
        enemy_kazu = len(enemy_x_1)
        for i in range(enemy_kazu):
            
            if enemy_x_1[i] < 101:
                new_enemy_v = 32
                new_enemy_x = enemy_x_1[i]
            elif enemy_x_1[i] < 201:
               new_enemy_v = 48
               new_enemy_x = enemy_x_1[i] - 100
            else:
               new_enemy_v = 64
               new_enemy_x = enemy_x_1[i] - 200
                
            new_enemy_v2 = randint(1,3)
            new_enemy = Enemy(new_enemy_x*8, enemy_y_1[i]*8, 
                               new_enemy_v, new_enemy_v2)
            self.enemys.append(new_enemy)
            
        #NPC creation
        npc_x_1 = self.npc_pos_x[xy_key]
        npc_y_1 = self.npc_pos_y[xy_key]
        npc_kazu = len(npc_x_1)
        for i in range(npc_kazu):
            
            if npc_x_1[i] < 101:
                new_npc_b = 16
                new_npc_x = npc_x_1[i]
            elif npc_x_1[i] < 201:
               new_npc_b = 8
               new_npc_x = npc_x_1[i] - 100
            elif npc_x_1[i] < 301:
               new_npc_b = 8
               new_npc_x = npc_x_1[i] - 200               
            else:
               new_npc_b = 16
               new_npc_x = npc_x_1[i] - 300
                
            if npc_y_1[i] < 101:
                new_npc_v = 0
                new_npc_y = npc_y_1[i]
            elif npc_y_1[i] < 201:
                new_npc_v = 16
                new_npc_y = npc_y_1[i] - 100
            elif npc_y_1[i] < 301:
                new_npc_v = 32
                new_npc_y = npc_y_1[i] - 200                
            else:
                new_npc_v = 48
                new_npc_y = npc_y_1[i] - 300
                
            new_npc = NPC(new_npc_x*8, new_npc_y*8, new_npc_b, new_npc_v)
            self.npcs.append(new_npc)
            
        self.map_move = 0
      
 def draw(self):
     pyxel.cls(0)
     
     #Debug
     #print(self.map_x)
     #print(self.map_y)
     
     #Draw tilemap
     pyxel.bltm(0,0,0,0 + self.map_x,0 + self.map_y,16,16)
 
     #Draw player
     if self.atc_flug == True:
         if self.Player.player_m == 0:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,0,16,8,8,14)
             pyxel.blt(self.Player.player_x+8,self.Player.player_y,
                           0,0,24,8,8,14)
         elif self.Player.player_m == 1:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,8,16,8,8,14)
             pyxel.blt(self.Player.player_x-8,self.Player.player_y,
                           0,8,24,8,8,14)
         elif self.Player.player_m == 2:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,16,16,8,8,14)
             pyxel.blt(self.Player.player_x,self.Player.player_y-8,
                           0,16,24,8,8,14)
         elif self.Player.player_m == 3:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,24,16,8,8,14)  
             pyxel.blt(self.Player.player_x,self.Player.player_y+8,
                           0,24,24,8,8,14)
     else:
         if self.Player.player_m == 0:
                 pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,0,0+self.Player.player_m2*8,8,8,14)
         elif self.Player.player_m == 1:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,8,0+self.Player.player_m2*8,8,8,14)
         elif self.Player.player_m == 2:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,16,0+self.Player.player_m2*8,8,8,14)
         elif self.Player.player_m == 3:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,24,0+self.Player.player_m2*8,8,8,14)
             
     #Draw NPCs
     npc_count = len(self.npcs)
     for e in range(npc_count):
         if self.npc_move < 50:
             pyxel.blt(self.npcs[e].npc_x,self.npcs[e].npc_y,
                       0,
                       0 + self.npcs[e].npc_v, 224,
                       self.npcs[e].npc_b,self.npcs[e].npc_b,14)
         else:
             pyxel.blt(self.npcs[e].npc_x,self.npcs[e].npc_y,
                       0,
                       0 + self.npcs[e].npc_v,240,
                       self.npcs[e].npc_b,self.npcs[e].npc_b,14)
          
     #Draw Enemys
     enemy_count = len(self.enemys)
     for e in range(enemy_count):
         if self.enemys[e].enemy_m == 0:
             pyxel.blt(self.enemys[e].enemy_x,self.enemys[e].enemy_y,
                       1,
                       8*self.enemys[e].enemy_v2,self.enemys[e].enemy_v,
                       8,8,14)
         else:
             pyxel.blt(self.enemys[e].enemy_x,self.enemys[e].enemy_y,
                       1,
                       8*self.enemys[e].enemy_v2,self.enemys[e].enemy_v+8,
                       8,8,14)
         if self.enemys[e].enemy_d == 1:
             pyxel.blt(self.enemys[e].enemy_x,self.enemys[e].enemy_y,
                       0,40,16,8,8,14)
             
     #Draw damage
     if self.Player.player_d == 1:
          pyxel.blt(self.Player.player_x,self.Player.player_y,0,32,16,8,8,14)      
          
     #Draw title text
     if self.game_start == False:
        #pyxel.cls(0)
        pyxel.rect(25, 30, 77, 17, 0)
        pyxel.rectb(25, 30, 77, 17, 7)
        pyxel.text(35, 35, "PYXEL KNIGHTS", 7)
        pyxel.rect(25, 57, 90, 52, 0)
        pyxel.rectb(25, 57, 90, 52, 7)
        pyxel.text(45, 65, "S = ", 7)
        self.Draw_fonts(self.text_list["0"], 60, 65)
        pyxel.text(45, 80, "L = ", 7)
        self.Draw_fonts(self.text_list["10"], 60, 80)
        pyxel.text(45, 94, "Q = ", 7)
        self.Draw_fonts(self.text_list["1"], 60, 95)
        
     else: #Draw player hp
        pyxel.rect(0, 120, 32, 18, 0)
        pyxel.text(2, 122, "HP="+ str(self.Player.player_h),7)
        
     #Draw movie
     if self.movie_flug == True:
        self.Movie_ctr(self.movie_count)
         
     #Draw gameover text
     if self.game_over == True:
        pyxel.cls(0)
        pyxel.text(20, 30, "GAME OVER!", 7)
        pyxel.text(80, 70, "R = RETRY ", 7)
        pyxel.text(80, 80, "Q = QUIT ", 7)
        

 
 def Player_ctr(self):
     
     #Get map coordinate
     x = 16*(self.map_count_x-1)
     y = 16*(self.map_count_y-1)

     #Get player coordinate        
     move_map_x = int(self.Player.player_x / 8 + x)
     move_map_y = int(self.Player.player_y / 8 + y)
     
     #Tilemap action
     #HP recovery
     if pyxel.tilemap(0).get(move_map_x, move_map_y) == 31:
         self.Player.player_h = 100    
         
     #Status view and pause
     if pyxel.btnp(pyxel.KEY_I):
                self.movie_flug = True
                self.movie_count = 2
        
     #Debug shop window
     if pyxel.btnp(pyxel.KEY_A):
                self.movie_flug = True
                self.movie_count = 226
     
     #Plyer move
     self.player_move = self.player_move + 1
     if (self.player_move > 6) and (self.atc_flug == False):
     
         if pyxel.tilemap(0).get(move_map_x, move_map_y-1) < 32:
             #Up
             if pyxel.btnp(pyxel.KEY_UP):
                 self.Player.player_y = self.Player.player_y - 8
                 self.player_move = 0
                 self.Player.player_m = 2
                 if self.Player.player_m2 == 0: #Move animation
                     self.Player.player_m2 = 1
                 else:
                     self.Player.player_m2 = 0      
                 if (self.Player.player_y - 8) < -8: #When map change
                     self.map_y = self.map_y - 16
                     self.Player.update(56, 120)
                     self.map_count_y = self.map_count_y - 1
                     self.map_move = 1
         elif pyxel.tilemap(0).get(move_map_x, move_map_y-1) >= 224:
             if pyxel.btnp(pyxel.KEY_UP):
                self.movie_flug = True
                self.movie_count = pyxel.tilemap(0).get(move_map_x,
                                                        move_map_y-1)
     
         if pyxel.tilemap(0).get(move_map_x, move_map_y+1) < 32:
             #Down
             if pyxel.btnp(pyxel.KEY_DOWN):
                 self.Player.player_y = self.Player.player_y + 8
                 self.player_move = 0
                 self.Player.player_m = 3     
                 if self.Player.player_m2 == 0: #Move animation
                     self.Player.player_m2 = 1
                 else:
                     self.Player.player_m2 = 0      
                 if (self.Player.player_y + 8) > 128: #When map change
                     self.map_y = self.map_y + 16
                     self.Player.update(56, 0)
                     self.map_count_y = self.map_count_y + 1
                     self.map_move = 1
         elif pyxel.tilemap(0).get(move_map_x, move_map_y+1) >= 224:
             if pyxel.btnp(pyxel.KEY_DOWN):
                self.movie_flug = True
                self.movie_count = pyxel.tilemap(0).get(move_map_x,
                                                        move_map_y+1)
             
         if pyxel.tilemap(0).get(move_map_x+1, move_map_y) < 32: 
             #Right
             if pyxel.btnp(pyxel.KEY_RIGHT):
                 self.Player.player_x = self.Player.player_x + 8
                 self.player_move = 0
                 self.Player.player_m = 0
                 if self.Player.player_m2 == 0: #Move animation
                     self.Player.player_m2 = 1
                 else:
                     self.Player.player_m2 = 0      
                 if (self.Player.player_x + 8) > 128: #When map change
                     self.map_x = self.map_x + 16
                     self.Player.update(0, 56)
                     self.map_count_x = self.map_count_x + 1
                     self.map_move = 1
         elif pyxel.tilemap(0).get(move_map_x+1, move_map_y) >= 224:
             if pyxel.btnp(pyxel.KEY_RIGHT):
                self.movie_flug = True
                self.movie_count = pyxel.tilemap(0).get(move_map_x+1,
                                                        move_map_y)
        
         if pyxel.tilemap(0).get(move_map_x-1, move_map_y) < 32: 
             #Left
             if pyxel.btnp(pyxel.KEY_LEFT):
                 self.Player.player_x = self.Player.player_x - 8
                 self.player_move = 0
                 if self.Player.player_m2 == 0: #Move animation
                     self.Player.player_m2 = 1
                 else:
                     self.Player.player_m2 = 0      
                 self.Player.player_m = 1
                 if (self.Player.player_x - 8) < -8: #When map change
                     self.map_x = self.map_x - 16
                     self.Player.update(120, 56)
                     self.map_count_x = self.map_count_x - 1
                     self.map_move = 1
         elif pyxel.tilemap(0).get(move_map_x-1, move_map_y) >= 224:
             if pyxel.btnp(pyxel.KEY_LEFT):
                self.movie_flug = True
                self.movie_count = pyxel.tilemap(0).get(move_map_x-1,
                                                        move_map_y)
            
     #Attack action       
     if pyxel.btnp(pyxel.KEY_SPACE):
         self.atc_flug = True
         pyxel.play(0,3,loop=False)
         
     if self.atc_flug == True:
         self.atc_count = self.atc_count + 1
         if self.atc_count > 8:
             self.atc_count = 0
             self.p_atc_x = 0
             self.p_atc_y = 0
             self.atc_flug = False
         else:
             if self.Player.player_m == 0:
                 self.p_atc_x = self.Player.player_x + 8
                 self.p_atc_y = self.Player.player_y
             elif self.Player.player_m == 1:
                 self.p_atc_x = self.Player.player_x - 8
                 self.p_atc_y = self.Player.player_y
             elif self.Player.player_m == 2:
                 self.p_atc_x = self.Player.player_x
                 self.p_atc_y = self.Player.player_y - 8
             elif self.Player.player_m == 3:
                 self.p_atc_x = self.Player.player_x
                 self.p_atc_y = self.Player.player_y + 8
       
 def Retry(self):
     #Player status
     self.Player = Player(8, 56)
     self.player_move = 0    
     self.atc_flug = False   
     self.atc_count = 0      
     self.p_atc_x = 0        
     self.p_atc_y = 0        
     
     #Map status
     self.stage_flug = 1     
     self.map_count_x = 1    
     self.map_count_y = 1    
     self.map_x = 0
     self.map_y = 0
     self.map_move = 0
     
     #Enemy status
     self.enemys = []
     
     #System status
     self.game_start = False 
     self.game_over = False 
     self.movie_flug = False 
             
 def Hit_chk(self):
     enemy_count = len(self.enemys)
     for e in range(enemy_count):
         self.enemys[e].enemy_d = 0
         enemy_pos_x = self.enemys[e].enemy_x
         enemy_pos_y = self.enemys[e].enemy_y
         if ((enemy_pos_x <= self.p_atc_x < enemy_pos_x + 8) and
             (enemy_pos_y <= self.p_atc_y < enemy_pos_y + 8)):
             self.enemys[e].enemy_d = 1
             #Music_ctr
             pyxel.play(1,0,loop=False)
             self.enemys[e].enemy_h = self.enemys[e].enemy_h -1
             #Enemy delete
             if self.enemys[e].enemy_h < 0:
                 self.Player.money += 10 * self.enemys[e].enemy_v2
                 del self.enemys[e]
                 #Music_ctr
                 pyxel.play(2,2,loop=False)
                 if len(self.enemys) == 0:
                     x = int(self.map_x / 16)
                     y = int(self.map_y / 16)
                     if x == 1 and y == 2:
                         self.MapEvents_ctr(x, y)
                 break
     
 def Dmg_chk(self):     
      self.Player.player_d = 0
      enemy_count = len(self.enemys)  
      player_pos_x = self.Player.player_x
      player_pos_y = self.Player.player_y
      for e in range(enemy_count):
          enemy_pos_x = self.enemys[e].enemy_x
          enemy_pos_y = self.enemys[e].enemy_y
          if ((enemy_pos_x <= player_pos_x < enemy_pos_x + 8) and
             (enemy_pos_y <= player_pos_y < enemy_pos_y + 8)):
              #Music_ctr
              pyxel.play(3,1,loop=False)
              self.Player.player_h = self.Player.player_h - 1
              self.Player.player_d = 1
              if self.Player.player_h <= 0:
                  self.game_over = True     
     

 def Enemy_ctr(self):        
     enemy_count = len(self.enemys)
     for e in range(enemy_count):
         self.enemys[e].enemy_m2 = self.enemys[e].enemy_m2 + 1
         if self.enemys[e].enemy_m2 > 47 - self.enemys[e].enemy_v2 * 7:
             self.enemys[e].enemy_m2 = 0
             enemy_pos_x = int(self.enemys[e].enemy_x / 8 + self.map_x)
             enemy_pos_y = int(self.enemys[e].enemy_y / 8 + self.map_y)
             enemy_pos_x2 = self.Player.player_x - self.enemys[e].enemy_x
             enemy_pos_y2 = self.Player.player_y - self.enemys[e].enemy_y
             #Check tilemap
             if (abs(enemy_pos_x2) < 35 and abs(enemy_pos_y2) < 35):
                 if abs(enemy_pos_x2) > abs(enemy_pos_y2):
                     #Move right
                     if enemy_pos_x2 > 0:
                         if (40> (pyxel.tilemap(0).get(enemy_pos_x+1, 
                                                       enemy_pos_y)) < 32):
                             self.enemys[e].enemy_x=self.enemys[e].enemy_x+8
                             self.enemys[e].enemy_m = 1
                     #Move left
                     else:
                         if (40> (pyxel.tilemap(0).get(enemy_pos_x-1, 
                                                       enemy_pos_y)) < 32):
                             self.enemys[e].enemy_x=self.enemys[e].enemy_x-8
                             self.enemys[e].enemy_m = 0           
                 else:
                     #Move down
                     if enemy_pos_y2 > 0:
                         if (40> (pyxel.tilemap(0).get(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                             self.enemys[e].enemy_y=self.enemys[e].enemy_y+8
                     #Move up
                     else:
                         if (40> (pyxel.tilemap(0).get(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                             self.enemys[e].enemy_y=self.enemys[e].enemy_y-8

 def NPC_ctr(self):        
     self.npc_move = self.npc_move + 1
     if self.npc_move > 100:
         self.npc_move = 0
         
 def MapEvents_ctr(self,x,y):
     xy_key = str(x) + "-" + str(y)
     if xy_key == "1-2":
         pyxel.tilemap(0).set(7+self.map_x, 10+self.map_y, ["006006"]) 
     elif xy_key == "0-1":
         pyxel.tilemap(0).set(7+self.map_x, 12+self.map_y, ["006006"]) 
     elif xy_key == "1-3.1":
         pyxel.tilemap(0).set(12+self.map_x, 12+self.map_y, ["0F1"]) 
         pyxel.tilemap(0).set(14+self.map_x, 7+self.map_y, ["006"]) 
         pyxel.tilemap(0).set(14+self.map_x, 8+self.map_y, ["006"]) 
     elif xy_key == "1-3.2":
         pyxel.tilemap(0).set(3+self.map_x, 1+self.map_y, ["0F2"]) 
         pyxel.tilemap(0).set(12+self.map_x, 7+self.map_y, ["006"]) 
         pyxel.tilemap(0).set(12+self.map_x, 8+self.map_y, ["006"]) 
     elif xy_key == "1-3.3":
         pyxel.tilemap(0).set(13+self.map_x, 5+self.map_y, ["0F3"]) 
         pyxel.tilemap(0).set(13+self.map_x, 7+self.map_y, ["006"]) 
         pyxel.tilemap(0).set(13+self.map_x, 8+self.map_y, ["006"]) 
     elif xy_key == "2-2":
         pyxel.tilemap(0).set(2+self.map_x, 7+self.map_y, ["006"]) 
         pyxel.tilemap(0).set(2+self.map_x, 8+self.map_y, ["006"]) 
     elif xy_key == "2-2.2":
         pyxel.tilemap(0).set(7+self.map_x, 14+self.map_y, ["00F00F"]) 
         pyxel.tilemap(0).set(7+self.map_x, 15+self.map_y, ["00F00F"]) 
     elif xy_key == "2-3":
         pyxel.tilemap(0).set(14+self.map_x, 13+self.map_y, ["021"]) 
         pyxel.tilemap(0).set(14+self.map_x, 12+self.map_y, ["021"]) 
         pyxel.tilemap(0).set(8+self.map_x, 2+self.map_y, ["0F7"]) 
     elif xy_key == "6-2":
         pyxel.tilemap(0).set(3+self.map_x, 7+self.map_y, ["011"]) 
         pyxel.tilemap(0).set(3+self.map_x, 8+self.map_y, ["011"])
     elif xy_key == "8-0.1":
         pyxel.tilemap(0).set(1+self.map_x, 0+self.map_y, ["022"]) 
     elif xy_key == "8-0.2":
         pyxel.tilemap(0).set(3+self.map_x, 3+self.map_y, ["063"]) 
     elif xy_key == "9-0.1":
         pyxel.tilemap(0).set(1+self.map_x, 14+self.map_y, ["044"]) 
     elif xy_key == "9-0.2":
         pyxel.tilemap(0).set(1+self.map_x, 0+self.map_y, ["022"]) 
     elif xy_key == "9-0.3":
         pyxel.tilemap(0).set(3+self.map_x, 3+self.map_y, ["063"]) 
     elif xy_key == "10-0":
         pyxel.tilemap(0).set(13+160, 12, ["005005"]) 
         pyxel.tilemap(0).set(13+160, 11, ["005005"]) 
         pyxel.tilemap(0).set(13+160, 10, ["005005"]) 
         pyxel.tilemap(0).set(5+self.map_x, 11+self.map_y, ["0ED"])

 def Movie_ctr(self,n):
     
     #Game start information//////////////////////////////////////////////////
     if n == 1:
         pyxel.rect(0, 65, 128, 63, 0)
         self.Draw_fonts(self.text_list["2"], 5, 70)
         self.Draw_fonts(self.text_list["3"], 5, 80)
         self.Draw_fonts(self.text_list["4"], 5, 95)
         self.Draw_fonts(self.text_list["5"], 5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     #////////////////////////////////////////////////////////////////////////
         
     #Status view/////////////////////////////////////////////////////////////
     elif n == 2:
         pyxel.rect(0, 0, 128, 128, 0)
         pyxel.rectb(0, 0, 128, 128, 7)
         pyxel.text(5, 5, "Status", 7) 
         pyxel.text(5, 15, "Items", 7) 
         pyxel.text(5, 110, "Money="+ str(self.Player.money)+" G", 7) 
         item_name = self.shop1.item_list
         l = len(item_name)
         for i in range(l):
             if i == 0:
                 pass
             else:
                 if self.items[i-1] == 1:
                     key = str(i)
                     pyxel.text(3, 15+(10*i), key+".", 7) 
                     self.Draw_fonts(item_name[key], 10, 15+(10*i))
         if pyxel.btn(pyxel.KEY_1):
             key1 = 1
             key2 = str(key1)
             if self.items[0] == 1:
                 pyxel.rect(0, 0, 120, 100, 0)
                 pyxel.rectb(0, 0, 120, 100, 7)
                 l2 = len(self.items_t[key2])
                 for i2 in range(l2):
                     self.Draw_fonts(self.items_t[key2][i2], 10, 15+(10*i2))
                 pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
         elif pyxel.btn(pyxel.KEY_2):
             if self.items[1] == 1:
                 key1 = 2
                 key2 = str(key1)
                 pyxel.rect(0, 0, 120, 100, 0)
                 pyxel.rectb(0, 0, 120, 100, 7)
                 l2 = len(self.items_t[key2])
                 for i2 in range(l2):
                     self.Draw_fonts(self.items_t[key2][i2], 10, 15+(10*i2))
                 pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
         elif pyxel.btn(pyxel.KEY_3):
             if self.items[2] == 1:
                 key1 = 3
                 key2 = str(key1)
                 pyxel.rect(0, 0, 120, 100, 0)
                 pyxel.rectb(0, 0, 120, 100, 7)
                 l2 = len(self.items_t[key2])
                 for i2 in range(l2):
                     self.Draw_fonts(self.items_t[key2][i2], 10, 15+(10*i2))
                 pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)                     
         elif pyxel.btn(pyxel.KEY_4):
             if self.items[3] == 1:
                 key1 = 4
                 key2 = str(key1)
                 pyxel.rect(0, 0, 120, 100, 0)
                 pyxel.rectb(0, 0, 120, 100, 7)
                 l2 = len(self.items_t[key2])
                 for i2 in range(l2):
                     self.Draw_fonts(self.items_t[key2][i2], 10, 15+(10*i2))
                 pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
         elif pyxel.btn(pyxel.KEY_5):
             if self.items[4] == 1:
                 key1 = 5
                 key2 = str(key1)
                 pyxel.rect(0, 0, 120, 100, 0)
                 pyxel.rectb(0, 0, 120, 100, 7)
                 l2 = len(self.items_t[key2])
                 for i2 in range(l2):
                     self.Draw_fonts(self.items_t[key2][i2], 10, 15+(10*i2))
                 pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
         elif pyxel.btn(pyxel.KEY_6):
             if self.items[5] == 1:
                 key1 = 6
                 key2 = str(key1)
                 pyxel.rect(0, 0, 120, 100, 0)
                 pyxel.rectb(0, 0, 120, 100, 7)
                 l2 = len(self.items_t[key2])
                 for i2 in range(l2):
                     self.Draw_fonts(self.items_t[key2][i2], 10, 15+(10*i2))
                 pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)                     
         elif pyxel.btn(pyxel.KEY_7):
             if self.items[6] == 1:
                 key1 = 7
                 key2 = str(key1)
                 pyxel.rect(0, 0, 120, 100, 0)
                 pyxel.rectb(0, 0, 120, 100, 7)
                 l2 = len(self.items_t[key2])
                 for i2 in range(l2):
                     self.Draw_fonts(self.items_t[key2][i2], 10, 15+(10*i2))
                 pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
         elif pyxel.btn(pyxel.KEY_8):
             if self.items[7] == 1:
                 key1 = 8
                 key2 = str(key1)
                 pyxel.rect(0, 0, 120, 100, 0)
                 pyxel.rectb(0, 0, 120, 100, 7)
                 l2 = len(self.items_t[key2])
                 for i2 in range(l2):
                     self.Draw_fonts(self.items_t[key2][i2], 10, 15+(10*i2))
                 pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
                
         pyxel.text(5, 120, "Press SPACE-KEY to return", 
                    pyxel.frame_count % 16)
    #/////////////////////////////////////////////////////////////////////////
         
    #Shop/////////////////////////////////////////////////////////////////////
     elif n == 226 or n == 227:
         
         pyxel.bltm(0,0,0,240,0,16,16)
         pyxel.blt(100 ,15 ,0 ,48 ,0 ,16 ,16 ,2)
         
         #Shop select
         s = self.shop1
         
         if pyxel.btnp(pyxel.KEY_1):
             if s.urikire[0] == 1:
                 s.text_n = 98
             else:
                 s.text_n = 1

         elif pyxel.btnp(pyxel.KEY_2):
             if s.urikire[1] == 1:
                 s.text_n = 98
             else:
                 s.text_n = 2

         elif pyxel.btnp(pyxel.KEY_3):
             if s.urikire[2] == 1:
                 s.text_n = 98
             else:
                 s.text_n = 3

         elif pyxel.btnp(pyxel.KEY_4):
             if s.urikire[3] == 1:
                 s.text_n = 98
             else:
                 s.text_n = 4
             
         for i in range(4):
             item_name = []
             if s.urikire[i] == 1:
                 item_name = s.item[4]
             else:
                 item_name = s.item[i]
             pyxel.text(10, 73 + (i * 10), str(i+1) + ".", 7)
             self.Draw_fonts(item_name, 20, 73 + (i * 10))
             pyxel.text(85, 73 + (i * 10), str(s.price[i])+" G", 7)
             
         shop_text = s.Show_text()
         text_len = len(shop_text)
         if s.text_n > 0 and s.text_n < 90:
             pyxel.text(12, 55, "( Y = Yes, N = No )", 7) 
             if pyxel.btnp(pyxel.KEY_Y):
                 p = s.text_n - 1
                 if self.Player.money - s.price[p] >= 0:
                     #Buy item
                     self.Player.money = self.Player.money - s.price[p]
                     s.urikire[p] = 1
                     s.text_n = 100
                     self.items[p] = 1
                 else:
                     s.text_n = 99
             elif pyxel.btnp(pyxel.KEY_N):
                 s.text_n = 0
         
        #Item Window
         if s.text_n > 5 or s.text_n == 0:
             pass
         else:
             pyxel.blt(100 ,45 ,0 ,48 ,16*s.text_n ,16 ,16 ,15)
            
         for t in range(text_len):
             self.Draw_fonts(shop_text[t],15, 15 + (t * 10))
         pyxel.text(10, 113, "SPACE-KEY=Exit" + " Money=" + 
                    str(self.Player.money) + " G", 7)   
     #////////////////////////////////////////////////////////////////////////
     
     #Save and Load///////////////////////////////////////////////////////////
     elif n == 252:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Save_data()
         if self.save_st == 1:
             self.Draw_fonts(self.text_list["6"],5, 105)
         else:
             self.Draw_fonts(self.text_list["7"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     
     elif n == 253:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Load_data()
         if self.load_st == 1:
             self.Draw_fonts(self.text_list["8"],5, 105)
         else:
             self.Draw_fonts(self.text_list["9"],5, 105)
         self.map_move = 1
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
    #/////////////////////////////////////////////////////////////////////////
         
     #Map event///////////////////////////////////////////////////////////////

     elif n == 228 or n == 229:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items[2] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(6, 2)
         else:
             self.Draw_fonts(self.text_list["101"], 5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
    
     elif n == 232 or n == 233 or n == 234 or n == 235:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items[3] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             x = int(self.map_x / 16)
             y = int(self.map_y / 16)
             self.MapEvents_ctr(x, y)
         else:
             self.Draw_fonts(self.text_list["101"], 5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 236:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(10, 0)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 238:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["103"],5, 105)
         self.MapEvents_ctr(1, 3.1)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 239:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["103"],5, 105)
         self.MapEvents_ctr(1, 3.2)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 240:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["103"],5, 105)
         self.MapEvents_ctr(1, 3.3)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 241:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["104"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 242:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["104"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 243:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["104"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 244:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["105"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 245:
         pyxel.rect(0, 100, 128, 63, 0)
         x = int(self.map_x / 16)
         y = int(self.map_y / 16)
         key = str(x) + "-" + str(y)
         if key == "1-0":
             self.Draw_fonts(self.text_list["106"],5, 105)
         elif key == "4-0":
             self.Draw_fonts(self.text_list["107"],5, 105)
         elif key == "7-0":
             self.Draw_fonts(self.text_list["108"],5, 105)             
         elif key == "0-1":
             self.Draw_fonts(self.text_list["109"],5, 105)
         elif key == "2-3":
             self.Draw_fonts(self.text_list["110"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 246:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(2, 3)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 248:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items[4] == 1:
             self.Draw_fonts(self.text_list["112"],5, 105)
             self.MapEvents_ctr(2, 2.2)
         else:
            self.Draw_fonts(self.text_list["111"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 249:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items[4] == 0:
             self.Draw_fonts(self.text_list["113"],5, 105)
         else:
             self.Draw_fonts(self.text_list["114"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 250:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items[6] == 0:
             self.Draw_fonts(self.text_list["115"],5, 105)
         else:
             self.Draw_fonts(self.text_list["114"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 251:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items[7] == 0:
             self.Draw_fonts(self.text_list["116"],5, 105)
         else:
             self.Draw_fonts(self.text_list["114"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     #////////////////////////////////////////////////////////////////////////
        
     #NPC text////////////////////////////////////////////////////////////////
     elif n == 224:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["200"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 225:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["201"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     #////////////////////////////////////////////////////////////////////////
     
     #Other///////////////////////////////////////////////////////////////////
     else:
         self.movie_flug = False
     #////////////////////////////////////////////////////////////0////////////
     
    #Return game
     if pyxel.btnp(pyxel.KEY_SPACE):
         self.movie_flug = False
     #Save Load status reset
         self.save_st = 0
         self.load_st = 0
     #Shop text reset.
         if n == 226 or n == 227:
             s.text_n = 0
     #Get item reset.
         if n == 249:
             if self.items[4] == 0:
                 self.items[4] = 1
                 self.MapEvents_ctr(9, 0.1)
         elif n == 250:
             if self.items[6] == 0:
                 self.items[6] = 1
                 self.MapEvents_ctr(9, 0.2)
         elif n == 251:
             if self.items[7] == 0:
                 self.items[7] = 1
                 self.MapEvents_ctr(9, 0.3)

 def Draw_fonts(self,txt,x,y):  
     txt_count = len(txt)      
     for i in range(txt_count):
         #Key check
         font_xy = self.font_list[txt[i]]
        
         fontx = font_xy[0]
         fonty = font_xy[1]
         pyxel.blt(x + 8 * i,y,1,fontx,fonty,8,8,14)
        
 def Save_data(self):
     #Save data
     try:
         with open('DATA/data.csv', 'w', newline="") as f:
                 writer = csv.writer(f)
                 data = []
                 for i in self.items:
                     data.append(i)
                 data.append(self.gate_flug_1)
                 data.append(self.map_count_x)
                 data.append(self.map_count_y)
                 data.append(self.map_x)
                 data.append(self.map_y)
                 data.append(self.Player.money)
                 data.append(self.Player.player_x)
                 data.append(self.Player.player_y)
                 
                 writer.writerow(data)
                 self.save_st = 1
     except:
         self.save_st = 2
                 
 def Load_data(self):
     #Load data
     data = []
     try:
         with open('DATA/data.csv') as f:
             reader = csv.reader(f)
             for row in reader:
                 data.append(row)
         i = len(self.items)
         for i2 in range(i):
           self.items[i2] = int(data[0][i2])
         self.gate_flug1 = int(data[0][i])
         self.map_count_x = int(data[0][i+1])
         self.map_count_y = int(data[0][i+2])
         self.map_x = int(data[0][i+3])
         self.map_y = int(data[0][i+4])
         self.Player.money = int(data[0][i+5])
         self.Player.player_x = int(data[0][i+6])
         self.Player.player_y = int(data[0][i+7])
         self.load_st = 1
         for i3 in range(4):
             self.shop1.urikire[i3] = self.items[i3]
     except:
        self.load_st = 2

           
class Player:
 def __init__(self, x, y):
     self.player_x = x
     self.player_y = y
     self.player_h = 100
     self.player_d = 0
     self.player_m = 0
     self.player_m2 = 0
     self.money = 1000
 def update(self, x, y):
     self.player_x = x
     self.player_y = y

class NPC:
  def __init__(self, x, y, b, v):
      self.npc_x = x
      self.npc_y = y
      self.npc_b = b
      self.npc_v = v
      self.npc_m = 0
  def update(self, x, y):
      self.npc_x = x
      self.npc_y = y
      
class Enemy:
  def __init__(self, x, y, v, v2):
      self.enemy_x = x
      self.enemy_y = y
      self.enemy_h = 10 + v2*5
      self.enemy_d = 0
      self.enemy_m = 0
      self.enemy_m2 = 0
      self.enemy_v = v
      self.enemy_v2 = v2
  def update(self, x, y):
      self.enemy_x = x
      self.enemy_y = y
      
class Shop:
  def __init__(self, n):
      #Text list set
      self.text_list_s = Text_list.text_get_s()
      self.item_list = Text_list.item_get()
      self.shop_v = n
      self.item = [self.item_list["1"],
                 self.item_list["2"],
                 self.item_list["3"],
                 self.item_list["4"],
                 self.item_list["0"]]
      self.price = [100,200,300,400]
      self.text_n = 0
      self.urikire = [0, 0, 0, 0]
  def Show_text(self):
      t = self.text_n
      if t == 0:
          return [self.text_list_s["51"],
                 self.text_list_s["52"],
                 self.text_list_s["53"],
                 self.text_list_s["54"],]
      elif t == 1:
          return [self.text_list_s["55"],
                  self.text_list_s["56"],
                  self.text_list_s["57"]]
      elif t == 2:
          return [self.text_list_s["58"],
                  self.text_list_s["59"],
                  self.text_list_s["60"]]
      elif t == 3:
          return [self.text_list_s["61"],
                  self.text_list_s["62"]]
      elif t == 4:
          return [self.text_list_s["63"],
                  self.text_list_s["64"],
                  self.text_list_s["65"]]
      elif t == 98:
          return [self.text_list_s["66"]]
      elif t == 99:
          return [self.text_list_s["67"],self.text_list_s["68"]]
      elif t == 100:
          return [self.text_list_s["69"]]

App()