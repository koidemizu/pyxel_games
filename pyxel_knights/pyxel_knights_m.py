# -*- coding: utf-8 -*-
#pyxel_knights_m.py

import pyxel
from random import randint
import csv
from module import Fontlist, Text_list, Npc_pos, Enemy_pos, Text_list_en

class App:
 def __init__(self):
     #Language set
     self.lng = "none"
     
     #Font set
     self.font_list = Fontlist.text_j()
     
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
     
     self.items = [0,0,0,0,0,0,0,0,]
     self.items2 = [0,0,0,0,0,0,0,0,]
     self.items3 = [0,0,0,0,0,0,0,0,]
     self.items4 = [0,0,0,0,0,0,0,0,]
     self.items5 = [0,0,0,0,0,0,0,0,]
     self.items6 = [0,0,0,0,0,0,0,0,]
     
     #self.items = [1,1,1,1,1,1,1,1,]
     #self.items2 = [1,1,1,1,1,1,1,1,]
     #self.items3 = [1,1,1,1,1,1,1,1,]
     
     self.gate_flug_1 = 0
     self.save_st = 0
     self.load_st = 0
     self.Event_save = False
     self.End_event_x = []
     self.End_event_y = []
     self.txt_key = 0
     self.text_key_flug = False
     self.enemy_crt_flug = False
     self.event_cnt = False
     self.boss1_flug = False
     self.boss2_flug = False
     self.boss3_flug = False
     self.item_page = 1
     self.page_move = 0
     
     pyxel.init(128,128, caption="Regicide", scale=5)

     #Image read
     pyxel.load('assets/pknights.pyxres')
     
     pyxel.run(self.update, self.draw)
     
 def update(self):
     
     if self.lng == "none":
         self.Movie_ctr(-1)
     else:
         if pyxel.btnp(pyxel.KEY_S) and self.game_start == False:
             self.game_start = True
             self.movie_flug = True
             self.movie_count = 1001
             self.music_flug = False
         if pyxel.btnp(pyxel.KEY_L) and self.game_start == False:
             self.game_start = True
             self.movie_flug = True
             self.movie_count = 253
             self.music_flug = False
             self.Load_data()
             
     if pyxel.btnp(pyxel.KEY_R) and self.game_over == True:
        self.Retry()
       
     if pyxel.btnp(pyxel.KEY_Q) and self.game_start == False:
         pyxel.quit()
         
     if pyxel.btnp(pyxel.KEY_Q) and self.game_over == True:
         #Return to title#########################################
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

         #Enemy status
         self.enemys = []
     
         #System status
         self.game_start = False 
         self.game_over = False 
         self.movie_flug = False 
         self.movie_count = 0
         self.music_flug = True
     
         self.items = [0,0,0,0,0,0,0,0,]
         self.items2 = [0,0,0,0,0,0,0,0,]
         self.items3 = [0,0,0,0,0,0,0,0,]
         self.items4 = [0,0,0,0,0,0,0,0,]
         self.items5 = [0,0,0,0,0,0,0,0,]
         self.items6 = [0,0,0,0,0,0,0,0,]
     
         self.gate_flug_1 = 0
         self.save_st = 0
         self.load_st = 0
         self.Event_save = False
         self.End_event_x = []
         self.End_event_y = []
         self.txt_key = 0
         self.text_key_flug = False
         self.enemy_crt_flug = False
         self.event_cnt = False
         self.boss1_flug = False
         self.boss2_flug = False
         self.boss3_flug = False
         self.item_page = 1
         self.page_move = 0
         ##############################################################
     
     if self.movie_flug == False:
         #Player controll
         if self.game_start == True:
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
        pyxel.clip()
        self.npcs.clear()
        self.enemys.clear()
        tgt_map_x = int(self.map_x / 16)
        tgt_map_y = int(self.map_y / 16)
        xy_key = str(tgt_map_x) + "-" + str(tgt_map_y)
        
        if xy_key in self.enemy_pos_x:
            #Enemy creation
            enemy_x_1 = self.enemy_pos_x[xy_key]
            enemy_y_1 = self.enemy_pos_y[xy_key]
            enemy_kazu = len(enemy_x_1)
            if (xy_key == "8-0" or
                xy_key == "9-0" or
                xy_key == "10-0" ):
                if self.items[5] == 0:
                    enemy_kazu = 0
            for i in range(enemy_kazu):
             
                if enemy_x_1[i] < 100:
                    new_enemy_v = 32
                    new_enemy_x = enemy_x_1[i]
                elif enemy_x_1[i] < 200:
                   new_enemy_v = 48
                   new_enemy_x = enemy_x_1[i] - 100
                elif enemy_x_1[i] < 300:
                   new_enemy_v = 64
                   new_enemy_x = enemy_x_1[i] - 200
                elif enemy_x_1[i] < 400:
                   new_enemy_v = 80
                   new_enemy_x = enemy_x_1[i] - 300
                elif enemy_x_1[i] < 500:
                   new_enemy_v = 96
                   new_enemy_x = enemy_x_1[i] - 400
                
                if (xy_key == "8-0" or
                   xy_key == "9-0" or
                   xy_key == "10-0" ):
                    new_enemy_v2 = randint(1,2)
                elif (xy_key == "0-8" or
                      xy_key == "0-7"):
                    new_enemy_v2 = randint(2,4)
                elif (xy_key == "1-8" or 
                     xy_key == "1-5"):
                    new_enemy_v2 = 4
                else:
                    new_enemy_v2 = randint(1,3)
                new_enemy = Enemy(new_enemy_x*8, enemy_y_1[i]*8, 
                                   new_enemy_v, new_enemy_v2)
                self.enemys.append(new_enemy)
            
        if xy_key in self.npc_pos_x:
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
                elif npc_x_1[i] < 401:
                   new_npc_b = 16
                   new_npc_x = npc_x_1[i] - 300
                elif npc_x_1[i] < 501:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 400
                elif npc_x_1[i] < 601:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 500
                elif npc_x_1[i] < 701:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 600
                elif npc_x_1[i] < 801:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 700
                elif npc_x_1[i] < 901:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 800
                elif npc_x_1[i] < 1001:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 900
                elif npc_x_1[i] < 1101:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 1000
                elif npc_x_1[i] < 1201:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 1100
                
                if npc_y_1[i] < 101:
                    new_npc_v = 0
                    new_npc_y = npc_y_1[i]
                elif npc_y_1[i] < 201:
                    new_npc_v = 16
                    new_npc_y = npc_y_1[i] - 100
                elif npc_y_1[i] < 301:
                    new_npc_v = 32
                    new_npc_y = npc_y_1[i] - 200                
                elif npc_y_1[i] < 401:
                    new_npc_v = 48
                    new_npc_y = npc_y_1[i] - 300
                elif npc_y_1[i] < 501:
                    new_npc_v = 64
                    new_npc_y = npc_y_1[i] - 400
                elif npc_y_1[i] < 601:
                    new_npc_v = 80
                    new_npc_y = npc_y_1[i] - 500
                elif npc_y_1[i] < 701:
                    new_npc_v = 96
                    new_npc_y = npc_y_1[i] - 600
                elif npc_y_1[i] < 801:
                    new_npc_v = 112
                    new_npc_y = npc_y_1[i] - 700
                elif npc_y_1[i] < 901:
                    new_npc_v = 128
                    new_npc_y = npc_y_1[i] - 800
                elif npc_y_1[i] < 1001:
                    new_npc_v = 144
                    new_npc_y = npc_y_1[i] - 900
                elif npc_y_1[i] < 1101:
                    new_npc_v = 160
                    new_npc_y = npc_y_1[i] - 1000
                elif npc_y_1[i] < 1201:
                    new_npc_v = 176
                    new_npc_y = npc_y_1[i] - 1100
                
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
     pn = self.Player.weapon - 1
     pn2 = pn * 40
     if self.atc_flug == True:
         if self.Player.player_m == 0:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,0,16+pn2,8,8,14)
             pyxel.blt(self.p_atc_x,self.p_atc_y,
                           0,0,24+pn2,8,8,14)
         elif self.Player.player_m == 1:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,8,16+pn2,8,8,14)
             pyxel.blt(self.p_atc_x,self.p_atc_y,
                           0,8,24+pn2,8,8,14)
         elif self.Player.player_m == 2:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,16,16+pn2,8,8,14)
             pyxel.blt(self.p_atc_x,self.p_atc_y,
                           0,16,24+pn2,8,8,14)
         elif self.Player.player_m == 3:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,24,16+pn2,8,8,14)  
             pyxel.blt(self.p_atc_x,self.p_atc_y,
                           0,24,24+pn2,8,8,14)
     else:
         if self.Player.player_m == 0:
                 pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,0,0+self.Player.player_m2*8+pn2,8,8,14)
         elif self.Player.player_m == 1:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,8,0+self.Player.player_m2*8+pn2,8,8,14)
         elif self.Player.player_m == 2:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,16,0+self.Player.player_m2*8+pn2,8,8,14)
         elif self.Player.player_m == 3:
             pyxel.blt(self.Player.player_x,self.Player.player_y,
                           0,24,0+self.Player.player_m2*8+pn2,8,8,14)
             
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
          
     #Map Gimic
     spx = self.map_count_x - 1
     spy = self.map_count_y - 1
     spkey = str(spx) + "-" + str(spy)
     if spkey == "0-5":
         pyxel.blt(7*8,4*8,1,192,32,16,16)
     elif spkey == "2-5" or spkey == "10-1":
         if self.items[5] == 1:
             wi = 48
         else:
             wi = 34
         pyxel.clip(self.Player.player_x-16,self.Player.player_y-16, wi, wi)
          
     #Draw title text
     if self.game_start == False: 
        if self.lng == "ja" or self.lng == "en":
            #pyxel.cls(0)
            pyxel.rect(25, 30, 70, 17, 0)
            pyxel.rectb(25, 30, 70, 17, 7)
            pyxel.text(40, 35, "Regicide", 7)
            pyxel.rect(25, 57, 90, 52, 0)
            pyxel.rectb(25, 57, 90, 52, 7)
            pyxel.text(45, 65, "S = ", 7)
            self.Draw_fonts(self.text_list["0"], 60, 65)
            pyxel.text(45, 80, "L = ", 7)
            self.Draw_fonts(self.text_list["10"], 60, 80)
            pyxel.text(45, 94, "Q = ", 7)
            self.Draw_fonts(self.text_list["1"], 60, 95)
            pyxel.blt(73,34,0,32,0,8,8,14)
        
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
        pyxel.text(20, 70, "R = RETRY(Load Data) ", 7)
        pyxel.text(20, 80, "Q = QUIT(Return to title) ", 7)
        
     #Select lunguage
     if self.lng == "none":
         pyxel.cls(0)
         pyxel.text(20, 30, "Select Languge.", 7)
         pyxel.text(40, 70, "J = Japanese ", 7)
         pyxel.text(40, 80, "E = English ", 7)

 
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
     #Map Event
     if pyxel.tilemap(0).get(move_map_x, move_map_y) == 29:
         self.movie_flug = True
         self.movie_count = 254
         self.Movie_ctr(self.movie_count)
     if pyxel.tilemap(0).get(move_map_x, move_map_y) == 30:
         self.movie_flug = True
         self.movie_count = 255
         self.Movie_ctr(self.movie_count)
         
     #Status view and pause
     if pyxel.btnp(pyxel.KEY_I):
         self.movie_flug = True
         self.movie_count = 2
        
     #Debug shop window
     if pyxel.btnp(pyxel.KEY_A):
         self.MapEvents_ctr(10, 0)
         self.movie_count = 2555
      #          self.movie_flug = True
       #         self.movie_count = 226
     
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
                print(self.movie_count) #DebugF
     
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
         #pyxel.play(0,3,loop=False)
         
     if self.atc_flug == True:
         if self.Player.weapon == 2:
             ap = 16
             at = 0
         elif self.Player.weapon == 1:
             ap = 8
             at = 0
         elif self.Player.weapon == 3:
             ap = 8
             at = 10    
        
         self.atc_count = self.atc_count + 1
         if self.atc_count > 8 + at:
             self.atc_count = 0
             self.p_atc_x = 0
             self.p_atc_y = 0
             self.atc_flug = False
         else:
             if self.Player.player_m == 0:
                 self.p_atc_x = self.Player.player_x + ap
                 self.p_atc_y = self.Player.player_y
             elif self.Player.player_m == 1:
                 self.p_atc_x = self.Player.player_x - ap
                 self.p_atc_y = self.Player.player_y
             elif self.Player.player_m == 2:
                 self.p_atc_x = self.Player.player_x
                 self.p_atc_y = self.Player.player_y - ap
             elif self.Player.player_m == 3:
                 self.p_atc_x = self.Player.player_x
                 self.p_atc_y = self.Player.player_y + ap
       
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
     self.game_over = False 
     self.game_start = True
     self.movie_flug = True
     self.movie_count = 253
     self.music_flug = False
     self.Load_data()
             
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
             #pyxel.play(1,0,loop=False)
             if self.Player.weapon == 3:
               pa = 2
             else:
               pa = 1
             self.enemys[e].enemy_h = self.enemys[e].enemy_h - pa
             #Enemy delete
         if self.enemys[e].enemy_h < 0:
             if self.enemys[e].enemy_v2 == 5:
                 m = 0
             else:
                 m = 10 * self.enemys[e].enemy_v2
             self.Player.money += m
             del self.enemys[e]
             #Music_ctr
             #pyxel.play(2,2,loop=False)
             if len(self.enemys) == 0:
                 x = int(self.map_x / 16)
                 y = int(self.map_y / 16)
                 if ((x == 1 and y == 2) or ((x == 10 and y == 0))):
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
              #pyxel.play(3,1,loop=False)
              self.Player.player_h = self.Player.player_h - 1
              self.Player.player_d = 1
              if self.Player.player_h <= 0:
                  self.game_over = True     
     

 def Enemy_ctr(self):        
     #new_enemy_w = []
     enemy_count = len(self.enemys)
     for e in range(enemy_count):
         self.enemys[e].enemy_m2 = self.enemys[e].enemy_m2 + 1
         if self.enemys[e].enemy_v2 == 4:
             vm2 = randint(1, 180) 
             vm = 0
         else:
             vm2 = 0
             vm = self.enemys[e].enemy_v2 * 7
         if self.enemys[e].enemy_m2 > 47 + vm2 - vm:
             self.enemys[e].enemy_m2 = 0
             enemy_pos_x = int(self.enemys[e].enemy_x / 8 + self.map_x)
             enemy_pos_y = int(self.enemys[e].enemy_y / 8 + self.map_y)
             enemy_pos_x2 = self.Player.player_x - self.enemys[e].enemy_x
             enemy_pos_y2 = self.Player.player_y - self.enemys[e].enemy_y
             #Check enemy v2
             if self.enemys[e].enemy_v2 < 4:  
                 #Check tilemap
                 if (abs(enemy_pos_x2) < 35 and abs(enemy_pos_y2) < 35):
                     if abs(enemy_pos_x2) > abs(enemy_pos_y2):
                         #Move right
                         if enemy_pos_x2 > 0:
                             if (40> (pyxel.tilemap(0).get(enemy_pos_x+1, 
                                                         enemy_pos_y)) < 32):
                                 self.enemys[e].enemy_x = \
                                     self.enemys[e].enemy_x + 8
                                 self.enemys[e].enemy_m = 1
                         #Move left
                         else:
                             if (40> (pyxel.tilemap(0).get(enemy_pos_x-1, 
                                                         enemy_pos_y)) < 32):
                                 self.enemys[e].enemy_x = \
                                     self.enemys[e].enemy_x-8
                                 self.enemys[e].enemy_m = 0           
                     else:
                         #Move down
                         if enemy_pos_y2 > 0:
                             if (40> (pyxel.tilemap(0).get(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                                 self.enemys[e].enemy_y = \
                                     self.enemys[e].enemy_y+8
                         #Move up
                         else:
                             if (40> (pyxel.tilemap(0).get(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                                 self.enemys[e].enemy_y = \
                                     self.enemys[e].enemy_y-8
             elif self.enemys[e].enemy_v2 == 4:
                 if enemy_pos_y2 > 0:
                     self.enemys[e].enemy_m = 0
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y+8, 96, 5)
                     new_enemy.enemy_m = 1
                     new_enemy.enemy_h = 6
                     #new_enemy_w.append(new_enemy)
                     self.enemys.append(new_enemy)
                 else:
                     self.enemys[e].enemy_m = 1
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y-8, 96, 5)
                     new_enemy.enemy_m = 0
                     new_enemy.enemy_h = 6
                     #new_enemy_w.append(new_enemy)
                     self.enemys.append(new_enemy)
             
             elif self.enemys[e].enemy_v2 == 5:
                 if self.enemys[e].enemy_m == 1:
                     self.enemys[e].enemy_y = self.enemys[e].enemy_y + 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
                     
                 else:
                     self.enemys[e].enemy_y = self.enemys[e].enemy_y - 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
     #for e in new_enemy_w:
      #   self.enemys.append(e)


 def NPC_ctr(self):        
     self.npc_move = self.npc_move + 1
     if self.npc_move > 100:
         self.npc_move = 0
         
 def MapEvents_ctr(self,x,y):
     xy_key = str(x) + "-" + str(y)
     #Event save
     if self.Event_save == False and self.load_st == 0:
         self.End_event_x.append(x)
         self.End_event_y.append(y)
         self.Event_save = True
     if xy_key == "1-2":
         pyxel.tilemap(0).set(7+16, 10+32, ["006006"]) 
     elif xy_key == "0-41":
         pyxel.tilemap(0).set(7+0, 2+64, ["014014"]) 
         pyxel.tilemap(0).set(7+0, 3+64, ["14C14D"]) 
     elif xy_key == "0-4":
         pyxel.tilemap(0).set(6+0, 8+64, ["006006006"]) 
         pyxel.tilemap(0).set(5+0, 9+64, ["006006006006006"]) 
         pyxel.tilemap(0).set(5+0, 10+64, ["006006006006006"]) 
     elif xy_key == "0-1":
         pyxel.tilemap(0).set(7+0, 12+16, ["006006"]) 
     elif xy_key == "0-10":
         pyxel.tilemap(0).set(13+160, 9, ["005005"]) 
         pyxel.tilemap(0).set(13+160, 12, ["027027"]) 
         pyxel.tilemap(0).set(1+160, 7, ["027"]) 
         pyxel.tilemap(0).set(1+160, 8, ["027"]) 
     elif xy_key == "0-101":
         pyxel.tilemap(0).set(11+160, 8, ["005"]) 
         pyxel.tilemap(0).set(11+160, 7, ["005"]) 
     elif xy_key == "0-3":
         pyxel.tilemap(0).set(13+0, 10+48, ["044"]) 
     elif xy_key == "1-31":
         pyxel.tilemap(0).set(12+16, 12+48, ["0F1"]) 
         pyxel.tilemap(0).set(14+16, 7+48, ["006"]) 
         pyxel.tilemap(0).set(14+16, 8+48, ["006"]) 
     elif xy_key == "1-32":
         pyxel.tilemap(0).set(3+16, 1+48, ["0F2"]) 
         pyxel.tilemap(0).set(12+16, 7+48, ["006"]) 
         pyxel.tilemap(0).set(12+16, 8+48, ["006"]) 
     elif xy_key == "1-33":
         pyxel.tilemap(0).set(13+16, 5+48, ["0F3"]) 
         pyxel.tilemap(0).set(13+16, 7+48, ["006"]) 
         pyxel.tilemap(0).set(13+16, 8+48, ["006"]) 
     elif xy_key == "2-2":
         pyxel.tilemap(0).set(2+32, 7+32, ["006"]) 
         pyxel.tilemap(0).set(2+32, 8+32, ["006"]) 
     elif xy_key == "2-22":
         pyxel.tilemap(0).set(7+32, 14+32, ["00F00F"]) 
         pyxel.tilemap(0).set(7+32, 15+32, ["00F00F"]) 
     elif xy_key == "2-3":
         pyxel.tilemap(0).set(14+32, 13+48, ["021"]) 
         pyxel.tilemap(0).set(14+32, 12+48, ["021"]) 
         pyxel.tilemap(0).set(8+32, 2+48, ["0F7"]) 
     elif xy_key == "6-2":
         pyxel.tilemap(0).set(3+96, 7+32, ["011"]) 
         pyxel.tilemap(0).set(3+96, 8+32, ["011"])
     elif xy_key == "7-7":
         pyxel.tilemap(0).set(7+112, 7+112, ["005005"]) 
     elif xy_key == "8-11":
         pyxel.tilemap(0).set(1+128, 0+0, ["022"]) 
     elif xy_key == "8-12":
         pyxel.tilemap(0).set(3+128, 3+0, ["063"]) 
     elif xy_key == "9-11":
         pyxel.tilemap(0).set(1+144, 14+0, ["044"]) 
     elif xy_key == "9-12":
         pyxel.tilemap(0).set(1+144, 0+0, ["022"]) 
     elif xy_key == "9-13":
         pyxel.tilemap(0).set(3+144, 3+0, ["063"]) 
     elif xy_key == "10-0":
         pyxel.tilemap(0).set(13+160, 12, ["005005"]) 
         pyxel.tilemap(0).set(1+160, 7, ["005"]) 
         pyxel.tilemap(0).set(1+160, 8, ["005"]) 
         if self.items5[0] == 0:
             self.items5[0] = 1
         if self.items5[4] == 0:
             self.items5[4] = 1
         if self.items5[5] == 0:
             self.items5[5] = 1
         if self.items5[6] == 0:
             self.items5[6] = 1
         if self.items5[7] == 0:
             self.items5[7] = 1
         self.boss1_flug = True

     elif xy_key == "10-101":
         pyxel.tilemap(0).set(13+160, 12, ["005005"]) 
         pyxel.tilemap(0).set(13+160, 11, ["005005"]) 
         pyxel.tilemap(0).set(13+160, 10, ["005005"]) 
         pyxel.tilemap(0).set(12+160, 7, ["005005005"]) 
         pyxel.tilemap(0).set(12+160, 8, ["005005005"]) 
         pyxel.tilemap(0).set(8+160, 7, ["005005005"]) 
         pyxel.tilemap(0).set(8+160, 8, ["005005005"]) 
         pyxel.tilemap(0).set(9+128, 9+32, ["021021"]) 
         pyxel.tilemap(0).set(9+128, 10+32, ["021021"]) 
         pyxel.tilemap(0).set(9+128, 11+32, ["021021"]) 
         pyxel.tilemap(0).set(9+128, 12+32, ["021021"]) 
         pyxel.tilemap(0).set(5+96, 11+32, ["0ED"])
     elif xy_key == "1-8":
         pyxel.tilemap(0).set(1+16, 7+128, ["000"]) 
         pyxel.tilemap(0).set(1+16, 8+128, ["000"]) 
         pyxel.tilemap(0).set(1+16, 9+128, ["000"]) 
     elif xy_key == "1-81":
         pyxel.tilemap(0).set(6+16, 1+128, ["000"]) 
     elif xy_key == "2-7":
         pyxel.tilemap(0).set(7+32, 6+112, ["000000"]) 
     elif xy_key == "2-6":
         pyxel.tilemap(0).set(7+0, 14+128, ["000000"])     
         pyxel.tilemap(0).set(14+32, 1+96, ["139"])     
     elif xy_key == "3-7":
         pyxel.tilemap(0).set(7+48, 13+112, ["003003"])     
         pyxel.tilemap(0).set(1+48, 11+112, ["13B"])     
     elif xy_key == "1-6":
         pyxel.tilemap(0).set(9+16, 1+96, ["000"]) 
     elif xy_key == "1-61":
         pyxel.tilemap(0).set(14+16, 1+96, ["044"]) 
     elif xy_key == "1-62":
         pyxel.tilemap(0).set(7+16, 5+96, ["000000"]) 
         pyxel.tilemap(0).set(7+16, 6+96, ["000000"]) 
     elif xy_key == "1-7":
         pyxel.tilemap(0).set(5+16, 6+112, ["000000"]) 
         pyxel.tilemap(0).set(5+16, 7+112, ["000000"]) 
         pyxel.tilemap(0).set(5+16, 8+112, ["000000"]) 
     else:
         pass

 def Movie_ctr(self,n):
     
     if n == -1:
     #Text list set
         if pyxel.btn(pyxel.KEY_J):
             if self.lng == "none":
                 self.text_list = Text_list.text_get()
                 self.items_t = Text_list.item_get_t()
                 self.items_t2 = Text_list.item_get_t2()
                 self.items_t3 = Text_list.item_get_t3()
                 self.items_t4 = Text_list.item_get_t4()
                 self.items_t5 = Text_list.item_get_t5()
                 self.items_t6 = Text_list.item_get_t6()
                 
                 self.lng = "ja"
                 self.shop1 = Shop(1, "ja")
                 self.shop2 = Shop(2, "ja")
                 self.shop3 = Shop(3, "ja")
                 self.shop4 = Shop(4, "ja")
                 self.shop5 = Shop(5, "ja")
                 self.shop6 = Shop(6, "ja")
         elif pyxel.btn(pyxel.KEY_E):
             if self.lng == "none":
                 self.text_list = Text_list_en.text_get()
                 self.items_t = Text_list_en.item_get_t()
                 self.items_t2 = Text_list_en.item_get_t2()
                 self.items_t3 = Text_list_en.item_get_t3()
                 self.items_t4 = Text_list_en.item_get_t4()
                 self.items_t5 = Text_list_en.item_get_t5()
                 self.items_t6 = Text_list_en.item_get_t6()                 
                 
                 self.lng = "en"
                 self.shop1 = Shop(1, "en")
                 self.shop2 = Shop(2, "en")
                 self.shop2 = Shop(2, "en")
                 self.shop3 = Shop(3, "en")
                 self.shop4 = Shop(4, "en")
                 self.shop5 = Shop(5, "en")
                 self.shop6 = Shop(6, "en")
     
     #Game start information//////////////////////////////////////////////////
     if n == 1001:
         pyxel.rect(0, 65, 128, 63, 0)
         pyxel.rect(0, 0, 128, 65, 0)
         pyxel.circ(62, 30, 28, 7)
         self.Draw_fonts(self.text_list["2"], 5, 70)
         self.Draw_fonts(self.text_list["3"], 5, 80)
         self.Draw_fonts(self.text_list["4"], 5, 90)
         self.Draw_fonts(self.text_list["5"], 5, 100)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1002:
         pyxel.rect(0, 65, 128, 63, 0)
         pyxel.rect(0, 0, 128, 65, 0)
         pyxel.circ(62, 30, 28, 7)
         pyxel.circ(76, 35, 24, 0)
         self.Draw_fonts(self.text_list["11"], 5, 70)
         self.Draw_fonts(self.text_list["12"], 5, 80)
         self.Draw_fonts(self.text_list["13"], 5, 90)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1003:
         pyxel.rect(0, 65, 128, 63, 0)
         pyxel.rect(0, 0, 128, 65, 0)
         pyxel.circ(62, 30, 28, 7)
         pyxel.circ(66, 32, 24, 0)
         self.Draw_fonts(self.text_list["14"], 5, 70)
         self.Draw_fonts(self.text_list["15"], 5, 80)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1004:
         pyxel.rect(0, 65, 128, 63, 0)
         pyxel.rect(0, 0, 128, 65, 0)
         pyxel.circ(62, 30, 28, 7)
         pyxel.circ(62, 30, 25, 0)
         self.Draw_fonts(self.text_list["16"], 5, 70)
         self.Draw_fonts(self.text_list["17"], 5, 80)
         self.Draw_fonts(self.text_list["18"], 5, 90)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1005:
         pyxel.rect(0, 65, 128, 63, 0)
         pyxel.rect(0, 0, 128, 65, 0)
         pyxel.circ(62, 30, 28, 7)
         pyxel.circ(62, 30, 25, 0)
         self.Draw_fonts(self.text_list["19"], 5, 70)
         self.Draw_fonts(self.text_list["20"], 5, 80)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1006:
         pyxel.rect(0, 65, 128, 63, 0)
         #pyxel.rect(0, 0, 128, 65, 0)
         pyxel.circ(62, 30, 28, 7)
         pyxel.circ(62, 30, 25, 0)
         self.Draw_fonts(self.text_list["21"], 5, 70)
         self.Draw_fonts(self.text_list["22"], 5, 80)
         self.Draw_fonts(self.text_list["23"], 5, 90)
         self.Draw_fonts(self.text_list["24"], 5, 100)
         self.event_cnt = False
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     #////////////////////////////////////////////////////////////////////////
         
     #Status view/////////////////////////////////////////////////////////////
     elif n == 2:
         self.page_move = self.page_move + 1
         if self.page_move > 5:
             if pyxel.btn(pyxel.KEY_N):
                 if self.item_page < 6:
                     self.item_page = self.item_page + 1
                     self.page_move = 0
             elif pyxel.btn(pyxel.KEY_B):
                 if self.item_page > 1:
                     self.item_page = self.item_page - 1
                     self.page_move = 0
         pyxel.rect(0, 0, 128, 128, 0)
         pyxel.rectb(0, 0, 128, 128, 7)
         pyxel.text(4, 5, "Items", 7)
         pyxel.text(30, 5, "N", 8)
         pyxel.text(33, 5, ":Next page", 7)
         pyxel.text(77, 5, "B", 12)
         pyxel.text(80, 5, ":Back page", 7)
         pyxel.text(85, 110, "Page:" + str(self.item_page), 9)
         pyxel.text(5, 15, "Keep holding down item number", 7)
         pyxel.text(5, 110, "Money="+ str(self.Player.money)+" G", 7) 
         item_name = self.shop1.item_list
         item_name2 = self.shop2.item_list
         item_name3 = self.shop3.item_list
         item_name4 = self.shop4.item_list
         item_name5 = self.shop5.item_list
         item_name6 = self.shop6.item_list
         l = len(item_name)
         if self.item_page == 1:
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
                         self.Draw_fonts(self.items_t[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_2):
                 if self.items[1] == 1:
                     key1 = 2
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_3):
                 if self.items[2] == 1:
                     key1 = 3
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_4):
                 if self.items[3] == 1:
                     key1 = 4
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t[key2][i2], 10, 
                                         15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_5):
                 if self.items[4] == 1:
                     key1 = 5
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_6):
                 if self.items[5] == 1:
                     key1 = 6
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_7):
                 if self.items[6] == 1:
                     key1 = 7
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_8):
                 if self.items[7] == 1:
                     key1 = 8
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,48 ,16*key1 ,16 ,16 ,15)
         elif self.item_page == 2:
             for i in range(l):
                 if i == 0:
                     pass
                 else:
                     if self.items2[i-1] == 1:
                         key = str(i)
                         pyxel.text(3, 15+(10*i), key+".", 7) 
                         self.Draw_fonts(item_name2[key], 10, 15+(10*i))
             if pyxel.btn(pyxel.KEY_1):
                 key1 = 1
                 key2 = str(key1)
                 if self.items2[0] == 1:
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t2[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t2[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,64 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_2):
                 if self.items2[1] == 1:
                     key1 = 2
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t2[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t2[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,64 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_3):
                 if self.items2[2] == 1:
                     key1 = 3
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t2[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t2[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,64 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_4):
                 if self.items2[3] == 1:
                     key1 = 4
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t2[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t2[key2][i2], 10, 
                                         15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,64 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_5):
                 if self.items2[4] == 1:
                     key1 = 5
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t2[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t2[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,64 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_6):
                 if self.items2[5] == 1:
                     key1 = 6
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t2[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t2[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,64 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_7):
                 if self.items2[6] == 1:
                     key1 = 7
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t2[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t2[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,64 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_8):
                 if self.items2[7] == 1:
                     key1 = 8
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t2[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t2[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,64 ,16*key1 ,16 ,16 ,15)              
         elif self.item_page == 3:
             for i in range(l):
                 if i == 0:
                     pass
                 else:
                     if self.items3[i-1] == 1:
                         key = str(i)
                         pyxel.text(3, 15+(10*i), key+".", 7) 
                         self.Draw_fonts(item_name3[key], 10, 15+(10*i))
             if pyxel.btn(pyxel.KEY_1):
                 key1 = 1
                 key2 = str(key1)
                 if self.items3[0] == 1:
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t3[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t3[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,80 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_2):
                 if self.items3[1] == 1:
                     key1 = 2
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t3[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t3[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,80 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_3):
                 if self.items3[2] == 1:
                     key1 = 3
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t3[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t3[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,80 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_4):
                 if self.items3[3] == 1:
                     key1 = 4
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t3[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t3[key2][i2], 10, 
                                         15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,80 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_5):
                 if self.items3[4] == 1:
                     key1 = 5
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t3[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t3[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,80 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_6):
                 if self.items3[5] == 1:
                     key1 = 6
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t3[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t3[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,80 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_7):
                 if self.items3[6] == 1:
                     key1 = 7
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t3[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t3[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,80 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_8):
                 if self.items3[7] == 1:
                     key1 = 8
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t3[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t3[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,80 ,16*key1 ,16 ,16 ,15)              
         elif self.item_page == 4:
             for i in range(l):
                 if i == 0:
                     pass
                 else:
                     if self.items4[i-1] == 1:
                         key = str(i)
                         pyxel.text(3, 15+(10*i), key+".", 7) 
                         self.Draw_fonts(item_name4[key], 10, 15+(10*i))
             if pyxel.btn(pyxel.KEY_1):
                 key1 = 1
                 key2 = str(key1)
                 if self.items4[0] == 1:
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t4[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t4[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,96 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_2):
                 if self.items4[1] == 1:
                     key1 = 2
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t4[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t4[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,96 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_3):
                 if self.items4[2] == 1:
                     key1 = 3
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t4[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t4[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,96 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_4):
                 if self.items4[3] == 1:
                     key1 = 4
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t4[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t4[key2][i2], 10, 
                                         15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,96 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_5):
                 if self.items4[4] == 1:
                     key1 = 5
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t4[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t4[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,96 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_6):
                 if self.items4[5] == 1:
                     key1 = 6
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t4[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t4[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,96 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_7):
                 if self.items4[6] == 1:
                     key1 = 7
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t4[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t4[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,96 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_8):
                 if self.items4[7] == 1:
                     key1 = 8
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t4[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t4[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,96 ,16*key1 ,16 ,16 ,15)                                       
         elif self.item_page == 5:
             for i in range(l):
                 if i == 0:
                     pass
                 else:
                     if self.items5[i-1] == 1:
                         key = str(i)
                         pyxel.text(3, 15+(10*i), key+".", 7) 
                         self.Draw_fonts(item_name5[key], 10, 15+(10*i))
             if pyxel.btn(pyxel.KEY_1):
                 key1 = 1
                 key2 = str(key1)
                 if self.items5[0] == 1:
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t5[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t5[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,112 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_2):
                 if self.items5[1] == 1:
                     key1 = 2
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t5[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t5[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,112 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_3):
                 if self.items5[2] == 1:
                     key1 = 3
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t5[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t5[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,112 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_4):
                 if self.items5[3] == 1:
                     key1 = 4
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t5[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t5[key2][i2], 10, 
                                         15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,112 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_5):
                 if self.items5[4] == 1:
                     key1 = 5
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t5[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t5[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,112 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_6):
                 if self.items5[5] == 1:
                     key1 = 6
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t5[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t5[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,112 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_7):
                 if self.items5[6] == 1:
                     key1 = 7
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t5[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t5[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,112 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_8):
                 if self.items5[7] == 1:
                     key1 = 8
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t5[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t5[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,112 ,16*key1 ,16 ,16 ,15)                   
         elif self.item_page == 6:
             for i in range(l):
                 if i == 0:
                     pass
                 else:
                     if self.items6[i-1] == 1:
                         key = str(i)
                         pyxel.text(3, 15+(10*i), key+".", 7) 
                         self.Draw_fonts(item_name6[key], 10, 15+(10*i))
             if pyxel.btn(pyxel.KEY_1):
                 key1 = 1
                 key2 = str(key1)
                 if self.items6[0] == 1:
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t6[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t6[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,128 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_2):
                 if self.items6[1] == 1:
                     key1 = 2
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t6[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t6[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,128 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_3):
                 if self.items6[2] == 1:
                     key1 = 3
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t6[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t6[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,128 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_4):
                 if self.items6[3] == 1:
                     key1 = 4
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t6[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t6[key2][i2], 10, 
                                         15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,128 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_5):
                 if self.items6[4] == 1:
                     key1 = 5
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t6[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t6[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,128 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_6):
                 if self.items6[5] == 1:
                     key1 = 6
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t6[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t6[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,128 ,16*key1 ,16 ,16 ,15)                     
             elif pyxel.btn(pyxel.KEY_7):
                 if self.items6[6] == 1:
                     key1 = 7
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t6[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t6[key2][i2], 
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,128 ,16*key1 ,16 ,16 ,15)
             elif pyxel.btn(pyxel.KEY_8):
                 if self.items6[7] == 1:
                     key1 = 8
                     key2 = str(key1)
                     pyxel.rect(0, 0, 120, 100, 0)
                     pyxel.rectb(0, 0, 120, 100, 7)
                     l2 = len(self.items_t6[key2])
                     for i2 in range(l2):
                         self.Draw_fonts(self.items_t6[key2][i2],
                                         10, 15+(10*i2))
                     pyxel.blt(100 ,47 ,0 ,128 ,16*key1 ,16 ,16 ,15)                   
            
         pyxel.text(5, 120, "Press SPACE-KEY to return", 
                    pyxel.frame_count % 16)
    #/////////////////////////////////////////////////////////////////////////
         
    #Shop/////////////////////////////////////////////////////////////////////
     elif n == 226 or n == 227:
         
         pyxel.bltm(0,0,0,240,0,16,16)
         
         #Shop select
         x = int(self.map_x / 16)
         y = int(self.map_y / 16)
         key = str(x) + "-" + str(y)
         if key == "8-2":
             s = self.shop1
             s2 = 1
         elif key == "3-7":
             s = self.shop2
             s2 = 2
        
         pyxel.blt(100 ,15 ,0 ,48 + 16*(s2 - 1) ,0 ,16 ,16 ,2)
         
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
                     if s2 == 1:
                         self.items[p] = 1
                     elif s2 == 2:
                         self.items2[p] = 1
                 else:
                     s.text_n = 99
             elif pyxel.btnp(pyxel.KEY_N):
                 s.text_n = 0
         
        #Item Window
         if s.text_n > 5 or s.text_n == 0:
             pass
         else:
             pyxel.blt(100 ,45 ,0 ,48 + 16*(s2 - 1) ,16*s.text_n ,16 ,16 ,15)
            
         for t in range(text_len):
             self.Draw_fonts(shop_text[t],13, 15 + (t * 10))
         pyxel.text(10, 113, "SPACE-KEY=Exit" + " Money=" + 
                    str(self.Player.money) + " G", 7)   
     #////////////////////////////////////////////////////////////////////////
         
     #Weapon Shop/////////////////////////////////////////////////////////////
     elif n == 282:
         self.map_x = 15 * 16
         self.map_y = 1 * 16
         self.map_count_x = 16
         self.map_count_y = 2
         self.Player.update(56, 104)
         self.movie_flug = False
     elif n == 334:
         self.map_x = 7 * 16
         self.map_y = 1 * 16
         self.map_count_x = 8
         self.map_count_y = 2
         self.Player.update(32, 56)
         self.movie_flug = False
     elif n == 335:
         self.Player.weapon = 1
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["50"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 336:
         self.Player.weapon = 2
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["51"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 337:
         self.Player.weapon = 3
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["52"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     #////////////////////////////////////////////////////////////////////////
         
     #Save and Load///////////////////////////////////////////////////////////
     elif n == 252:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.save_st == 0:
             self.Save_data()
         if self.save_st == 1:
             self.Draw_fonts(self.text_list["6"],5, 105)
         else:
             self.Draw_fonts(self.text_list["7"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     
     elif n == 253:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.load_st == 0:
             self.Load_data()
         if self.load_st == 1:
             self.Draw_fonts(self.text_list["8"],5, 105)
             e = len(self.End_event_x)
             for e2 in range(e):
                 self.MapEvents_ctr(self.End_event_x[e2], self.End_event_y[e2])
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
         self.MapEvents_ctr(10, 101)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 238:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["103"],5, 105)
         self.MapEvents_ctr(1, 31)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 239:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["103"],5, 105)
         self.MapEvents_ctr(1, 32)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 240:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["103"],5, 105)
         self.MapEvents_ctr(1, 33)
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
     #Ship#######################################################
     elif n == 244:
         x = int(self.map_x / 16)
         y = int(self.map_y / 16)
         key = str(x) + "-" + str(y)
         pyxel.rect(0, 40, 128, 88, 0)
         self.Draw_fonts(self.text_list["105_0"],5, 45)
         if key == "2-3":
             if self.items5[4] == 1:
                 pyxel.text(5, 65, "1.", 7)
                 self.Draw_fonts(self.text_list["105_1"],15, 65)
             if self.items5[5] == 1:
                 pyxel.text(5, 75, "2.", 7)
                 self.Draw_fonts(self.text_list["105_2"],15, 75)
             if self.items5[6] == 1:
                 pyxel.text(5, 85, "3.", 7)
                 self.Draw_fonts(self.text_list["105_3"],15, 85)
             if self.items5[7] == 1:
                 pyxel.text(5, 95, "4.", 7)
                 self.Draw_fonts(self.text_list["105_4"],15, 95)
             x = pyxel.tilemap(0).get(14+32, 13+48)
             if x == 33:
                 if pyxel.btn(pyxel.KEY_1):
                     if self.items5[4] == 1:
                         self.event_cnt = True
                         self.movie_count = 2441
                 if pyxel.btn(pyxel.KEY_2):
                     if self.items5[5] == 1:
                         self.event_cnt = True
                         self.movie_count = 2442
                 if pyxel.btn(pyxel.KEY_3):
                     if self.items5[6] == 1:
                         self.event_cnt = True
                         self.movie_count = 2443
                 if pyxel.btn(pyxel.KEY_4):
                     if self.items5[7] == 1:
                         self.event_cnt = True
                         self.movie_count = 2444
             else:
                self.Draw_fonts(self.text_list["105_7"],15, 105)
                         
         elif key == "3-8":
             if self.items5[5] == 1:
                 pyxel.text(5, 65, "1.", 7)
                 self.Draw_fonts(self.text_list["105_2"],15, 65)
             if self.items5[6] == 1:
                 pyxel.text(5, 75, "2.", 7)
                 self.Draw_fonts(self.text_list["105_3"],15, 75)
             if self.items5[7] == 1:
                 pyxel.text(5, 85, "3.", 7)
                 self.Draw_fonts(self.text_list["105_4"],15, 85)
             pyxel.text(5, 95, "4.", 7)
             self.Draw_fonts(self.text_list["105_6"],15, 95)
             x = pyxel.tilemap(0).get(14+32, 13+48)
             if x == 33:
                 if pyxel.btn(pyxel.KEY_1):
                     if self.items5[5] == 1:
                         self.event_cnt = True
                         self.movie_count = 2442
                 if pyxel.btn(pyxel.KEY_2):
                     if self.items5[6] == 1:
                         self.event_cnt = True
                         self.movie_count = 2443
                 if pyxel.btn(pyxel.KEY_3):
                     if self.items5[7] == 1:
                         self.event_cnt = True
                         self.movie_count = 2444
                 if pyxel.btn(pyxel.KEY_4):
                     self.event_cnt = True
                     self.movie_count = 2440
        
         elif key == "10-8":
             if self.items5[4] == 1:
                 pyxel.text(5, 65, "1.", 7)
                 self.Draw_fonts(self.text_list["105_1"],15, 65)
             if self.items5[5] == 1:
                 pyxel.text(5, 75, "2.", 7)
                 self.Draw_fonts(self.text_list["105_2"],15, 75)
             if self.items5[7] == 1:
                 pyxel.text(5, 85, "3.", 7)
                 self.Draw_fonts(self.text_list["105_4"],15, 85)
             pyxel.text(5, 95, "4.", 7)
             self.Draw_fonts(self.text_list["105_6"],15, 95)
             x = pyxel.tilemap(0).get(14+32, 13+48)
             if x == 33:
                 if pyxel.btn(pyxel.KEY_1):
                     if self.items5[4] == 1:
                         self.event_cnt = True
                         self.movie_count = 2441
                 if pyxel.btn(pyxel.KEY_2):
                     if self.items5[5] == 1:
                         self.event_cnt = True
                         self.movie_count = 2442
                 if pyxel.btn(pyxel.KEY_3):
                     if self.items5[7] == 1:
                         self.event_cnt = True
                         self.movie_count = 2444
                 if pyxel.btn(pyxel.KEY_4):
                     self.event_cnt = True
                     self.movie_count = 2440
                     
         elif key == "7-9":
             if self.items5[4] == 1:
                 pyxel.text(5, 65, "1.", 7)
                 self.Draw_fonts(self.text_list["105_1"],15, 65)
             if self.items5[6] == 1:
                 pyxel.text(5, 75, "2.", 7)
                 self.Draw_fonts(self.text_list["105_3"],15, 75)
             if self.items5[7] == 1:
                 pyxel.text(5, 85, "3.", 7)
                 self.Draw_fonts(self.text_list["105_4"],15, 85)
             pyxel.text(5, 95, "4.", 7)
             self.Draw_fonts(self.text_list["105_6"],15, 95)
             x = pyxel.tilemap(0).get(14+32, 13+48)
             if x == 33:
                 if pyxel.btn(pyxel.KEY_1):
                     if self.items5[4] == 1:
                         self.event_cnt = True
                         self.movie_count = 2441
                 if pyxel.btn(pyxel.KEY_2):
                     if self.items5[6] == 1:
                         self.event_cnt = True
                         self.movie_count = 2443
                 if pyxel.btn(pyxel.KEY_3):
                     if self.items5[7] == 1:
                         self.event_cnt = True
                         self.movie_count = 2444
                 if pyxel.btn(pyxel.KEY_4):
                     self.event_cnt = True
                     self.movie_count = 2440     
                     
         elif key == "7-8":
             if self.items5[4] == 1:
                 pyxel.text(5, 65, "1.", 7)
                 self.Draw_fonts(self.text_list["105_1"],15, 65)
             if self.items5[5] == 1:
                 pyxel.text(5, 75, "2.", 7)
                 self.Draw_fonts(self.text_list["105_2"],15, 75)
             if self.items5[6] == 1:
                 pyxel.text(5, 85, "3.", 7)
                 self.Draw_fonts(self.text_list["105_3"],15, 85)
             pyxel.text(5, 95, "4.", 7)
             self.Draw_fonts(self.text_list["105_6"],15, 95)
             x = pyxel.tilemap(0).get(14+32, 13+48)
             if x == 33:
                 if pyxel.btn(pyxel.KEY_1):
                     if self.items5[4] == 1:
                         self.event_cnt = True
                         self.movie_count = 2441
                 if pyxel.btn(pyxel.KEY_2):
                     if self.items5[5] == 1:
                         self.event_cnt = True
                         self.movie_count = 2442
                 if pyxel.btn(pyxel.KEY_3):
                     if self.items5[6] == 1:
                         self.event_cnt = True
                         self.movie_count = 2443
                 if pyxel.btn(pyxel.KEY_4):
                     self.event_cnt = True
                     self.movie_count = 2440                     
                         
         pyxel.text(5, 55, "Press Destination number.", 7)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2440:
         pyxel.bltm(0,0,0,112,48,16,16)
         pyxel.rect(0, 80, 128, 88, 0)
         self.event_cnt = False
         self.Draw_fonts(self.text_list["105_6"],15, 90)
         self.Draw_fonts(self.text_list["105"],55, 100)
         self.map_x = 2 * 16
         self.map_y = 3 * 16
         self.map_count_x = 3
         self.map_count_y = 4
         self.Player.update(24, 64)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2441:
         pyxel.bltm(0,0,0,112,48,16,16)
         pyxel.rect(0, 80, 128, 88, 0)
         self.event_cnt = False
         self.Draw_fonts(self.text_list["105_1"],15, 90)
         self.Draw_fonts(self.text_list["105"],55, 100)
         self.map_x = 3 * 16
         self.map_y = 8 * 16
         self.map_count_x = 4
         self.map_count_y = 9
         self.Player.update(48, 48)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2442:
         pyxel.bltm(0,0,0,112,48,16,16)
         pyxel.rect(0, 80, 128, 88, 0)
         self.event_cnt = False
         self.Draw_fonts(self.text_list["105_2"],15, 90)
         self.Draw_fonts(self.text_list["105"],55, 100)
         self.map_x = 7 * 16
         self.map_y = 9 * 16
         self.map_count_x = 8
         self.map_count_y = 10
         self.Player.update(88, 56)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2443:
         pyxel.bltm(0,0,0,112,48,16,16)
         pyxel.rect(0, 80, 128, 88, 0)
         self.event_cnt = False
         self.Draw_fonts(self.text_list["105_3"],15, 90)
         self.Draw_fonts(self.text_list["105"],55, 100)
         self.map_x = 10 * 16
         self.map_y = 8 * 16
         self.map_count_x = 11
         self.map_count_y = 9
         self.Player.update(48, 40)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)         
     elif n == 2444:
         pyxel.bltm(0,0,0,112,48,16,16)
         pyxel.rect(0, 80, 128, 88, 0)
         self.event_cnt = False
         self.Draw_fonts(self.text_list["105_4"],15, 90)
         self.Draw_fonts(self.text_list["105"],55, 100)
         self.map_x = 7 * 16
         self.map_y = 8 * 16
         self.map_count_x = 8
         self.map_count_y = 9
         self.Player.update(48, 64)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     ##################################################################
         
     #Information bord#################################################
     elif n == 245:
         pyxel.rect(0, 100, 128, 63, 0)
         x = int(self.map_x / 16)
         y = int(self.map_y / 16)
         key = str(x) + "-" + str(y)
         if key == "1-0":
             self.Draw_fonts(self.text_list["106"],5, 105)
         elif key == "0-0":
             pyxel.rect(0,95,128,33,0)
             pyxel.text(5, 100, "Press Key-I : View status.", 7)
             pyxel.text(5, 110, "Press Space : Attack.", 7)
         elif key == "4-0":
             self.Draw_fonts(self.text_list["107"],5, 105)
         elif key == "0-4":
             self.Draw_fonts(self.text_list["108"],5, 105)
         elif key == "7-0":
             self.Draw_fonts(self.text_list["108"],5, 105)             
         elif key == "0-1":
             self.Draw_fonts(self.text_list["109"],5, 105)
         elif key == "2-3":
             self.Draw_fonts(self.text_list["110"],5, 105)
         elif key == "10-2":
             self.Draw_fonts(self.text_list["129"],5, 105)
         elif key == "3-8":
             self.Draw_fonts(self.text_list["130"],5, 105)
         elif key == "7-8":
             self.Draw_fonts(self.text_list["131"],5, 105)
         elif key == "15-1":
             self.Draw_fonts(self.text_list["53"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     ###################################################################
         
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
             self.MapEvents_ctr(2, 22)
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
     elif n == 254:
         if self.items[5] == 0:
             self.movie_flug = False
         else:
             self.MapEvents_ctr(0, 10)
             pyxel.rect(0, 100, 128, 63, 0)
             pyxel.rect(0, 82, 18, 20, 0)
             pyxel.rect(18, 90, 110, 10, 0)
             pyxel.blt(2,84,1,0,240,16,16,14)
             self.Draw_fonts(self.text_list["123"],20, 92)
             self.Draw_fonts(self.text_list["117"],5, 105)
             if self.enemy_crt_flug == False:
                 new_enemy = Enemy(7*8, 8*8,80, 3)
                 new_enemy.enemy_m = 1
                 new_enemy.enemy_h = 80
                 self.enemys.append(new_enemy)
                 new_enemys = []
                 new_enemys.append(Enemy(5*8, 8*8,80, 2))
                 new_enemys.append(Enemy(5*8, 7*8,80, 2))
                 new_enemys.append(Enemy(2*8, 9*8,80, 1))
                 new_enemys.append(Enemy(2*8, 6*8,80, 1))
                 for e in new_enemys:
                     e.enemy_m = 1
                 for e2 in new_enemys:
                     self.enemys.append(e2)
                 self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 255:
         if self.items[5] == 0:
             self.movie_flug = False
         else:
             self.MapEvents_ctr(0, 101)
             pyxel.rect(0, 100, 128, 63, 0)
             pyxel.rect(0, 82, 18, 20, 0)
             pyxel.rect(18, 90, 110, 10, 0)
             pyxel.blt(2,84,1,0,240,16,16,14)
             self.Draw_fonts(self.text_list["123"],20, 92)
             self.Draw_fonts(self.text_list["118"],5, 105)
             self.event_cnt = True
             if self.enemy_crt_flug == False:
                 self.enemys.append(Enemy(13*8, 9*8,80, 2))
                 self.enemys.append(Enemy(14*8, 10*8,80, 1))
                 self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2551:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,0,240,16,16,14)
         self.Draw_fonts(self.text_list["123"],20, 92)
         self.MapEvents_ctr(0, 101)
         self.Draw_fonts(self.text_list["119"],5, 105)
         self.event_cnt = True
             #if self.enemy_crt_flug == False:
              #   new_enemy = Enemy(8*8, 8*8,80, 3)
               #  new_enemy.enemy_m = 1
                # self.enemys.append(new_enemy)
                 #self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2552:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,0,240,16,16,14)
         self.Draw_fonts(self.text_list["123"],20, 92)
         self.MapEvents_ctr(0, 101)
         self.Draw_fonts(self.text_list["120"],5, 105)
         self.event_cnt = True
             #if self.enemy_crt_flug == False:
              #   new_enemy = Enemy(8*8, 8*8,80, 3)
               #  new_enemy.enemy_m = 1
                # self.enemys.append(new_enemy)
                 #self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2553:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,0,240,16,16,14)
         self.Draw_fonts(self.text_list["123"],20, 92)
         self.MapEvents_ctr(0, 101)
         self.Draw_fonts(self.text_list["121"],5, 105)
         self.event_cnt = True
             #if self.enemy_crt_flug == False:
              #   new_enemy = Enemy(8*8, 8*8,80, 3)
               #  new_enemy.enemy_m = 1
                # self.enemys.append(new_enemy)
                 #self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2554:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,0,240,16,16,14)
         self.Draw_fonts(self.text_list["123"],20, 92)
         self.MapEvents_ctr(0, 101)
         self.Draw_fonts(self.text_list["122"],5, 105)
         self.event_cnt = False
             #if self.enemy_crt_flug == False:
              #   new_enemy = Enemy(8*8, 8*8,80, 3)
               #  new_enemy.enemy_m = 1
                # self.enemys.append(new_enemy)
                 #self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2555:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["132"],5, 105)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2556:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["133"],5, 105)
         self.event_cnt = False
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 259:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items[5] == 0:
             self.Draw_fonts(self.text_list["124"],5, 105)
         else:
             self.Draw_fonts(self.text_list["114"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 270:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.boss1_flug == True:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(7, 7)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 271:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.boss1_flug == True:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(7, 7)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 272:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.boss2_flug == True:
             self.Draw_fonts(self.text_list["100"],5, 105)
             #self.MapEvents_ctr(7, 7)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 273:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.boss2_flug == True:
             self.Draw_fonts(self.text_list["100"],5, 105)
             #self.MapEvents_ctr(7, 7)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 274:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.boss3_flug == True:
             self.Draw_fonts(self.text_list["100"],5, 105)
             #self.MapEvents_ctr(7, 7)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 275:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.boss3_flug == True:
             self.Draw_fonts(self.text_list["100"],5, 105)
             #self.MapEvents_ctr(7, 7)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 288:
         pyxel.rect(0, 90, 128, 63, 0)
         self.Draw_fonts(self.text_list["999"],5, 95)
         self.Draw_fonts(self.text_list["999_1"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
#/////AREA2///////////////////////////////////////////////////////////////////
     elif n == 303 or n == 302 or n == 304:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["135"],5, 105)
         self.MapEvents_ctr(1, 8)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 3031:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,16,240,16,16,14)
         self.Draw_fonts(self.text_list["136"],20, 92)
         self.Draw_fonts(self.text_list["137"],5, 105)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 3032:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,16,240,16,16,14)
         self.Draw_fonts(self.text_list["136"],20, 92)
         self.Draw_fonts(self.text_list["138"],5, 105)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 3033:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,16,240,16,16,14)
         self.Draw_fonts(self.text_list["136"],20, 92)
         self.Draw_fonts(self.text_list["139"],5, 105)
         self.MapEvents_ctr(1, 81)
         self.event_cnt = False
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)

     elif n == 305 or n == 306:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items2[3] == True:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(2, 7)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 312:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(2, 6)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 314:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(3, 7)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)

     elif n == 311:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items2[4] == True:
             self.Draw_fonts(self.text_list["141"],5, 105)
             tx = self.map_count_x - 1
             ty = self.map_count_y - 1
             tkey = str(tx) + "-" + str(ty)
             if tkey == "0-4":
                 self.MapEvents_ctr(0, 4)
             elif tkey == "1-6":
                 self.MapEvents_ctr(1, 62)
             elif tkey == "1-7":
                 self.MapEvents_ctr(1, 7)
         else:
             self.Draw_fonts(self.text_list["140"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 316:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items2[2] == True:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(1, 6)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 317:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items2[4] == 0:
             self.Draw_fonts(self.text_list["113_1"],5, 105)
         else:
             self.Draw_fonts(self.text_list["114"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 326 or n == 327 or n == 328 or n == 329:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items2[5] == 0:
             self.Draw_fonts(self.text_list["124"],5, 105)
         else:
             self.Draw_fonts(self.text_list["114"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)

         
     #////////////////////////////////////////////////////////////////////////
        
     #NPC text////////////////////////////////////////////////////////////////
     elif n == 224:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["200"],0, 105)
         self.Draw_fonts(self.text_list["300"],20, 92)
         pyxel.blt(2,84,0,0,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 256:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         if self.text_key_flug == False:
             tn = randint(4, 6)
             self.text_key = str(200 + tn)
             self.text_key_flug = True
         self.Draw_fonts(self.text_list[self.text_key],0, 105)
         self.Draw_fonts(self.text_list["301"],20, 92)
         pyxel.blt(2,84,0,16,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 257:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         if self.text_key_flug == False:
             tn = randint(1, 3)
             self.text_key = str(200 + tn)
             self.text_key_flug = True
         self.Draw_fonts(self.text_list[self.text_key],0, 105)
         self.Draw_fonts(self.text_list["301"],20, 92)
         pyxel.blt(2,84,0,32,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 260:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["125"],0, 105)
         self.Draw_fonts(self.text_list["302"],20, 92)
         pyxel.blt(2,84,0,64,208,16,16,14)  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 2601:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["126"],0, 105)
         self.Draw_fonts(self.text_list["302"],20, 92)
         pyxel.blt(2,84,0,64,208,16,16,14)  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16) 
     elif n == 2602:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["127"],0, 105)
         self.Draw_fonts(self.text_list["302"],20, 92)
         pyxel.blt(2,84,0,64,208,16,16,14)  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16) 
     elif n == 2603:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["128"],0, 105)
         self.Draw_fonts(self.text_list["302"],20, 92)
         pyxel.blt(2,84,0,64,208,16,16,14)  
         self.event_cnt = False
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 261:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         if self.text_key_flug == False:
             tn = randint(7, 9)
             self.text_key = str(200 + tn)
             self.text_key_flug = True
         self.Draw_fonts(self.text_list[self.text_key],0, 105)
         self.Draw_fonts(self.text_list["301"],20, 92)
         pyxel.blt(2,84,0,80,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 262:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         if self.text_key_flug == False:
             tn = randint(10, 12)
             self.text_key = str(200 + tn)
             self.text_key_flug = True
         self.Draw_fonts(self.text_list[self.text_key],0, 105)
         self.Draw_fonts(self.text_list["301"],20, 92)
         pyxel.blt(2,84,0,96,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     #////////////////////////////////////////////////////////////////////////
     
     #Other///////////////////////////////////////////////////////////////////
     else:
         self.movie_flug = False
     #////////////////////////////////////////////////////////////////////////
     
    #Return game
     if pyxel.btnp(pyxel.KEY_SPACE):
         if self.event_cnt == False:
             self.movie_flug = False
         else:
            #Event cntinue
            if n == 255:
                self.movie_count = 2551
            elif n == 2551:
                self.movie_count = 2552
            elif n == 2552:
                self.movie_count = 2553
            elif n == 2553:
                self.movie_count = 2554
            elif n == 2555:
                self.movie_count = 2556
            elif n == 1001:
                self.movie_count = 1002
            elif n == 1002:
                self.movie_count = 1003
            elif n == 1003:
                self.movie_count = 1004
            elif n == 1004:
                self.movie_count = 1005
            elif n == 1005:
                self.movie_count = 1006
            elif n == 260:
                self.movie_count = 2601
            elif n == 2601:
                self.movie_count = 2602
            elif n == 2602:
                self.movie_count = 2603
            elif n == 303 or n == 302 or n == 304:
                self.movie_count = 3031
            elif n == 3031:
                self.movie_count = 3032
            elif n == 3032:
                self.movie_count = 3033


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
                 self.MapEvents_ctr(9, 11)
         elif n == 250:
             if self.items[6] == 0:
                 self.items[6] = 1
                 self.MapEvents_ctr(9, 12)
         elif n == 251:
             if self.items[7] == 0:
                 self.items[7] = 1
                 self.MapEvents_ctr(9, 13)
         elif n == 259:
             if self.items[5] == 0:
                 self.items[5] = 1
                 self.MapEvents_ctr(0, 3)
         elif n == 317:
             if self.items2[4] == 0:
                 self.items2[4] = 1
                 self.MapEvents_ctr(1, 61)
         elif n == 326 or n == 327 or n == 328 or n == 329:
             if self.items2[5] == 0:
                 self.items2[5] = 1
                 self.MapEvents_ctr(0, 41)
            
     #Event save reset.
         if self.Event_save == True:
             self.Event_save = False
     #Text_key reset.
         if self.text_key_flug == True:
             self.text_key_flug = False
             self.text_key = 0
     #Enemy flug reset.
         if self.enemy_crt_flug == True:
             self.enemy_crt_flug = False
     #Item page reset.
         self.item_page = 1

 def Draw_fonts(self,txt,x,y):  
     txt_count = len(txt)      
     if self.lng == "ja":
         for i in range(txt_count):
             #Key check
             font_xy = self.font_list[txt[i]]
        
             fontx = font_xy[0]
             fonty = font_xy[1]
             pyxel.blt(x + 8 * i,y,1,fontx,fonty,8,8,14)
     else:
         pyxel.text(x, y, txt, 7)
        
 def Save_data(self):
     #Save data
     try:
         with open('DATA/data.csv', 'w', newline="") as f:
                 writer = csv.writer(f)
                 data = []
                 data2 = []
                 data3 = []
                 data4 = []
                 for i in self.items:
                     data.append(i)
                 for i2 in self.items2:
                     data.append(i2)
                 for i3 in self.items3:
                     data.append(i3)
                 for i4 in self.items4:
                     data.append(i4)
                 for i5 in self.items5:
                     data.append(i5)
                 for i6 in self.items6:
                     data.append(i6)
                 data.append(self.gate_flug_1)
                 data.append(self.map_count_x)
                 data.append(self.map_count_y)
                 data.append(self.map_x)
                 data.append(self.map_y)
                 data.append(self.Player.money)
                 data.append(self.Player.player_x)
                 data.append(self.Player.player_y)
                 writer.writerow(data)
                 
                 for i7 in self.End_event_x:
                      data2.append(i7)
                 writer.writerow(data2)
                 for i8 in self.End_event_y:
                      data3.append(i8)
                 writer.writerow(data3)
                 data4.append(self.Player.weapon)
                 writer.writerow(data4)
                 
                 self.save_st = 1
     except:
         self.save_st = 2
                 
 def Load_data(self):
     data = []
     try:
         with open('DATA/data.csv') as f:
             reader = csv.reader(f)
             for row in reader:
                 data.append(row)
         i = 48
         for i2 in range(i):
           
           if i2 < 8:
               self.items[i2] = int(data[0][i2])
           elif i2 < 16:
               self.items2[i2-8] = int(data[0][i2])
           elif i2 < 24:
               self.items3[i2-16] = int(data[0][i2])
           elif i2 < 32:
               self.items4[i2-24] = int(data[0][i2])
           elif i2 < 40:
               self.items5[i2-32] = int(data[0][i2])
           elif i2 < 48:
               self.items6[i2-40] = int(data[0][i2])
           
         self.gate_flug1 = int(data[0][i])
         self.map_count_x = int(data[0][i+1])
         self.map_count_y = int(data[0][i+2])
         self.map_x = int(data[0][i+3])
         self.map_y = int(data[0][i+4])
         self.Player.money = int(data[0][i+5])
         self.Player.player_x = int(data[0][i+6])
         self.Player.player_y = int(data[0][i+7])
         for i4 in data[1]:
             self.End_event_x.append(int(i4))
         for i5 in data[2]:
             self.End_event_y.append(int(i5))
         self.load_st = 1
         for i3 in range(4):
             self.shop1.urikire[i3] = self.items[i3]
         self.Player.weapon = int(data[3][0])
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
     self.money = 0
     self.weapon = 1
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
  def __init__(self, n, l):
      #Text list set
      if l == "ja":
          if n == 1:
              self.text_list_s = Text_list.text_get_s()
              self.item_list = Text_list.item_get()
          elif n == 2:
              self.text_list_s = Text_list.text_get_s2()
              self.item_list = Text_list.item_get2()
          elif n == 3:
              self.text_list_s = Text_list.text_get_s3()
              self.item_list = Text_list.item_get3()
          elif n == 4:
              self.text_list_s = Text_list.text_get_s4()
              self.item_list = Text_list.item_get4()
          elif n == 5:
              self.text_list_s = Text_list.text_get_s5()
              self.item_list = Text_list.item_get5()
          elif n == 6:
              self.text_list_s = Text_list.text_get_s6()
              self.item_list = Text_list.item_get6()
      elif l == "en":
          if n == 1:
              self.text_list_s = Text_list_en.text_get_s()
              self.item_list = Text_list_en.item_get()
          elif n == 2:
              self.text_list_s = Text_list_en.text_get_s2()
              self.item_list = Text_list_en.item_get2()
          elif n == 3:
              self.text_list_s = Text_list_en.text_get_s3()
              self.item_list = Text_list_en.item_get3()
          elif n == 4:
              self.text_list_s = Text_list_en.text_get_s4()
              self.item_list = Text_list_en.item_get4()
          elif n == 5:
              self.text_list_s = Text_list_en.text_get_s5()
              self.item_list = Text_list_en.item_get5()
          elif n == 6:
              self.text_list_s = Text_list_en.text_get_s6()
              self.item_list = Text_list_en.item_get6()
        
      self.shop_v = n
      self.item = [self.item_list["1"],
                 self.item_list["2"],
                 self.item_list["3"],
                 self.item_list["4"],
                 self.item_list["0"]]
      if n == 1:
          self.price = [100,150,250,250]
      elif n == 2:  
          self.price = [100,150,250,250]
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