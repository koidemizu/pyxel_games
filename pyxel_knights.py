# -*- coding: utf-8 -*-

import pyxel
from random import randint

class App:
 def __init__(self):
     #Font set
     self.font_list = {
         "a":[0,0],
         "A":[8,0],
         "i":[16,0],
         "I":[24,0],
         "u":[32,0],
         "U":[40,0],
         "e":[48,0],
         "E":[56,0],
         "o":[64,0],
         "O":[72,0],
         "KA":[80,0],
         "GA":[88,0],
         "KI":[96,0],
         "GI":[104,0],
         "KU":[112,0],
         "GU":[120,0],
         "KE":[128,0],
         "GE":[136,0],
         "KO":[144,0],
         "GO":[152,0],
         "SA":[160,0],
         "ZA":[168,0],
         "SI":[176,0],
         "JI":[184,0],
         "SU":[192,0],
         "ZU":[200,0],
         "SE":[208,0],
         "ZE":[216,0],
         "SO":[224,0],
         "ZO":[232,0],
         "TA":[240,0],
         "DA":[248,0],
         "TI":[0,8],
         "DI":[8,8],
         "tu":[16,8],
         "TU":[24,8],
         "DU":[32,8],
         "TE":[40,8],
         "DE":[48,8],
         "TO":[56,8],
         "DO":[64,8],
         "NA":[72,8],
         "NI":[80,8],
         "NU":[88,8],
         "NE":[96,8],
         "NO":[104,8],
         "HA":[112,8],
         "BA":[120,8],
         "PA":[128,8],
         "HI":[136,8],
         "BI":[144,8],
         "PI":[152,8],
         "HU":[160,8],
         "BU":[168,8],
         "PU":[176,8],
         "HE":[184,8],
         "BE":[192,8],
         "PE":[200,8],
         "HO":[208,8],
         "BO":[216,8],
         "PO":[224,8],
         "MA":[232,8],
         "MI":[240,8],
         "MU":[248,8],
         "ME":[0,16],
         "MO":[8,16],
         "ya":[16,16],
         "YA":[24,16],
         "yu":[32,16],
         "YU":[40,16],
         "yo":[48,16],
         "YO":[56,16],
         "RA":[64,16],
         "RI":[72,16],
         "RU":[80,16],
         "RE":[88,16],
         "RO":[96,16],
         "wa":[104,16],
         "WA":[112,16],
         "WI":[120,16],
         "WE":[128,16],
         "WO":[136,16],
         "NN":[144,16],
         }
     
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
     self.npc_pos_x = {
               "0-0":[],
               "1-0":[],
               "2-0":[],
               "3-0":[],
               "4-0":[],
               "5-0":[13],
               "6-0":[12,12],
               "7-0":[107,208],
               "8-0":[],
               "9-0":[],
               "10-0":[],
               "0-1":[],
               "1-1":[],
               "2-1":[],
               "3-1":[],
               "4-1":[],
               "5-1":[],
               "6-1":[],
               "7-1":[],
               "8-1":[7],
               "9-1":[],
               "10-1":[],
               "0-2":[],
               "1-2":[],
               "2-2":[],
               "3-2":[],
               "4-2":[],
               "5-2":[],
               "6-2":[],
               "7-2":[],
               "8-2":[313],
               "9-2":[],
               "10-2":[],
               "0-3":[],
               "1-3":[],
               "2-3":[],
               "3-3":[],
               "4-3":[],
               "5-3":[],
               "6-3":[],
               "7-3":[],
               "8-3":[13],
               "9-3":[],
               "10-3":[],
               }
     self.npc_pos_y = {
               "0-0":[],
               "1-0":[],
               "2-0":[],
               "3-0":[],
               "4-0":[],
               "5-0":[9],
               "6-0":[4,10],
               "7-0":[107,212],
               "8-0":[],
               "9-0":[],
               "10-0":[],
               "0-1":[],
               "1-1":[],
               "2-1":[],
               "3-1":[],
               "4-1":[],
               "5-1":[],
               "6-1":[],
               "7-1":[],
               "8-1":[5],
               "9-1":[],
               "10-1":[],
               "0-2":[],
               "1-2":[],
               "2-2":[],
               "3-2":[],
               "4-2":[],
               "5-2":[],
               "6-2":[],
               "7-2":[],
               "8-2":[307],
               "9-2":[],
               "10-2":[],
               "0-3":[],
               "1-3":[],
               "2-3":[],
               "3-3":[],
               "4-3":[],
               "5-3":[],
               "6-3":[],
               "7-3":[],
               "8-3":[13],
               "9-3":[],
               "10-3":[],
               }      
     
     #Enemy status
     self.enemys = []
     self.enemy_pos_x = {
               "0-0":[],
               "1-0":[5,13],
               "2-0":[9,12,13],
               "3-0":[10,12,8],
               "4-0":[6,8,9,12],
               "5-0":[],
               "6-0":[],
               "7-0":[],
               "8-0":[],
               "9-0":[],
               "10-0":[],
               "0-1":[5,106,108],
               "1-1":[5,5,11,11,7,8],
               "2-1":[2,3,2,3,4],
               "3-1":[],
               "4-1":[],
               "5-1":[],
               "6-1":[],
               "7-1":[],
               "8-1":[],
               "9-1":[],
               "10-1":[],
               "0-2":[106,108,109,1012],
               "1-2":[107,108,104,105,111,112,106,108,110],
               "2-2":[],
               "3-2":[7,8,9,10,11,11,12],
               "4-2":[210],
               "5-2":[205,208,210,211],
               "6-2":[],
               "7-2":[],
               "8-2":[],
               "9-2":[],
               "10-2":[],
               "0-3":[],
               "1-3":[],
               "2-3":[],
               "3-3":[],
               "4-3":[],
               "5-3":[],
               "6-3":[],
               "7-3":[],
               "8-3":[13],
               "9-3":[],
               "10-3":[],
               }
     self.enemy_pos_y = {
               "0-0":[],
               "1-0":[5,7],
               "2-0":[7,8,2],
               "3-0":[7,8,11],
               "4-0":[7,8,7,8],
               "5-0":[],
               "6-0":[],
               "7-0":[],
               "8-0":[],
               "9-0":[],
               "10-0":[],
               "0-1":[5,10,10],
               "1-1":[5,10,5,10,8,7],
               "2-1":[7,8,9,10,11],
               "3-1":[],
               "4-1":[],
               "5-1":[],
               "6-1":[],
               "7-1":[],
               "8-1":[],
               "9-1":[],
               "10-1":[],
               "0-2":[7,11,7,8],
               "1-2":[5,6,7,8,7,8,2,3,3],
               "2-2":[],
               "3-2":[10,10,10,10,10,5,5,],
               "4-2":[7],
               "5-2":[4,8,7,9],
               "6-2":[],
               "7-2":[],
               "8-2":[],
               "9-2":[],
               "10-2":[],
               "0-3":[],
               "1-3":[],
               "2-3":[],
               "3-3":[],
               "4-3":[],
               "5-3":[],
               "6-3":[],
               "7-3":[],
               "8-3":[13],
               "9-3":[],
               "10-3":[],
               }
     
     #System status
     self.game_start = False 
     self.game_over = False 
     self.movie_flug = False 
     self.movie_count = 0
     self.music_flug = True
     
     pyxel.init(128,128)

     #Image read
     pyxel.load('assets/pknights.pyxres')
     
     pyxel.run(self.update, self.draw)
     
 def update(self):

     if pyxel.btnp(pyxel.KEY_S) and self.game_start == False:
       self.game_start = True
       self.movie_flug = True
       self.movie_count = 1
       self.music_flug = False
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
            new_enemy = Enemy1(new_enemy_x*8, enemy_y_1[i]*8, 
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
        pyxel.cls(0)
        pyxel.text(35, 40, "PYXEL KNIGHTS", 7)
        pyxel.text(45, 70, "S = ", 7)
        self.Draw_fonts(["HA","JI","ME","RU"], 60, 70)
        pyxel.text(45, 85, "Q = ", 7)
        self.Draw_fonts(["YA","ME","RU"], 60, 85)
     else: #Draw player hp
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
                 del self.enemys[e]
                 #Music_ctr
                 pyxel.play(2,2,loop=False)
                 if len(self.enemys) == 0:
                     x = int(self.map_x / 16)
                     y = int(self.map_y / 16)
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
        #pyxel.tilemap(0).set(8+self.map_x, 10+self.map_y, ["010", "012"]) 

 def Movie_ctr(self,n):
     if n == 1:
         pyxel.rect(0, 65, 128, 63, 0)
         self.Draw_fonts(["A","NA","TA","HA","O","U","KO","KU","NO",
                          "KA","KI","yu","U","KI","SI"], 5, 70)
         self.Draw_fonts(["MI","YA","KO","NO","HA","ZU","RE","NI",
                          "SU","NN","DE","I","MA","SU"], 5, 80)
         self.Draw_fonts(["KO","NO","SE","KA","I","WO","KI","MA","MA",
                          "NI"], 5, 95)
         self.Draw_fonts(["BO","U","KE","NN","SI","TE","MI","MA","SI",
                          "yo","U"], 5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 224:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(["MI","YA","KO","NO","E","I","HE","I","DA"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 225:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(["MI","YA","KO","NO","JI","yu","U","NI","NN",
                          "DA"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     if pyxel.btnp(pyxel.KEY_SPACE):
         self.movie_flug = False

 def Draw_fonts(self,txt,x,y):  
     txt_count = len(txt)      
     for i in range(txt_count):
         #Key check
         font_xy = self.font_list[txt[i]]
        
         fontx = font_xy[0]
         fonty = font_xy[1]
         pyxel.blt(x + 8 * i,y,1,fontx,fonty,8,8,14)
        
           
class Player:
 def __init__(self, x, y):
     self.player_x = x
     self.player_y = y
     self.player_h = 100
     self.player_d = 0
     self.player_m = 0
     self.player_m2 = 0
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
      
class Enemy1:
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


App()