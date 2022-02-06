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
     self.atc_v = 0
     self.atc_vf = False
     self.atc_count = 0      
     self.p_atc_x = 0        
     self.p_atc_y = 0        
     
     self.timer_f = False
     self.timer = 0
     
     self.sel_chap = ""
     
     #Map status
     self.stage_flug = 1     
     self.map_count_x = 1    
     self.map_count_y = 1    
     self.map_x = 0
     self.map_y = 0
     self.map_move = 0
     self.b3_l = False
     self.set_para = 0
     self.set_para2 = 0

     #NPC status
     self.npcs = []
     self.npc_move = 0
     self.npc_pos_x = Npc_pos.npc_posx()
     self.npc_pos_y = Npc_pos.npc_posy()

     #Enemy status
     self.enemys = []
     self.enemy_pos_x = Enemy_pos.enemy_posx()
     self.enemy_pos_y = Enemy_pos.enemy_posy()
     self.e_atk_count = 0
     self.e_atk_flug = True
     
     #System status
     self.game_start = False 
     self.game_over = False 
     self.movie_flug = False 
     self.movie_count = 0
     self.music_flug = True
     self.map_ch_cn = 0
     self.map_ch_fl = 0
     self.map_ch_fl2 = False
     self.o_cnt = 0
     self.t_cnt = 0
     self.game_end = False
     
     self.tile_camera_cn = 0
     self.tile_camera_cnx = 0
     self.tile_camera_cny = 0
     
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
     self.item_page = 1
     self.page_move = 0
     self.n1 = 0
     self.n2 = 0
     self.n3 = 0
     self.sn = 1
     
     pyxel.init(200,129, title="Regicide", capture_sec=30, quit_key=pyxel.KEY_NONE)

     #Image read
     pyxel.load('assets/pknights.pyxres')
     
     pyxel.run(self.update, self.draw)
     
 def update(self):
     #x = int(self.map_x / 16)
     #y = int(self.map_y / 16)
     #print(x)
     #print(y)
     if self.timer_f == True:
         self.timer += 1      
     
     if self.lng == "none":
         self.Movie_ctr(-1)
     else:
         if pyxel.btnp(pyxel.KEY_1) and self.game_start == False:
             self.sel_chap = "Chapter 1"
             self.timer_f = False
             self.timer = 0
             self.game_start = True
             self.movie_flug = True
             self.Load_data(0)
             if self.load_st == 1:
                 self.Draw_fonts(self.text_list["8"],5, 105)
                 e = len(self.End_event_x)
                 for e2 in range(e):
                     self.MapEvents_ctr(self.End_event_x[e2], 
                                        self.End_event_y[e2])
             self.movie_count = 1001
             self.music_flug = False             
         elif pyxel.btnp(pyxel.KEY_2) and self.game_start == False:
             self.sel_chap = "Chapter 2"
             self.timer_f = False
             self.timer = 0
             self.game_start = True
             self.movie_flug = True
             self.Load_data(1)
             if self.load_st == 1:
                 self.Draw_fonts(self.text_list["8"],5, 105)
                 e = len(self.End_event_x)
                 for e2 in range(e):
                     self.MapEvents_ctr(self.End_event_x[e2], 
                                        self.End_event_y[e2])
             self.movie_count = 1010
             self.music_flug = False             
             
         elif pyxel.btnp(pyxel.KEY_3) and self.game_start == False:
             self.sel_chap = "Chapter 3"
             self.timer_f = False
             self.timer = 0
             self.game_start = True
             self.movie_flug = True
             self.Load_data(2)
             if self.load_st == 1:
                 self.Draw_fonts(self.text_list["8"],5, 105)
                 e = len(self.End_event_x)
                 for e2 in range(e):
                     self.MapEvents_ctr(self.End_event_x[e2], 
                                        self.End_event_y[e2])
             self.movie_count = 1015
             self.music_flug = False                          
             
         elif pyxel.btnp(pyxel.KEY_4) and self.game_start == False:
             self.sel_chap = "Chapter 4"
             self.timer_f = False
             self.timer = 0
             self.game_start = True
             self.movie_flug = True
             self.Load_data(3)
             if self.load_st == 1:
                 self.Draw_fonts(self.text_list["8"],5, 105)
                 e = len(self.End_event_x)
                 for e2 in range(e):
                     self.MapEvents_ctr(self.End_event_x[e2], 
                                        self.End_event_y[e2])
             self.movie_count = 1020
             self.music_flug = False          
             
         elif pyxel.btnp(pyxel.KEY_5) and self.game_start == False:
             self.sel_chap = "Chapter 5"
             self.timer_f = False
             self.timer = 0
             self.game_start = True
             self.movie_flug = True
             self.Load_data(4)
             if self.load_st == 1:
                 self.Draw_fonts(self.text_list["8"],5, 105)
                 e = len(self.End_event_x)
                 for e2 in range(e):
                     self.MapEvents_ctr(self.End_event_x[e2], 
                                        self.End_event_y[e2])
             self.movie_count = 1030
             self.music_flug = False                       
             
         elif pyxel.btnp(pyxel.KEY_6) and self.game_start == False:
             self.sel_chap = "Chapter 6"
             self.timer_f = False
             self.timer = 0
             self.game_start = True
             self.movie_flug = True
             self.Load_data(5)
             if self.load_st == 1:
                 self.Draw_fonts(self.text_list["8"],5, 105)
                 e = len(self.End_event_x)
                 for e2 in range(e):
                     self.MapEvents_ctr(self.End_event_x[e2], 
                                        self.End_event_y[e2])
             self.movie_count = 1040
             self.music_flug = False                       
             
     if pyxel.btnp(pyxel.KEY_Q) and self.game_start == False:
         pyxel.quit()
         
     if pyxel.btnp(pyxel.KEY_M):
         self.movie_count = 1050
         self.movie_flug = True
         
     if pyxel.btnp(pyxel.KEY_Q) and self.game_over == True:
         #Return to title#########################################
         #Player status
         self.Player = Player(8, 56)
         self.player_move = 0    
         self.atc_flug = False   
         self.atc_v = 0
         self.atc_vf = False
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
         self.set_para = 0
         self.set_para2 = 0

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
         self.item_page = 1
         self.page_move = 0
         self.n1 = 0
         self.n2 = 0
         self.n3 = 0
         self.sn = 1
         ##############################################################

     if pyxel.btnp(pyxel.KEY_SPACE) and self.game_end == True:
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
         self.set_para = 0
         self.set_para2 = 0
         

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
         self.game_end = False
     
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
         self.item_page = 1
         self.page_move = 0
         self.n1 = 0
         self.n2 = 0
         self.n3 = 0
         self.sn = 1
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
        self.Player.last_p = [0, 0]
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
                elif enemy_x_1[i] < 600:
                   new_enemy_v = 112
                   new_enemy_x = enemy_x_1[i] - 500
                elif enemy_x_1[i] < 700:
                   new_enemy_v = 128
                   new_enemy_x = enemy_x_1[i] - 600
                
                if (xy_key == "8-0" or
                   xy_key == "9-0" or
                   xy_key == "10-0" or
                   xy_key == "11-8" or
                   xy_key == "12-8"):
                    new_enemy_v2 = randint(1,2)
                elif (xy_key == "0-8" or
                      xy_key == "0-7" or
                      xy_key == "0-6" or
                      xy_key == "1-6" or
                      xy_key == "1-7" ):
                    new_enemy_v2 = randint(2,5)
                elif xy_key == "1-8":
                    new_enemy_v2 = 4
                elif xy_key == "1-5":
                    new_enemy_v2 = randint(4, 5)
                elif xy_key == "5-10" or xy_key == "7-10":
                    new_enemy_v2 = randint(4, 5)
                    if enemy_x_1[i] == 511:
                        new_enemy_v2 = 12
                elif xy_key == "5-11" or xy_key == "7-11":
                    new_enemy_v2 = randint(1, 3)
                elif (xy_key == "5-12" or xy_key == "6-12" or 
                      xy_key == "7-12" or xy_key == "11-7"):
                    new_enemy_v2 = randint(1, 5)
                elif xy_key == "5-13":
                    if enemy_x_1[i] == 502:
                        new_enemy_v2 = 12
                    else:
                        new_enemy_v2 = 1
                elif xy_key == "6-13":
                    if ((enemy_x_1[i] == 504) or (enemy_x_1[i] == 506) or
                        (enemy_x_1[i] == 512)):
                        new_enemy_v2 = 12
                    else:
                        new_enemy_v2 = 1
                elif xy_key == "5-14":
                    if ((enemy_x_1[i] == 502) or (enemy_x_1[i] == 502)):
                        new_enemy_v2 = 12
                    else:
                        new_enemy_v2 = 4
                elif (xy_key == "14-8" or xy_key == "15-8"
                     or xy_key == "14-7" or xy_key == "15-7"):
                    vc1 = randint(1, 7)
                    vc2 = randint(1, 7)
                    if vc1 == vc2:
                        new_enemy_v2 = 19
                    else:
                        new_enemy_v2 = 1
                elif (xy_key == "13-9"):
                    new_enemy_v2 = 19
                elif xy_key == "15-5" or xy_key == "14-6" or xy_key == "13-5":
                    new_enemy_v2 = randint(1, 3)
                    if new_enemy_v2 == 3:
                        new_enemy_v2 = 12
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
                elif npc_x_1[i] < 1301:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 1200
                elif npc_x_1[i] < 1401:
                   new_npc_b = 8
                   new_npc_x = npc_x_1[i] - 1300
                
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
                elif npc_y_1[i] < 1301:
                    new_npc_v = 192
                    new_npc_y = npc_y_1[i] - 1200
                elif npc_y_1[i] < 1401:
                    new_npc_v = 208
                    new_npc_y = npc_y_1[i] - 1300
                
                new_npc = NPC(new_npc_x*8, new_npc_y*8, new_npc_b, new_npc_v)
                self.npcs.append(new_npc)
            
        self.map_move = 0
      
 def draw(self):
     pyxel.cls(0)
     
     #Debug
     #print(self.map_x)
     #print(self.map_y)
     
     #Draw Map change effect
    # if self.map_ch_fl > 0:
     #    self.Map_Change_EF()
     #Map Gimic1
     spx = self.map_count_x - 1
     spy = self.map_count_y - 1
     spkey = str(spx) + "-" + str(spy)
     
     if self.map_ch_fl > 0:
         if spkey == "2-5" or spkey == "10-1":
             pass
         else:
             self.Map_Change_EF()
             
     #Draw tilemap
     pyxel.bltm(0,0,0,0 + self.map_x * 8, 0 + self.map_y * 8, 128, 128)
              
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
          
     #Map Gimic2
     if spkey == "0-5":
         pyxel.blt(7*8,4*8,1,192,32,16,16)
     elif spkey == "2-3":
         pyxel.blt(3*8,1*8,1,208,32,24,24,14)         
     elif spkey == "2-5" or spkey == "10-1":
         if self.items[6] == 1:
             if self.items3[4] == 1:
                 wi = 128
             else:
                 wi = 56
         else:
             wi = 34
         pyxel.clip(self.Player.player_x-(wi/2),self.Player.player_y-(wi/2),
                    wi, wi)
     elif spkey == "3-14":
         if self.b3_l == True:
             wi = 64
             pyxel.clip(self.Player.player_x-(wi/2),self.Player.player_y-(wi/2),
                        wi, wi)
         else:
             pyxel.clip()
          
     #Draw title text
     if self.game_start == False: 
        if self.lng == "ja" or self.lng == "en":
            pyxel.cls(0)
            pyxel.rectb(0, 40 , 200, 88, 1)
            pyxel.rectb(0, 0 , 200, 128, 1)
            pyxel.blt(38, 9, 0, 32, 0, 8, 8, 14)
            pyxel.text(5, 10, "Regicide", 7)
            pyxel.text(5, 20, "Press the Chapter Number key. ", 7)
            pyxel.text(5, 30, "[1, 2, 3, 4, 5, 6]", 8)
            pyxel.text(5, 45, "Chapter 1: Journey to the Royal Palace", 7)
            pyxel.text(5, 55, "Chapter 2: Exploring the old harbor", 7)
            pyxel.text(5, 65, "Chapter 3: Frontier village", 7)
            pyxel.text(5, 75, "Chapter 4: Royal Magic Institute", 7)
            pyxel.text(5, 85, "Chapter 5: East capital", 7)
            pyxel.text(5, 95, "Chapter 6: Inheritance altar", 7)
        
     else: #Draw player info
        pyxel.rect(130, 2, 32, 18, 0)
        pyxel.rect(131, 2, 67, 16, 1)
        pyxel.blt(135, 20, 0, 40, 0, 8, 8, 14)
        pyxel.blt(135, 30, 0, 40, 8, 8, 8, 14)
        pyxel.blt(135, 40, 0, 32, 8, 8, 8, 14)
        pyxel.text(145, 7, self.sel_chap, 7)
        pyxel.text(150, 22,  str(self.Player.player_h),7)
        pyxel.text(150, 32,  str(self.Player.money),7)
        s = int(self.timer / 30)
        s2 = int(s % 60)
        m = int(s / 60)
        m2 = int(m % 60)
        h = int(m / 60)
        pyxel.text(150, 42,
                     str(h).zfill(2) + ":" 
                   + str(m2).zfill(2) + ":" 
                   + str(s2).zfill(2), 7)
        #pyxel.text(132, 22, str(self.tile_camera_cnx),7)
        #pyxel.text(132, 32, str(self.tile_camera_cny),7)
        
     #Draw movie
     if self.movie_flug == True:
        self.Movie_ctr(self.movie_count)
         
     #Draw gameover text
     if self.game_over == True:
        pyxel.cls(0)
        if self.timer_f == True:
            pyxel.text(20, 30, "GAME OVER!", 7)
        else:
            pyxel.text(20, 30, "THANK YOU FOR PLAYING!!", 7)
        pyxel.text(20, 70, "Q = QUIT(Return to title) ", 7)
        
     #Select lunguage
     if self.lng == "none":
         pyxel.cls(0)
         pyxel.rectb(0, 0 , 200, 128, 1)
         pyxel.text(60, 30, "Select Languge.", 7)
         pyxel.text(80, 70, "J = Japanese ", 7)
         pyxel.text(80, 80, "E = English ", 7)
         
     if self.game_start == False: 
         pass
     else:
         pyxel.rectb(0, 0, 129, 129, 7)
         pyxel.rectb(129, 0, 71, 129, 1)

 
 def Player_ctr(self):
     
     #Get map coordinate
     x = 16*(self.map_count_x-1)
     y = 16*(self.map_count_y-1)

     #Get player coordinate        
     move_map_x = int(self.Player.player_x / 8 + x)
     move_map_y = int(self.Player.player_y / 8 + y)
     print(move_map_x)
     print(move_map_x)
     #Tilemap action
     #HP recovery
     if self.Tile_cnv(move_map_x, move_map_y) == 31:
         self.Player.player_h = 100    
     #Map Event
     if self.Tile_cnv(move_map_x, move_map_y) == 29:
         self.movie_flug = True
         self.movie_count = 254
         self.Movie_ctr(self.movie_count)
     if self.Tile_cnv(move_map_x, move_map_y) == 30:
         self.movie_flug = True
         self.movie_count = 255
         self.Movie_ctr(self.movie_count)
         
     #Status view and pause
     if pyxel.btnp(pyxel.KEY_I):
         self.movie_flug = True
         self.movie_count = 2
     
     #HP Auto recover
     if self.items4[4] == 1:
         if pyxel.frame_count % 120 == 0:
             if self.Player.player_h < 100:
                 self.Player.player_h += 1
     
     #Plyer move
     self.player_move = self.player_move + 1
     if (self.player_move > 6) and (self.atc_flug == False):
         #print(self.Tile_cnv(move_map_x, move_map_y-1))
     
         if self.Tile_cnv(move_map_x, move_map_y-1) < 32:
             #Up
             if pyxel.btn(pyxel.KEY_UP):
                 self.Player.last_p = [self.Player.player_x,
                                       self.Player.player_y]
                 self.Player.player_y = self.Player.player_y - 8
                 self.player_move = 0
                 self.Player.player_m = 2
                 if self.Player.player_m2 == 0: #Move animation
                     self.Player.player_m2 = 1
                 else:
                     self.Player.player_m2 = 0      
                 if (self.Player.player_y - 8) < -8: #When map change
                     self.map_ch_fl = 1
                     self.map_y = self.map_y - 16
                     self.Player.update(self.Player.player_x, 120)
                     self.map_count_y = self.map_count_y - 1
                     self.map_move = 1
                     
         elif self.Tile_cnv(move_map_x, move_map_y-1) >= 224:
             if pyxel.btn(pyxel.KEY_UP):
                self.movie_flug = True
                self.movie_count = self.Tile_cnv(move_map_x,
                                                        move_map_y-1)
                print(self.movie_count) #Debug
     
         if self.Tile_cnv(move_map_x, move_map_y+1) < 32:
             #Down
             if pyxel.btn(pyxel.KEY_DOWN):
                 self.Player.last_p = [self.Player.player_x,
                                       self.Player.player_y]                 
                 self.Player.player_y = self.Player.player_y + 8
                 self.player_move = 0
                 self.Player.player_m = 3     
                 if self.Player.player_m2 == 0: #Move animation
                     self.Player.player_m2 = 1
                 else:
                     self.Player.player_m2 = 0      
                 if (self.Player.player_y + 8) > 128: #When map change
                     self.map_ch_fl = 1
                     self.map_y = self.map_y + 16
                     self.Player.update(self.Player.player_x, 0)
                     self.map_count_y = self.map_count_y + 1
                     self.map_move = 1
                     
         elif self.Tile_cnv(move_map_x, move_map_y+1) >= 224:
             if pyxel.btn(pyxel.KEY_DOWN):
                self.movie_flug = True
                self.movie_count = self.Tile_cnv(move_map_x,
                                                        move_map_y+1)
                print(self.movie_count) #DebugF
             
         if self.Tile_cnv(move_map_x+1, move_map_y) < 32: 
             #Right
             if pyxel.btn(pyxel.KEY_RIGHT):
                 self.Player.last_p = [self.Player.player_x,
                                       self.Player.player_y]                 
                 self.Player.player_x = self.Player.player_x + 8
                 self.player_move = 0
                 self.Player.player_m = 0
                 if self.Player.player_m2 == 0: #Move animation
                     self.Player.player_m2 = 1
                 else:
                     self.Player.player_m2 = 0      
                 if (self.Player.player_x + 8) > 128: #When map change
                     self.map_ch_fl = 1
                     self.map_x = self.map_x + 16
                     self.Player.update(0, self.Player.player_y)
                     self.map_count_x = self.map_count_x + 1
                     self.map_move = 1
                     
         elif self.Tile_cnv(move_map_x+1, move_map_y) >= 224:
             if pyxel.btn(pyxel.KEY_RIGHT):
                self.movie_flug = True
                self.movie_count = self.Tile_cnv(move_map_x+1,
                                                        move_map_y)
                print(self.movie_count) #DebugF
        
         if self.Tile_cnv(move_map_x-1, move_map_y) < 32: 
             #Left
             if pyxel.btn(pyxel.KEY_LEFT):
                 self.Player.last_p = [self.Player.player_x,
                                       self.Player.player_y]                 
                 self.Player.player_x = self.Player.player_x - 8
                 self.player_move = 0
                 if self.Player.player_m2 == 0: #Move animation
                     self.Player.player_m2 = 1
                 else:
                     self.Player.player_m2 = 0      
                 self.Player.player_m = 1
                 if (self.Player.player_x - 8) < -8: #When map change
                     self.map_ch_fl = 1
                     self.map_x = self.map_x - 16
                     self.Player.update(120, self.Player.player_y)
                     self.map_count_x = self.map_count_x - 1
                     self.map_move = 1
                     
         elif self.Tile_cnv(move_map_x-1, move_map_y) >= 224:
             if pyxel.btn(pyxel.KEY_LEFT):
                self.movie_flug = True
                self.movie_count = self.Tile_cnv(move_map_x-1,
                                                        move_map_y)
                print(self.movie_count) #DebugF
            
     #Attack action       
     if pyxel.btnp(pyxel.KEY_SPACE):
         if self.atc_flug == False:
             self.atc_v = 1         
         self.atc_flug = True
     elif pyxel.btnp(pyxel.KEY_V):
         if self.atc_flug == False:
             self.atc_vf = True
             self.atc_v = 2
         self.atc_flug = True
         
     if self.atc_flug == True:
         if self.atc_v == 1:
             if self.Player.weapon == 2:
                 ap = 16
                 at = 0
             elif self.Player.weapon == 1:
                 ap = 8
                 at = 0
             elif self.Player.weapon == 3:
                 ap = 8
                 at = 10    
         elif self.atc_v == 2:
             if self.Player.weapon == 2:
                 if self.atc_vf == True:
                     self.atc_vf = False
                 ap = 24
                 at = 0
             elif self.Player.weapon == 1:
                 if self.Player.last_p[0] == 0 and self.Player.last_p[1] == 0:
                     ap = 8
                     at = 0
                 else:
                     if self.atc_vf == True:
                         self.Player.last_p2 = [self.Player.player_x,
                                                self.Player.player_y]
                         self.atc_vf = False
                     lx = self.Player.last_p[0]
                     ly = self.Player.last_p[1]                    
                     self.Player.player_x = lx
                     self.Player.player_y = ly
                     ap = 8
                     at = 0     
             elif self.Player.weapon == 3:
                 if self.atc_vf == True:
                     self.atc_vf = False
                     if self.Player.player_m == 0:
                         self.Player.player_m = 3
                     elif self.Player.player_m == 1:
                         self.Player.player_m = 2      
                     elif self.Player.player_m == 2:
                         self.Player.player_m = 0
                     elif self.Player.player_m == 3:
                         self.Player.player_m = 1
                 ap = 8
                 at = 5   
                     
         self.atc_count = self.atc_count + 1
         if self.atc_count > 8 + at:
             self.atc_count = 0
             self.p_atc_x = 0
             self.p_atc_y = 0
             self.atc_flug = False
             if self.atc_v == 2:
                 self.Player.last_p = self.Player.last_p2
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
     
     self.timer_f = False
     self.timer = 0
     
     self.sel_chap = ""
     
     #Map status
     self.stage_flug = 1     
     self.map_count_x = 1    
     self.map_count_y = 1    
     self.map_x = 0
     self.map_y = 0
     self.map_move = 0
     self.set_para = 0
     self.set_para2 = 0
     
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
             self.enemys[e].enemy_da += 1
             #Music_ctr
             pyxel.play(1,0,loop=False)
             if self.Player.weapon == 3:
               pa = 2
             else:
               pa = 1
             if self.enemys[e].enemy_v2 == 9:
                 self.enemys[e].enemy_h = self.enemys[e].enemy_h - 100
             else:
                 self.enemys[e].enemy_h = self.enemys[e].enemy_h - pa
             #Enemy delete
         if self.enemys[e].enemy_h < 0:
             if self.enemys[e].enemy_v2==15 or self.enemys[e].enemy_v2==16:
                 self.enemy_ld = False
             if ((self.enemys[e].enemy_v2==6)or(self.enemys[e].enemy_v2==7) or
                 (self.enemys[e].enemy_v2==9)or(self.enemys[e].enemy_v2==11)or
                 (self.enemys[e].enemy_v2==20)or(self.enemys[e].enemy_v2==22)or
                 (self.enemys[e].enemy_v2==25)):
                 m = 0
             else:
                 m = 10 * self.enemys[e].enemy_v2
                 #Music_ctr
                 pyxel.play(2,2,loop=False)
             self.Player.money += m
             if self.enemys[e].enemy_v2 == 18:
                 self.enemys.clear()
             else:
                 del self.enemys[e]

             if len(self.enemys) == 0:
                 x = int(self.map_x / 16)
                 y = int(self.map_y / 16)
                 if ((x == 1 and y == 2) or (x == 10 and y == 0) or
                     (x == 1 and y == 5) or (x == 4 and y == 9) or
                     (x == 0 and y == 9) or (x == 1 and y == 8) or
                     (x == 1 and y == 5) or (x == 3 and y == 14) or
                     (x == 14 and y == 3)or (x == 6 and y == 6) or
                     (x == 13 and y == 9) or (x == 14 and y == 2) or
                     (x == 1 and y == 3)):
                     self.MapEvents_ctr(x, y)
                     self.Event_save = False
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
                  pyxel.clip()
                  pyxel.load('assets/pknights.pyxres') #Map reset
     

 def Enemy_ctr(self):        
     #new_enemy_w = []
     enemy_count = len(self.enemys)
     for e in range(enemy_count):
         self.enemys[e].enemy_m2 = self.enemys[e].enemy_m2 + 1
         if self.enemys[e].enemy_v2 == 4 or self.enemys[e].enemy_v2 == 5:
             vm2 = randint(40, 180) 
             vm = 0
         elif self.enemys[e].enemy_v2 == 6 or self.enemys[e].enemy_v2 == 7:
             vm2 = 0
             vm = 30         
         elif self.enemys[e].enemy_v2 == 10:
             vm2 = 0
             vm = 30          
         elif self.enemys[e].enemy_v2 == 8:
             vm2 = vm2 = randint(1, 100) 
             vm = 0          
         elif self.enemys[e].enemy_v2 == 9 or self.enemys[e].enemy_v2 == 25:
             vm2 = 0
             vm = 44         
         elif self.enemys[e].enemy_v2 == 12:
             vm2 = 0
             vm = 5         
         elif self.enemys[e].enemy_v2 == 14:
             vm2 = 15
             vm = 0         
         elif self.enemys[e].enemy_v2 == 19:
             vm2 = 0
             vm = 30       
         elif self.enemys[e].enemy_v2 == 21:
             vm2 = 0
             vm = 25
         elif self.enemys[e].enemy_v2 == 23:
             vm2 = 15
             vm = 0            
         elif self.enemys[e].enemy_v2 == 24:
             if self.enemys[e].enemy_v == 64:
                 vm2 = 0
                 vm = 18     
             else:
                 vm2 = 0
                 vm = 22             
         elif self.enemys[e].enemy_v2 == 15 or self.enemys[e].enemy_v2 == 16:
             vm2 = 0
             vm = 0  
             if self.enemy_ld == False:
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 100
         elif self.enemys[e].enemy_v2 == 17:
             if self.enemy_ld == False:
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 100
         elif self.enemys[e].enemy_v2 == 18:
             vm2 = 30
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
             
             #Normal enemy////////////////////////////////////////////////////
             if self.enemys[e].enemy_v2 < 4:  
                 #Check tilemap
                 if (abs(enemy_pos_x2) < 35 and abs(enemy_pos_y2) < 35):
                     if abs(enemy_pos_x2) > abs(enemy_pos_y2):
                         #Move right
                         if enemy_pos_x2 > 0:
                             if (40> (self.Tile_cnv(enemy_pos_x+1, 
                                                         enemy_pos_y)) < 32):
                                 self.enemys[e].enemy_x = \
                                     self.enemys[e].enemy_x + 8
                                 self.enemys[e].enemy_m = 1
                         #Move left
                         else:
                             if (40> (self.Tile_cnv(enemy_pos_x-1, 
                                                         enemy_pos_y)) < 32):
                                 self.enemys[e].enemy_x = \
                                     self.enemys[e].enemy_x-8
                                 self.enemys[e].enemy_m = 0           
                     elif abs(enemy_pos_x2) == abs(enemy_pos_y2):
                         m = randint(1, 2)
                         if m == 1:
                             #Move right
                             if enemy_pos_x2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x+1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x + 8
                                     self.enemys[e].enemy_m = 1
                             #Move left
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x-1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x-8
                                     self.enemys[e].enemy_m = 0                 
                         else:
                             #Move down
                             if enemy_pos_y2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y+8
                             #Move up
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y-8                                 
                     else:
                         #Move down
                         if enemy_pos_y2 > 0:
                             if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                                 self.enemys[e].enemy_y = \
                                     self.enemys[e].enemy_y+8
                         #Move up
                         else:
                             if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                                 self.enemys[e].enemy_y = \
                                     self.enemys[e].enemy_y-8
             #////////////////////////////////////////////////////////////////
                                    
             #Crossbow////////////////////////////////////////////////////////
             elif self.enemys[e].enemy_v2 == 4:
                 if enemy_pos_y2 > 0:
                     self.enemys[e].enemy_m = 0
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y+8, 
                                        self.enemys[e].enemy_v, 6)
                     new_enemy.enemy_m = 1
                     new_enemy.enemy_h = 6
                     #new_enemy_w.append(new_enemy)
                     self.enemys.append(new_enemy)
                 else:
                     self.enemys[e].enemy_m = 1
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y-8, 
                                        self.enemys[e].enemy_v, 6)
                     new_enemy.enemy_m = 0
                     new_enemy.enemy_h = 6
                     #new_enemy_w.append(new_enemy)
                     self.enemys.append(new_enemy)
             
             elif self.enemys[e].enemy_v2 == 6:
                 if self.enemys[e].enemy_m == 1:
                     self.enemys[e].enemy_y = self.enemys[e].enemy_y + 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
                     
                 else:
                     self.enemys[e].enemy_y = self.enemys[e].enemy_y - 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
                     
             elif self.enemys[e].enemy_v2 == 5:
                 if enemy_pos_x2 > 0:
                     self.enemys[e].enemy_m = 0
                     new_enemy = Enemy(self.enemys[e].enemy_x+8, 
                                        self.enemys[e].enemy_y, 
                                        self.enemys[e].enemy_v, 7)
                     new_enemy.enemy_m = 1
                     new_enemy.enemy_h = 6
                     #new_enemy_w.append(new_enemy)
                     self.enemys.append(new_enemy)
                 else:
                     self.enemys[e].enemy_m = 1
                     new_enemy = Enemy(self.enemys[e].enemy_x-8, 
                                        self.enemys[e].enemy_y, 
                                        self.enemys[e].enemy_v, 7)
                     new_enemy.enemy_m = 0
                     new_enemy.enemy_h = 6
                     #new_enemy_w.append(new_enemy)
                     self.enemys.append(new_enemy)
             
             elif self.enemys[e].enemy_v2 == 7:
                 if self.enemys[e].enemy_m == 1:
                     self.enemys[e].enemy_x = self.enemys[e].enemy_x + 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
                     
                 else:
                     self.enemys[e].enemy_x = self.enemys[e].enemy_x - 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
            #/////////////////////////////////////////////////////////////////
                     
            #Knif/////////////////////////////////////////////////////////////
             elif self.enemys[e].enemy_v2 == 8:
                 if self.enemys[e].enemy_h > 200:
                     self.enemys[e].enemy_m = 1
                     self.enemys[e].enemy_x = 2*8
                     self.enemys[e].enemy_y = 8*8
                     new_enemy = Enemy(self.enemys[e].enemy_x+8, 
                                        self.enemys[e].enemy_y, 96, 9)
                     new_enemy.enemy_m = 1
                     new_enemy.enemy_h = 12
                     self.enemys.append(new_enemy)
                 elif self.enemys[e].enemy_h > 150:
                     self.enemys[e].enemy_m = 0
                     self.enemys[e].enemy_x = 14*8
                     self.enemys[e].enemy_y = 8*8
                     #n = randint(-1, 1)
                     for f in range(2):
                         n = randint(-1, 1)
                         new_enemy = Enemy(self.enemys[e].enemy_x-8, 
                                        self.enemys[e].enemy_y+(n*8), 96, 9)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 12
                         self.enemys.append(new_enemy)
                 elif self.enemys[e].enemy_h > 100:
                     self.enemys[e].enemy_m = 1
                     self.enemys[e].enemy_x = 2*8
                     self.enemys[e].enemy_y = 8*8
                     #n = randint(-1, 1)
                     for f in range(2):
                         n = randint(-1, 1)
                         n2 = randint(-1, 2)
                         new_enemy = Enemy(self.enemys[e].enemy_x+(8*n2), 
                                        self.enemys[e].enemy_y+(n*8), 96, 9)
                         new_enemy.enemy_m = 1
                         new_enemy.enemy_h = 12
                         self.enemys.append(new_enemy)
                 else:
                     m = randint(-1, 1)
                     m2 = randint(1, 2)
                     if m2 == 1:
                         self.enemys[e].enemy_m = 1
                         self.enemys[e].enemy_y = (8+m)*8
                         self.enemys[e].enemy_x = 2*8
                     else:
                         self.enemys[e].enemy_m = 0
                         self.enemys[e].enemy_y = (8+m)*8
                         self.enemys[e].enemy_x = 14*8
                     #n = randint(-1, 1)
                     for f in range(3):
                         if m2 == 1:
                             n = randint(-1, 1)
                             n2 = randint(-1, 2)
                             new_enemy = Enemy(self.enemys[e].enemy_x+(8*n2), 
                                        self.enemys[e].enemy_y+(n*8), 96, 9)
                             new_enemy.enemy_m = 1
                             new_enemy.enemy_h = 12
                             self.enemys.append(new_enemy)
                         else:
                             n = randint(-1, 1)
                             n2 = randint(-1, 2)
                             new_enemy = Enemy(self.enemys[e].enemy_x+(-8*n2), 
                                        self.enemys[e].enemy_y+(n*8), 96, 9)
                             new_enemy.enemy_m = 0
                             new_enemy.enemy_h = 12
                             self.enemys.append(new_enemy)
             
             elif self.enemys[e].enemy_v2 == 9:
                 if self.enemys[e].enemy_m == 1:
                     self.enemys[e].enemy_x = self.enemys[e].enemy_x + 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
                     
                 else:
                     self.enemys[e].enemy_x = self.enemys[e].enemy_x - 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
             
             elif self.enemys[e].enemy_v2 == 25:
                 if self.enemys[e].enemy_m == 1:
                     self.enemys[e].enemy_y = self.enemys[e].enemy_y + 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
                     
                 else:
                     self.enemys[e].enemy_y = self.enemys[e].enemy_y - 8
                     self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1                     
            #/////////////////////////////////////////////////////////////////
    
            #Area2 Boss///////////////////////////////////////////////////////
             elif self.enemys[e].enemy_v2 == 10:  
                 #Check tilemap
                 if (abs(enemy_pos_x2) < 100 and abs(enemy_pos_y2) < 100):
                     print(abs(enemy_pos_x2))
                     print(abs(enemy_pos_y2))
                     if abs(enemy_pos_x2) < 10 and abs(enemy_pos_y2) < 10:
                         self.enemys[e].enemy_m = 1
                         #v = randint(1, 2)
                         v = 1
                         if v == 1:
                             for a in range(4):
                                 if a == 0:
                                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                            self.enemys[e].enemy_y-8, 96, 11)
                                 elif a == 1:
                                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                            self.enemys[e].enemy_y+8, 96, 11)
                                 elif a == 2:
                                     new_enemy=Enemy(self.enemys[e].enemy_x+8, 
                                            self.enemys[e].enemy_y, 96, 11)
                                 elif a == 3:
                                     new_enemy=Enemy(self.enemys[e].enemy_x-8, 
                                            self.enemys[e].enemy_y, 96, 11)
                                 if a == 2:
                                     new_enemy.enemy_m = 1
                                 else:
                                     new_enemy.enemy_m = 0
                                 new_enemy.enemy_h = 12
                                 self.enemys.append(new_enemy)
                         elif v == 2:
                             for a in range(4):
                                 if a == 0:
                                     new_enemy=Enemy(self.enemys[e].enemy_x+8, 
                                            self.enemys[e].enemy_y-8, 96, 11)
                                 elif a == 1:
                                     new_enemy=Enemy(self.enemys[e].enemy_x-8, 
                                            self.enemys[e].enemy_y-8, 96, 11)
                                 elif a == 2:
                                     new_enemy=Enemy(self.enemys[e].enemy_x+8, 
                                            self.enemys[e].enemy_y+8, 96, 11)
                                 elif a == 3:
                                     new_enemy=Enemy(self.enemys[e].enemy_x-8, 
                                            self.enemys[e].enemy_y+8, 96, 11)
                                 new_enemy.enemy_m = 0
                                 new_enemy.enemy_h = 26
                                 self.enemys.append(new_enemy)
                     elif abs(enemy_pos_x2) > abs(enemy_pos_y2):
                         self.enemys[e].enemy_m = 0
                         #Move right
                         if enemy_pos_x2 > 0:
                             if (40> (self.Tile_cnv(enemy_pos_x+1, 
                                                         enemy_pos_y)) < 32):
                                 self.enemys[e].enemy_x = \
                                     self.enemys[e].enemy_x + 8
                         #Move left
                         else:
                             if (40> (self.Tile_cnv(enemy_pos_x-1, 
                                                         enemy_pos_y)) < 32):
                                 self.enemys[e].enemy_x = \
                                     self.enemys[e].enemy_x-8
                     else:
                         self.enemys[e].enemy_m = 0
                         #Move down
                         if enemy_pos_y2 > 0:
                             if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                                 self.enemys[e].enemy_y = \
                                     self.enemys[e].enemy_y+8
                         #Move up
                         else:
                             if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                                 self.enemys[e].enemy_y = \
                                     self.enemys[e].enemy_y-8
             elif self.enemys[e].enemy_v2 == 11:
                 self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1
             #////////////////////////////////////////////////////////////////
                 
             #Normal + knif///////////////////////////////////////////////////
             elif self.enemys[e].enemy_v2 == 12:  
                 a = randint(0, 2)
                 b = randint(1, 4)

                 if abs(enemy_pos_y2) <= (6 + b):
                     if enemy_pos_x2 > 0:
                         p = 1
                         q = 9
                         self.enemys[e].enemy_m = 1
                     else:
                         p = 0
                         q = 9
                         self.enemys[e].enemy_m = 0
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y, 
                                        self.enemys[e].enemy_v, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 9
                     self.enemys.append(new_enemy)
                 elif abs(enemy_pos_x2)<=(6+b) and self.enemys[e].enemy_v==128:
                     if enemy_pos_y2 > 0:
                         p = 1
                         q = 6
                         self.enemys[e].enemy_m = 1
                     else:
                         p = 0
                         q = 6
                         self.enemys[e].enemy_m = 0
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y, 
                                        144, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 3
                     self.enemys.append(new_enemy)

                 else:
                     #Check tilemap
                     if (abs(enemy_pos_x2) < 45 and abs(enemy_pos_y2) < 45):
                         if abs(enemy_pos_y2) > abs(enemy_pos_x2):
                             #Move down
                             if enemy_pos_y2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y+8
                             #Move up
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y-8
                         else:
                             #Move right
                             if enemy_pos_x2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x+1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x + 8
                                     self.enemys[e].enemy_m = 1
                             #Move left
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x-1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x-8
                                     self.enemys[e].enemy_m = 0           
             #////////////////////////////////////////////////////////////////
                     
             #Area3 Boss//////////////////////////////////////////////////////
             elif self.enemys[e].enemy_v2 == 14:  
                 a = randint(0, 2)
                 if (abs(enemy_pos_y2) <= 16 and 
                    (abs(enemy_pos_x2) > abs(enemy_pos_y2))):
                     if enemy_pos_x2 > 0:
                         p = 1
                         q = 9
                         x2 = 8
                         self.enemys[e].enemy_m = 1
                     else:
                         p = 0
                         q = 9
                         x2 = -8
                         self.enemys[e].enemy_m = 0
                         
                     self.enemys[e].enemy_m = 1
                         
                     new_enemy = Enemy(self.enemys[e].enemy_x+x2, 
                                        self.enemys[e].enemy_y, 112, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 9
                     self.enemys.append(new_enemy)
                     
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y+8, 112, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 9
                     self.enemys.append(new_enemy)
                     
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y-8, 112, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 9
                     self.enemys.append(new_enemy)
                     
                 else:
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y+8, 112, 6)
                     new_enemy.enemy_m = 1
                     new_enemy.enemy_h = 4
                     self.enemys.append(new_enemy)
                     self.enemys[e].enemy_m = 1

                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y-8, 112, 6)
                     new_enemy.enemy_m = 0
                     new_enemy.enemy_h = 4
                     self.enemys.append(new_enemy)                     
                     #Check tilemap
                     if (abs(enemy_pos_x2) < 45 and abs(enemy_pos_y2) < 45):
                         if abs(enemy_pos_y2) > abs(enemy_pos_x2):
                             #Move down
                             if enemy_pos_y2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y+8
                             #Move up
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y-8
                         else:
                             #Move right
                             if enemy_pos_x2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x+1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x + 8
                             #Move left
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x-1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x-8
                
                 if self.enemys[e].enemy_da > 10:
                     self.enemys[e].enemy_da = 0
                     p = randint(1, 4)
                     if p == 1:
                         self.enemys[e].enemy_x = 1*8
                         self.enemys[e].enemy_y = 3*8
                     elif p == 2:
                         self.enemys[e].enemy_x = 1*8
                         self.enemys[e].enemy_y = 12*8
                     elif p == 3:
                         self.enemys[e].enemy_x = 10*8
                         self.enemys[e].enemy_y = 2*8
                     elif p == 4:
                         self.enemys[e].enemy_x = 12*8
                         self.enemys[e].enemy_y = 11*8
             #////////////////////////////////////////////////////////////////
                         
             #IKA////////////////////////////////////////////////////
             elif self.enemys[e].enemy_v2==15 or self.enemys[e].enemy_v2==16:  
                 
                 if (abs(enemy_pos_x2) < 150 and abs(enemy_pos_y2) < 150):
                     if abs(enemy_pos_x2) > abs(enemy_pos_y2):
                         #Move right
                         if enemy_pos_x2 > 0:
                             a1 = self.enemys[e].enemy_v2
                             a2 = self.enemys[e].enemy_m
                             if a1 == 15 and a2 == 0:
                                 nm1 = 128
                                 nm2 = 0
                             elif a1 == 15 and a2 == 1:
                                 nm1 = 96
                                 nm2 = 1
                             else:
                                 nm1 = 112
                                 nm2 = 1
                             new_enemy = Enemy(self.enemys[e].enemy_x, 
                             self.enemys[e].enemy_y, nm1, 17)
                             new_enemy.enemy_m = nm2
                             new_enemy.enemy_h = 20
                             self.enemys.append(new_enemy)                
                             self.enemys[e].enemy_x = \
                                 self.enemys[e].enemy_x + 8
                             self.enemys[e].enemy_v2 = 16
                             self.enemys[e].enemy_m = 1
                         #Move left
                         else:
                             a1 = self.enemys[e].enemy_v2
                             a2 = self.enemys[e].enemy_m
                             if a1 == 15 and a2 == 0:
                                 nm1 = 128
                                 nm2 = 1
                             elif a1 == 15 and a2 == 1:
                                 nm1 = 96
                                 nm2 = 0
                             else:
                                 nm1 = 112
                                 nm2 = 1                             
                             new_enemy = Enemy(self.enemys[e].enemy_x, 
                             self.enemys[e].enemy_y, nm1, 17)
                             new_enemy.enemy_m = nm2
                             new_enemy.enemy_h = 20
                             self.enemys.append(new_enemy)       
                             self.enemys[e].enemy_x = \
                                 self.enemys[e].enemy_x-8
                             self.enemys[e].enemy_v2 = 16
                             self.enemys[e].enemy_m = 0           
                     else:
                         #Move down
                         if enemy_pos_y2 > 0:
                             a1 = self.enemys[e].enemy_v2
                             a2 = self.enemys[e].enemy_m
                             if a1 == 16 and a2 == 0:
                                 nm1 = 128
                                 nm2 = 0
                             elif a1 == 16 and a2 == 1:
                                 nm1 = 128
                                 nm2 = 1
                             else:
                                 nm1 = 112
                                 nm2 = 0                             
                             new_enemy = Enemy(self.enemys[e].enemy_x, 
                             self.enemys[e].enemy_y, nm1, 17)
                             new_enemy.enemy_m = nm2
                             new_enemy.enemy_h = 20
                             self.enemys.append(new_enemy)       
                             self.enemys[e].enemy_y = \
                                 self.enemys[e].enemy_y+8
                             self.enemys[e].enemy_v2 = 15
                             self.enemys[e].enemy_m = 1
                         #Move up
                         else:
                             a1 = self.enemys[e].enemy_v2
                             a2 = self.enemys[e].enemy_m
                             if a1 == 16 and a2 == 0:
                                 nm1 = 96
                                 nm2 = 1
                             elif a1 == 16 and a2 == 1:
                                 nm1 = 96
                                 nm2 = 0
                             else:
                                 nm1 = 112
                                 nm2 = 0                             
                             new_enemy = Enemy(self.enemys[e].enemy_x, 
                             self.enemys[e].enemy_y, nm1, 17)
                             new_enemy.enemy_m = nm2
                             new_enemy.enemy_h = 20
                             self.enemys.append(new_enemy)       
                             self.enemys[e].enemy_y = \
                                 self.enemys[e].enemy_y-8
                             self.enemys[e].enemy_v2 = 15
                             self.enemys[e].enemy_m = 0
                                 
             elif self.enemys[e].enemy_v2 == 17:
                 pass
                     
             elif self.enemys[e].enemy_v2 == 18:
                 if self.e_atk_flug == False:
                     print(self.e_atk_count)
                     self.e_atk_count = self.e_atk_count + 1
                     if self.enemy_ld == False and self.e_atk_count < 4:
                         new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y + 8, 
                                        self.enemys[e].enemy_v, 6)
                         new_enemy.enemy_m = 1
                         new_enemy.enemy_h = 6
                         self.enemys.append(new_enemy)
                     elif self.e_atk_count > 3:
                         self.e_atk_flug = True
                         self.enemy_ld = True
                         self.e_atk_count = 0
                 
                 else:
                     a = randint(1, 3)
                     if a == 1:
                         new_enemy = Enemy(4*8, 4*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)    
                         
                         new_enemy = Enemy(11*8, 2*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)       
                         
                         new_enemy = Enemy(3*8, 6*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)                                

                         new_enemy = Enemy(12*8, 6*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)           
                         
                         self.enemy_ld = True
                         self.e_atk_flug = False
                     elif a == 2:
                         new_enemy = Enemy(3*8, 5*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)    
                         
                         new_enemy = Enemy(10*8, 4*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)       
                         
                         new_enemy = Enemy(5*8, 7*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)                 
                         
                         new_enemy = Enemy(8*8, 7*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)                                    
                         
                         self.enemy_ld = True
                         self.e_atk_flug = False
                     elif a == 3:
                         new_enemy = Enemy(3*8, 2*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)    
                         
                         new_enemy = Enemy(12*8, 5*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)       
                         
                         new_enemy = Enemy(10*8, 4*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)               
                         
                         new_enemy = Enemy(2*8, 7*8, 112, 15)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 20
                         self.enemys.append(new_enemy)                                    
                         
                         self.enemy_ld = True
                         self.e_atk_flug = False
                         
             #////////////////////////////////////////////////////////////////
                         
             #Kenshi///////////////////////////////////////////////////
             elif self.enemys[e].enemy_v2 == 19:  
                 a = randint(0, 2)
                 b = randint(1, 3)
                 if abs(enemy_pos_y2) <= (5 + b) and abs(enemy_pos_x2) <= 8:
                     if enemy_pos_x2 > 0:
                         p = 0
                         q = 20
                         self.enemys[e].enemy_m = 0
                         x = self.enemys[e].enemy_x + 8
                     else:
                         p = 1
                         q = 20
                         self.enemys[e].enemy_m = 1
                         x = self.enemys[e].enemy_x - 8
                     new_enemy = Enemy(x, self.enemys[e].enemy_y, 128, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 9
                     self.enemys.append(new_enemy)
                 else:
                     #Check tilemap
                     if (abs(enemy_pos_x2) < 45 and abs(enemy_pos_y2) < 45):
                         if abs(enemy_pos_y2) > abs(enemy_pos_x2):
                             #Move down
                             if enemy_pos_y2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y+8
                             #Move up
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y-8
                         else:
                             #Move right
                             if enemy_pos_x2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x+1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x + 8
                                     self.enemys[e].enemy_m = 0
                             #Move left
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x-1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x-8
                                     self.enemys[e].enemy_m = 1           
             
             elif self.enemys[e].enemy_v2 == 20:
                 self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1    
                                                          
             #////////////////////////////////////////////////////////////////                    
                 
             #AREA4 BOSS///////////////////////////////////////////////////
             elif self.enemys[e].enemy_v2 == 21:  
                 
                 if self.enemys[e].enemy_h < 150:
                     f1 = randint(1, 10)
                     f2 = randint(1, 10)
                     if f1 == f2:
                         x = 32
                         new_enemy = Enemy(x, 48, 128, 23)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 5
                         self.enemys.append(new_enemy)
                         x = 88
                         new_enemy = Enemy(x, 48, 128, 23)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 4
                         self.enemys.append(new_enemy)
                              
                 a = randint(0, 2)
                 b = randint(1, 5)
                 b2 = randint(1, 3)
                 if abs(enemy_pos_y2) <= (5 + b) and abs(enemy_pos_x2) <= 8:
                     if enemy_pos_x2 > 0:
                         p = 0
                         q = 22
                         self.enemys[e].enemy_m = 0
                         x = self.enemys[e].enemy_x + 8
                     else:
                         p = 1
                         q = 22
                         self.enemys[e].enemy_m = 1
                         x = self.enemys[e].enemy_x - 8
                     new_enemy = Enemy(x, self.enemys[e].enemy_y, 128, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 9
                     self.enemys.append(new_enemy)
                 elif abs(enemy_pos_y2) <= (6 + b) and b2 == 1:
                     if enemy_pos_x2 > 0:
                         p = 1
                         q = 9
                         self.enemys[e].enemy_m = 0
                     else:
                         p = 0
                         q = 9
                         self.enemys[e].enemy_m = 1
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y, 
                                        self.enemys[e].enemy_v, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 9
                     self.enemys.append(new_enemy)
                 elif abs(enemy_pos_x2) <= (6 + b) and b2 == 1:
                     if enemy_pos_y2 > 0:
                         p = 1
                         q = 6
                         self.enemys[e].enemy_m = 1
                     else:
                         p = 0
                         q = 6
                         self.enemys[e].enemy_m = 0
                     new_enemy = Enemy(self.enemys[e].enemy_x, 
                                        self.enemys[e].enemy_y, 
                                        144, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 3
                     self.enemys.append(new_enemy)                     
                 else:
                     #Check tilemap
                     if (abs(enemy_pos_x2) < 45 and abs(enemy_pos_y2) < 45):
                         if abs(enemy_pos_y2) > abs(enemy_pos_x2):
                             #Move down
                             if enemy_pos_y2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y+8
                             #Move up
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y-8
                         else:
                             #Move right
                             if enemy_pos_x2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x+1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x + 8
                                     self.enemys[e].enemy_m = 0
                             #Move left
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x-1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x-8
                                     self.enemys[e].enemy_m = 1           
             
             elif self.enemys[e].enemy_v2 == 22:
                 self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1    
                                                          
             elif self.enemys[e].enemy_v2 == 23:  
                 #Check tilemap
                 self.enemys[e].enemy_h = self.enemys[e].enemy_h - 1   
                 if (abs(enemy_pos_x2) < 128 and abs(enemy_pos_y2) < 128):
                     if abs(enemy_pos_x2) > abs(enemy_pos_y2):
                         #Move right
                         if enemy_pos_x2 > 0:
                             self.enemys[e].enemy_x = \
                                     self.enemys[e].enemy_x + 8
                             self.enemys[e].enemy_m = 1
                         #Move left
                         else:
                             self.enemys[e].enemy_x = \
                                     self.enemys[e].enemy_x-8
                             self.enemys[e].enemy_m = 0           
                     else:
                         #Move down
                         if enemy_pos_y2 > 0:
                             self.enemys[e].enemy_y = \
                                     self.enemys[e].enemy_y+8
                         #Move up
                         else:
                             self.enemys[e].enemy_y = \
                                     self.enemys[e].enemy_y-8                 
             #////////////////////////////////////////////////////////////////  
             #AREA5 BOSS//////////////////////////////////////////////////////
             elif self.enemys[e].enemy_v2 == 24:         
                 
                 self.enemys[e].enemy_da += 1 
                 t = randint(1, 10)
                 
                 if self.enemys[e].enemy_h < 200:
                     tt = 35
                 else:
                     tt = 70
                 
                 ev = self.enemys[e].enemy_v
                 print(ev)
                 
                 if ((self.enemys[e].enemy_da) > tt + t and
                    (abs(enemy_pos_y2) <= 24) and (abs(enemy_pos_x2) <= 24)):
                 
                     self.enemys[e].enemy_da = 0
                     x = self.enemys[e].enemy_x - 16
                     y = self.enemys[e].enemy_y + 40
                     for i in range(5):
                         new_enemy = Enemy(x + (i * 8), y, ev, 6)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 5
                         self.enemys.append(new_enemy)         
                     x = self.enemys[e].enemy_x - 16
                     y = self.enemys[e].enemy_y - 40
                     for i in range(5):
                         new_enemy = Enemy(x + (i * 8), y, ev, 6)
                         new_enemy.enemy_m = 1
                         new_enemy.enemy_h = 5
                         self.enemys.append(new_enemy)      
                     x = self.enemys[e].enemy_x + 40
                     y = self.enemys[e].enemy_y - 16
                     for i in range(5):
                         new_enemy = Enemy(x, y + (i * 8), ev, 7)
                         new_enemy.enemy_m = 0
                         new_enemy.enemy_h = 5
                         self.enemys.append(new_enemy)         
                     x = self.enemys[e].enemy_x - 40
                     y = self.enemys[e].enemy_y - 16
                     for i in range(5):
                         new_enemy = Enemy(x, y + (i * 8), ev, 7)
                         new_enemy.enemy_m = 1
                         new_enemy.enemy_h = 5
                         self.enemys.append(new_enemy)      
                         
                 
                 a = randint(0, 2)
                 b = randint(1, 5)
                 b2 = randint(1, 3)
                 if abs(enemy_pos_y2) <= 8 and abs(enemy_pos_x2) >= 32:
                     if enemy_pos_x2 > 0:
                         p = 1
                         q = 9
                         self.enemys[e].enemy_m = 0
                         x = self.enemys[e].enemy_x + 8
                         y = self.enemys[e].enemy_y 
                     else:
                         p = 0
                         q = 9
                         self.enemys[e].enemy_m = 1
                         x = self.enemys[e].enemy_x - 8
                         y = self.enemys[e].enemy_y
                     new_enemy = Enemy(x, y, ev, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 9
                     self.enemys.append(new_enemy)                                                    
                 elif abs(enemy_pos_x2) <= 8 and abs(enemy_pos_y2) >= 32:
                     if enemy_pos_y2 > 0:
                         p = 1
                         q = 25
                         self.enemys[e].enemy_m = 0
                         y = self.enemys[e].enemy_y + 8
                         x = self.enemys[e].enemy_x 
                     else:
                         p = 0
                         q = 25
                         self.enemys[e].enemy_m = 1
                         y = self.enemys[e].enemy_y - 8
                         x = self.enemys[e].enemy_x
                     new_enemy = Enemy(x, y, ev, q)
                     new_enemy.enemy_m = p
                     new_enemy.enemy_h = 9
                     self.enemys.append(new_enemy)                                                          
                 elif abs(enemy_pos_y2) <= (5 + b) and abs(enemy_pos_x2) <= 8:
                     if enemy_pos_x2 > 0:
                         p = randint(0, 1)
                         q = 22
                         self.enemys[e].enemy_m = 0
                         x = self.enemys[e].enemy_x + 8
                         y = self.enemys[e].enemy_y - 8
                     else:
                         p = randint(0, 1)
                         q = 22
                         self.enemys[e].enemy_m = 1
                         x = self.enemys[e].enemy_x - 8
                         y = self.enemys[e].enemy_y - 8
                     for i in range(3):
                         pp = 0
                         if self.enemys[e].enemy_h < 200:
                             if i == 0 or i == 2:
                                 if self.enemys[e].enemy_m == 0:
                                     pp = 8
                                 else:
                                     pp = -8
                             else:
                                 pp = 0
                         new_enemy = Enemy(x+pp, y + (8 * i), ev, q)
                         new_enemy.enemy_m = p
                         new_enemy.enemy_h = 9
                         self.enemys.append(new_enemy)        
                 elif abs(enemy_pos_y2) <= 8 and abs(enemy_pos_x2) <= (5 + b):
                     if enemy_pos_y2 > 0:
                         p = randint(0, 1)
                         q = 22
                         self.enemys[e].enemy_m = 0
                         y = self.enemys[e].enemy_y + 8
                         x = self.enemys[e].enemy_x - 8
                     else:
                         p = randint(0, 1)
                         q = 22
                         self.enemys[e].enemy_m = 1
                         y = self.enemys[e].enemy_y - 8
                         x = self.enemys[e].enemy_x - 8
                     for i in range(3):
                         pp = 0
                         if self.enemys[e].enemy_h < 200:                         
                             if i == 0 or i == 2:
                                 if self.enemys[e].enemy_m == 0:
                                     pp = 8
                                 else:
                                     pp = -8
                             else:
                                 pp = 0                         
                         new_enemy = Enemy(x + (8 * i), y+pp, ev, q)
                         new_enemy.enemy_m = p
                         new_enemy.enemy_h = 9
                         self.enemys.append(new_enemy)                                 
                 else:
                     #Check tilemap
                     if (abs(enemy_pos_x2) < 45 and abs(enemy_pos_y2) < 45):
                         if abs(enemy_pos_y2) > abs(enemy_pos_x2):
                             #Move down
                             if enemy_pos_y2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y+1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y+8
                             #Move up
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x, 
                                                       enemy_pos_y-1)) < 32):
                                     self.enemys[e].enemy_y = \
                                         self.enemys[e].enemy_y-8
                         else:
                             #Move right
                             if enemy_pos_x2 > 0:
                                 if (40> (self.Tile_cnv(enemy_pos_x+1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x + 8
                                     self.enemys[e].enemy_m = 0
                             #Move left
                             else:
                                 if (40> (self.Tile_cnv(enemy_pos_x-1, 
                                                         enemy_pos_y)) < 32):
                                     self.enemys[e].enemy_x = \
                                         self.enemys[e].enemy_x-8
                                     self.enemys[e].enemy_m = 1                               


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
         self.Tile_cnv_set(7+16, 10+32, ["006006"]) 
     elif xy_key == "0-41":
         self.Tile_cnv_set(7+0, 2+64, ["014014"]) 
         self.Tile_cnv_set(7+0, 3+64, ["14C14D"]) 
         self.Tile_cnv_set(8+16, 7+128, ["155"]) 
         self.Tile_cnv_set(8+16, 8+128, ["155"]) 
         self.Tile_cnv_set(8+16, 9+128, ["155"]) 
         self.Tile_cnv_set(4+32, 12+96, ["005"]) 
     elif xy_key == "0-4":
         self.Tile_cnv_set(6+0, 8+64, ["006006006"]) 
         self.Tile_cnv_set(5+0, 9+64, ["006006006006006"]) 
         self.Tile_cnv_set(5+0, 10+64, ["006006006006006"]) 
     elif xy_key == "0-1":
         self.Tile_cnv_set(7+0, 12+16, ["006006"]) 
     elif xy_key == "0-10":
         self.Tile_cnv_set(13+160, 9, ["005005"]) 
         self.Tile_cnv_set(13+160, 12, ["027027"]) 
         self.Tile_cnv_set(1+160, 7, ["027"]) 
         self.Tile_cnv_set(1+160, 8, ["027"]) 
     elif xy_key == "0-101":
         self.Tile_cnv_set(11+160, 8, ["005"]) 
         self.Tile_cnv_set(11+160, 7, ["005"]) 
     elif xy_key == "0-3":
         self.Tile_cnv_set(13+0, 10+48, ["044"]) 
     elif xy_key == "1-3":         
         self.Tile_cnv_set(7+16, 15+48, ["006"]) 
         self.Tile_cnv_set(7+16, 0+64, ["006"])          
         self.Tile_cnv_set(11+16, 7+64, ["006"])        
         self.Tile_cnv_set(11+16, 8+64, ["006"])        
     elif xy_key == "1-31":
         self.Tile_cnv_set(12+16, 12+48, ["0F1"]) 
         self.Tile_cnv_set(14+16, 7+48, ["006"]) 
         self.Tile_cnv_set(14+16, 8+48, ["006"]) 
     elif xy_key == "1-32":
         self.Tile_cnv_set(3+16, 1+48, ["0F2"]) 
         self.Tile_cnv_set(12+16, 7+48, ["006"]) 
         self.Tile_cnv_set(12+16, 8+48, ["006"]) 
     elif xy_key == "1-33":
         self.Tile_cnv_set(13+16, 5+48, ["0F3"]) 
         self.Tile_cnv_set(13+16, 7+48, ["006"]) 
         self.Tile_cnv_set(13+16, 8+48, ["006"]) 
     elif xy_key == "2-2":
         self.Tile_cnv_set(2+32, 7+32, ["006"]) 
         self.Tile_cnv_set(2+32, 8+32, ["006"]) 
     elif xy_key == "2-22":
         self.Tile_cnv_set(7+32, 14+32, ["00F00F"]) 
         self.Tile_cnv_set(7+32, 15+32, ["00F00F"]) 
     elif xy_key == "2-3":
         self.Tile_cnv_set(14+32, 13+48, ["021"]) 
         self.Tile_cnv_set(14+32, 12+48, ["021"]) 
         self.Tile_cnv_set(8+32, 2+48, ["0F7"]) 
     elif xy_key == "6-2":
         self.Tile_cnv_set(3+96, 7+32, ["011"]) 
         self.Tile_cnv_set(3+96, 8+32, ["011"])
     elif xy_key == "7-7":
         self.Tile_cnv_set(7+112, 7+112, ["005005"]) 
     elif xy_key == "7-6":
         self.Tile_cnv_set(7+112, 7+96, ["005005"]) 
     elif xy_key == "7-5":
         self.Tile_cnv_set(7+112, 12+80, ["005005"]) 
     elif xy_key == "6-5":
         self.Tile_cnv_set(7+96, 10+80, ["005005"]) 
     elif xy_key == "8-11":
         self.Tile_cnv_set(1+128, 0+0, ["022"]) 
     elif xy_key == "8-12":
         self.Tile_cnv_set(3+128, 3+0, ["063"]) 
     elif xy_key == "9-11":
         self.Tile_cnv_set(1+144, 14+0, ["044"]) 
     elif xy_key == "9-12":
         self.Tile_cnv_set(1+144, 0+0, ["022"]) 
     elif xy_key == "9-13":
         self.Tile_cnv_set(3+144, 3+0, ["063"]) 
     elif xy_key == "10-0":
         self.Tile_cnv_set(13+160, 12, ["005005"]) 
         self.Tile_cnv_set(1+160, 7, ["005"]) 
         self.Tile_cnv_set(1+160, 8, ["005"]) 
         if self.sel_chap == "Chapter 1":
             self.timer_f = False
             self.movie_flug = True             
             self.movie_count = 1050
             self.music_flug = False                         
             print("Chapter Clear!")
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

     elif xy_key == "10-101":
         self.Tile_cnv_set(13+160, 12, ["005005"]) 
         self.Tile_cnv_set(13+160, 11, ["005005"]) 
         self.Tile_cnv_set(13+160, 10, ["005005"]) 
         self.Tile_cnv_set(12+160, 7, ["005005005"]) 
         self.Tile_cnv_set(12+160, 8, ["005005005"]) 
         self.Tile_cnv_set(8+160, 7, ["005005005"]) 
         self.Tile_cnv_set(8+160, 8, ["005005005"]) 
         self.Tile_cnv_set(9+128, 9+32, ["021021"]) 
         self.Tile_cnv_set(9+128, 10+32, ["021021"]) 
         self.Tile_cnv_set(9+128, 11+32, ["021021"]) 
         self.Tile_cnv_set(9+128, 12+32, ["021021"]) 
         self.Tile_cnv_set(5+96, 11+32, ["0ED"])
     elif xy_key == "1-4":
         self.Tile_cnv_set(7+16, 0+64, ["006"]) 
         self.Tile_cnv_set(7+16, 15+48, ["006"]) 
     elif xy_key == "1-5":
         self.Tile_cnv_set(7+16, 1+80, ["000"]) 
         #self.Tile_cnv_set(1+16, 8+80, ["000"]) 
     elif xy_key == "1-8":
         self.Tile_cnv_set(1+16, 7+128, ["000"]) 
         self.Tile_cnv_set(1+16, 8+128, ["000"]) 
         self.Tile_cnv_set(1+16, 9+128, ["000"]) 
         self.Tile_cnv_set(15+16, 7+128, ["002"]) 
     elif xy_key == "1-80":
         self.Tile_cnv_set(1+16, 7+128, ["000"]) 
         self.Tile_cnv_set(1+16, 8+128, ["000"]) 
         self.Tile_cnv_set(1+16, 9+128, ["000"]) 
     elif xy_key == "1-81":
         self.Tile_cnv_set(6+16, 1+128, ["000"]) 
     elif xy_key == "1-82":
         self.Tile_cnv_set(1+16, 7+128, ["04F"]) 
         self.Tile_cnv_set(1+16, 8+128, ["04F"]) 
         self.Tile_cnv_set(1+16, 9+128, ["04F"]) 
         self.Tile_cnv_set(15+16, 7+128, ["04F"]) 
         self.Tile_cnv_set(8+16, 7+128, ["002"]) 
         self.Tile_cnv_set(8+16, 8+128, ["002"]) 
         self.Tile_cnv_set(8+16, 9+128, ["002"]) 
     elif xy_key == "2-7":
         self.Tile_cnv_set(7+32, 6+112, ["000000"]) 
     elif xy_key == "2-6":
         self.Tile_cnv_set(7+0, 14+128, ["000000"])     
         self.Tile_cnv_set(14+32, 1+96, ["139"])     
     elif xy_key == "3-7":
         self.Tile_cnv_set(7+48, 13+112, ["003003"])     
         self.Tile_cnv_set(1+48, 11+112, ["13B"])     
     elif xy_key == "1-6":
         self.Tile_cnv_set(9+16, 1+96, ["000"]) 
     elif xy_key == "1-61":
         self.Tile_cnv_set(14+16, 1+96, ["044"]) 
     elif xy_key == "1-62":
         self.Tile_cnv_set(7+16, 5+96, ["000000"]) 
         self.Tile_cnv_set(7+16, 6+96, ["000000"]) 
     elif xy_key == "1-7":
         self.Tile_cnv_set(5+16, 6+112, ["000000"]) 
         self.Tile_cnv_set(5+16, 7+112, ["000000"]) 
         self.Tile_cnv_set(5+16, 8+112, ["000000"]) 
     elif xy_key == "0-9":
         self.Tile_cnv_set(7+0, 13+144, ["000000"]) 
         self.Tile_cnv_set(7+0, 1+144, ["000000"]) 
         if self.sel_chap == "Chapter 3":
             self.timer_f = False
             self.movie_flug = True             
             self.movie_count = 1050
             self.music_flug = False                         
             print("Chapter Clear!")
         if self.items5[1] == 0:
             self.items5[1] = 1
         if self.items2[7] == 0:
             self.items2[7] = 1
         if self.items2[6] == 0:
             self.items2[6] = 1             
     elif xy_key == "0-91":
         self.Tile_cnv_set(7+0, 1+144, ["020020"]) 
         self.Tile_cnv_set(7+0, 3+144, ["000000"]) 
     elif xy_key == "0-11":
         self.Tile_cnv_set(5+0, 8+176, ["020003003003003"]) 
         self.Tile_cnv_set(5+0, 7+176, ["020003003003003"]) 
         self.Tile_cnv_set(5+0, 6+176, ["020003003003003"]) 
         self.Tile_cnv_set(11+0, 6+176, ["227"]) 
     elif xy_key == "5-11":
         self.Tile_cnv_set(7+96, 8+176, ["006006"]) 
         self.Tile_cnv_set(7+96, 9+176, ["006006"]) 
         self.Tile_cnv_set(3+80, 3+176, ["157"]) 
     elif xy_key == "7-11":
         self.Tile_cnv_set(7+96, 10+176, ["006006"]) 
         self.Tile_cnv_set(7+96, 11+176, ["006006"]) 
         self.Tile_cnv_set(11+112, 3+176, ["157"]) 
     elif xy_key == "6-10":
         self.Tile_cnv_set(7+96, 4+160, ["00A00A"]) 
         self.Tile_cnv_set(2+96, 1+160, ["15E"]) 
         self.Tile_cnv_set(7+96, 1+160, ["15D15D"]) 
     elif xy_key == "6-101":
         self.Tile_cnv_set(7+96, 1+160, ["00A00A"]) 
         self.Tile_cnv_set(2+96, 1+160, ["15F"]) 
     elif xy_key == "6-13":
         self.Tile_cnv_set(7+96, 8+208, ["006006"]) 
         self.Tile_cnv_set(7+96, 7+208, ["006006"]) 
         self.Tile_cnv_set(13+96, 4+208, ["15C"]) 
     elif xy_key == "4-14":
         self.Tile_cnv_set(6+64, 8+224, ["006"]) 
         self.Tile_cnv_set(6+64, 7+224, ["006"]) 
     elif xy_key == "3-140":
         self.Tile_cnv_set(12+48, 8+224, ["006"]) 
         self.Tile_cnv_set(12+48, 7+224, ["006"]) 
         self.Tile_cnv_set(15+48, 8+224, ["027"]) 
         self.Tile_cnv_set(15+48, 7+224, ["027"]) 
     elif xy_key == "4-111":
         self.Tile_cnv_set(6+64, 1+176, ["001001"]) 
     elif xy_key == "3-121":
         self.Tile_cnv_set(11+48, 5+192, ["001001"]) 
     elif xy_key == "3-141":
         self.Tile_cnv_set(7+48, 15+224, ["006006"]) 
     elif xy_key == "3-14":
         self.Tile_cnv_set(15+48, 8+224, ["00A"]) 
         self.Tile_cnv_set(15+48, 7+224, ["00A"]) 
         self.b3_l = False
         if self.sel_chap == "Chapter 4":
             self.timer_f = False
             self.movie_flug = True             
             self.movie_count = 1050
             self.music_flug = False                         
             print("Chapter Clear!")
         pyxel.clip()
         if self.items3[6] == 0:
             self.items3[6] = 1
         if self.items3[7] == 0:
             self.items3[7] = 1          
         if self.items5[2] == 0:
             self.items5[2] = 1          
     elif xy_key == "5-14":
         self.Tile_cnv_set(9+80, 8+224, ["044"]) 
         if self.items3[4] == 0:
             self.items3[4] = 1
     elif xy_key == "3-15":
         self.Tile_cnv_set(7+48, 5+240, ["00A00A"]) 
         if self.items3[5] == 0:
             self.items3[5] = 1             
     elif xy_key == "4-90":
         self.Tile_cnv_set(5+64, 2+144, ["091072073074091"]) 
         self.Tile_cnv_set(6+64, 3+144, ["092093094"]) 
         #self.Tile_cnv_set(5+64, 3+144, ["091092093094091091091"]) 
         self.Tile_cnv_set(4+64, 4+144, ["091"]) 
         self.Tile_cnv_set(10+64, 4+144, ["091091"]) 
         self.Tile_cnv_set(4+64, 5+144, ["091091"]) 
         self.Tile_cnv_set(9+64, 5+144, ["091091"]) 
         self.Tile_cnv_set(4+64, 6+144, ["091091091"]) 
         self.Tile_cnv_set(8+64, 6+144, ["091091091"]) 
         self.Tile_cnv_set(7+64, 8+144, ["001"]) 
         self.Tile_cnv_set(6+64, 15+144, ["020020"]) 
     elif xy_key == "4-9":
         self.Tile_cnv_set(5+64, 2+144, ["021021021021021"]) 
         self.Tile_cnv_set(6+64, 3+144, ["021021021"]) 
         self.Tile_cnv_set(4+64, 4+144, ["021"]) 
         self.Tile_cnv_set(10+64, 4+144, ["021021"]) 
         self.Tile_cnv_set(4+64, 5+144, ["021021"]) 
         self.Tile_cnv_set(9+64, 5+144, ["021021"]) 
         self.Tile_cnv_set(4+64, 6+144, ["021021021"]) 
         self.Tile_cnv_set(8+64, 6+144, ["021021021"]) 
         self.Tile_cnv_set(0+64, 9+144, ["001"])          
         self.Tile_cnv_set(0+64, 10+144, ["001"])          
         self.Tile_cnv_set(6+64, 15+144, ["001001"]) 
     elif xy_key == "13-7":
         if self.items4[4] == 0:
             self.items4[4] = 1
             self.Tile_cnv_set(3+208, 5+112, ["044"]) 
     elif xy_key == "13-8":
         self.Tile_cnv_set(13+208, 13+128, ["000000"])          
     elif xy_key == "13-9":
         self.Tile_cnv_set(7+208, 12+144, ["00C00C"])          
     elif xy_key == "14-5":
         self.Tile_cnv_set(7+224, 6+80, ["001001"])                       
     elif xy_key == "13-4":
         self.Tile_cnv_set(9+208, 12+64, ["006"])             
     elif xy_key == "15-4":
         self.Tile_cnv_set(6+240, 12+64, ["000000000000000"])          
     elif xy_key == "14-501":
         self.Tile_cnv_set(5+224, 9+64, ["1AD"]) 
         self.Tile_cnv_set(7+224, 0+64, ["003003"]) 
         self.Tile_cnv_set(6+224, 7+64, ["02101B01C021"]) 
     elif xy_key == "14-502":
         self.Tile_cnv_set(10+224, 9+64, ["1AF"]) 
         self.Tile_cnv_set(7+224, 1+64, ["003003"]) 
         self.Tile_cnv_set(6+224, 6+64, ["02101B01C021"]) 
     elif xy_key == "14-30":
         self.Tile_cnv_set(7+224, 13+48, ["003003"]) 
         self.Tile_cnv_set(7+224, 8+48, ["016017"]) 
         self.Tile_cnv_set(7+224, 9+48, ["018019"])          
         self.Tile_cnv_set(7+224, 15+48, ["1A11A1"])    
     elif xy_key == "14-3":
         self.Tile_cnv_set(7+224, 5+48, ["012012"]) 
         self.Tile_cnv_set(7+224, 15+48, ["003003"])              
         self.Tile_cnv_set(7+240, 0+64, ["000"])      
         self.Tile_cnv_set(7+240, 1+64, ["000"])      
         self.Tile_cnv_set(7+240, 2+64, ["000"])      
         self.Tile_cnv_set(7+240, 3+64, ["000"])      
         self.Tile_cnv_set(7+240, 4+64, ["000"])      
         self.Tile_cnv_set(7+240, 5+64, ["000"])      
         self.Tile_cnv_set(7+240, 6+64, ["000"])      
         self.Tile_cnv_set(7+240, 7+64, ["000"])      
         self.Tile_cnv_set(7+240, 8+64, ["000"])      
         self.Tile_cnv_set(7+240, 9+64, ["000"])      
         self.Tile_cnv_set(7+240, 10+64, ["000"])      
         self.Tile_cnv_set(7+240, 11+64, ["000"])    
         if self.sel_chap == "Chapter 5":
             self.timer_f = False
             self.movie_flug = True             
             self.movie_count = 1050
             self.music_flug = False                         
             print("Chapter Clear!")         
         if self.items4[6] == 0:
             self.items4[6] = 1     
         if self.items4[7] == 0:
             self.items4[7] = 1                  
         if self.items5[3] == 0:
             self.items5[3] = 1                       
     elif xy_key == "14-31":
         if self.items4[5] == 0:
             self.items4[5] = 1         
         self.Tile_cnv_set(7+224, 2+48, ["1CF1D0"])     
     elif xy_key == "6-60":
         self.Tile_cnv_set(8+96, 8+96, ["005"]) 
         self.Tile_cnv_set(7+96, 2+96, ["005005"]) 
         self.Tile_cnv_set(7+96, 0+96, ["022022"]) 
     elif xy_key == "6-6":
         self.Tile_cnv_set(7+96, 12+96, ["005005"]) 
         self.Tile_cnv_set(7+96, 0+96, ["005005"])
         self.Tile_cnv_set(6+224, 4+16, ["022006006022"])
         self.Tile_cnv_set(6+224, 5+16, ["022006006022"])
         self.Tile_cnv_set(6+224, 6+16, ["022006006022"])
         self.Tile_cnv_set(6+224, 7+16, ["022006006022"])
         self.Tile_cnv_set(6+224, 8+16, ["022006006022"])
         if self.sel_chap == "Chapter 6":
             self.timer_f = False
             self.movie_flug = True             
             self.movie_count = 1050
             self.music_flug = False                         
             print("Chapter Clear!")
         if self.items6[0] == 0:
             self.items6[0] = 1                 
     elif xy_key == "14-1":
         self.Tile_cnv_set(7+224, 9+16, ["006006"]) 
     elif xy_key == "14-101":
         self.Tile_cnv_set(7+224, 11+16, ["1BD1BE"])          
         self.Tile_cnv_set(7+224, 12+16, ["1DD1DE"])   
         self.set_para2 = 1
     elif xy_key == "14-102":
         self.Tile_cnv_set(7+224, 11+16, ["1BB1BC"])          
         self.Tile_cnv_set(7+224, 12+16, ["1DB1DC"])        
         self.set_para2 = 2
     elif xy_key == "14-103":
         self.Tile_cnv_set(7+224, 11+16, ["23C23D"])          
         self.Tile_cnv_set(7+224, 12+16, ["25C25D"])             
         self.set_para2 = 3
     elif xy_key == "14-104":
         self.Tile_cnv_set(6+224, 11+16, ["23E"])          
         self.Tile_cnv_set(6+224, 12+16, ["25E"])                      
         self.Tile_cnv_set(7+224, 11+16, ["1FD1FE"])
         self.Tile_cnv_set(7+224, 12+16, ["21D21E"])
         self.Tile_cnv_set(7+224, 14+16, ["006006"]) 
     elif xy_key == "14-200":
         self.Tile_cnv_set(0+224, 15+32, 
                        ["2A72A82A32A42A32A42A32A42A32A42A32A42A32A42A42A5"])          
         self.Tile_cnv_set(0+224, 14+32, 
                        ["286287282283282283282283282283282283282283284285"])    
         for i in range(12):
             self.Tile_cnv_set(14+224, 13-i+32, 
                            ["28C28D"])              
             self.Tile_cnv_set(0+224, 13-i+32, 
                            ["28E28F"])                       
         self.Tile_cnv_set(0+224, 0+32, ["288289"])                           
         self.Tile_cnv_set(14+224, 0+32, ["28A28B"])                           
         self.Tile_cnv_set(0+224, 1+32, ["2A82A9"])                           
         self.Tile_cnv_set(14+224, 1+32, ["2AA2AB"])                  
         self.Tile_cnv_set(2+224, 1+32, 
                              ["2B02B12B02B12B02B12B02B12B02B12B02B1"])     
         self.Tile_cnv_set(2+224, 0+32, 
                              ["290291290291290291290291290291290291"])     
         self.Tile_cnv_set(2+224, 1+32, 
                              ["2B02B12B02B12B02B12B02B12B02B12B02B1"])     
         self.Tile_cnv_set(6+224, 15+32, 
                        ["2B32B42B5"])          
         self.Tile_cnv_set(6+224, 14+32, 
                        ["293294295"])                           
         self.Tile_cnv_set(7+224, 10+32, 
                        ["342343"])                 
         self.Tile_cnv_set(7+224, 11+32, 
                        ["362363"])          
         self.Tile_cnv_set(7+224, 12+32, 
                        ["342343"])          
         self.Tile_cnv_set(7+224, 13+32, 
                        ["362363"])                          
         self.Tile_cnv_set(7+224, 7+32, 
                        ["2E22E3"])                 
         self.Tile_cnv_set(7+224, 8+32, 
                        ["302303"])        
         self.Tile_cnv_set(7+224, 9+32, 
                        ["342343"])        
         self.Tile_cnv_set(7+224, 3+32, 
                        ["006006"])             
     elif xy_key == "14-210":
         self.Tile_cnv_set(6+224, 8+32,["006"])          
         self.Tile_cnv_set(7+224, 7+32, 
                        ["2E42E5"])                 
         self.Tile_cnv_set(7+224, 8+32,        
                        ["304305"])      
     elif xy_key == "14-2":
         self.Tile_cnv_set(0+224, 15+32, 
                        ["047047047047047047047047047047047047047047047047"])          
         self.Tile_cnv_set(0+224, 14+32, 
                        ["047047309309309309309309309309309309309309047047"])    
         for i in range(12):
             self.Tile_cnv_set(14+224, 13-i+32, 
                            ["2E9047"])              
             self.Tile_cnv_set(0+224, 13-i+32, 
                            ["0472E8"])                                       
         self.Tile_cnv_set(0+224, 1+32, 
                    ["047047308308308308308308308308308308308308047047"])     
         self.Tile_cnv_set(0+224, 0+32, 
                    ["047047047047047047047047047047047047047047047047"])     
         self.Tile_cnv_set(7+224, 1+32, 
                    ["006006"])     
         self.Tile_cnv_set(7+224, 0+32, 
                    ["006006"])              
         self.Tile_cnv_set(7+224, 11+16, ["2E62E7"])                       
         self.Tile_cnv_set(7+224, 12+16, ["306307"])          
         self.Tile_cnv_set(7+192, 3+0, ["005"])     
         self.npc_pos_x["12-0"] = []
         self.npc_pos_y["12-0"] = []
         self.Tile_cnv_set(3+0, 3+80, ["006006"])     
         self.npc_pos_x["0-5"] = []
         self.npc_pos_y["0-5"] = []
         self.Tile_cnv_set(1+112, 6+32, ["000"])     
         self.npc_pos_x["7-2"] = [508,612]
         self.npc_pos_y["7-2"] = [510,607]
         self.Tile_cnv_set(6+144, 3+32, ["1BA"])  
         self.Tile_cnv_set(13+208, 1+48, ["1BA"])  
         self.Tile_cnv_set(1+0, 11+64, ["1BA1BA"])  
     elif xy_key == "13-0":
         self.Tile_cnv_set(14+208, 7+0, ["012"]) 
         self.Tile_cnv_set(14+208, 8+0, ["012"]) 
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
         
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1007:         
         if self.tile_camera_cnx > 1279 and self.tile_camera_cny < 20:             
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                                    
         elif self.tile_camera_cnx > 1279:
             self.tile_camera_cny -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                           
         elif self.tile_camera_cny > 257:
             self.tile_camera_cnx += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                  
         elif self.tile_camera_cnx > 897:
             self.tile_camera_cny += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)         
         elif self.tile_camera_cn > 20:
             self.tile_camera_cnx += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8,
                        128, 128)                      
         else:
             self.tile_camera_cn += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8,
                        0 + self.map_y * 8,
                        128, 128)                    
         self.event_cnt = False
         pyxel.rect(0, 90, 129, 39, 0)
         pyxel.rectb(1, 90, 127, 38, 8)
         self.Draw_fonts(self.text_list["3000"], 4, 95)
         self.Draw_fonts(self.text_list["3001"], 4, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)         
     elif n == 1010:
         pyxel.bltm(0, 0, 1, 0, 0, 128, 128)               
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["25"], 5, 90)
         self.Draw_fonts(self.text_list["26"], 5, 100)         
         self.Draw_fonts(self.text_list["27"], 5, 110)
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1011:
         pyxel.bltm(0, 0, 1, 0, 0, 128, 128)               
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["28"], 5, 90)
         self.Draw_fonts(self.text_list["29"], 5, 100)                  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1012:
         pyxel.bltm(0, 0, 1, 0, 0, 128, 128)               
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["30"], 5, 90)
         self.Draw_fonts(self.text_list["31"], 5, 100)                  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1013:         
         if self.tile_camera_cnx < -1020 and self.tile_camera_cny > 258:         
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                                    
         elif self.tile_camera_cnx < -515 and self.tile_camera_cny > 258:
             self.tile_camera_cnx -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                                              
         elif self.tile_camera_cnx < -515:
             self.tile_camera_cny += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                                 
         elif self.tile_camera_cnx < -385 and self.tile_camera_cny < 18:
             self.tile_camera_cnx -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                           
         elif self.tile_camera_cnx < -385:
             self.tile_camera_cny -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                  
         elif self.tile_camera_cny > 256:
             self.tile_camera_cnx -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)         
         elif self.tile_camera_cn > 20:
             self.tile_camera_cny += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                      
         else:
             self.tile_camera_cn += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8,
                        0 + self.map_y * 8,
                        128, 128)                    
         self.event_cnt = False
         pyxel.rect(0, 90, 129, 39, 0)
         pyxel.rectb(1, 90, 127, 38, 8)
         self.Draw_fonts(self.text_list["3000"], 4, 95)
         self.Draw_fonts(self.text_list["3002"], 4, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                  
         
     elif n == 1015:
         pyxel.bltm(0, 0, 1, 16*8, 0, 128, 128)               
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["32"], 5, 90)
         self.Draw_fonts(self.text_list["33"], 5, 100)                  
         self.Draw_fonts(self.text_list["34"], 5, 110)        
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1016:
         pyxel.bltm(0, 0, 1, 16*8, 0, 128, 128)                              
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["35"], 5, 90)
         self.Draw_fonts(self.text_list["36"], 5, 100)                  
         self.Draw_fonts(self.text_list["37"], 5, 110)                  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1017:         
         if (self.tile_camera_cnx > 2 and self.tile_camera_cny > -14
             and self.tile_camera_cn > 30):         
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                                 
         elif self.tile_camera_cnx > 2 and self.tile_camera_cn > 30:
             self.tile_camera_cny += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                                
         elif self.tile_camera_cny > -124 and self.tile_camera_cn > 30:
             self.tile_camera_cnx += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                   
         elif self.tile_camera_cnx > -138 and self.tile_camera_cn > 30:
             self.tile_camera_cny += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                           
         elif self.tile_camera_cny < -248:
             self.tile_camera_cn += 1
             self.tile_camera_cnx += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                  
         elif self.tile_camera_cnx < -377:
             self.tile_camera_cny -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)         
         elif self.tile_camera_cn > 10:
             self.tile_camera_cnx -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                      
         else:
             self.tile_camera_cn += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8,
                        0 + self.map_y * 8,
                        128, 128)                    
         self.event_cnt = False
         pyxel.rect(0, 90, 129, 39, 0)
         pyxel.rectb(1, 90, 127, 38, 8)
         self.Draw_fonts(self.text_list["3000"], 4, 95)
         self.Draw_fonts(self.text_list["3003"], 4, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                                        
         
     elif n == 1020:
         pyxel.bltm(0, 0, 1, 32*8, 0, 128, 128)               
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["38"], 5, 90)
         self.Draw_fonts(self.text_list["39"], 5, 100)                  
         self.Draw_fonts(self.text_list["40"], 5, 110)        
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1021:
         pyxel.bltm(0, 0, 1, 32*8, 0, 128, 128)                              
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["41"], 5, 90)
         self.Draw_fonts(self.text_list["42"], 5, 100)                  
         self.Draw_fonts(self.text_list["43"], 5, 110)                  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1022:
         pyxel.bltm(0, 0, 1, 32*8, 0, 128, 128)                              
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["44"], 5, 90)
         self.Draw_fonts(self.text_list["45"], 5, 100)                  
         self.Draw_fonts(self.text_list["46"], 5, 110)                  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)         
     elif n == 1023:         
         if (self.tile_camera_cnx < -393 and self.tile_camera_cny > 641
             and self.tile_camera_cn > 30):         
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                                 
 
         elif self.tile_camera_cny > 641:
             self.tile_camera_cn += 1
             self.tile_camera_cnx -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                  
         elif self.tile_camera_cnx < -128:
             self.tile_camera_cny += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)         
         elif self.tile_camera_cn > 10:
             self.tile_camera_cnx -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                      
         else:
             self.tile_camera_cn += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8,
                        0 + self.map_y * 8,
                        128, 128)                    
         self.event_cnt = False
         pyxel.rect(0, 90, 129, 39, 0)
         pyxel.rectb(1, 90, 127, 38, 8)
         self.Draw_fonts(self.text_list["3000"], 4, 95)
         self.Draw_fonts(self.text_list["3004"], 4, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                                    
         
     elif n == 1030:
         pyxel.bltm(0, 0, 1, 48*8, 0, 128, 128)               
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["60"], 5, 90)
         self.Draw_fonts(self.text_list["61"], 5, 100)                  
         self.Draw_fonts(self.text_list["62"], 5, 110)        
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1031:
         pyxel.bltm(0, 0, 1, 48*8, 0, 128, 128)                              
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["63"], 5, 90)
         self.Draw_fonts(self.text_list["64"], 5, 100)                  
         self.Draw_fonts(self.text_list["65"], 5, 110)                  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1032:
         pyxel.bltm(0, 0, 1, 48*8, 0, 128, 128)                              
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["66"], 5, 90)
         self.Draw_fonts(self.text_list["67"], 5, 100)                  
         self.Draw_fonts(self.text_list["68"], 5, 110)                  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)         
     elif n == 1033:         
         if self.tile_camera_cny < -603:         
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                                          
         elif self.tile_camera_cnx > 511:
             self.tile_camera_cny -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)         
         elif self.tile_camera_cn > 10:
             self.tile_camera_cnx += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                      
         else:
             self.tile_camera_cn += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8,
                        0 + self.map_y * 8,
                        128, 128)                    
         self.event_cnt = False
         pyxel.rect(0, 90, 129, 39, 0)
         pyxel.rectb(1, 90, 127, 38, 8)
         self.Draw_fonts(self.text_list["3000"], 4, 95)
         self.Draw_fonts(self.text_list["3005"], 4, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)             

     elif n == 1040:
         pyxel.bltm(0, 0, 1, 64*8, 0, 128, 128)               
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["70"], 5, 90)
         self.Draw_fonts(self.text_list["71"], 5, 100)                  
         self.Draw_fonts(self.text_list["72"], 5, 110)        
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1041:
         pyxel.bltm(0, 0, 1, 64*8, 0, 128, 128)                              
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["73"], 5, 90)
         self.Draw_fonts(self.text_list["74"], 5, 100)                  
         self.Draw_fonts(self.text_list["75"], 5, 110)                  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 1042:
         pyxel.bltm(0, 0, 1, 64*8, 0, 128, 128)                              
         pyxel.rect(0, 85, 128, 63, 0)         
         self.Draw_fonts(self.text_list["76"], 5, 90)
         self.Draw_fonts(self.text_list["77"], 5, 100)                  
         self.Draw_fonts(self.text_list["78"], 5, 110)                  
         self.event_cnt = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                 
     elif n == 1043:         
         if (self.tile_camera_cnx < -128 and self.tile_camera_cny > -254
            and self.tile_camera_cn > 30):         
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                         
         elif self.tile_camera_cnx < -128:
             self.tile_camera_cny += 1
             self.tile_camera_cn += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                          
         elif self.tile_camera_cny < -380:
             self.tile_camera_cnx -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)         
         elif self.tile_camera_cn > 10:
             self.tile_camera_cny -= 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8 + self.tile_camera_cnx,
                        0 + self.map_y * 8 + self.tile_camera_cny,
                        128, 128)                      
         else:
             self.tile_camera_cn += 1
             pyxel.bltm(0,0,0,
                        0 + self.map_x * 8,
                        0 + self.map_y * 8,
                        128, 128)                    
         self.event_cnt = False
         pyxel.rect(0, 90, 129, 39, 0)
         pyxel.rectb(1, 90, 127, 38, 8)
         self.Draw_fonts(self.text_list["3000"], 4, 95)
         self.Draw_fonts(self.text_list["3006"], 4, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                                               
     #////////////////////////////////////////////////////////////////////////
     
     #Chapter Clear Screen////////////////////////////////////////////////////
     elif n == 1050:
         #pyxel.bltm(0, 0, 1, 64*8, 0, 128, 128)        
         s = int(self.timer / 30)
         s2 = int(s % 60)
         m = int(s / 60)
         m2 = int(m % 60)
         h = int(m / 60)
         pyxel.text(150, 42,
                     str(h).zfill(2) + ":" 
                   + str(m2).zfill(2) + ":" 
                   + str(s2).zfill(2), 7)                      
         pyxel.rect(0, 85, 128, 63, 0)         
         pyxel.text(5, 90, str(self.sel_chap) + " Clear!!", 7)
         pyxel.text(5, 102, "Clear time = " 
                    + str(h).zfill(2) + ":" 
                    + str(m2).zfill(2) + ":" 
                    + str(s2).zfill(2), 7)
         self.timer_f = False          
         self.event_cnt = False
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)        
        
     #///////////////////////////////////////////////////////////////////////
         
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
         
         pyxel.bltm(0, 0, 0, 240 * 8, 0, 128, 128)
         
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
         elif key == "3-13":
             s = self.shop3
             s2 = 3
         elif key == "12-8":
             s = self.shop4
             s2 = 4     
        
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
                     elif s2 == 3:
                         self.items3[p] = 1
                     elif s2 == 4:
                         self.items4[p] = 1                         
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
         self.map_ch_fl = 1
     elif n == 334:
         self.map_x = 7 * 16
         self.map_y = 1 * 16
         self.map_count_x = 8
         self.map_count_y = 2
         self.Player.update(32, 56)
         self.movie_flug = False
         self.map_ch_fl = 1
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
         if self.sel_chap == "Chapter 2":
             pass
         else:
             pyxel.rect(0, 40, 128, 88, 0)
             self.Draw_fonts(self.text_list["105_0"],5, 45)
         if key == "2-3":
             if self.sel_chap == "Chapter 2":
                 pass
             else:
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
             x = self.Tile_cnv(14+32, 13+48)
             if x == 33:
                 if self.sel_chap == "Chapter 2":
                     self.event_cnt = True
                     self.movie_count = 1050
                 else:
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
             x = self.Tile_cnv(14+32, 13+48)
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
             x = self.Tile_cnv(14+32, 13+48)
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
             x = self.Tile_cnv(14+32, 13+48)
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
             x = self.Tile_cnv(14+32, 13+48)
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
         
         if self.sel_chap == "Chapter 2":
             pass                         
         else:
             pyxel.text(5, 55, "Press Destination number.", 7)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 2440:
         pyxel.bltm(0, 0, 0, 112 * 8, 48 * 8, 16*8, 16*8)
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
         pyxel.bltm(0, 0, 0, 112 * 8, 48 * 8, 16*8, 16*8)
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
         pyxel.bltm(0, 0, 0, 112 * 8, 48 * 8, 16*8, 16*8)
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
         pyxel.bltm(0, 0, 0, 112 * 8, 48 * 8, 16*8, 16*8)
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
         pyxel.bltm(0, 0, 0, 112 * 8, 48 * 8, 16*8, 16*8)
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
         elif key == "1-4":
             self.Draw_fonts(self.text_list["156"],5, 105)
         elif key == "7-0":
             self.Draw_fonts(self.text_list["108"],5, 105)             
         elif key == "0-1":
             self.Draw_fonts(self.text_list["109"],5, 105)
         elif key == "2-3":
             self.Draw_fonts(self.text_list["110"],5, 105)
         elif key == "10-2":
             self.Draw_fonts(self.text_list["129"],5, 105)
         elif key == "9-1":
             self.Draw_fonts(self.text_list["241"],5, 105)
         elif key == "3-8":
             self.Draw_fonts(self.text_list["130"],5, 105)
         elif key == "7-8":
             self.Draw_fonts(self.text_list["131"],5, 105)
         elif key == "15-1":
             self.Draw_fonts(self.text_list["53"],5, 105)
         elif key == "0-5":
             self.Draw_fonts(self.text_list["108"],5, 105)
         elif key == "2-7":
             pyxel.rect(0,95,128,33,0)
             self.Draw_fonts(self.text_list["151"],5, 100)
             self.Draw_fonts(self.text_list["151_1"],5, 110)
         elif key == "1-6":
             self.Draw_fonts(self.text_list["152"],5, 105)
         elif key == "6-9":
             self.Draw_fonts(self.text_list["226"],5, 105)
         elif key == "5-10":
             self.Draw_fonts(self.text_list["227"],5, 105)
         elif key == "7-10":
             self.Draw_fonts(self.text_list["227"],5, 105)
         elif key == "6-11":
             self.Draw_fonts(self.text_list["228"],5, 105)
         elif key == "6-12":
             self.Draw_fonts(self.text_list["234"],5, 105)
         elif key == "5-12":
             if self.Player.player_y < 50:
                 self.Draw_fonts(self.text_list["235"],5, 105)
             else:
                 self.Draw_fonts(self.text_list["236"],5, 105)
         elif key == "7-12":
             self.Draw_fonts(self.text_list["237"],5, 105)
         elif key == "6-13":
             self.Draw_fonts(self.text_list["242"],5, 105)
         elif key == "6-14":
             if self.Player.player_y < 50:
                 self.Draw_fonts(self.text_list["243"],5, 105)
             else:
                 self.Draw_fonts(self.text_list["244"],5, 105)
         elif key == "7-14":
             self.Draw_fonts(self.text_list["245"],5, 105)
         elif key == "13-8":
             self.Draw_fonts(self.text_list["402"],5, 105)             
         elif key == "14-5":
             self.Draw_fonts(self.text_list["403"],5, 105)                        
         elif key == "13-7":
             self.Draw_fonts(self.text_list["404"],5, 105)                                     
         elif key == "13-6":
             self.Draw_fonts(self.text_list["419"],5, 105)                         
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     ###################################################################
         
     #library###########################################################
     elif n == 386:
         pyxel.rect(0, 5, 128, 118, 0)
         pyxel.rectb(0, 5, 128, 118, 4)
         self.Draw_fonts(self.text_list["1000"],2, 7)
         self.Draw_fonts(self.text_list["1001"],2, 27)
         self.Draw_fonts(self.text_list["1002"],2, 37)
         self.Draw_fonts(self.text_list["1003"],2, 47)
         self.Draw_fonts(self.text_list["1004"],2, 57)
         self.Draw_fonts(self.text_list["1005"],2, 67)
         self.Draw_fonts(self.text_list["1006"],2, 77)
         self.Draw_fonts(self.text_list["1007"],2, 87)
         self.Draw_fonts(self.text_list["1008"],2, 97)
         pyxel.text(5, 115, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 384:
         pyxel.rect(0, 5, 128, 118, 0)
         pyxel.rectb(0, 5, 128, 118, 4)
         self.Draw_fonts(self.text_list["1009"],2, 7)
         self.Draw_fonts(self.text_list["1010"],2, 27)
         self.Draw_fonts(self.text_list["1011"],2, 37)
         self.Draw_fonts(self.text_list["1012"],2, 47)
         self.Draw_fonts(self.text_list["1013"],2, 57)
         self.Draw_fonts(self.text_list["1014"],2, 67)
         self.Draw_fonts(self.text_list["1015"],2, 77)
         self.Draw_fonts(self.text_list["1016"],2, 87)
         self.Draw_fonts(self.text_list["1017"],2, 97)
         pyxel.text(5, 115, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)

     elif n == 388:
         pyxel.rect(0, 5, 128, 118, 0)
         pyxel.rectb(0, 5, 128, 118, 4)
         self.Draw_fonts(self.text_list["1018"],2, 7)
         self.Draw_fonts(self.text_list["1019"],2, 27)
         self.Draw_fonts(self.text_list["1020"],2, 37)
         self.Draw_fonts(self.text_list["1021"],2, 47)
         self.Draw_fonts(self.text_list["1022"],2, 57)
         self.Draw_fonts(self.text_list["1023"],2, 67)
         self.Draw_fonts(self.text_list["1024"],2, 77)
         self.Draw_fonts(self.text_list["1025"],2, 87)
         self.Draw_fonts(self.text_list["1026"],2, 97)
         pyxel.text(5, 115, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 390:
         pyxel.rect(0, 5, 128, 118, 0)
         pyxel.rectb(0, 5, 128, 118, 4)
         self.Draw_fonts(self.text_list["1027"],2, 7)
         self.Draw_fonts(self.text_list["1028"],2, 27)
         self.Draw_fonts(self.text_list["1029"],2, 37)
         self.Draw_fonts(self.text_list["1030"],2, 47)
         self.Draw_fonts(self.text_list["1031"],2, 57)
         self.Draw_fonts(self.text_list["1032"],2, 67)
         self.Draw_fonts(self.text_list["1033"],2, 77)
         self.Draw_fonts(self.text_list["1034"],2, 87)
         self.Draw_fonts(self.text_list["1035"],2, 97)
         pyxel.text(5, 115, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)

     elif n == 392:
         pyxel.rect(0, 5, 128, 118, 0)
         pyxel.rectb(0, 5, 128, 118, 4)
         self.Draw_fonts(self.text_list["1036"],2, 7)
         self.Draw_fonts(self.text_list["1037"],2, 27)
         self.Draw_fonts(self.text_list["1038"],2, 37)
         self.Draw_fonts(self.text_list["1039"],2, 47)
         self.Draw_fonts(self.text_list["1040"],2, 57)
         self.Draw_fonts(self.text_list["1041"],2, 67)
         self.Draw_fonts(self.text_list["1042"],2, 77)
         self.Draw_fonts(self.text_list["1043"],2, 87)
         self.Draw_fonts(self.text_list["1044"],2, 97)
         pyxel.text(5, 115, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
    
     elif n == 394:
         pyxel.rect(0, 5, 128, 118, 0)
         pyxel.rectb(0, 5, 128, 118, 4)
         self.Draw_fonts(self.text_list["1045"],2, 7)
         self.Draw_fonts(self.text_list["1046"],2, 27)
         self.Draw_fonts(self.text_list["1047"],2, 37)
         self.Draw_fonts(self.text_list["1048"],2, 47)
         self.Draw_fonts(self.text_list["1049"],2, 57)
         self.Draw_fonts(self.text_list["1050"],2, 67)
         self.Draw_fonts(self.text_list["1051"],2, 77)
         self.Draw_fonts(self.text_list["1052"],2, 87)
         self.Draw_fonts(self.text_list["1053"],2, 97)
         pyxel.text(5, 115, "Press SPACE-KEY to continue...", 
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
             new_enemy.enemy_h = 120
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
         if self.items5[0] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(7, 7)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 271:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items5[0] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(7, 7)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 272:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items5[1] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(7, 6)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 273:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items5[1] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(7, 6)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 274:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items5[2] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(7, 5)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 275:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items5[2] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(7, 5)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 276:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items5[3] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(6, 5)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     elif n == 277:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items5[3] == 1:
             self.Draw_fonts(self.text_list["100"],5, 105)
             self.MapEvents_ctr(6, 5)
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
         self.MapEvents_ctr(1, 80)
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
             elif tkey == "1-4":
                 self.MapEvents_ctr(1, 4)
             elif tkey == "15-4":
                 self.MapEvents_ctr(15, 4)                 
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

     elif n == 338:
         self.MapEvents_ctr(0, 91)
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,16,240,16,16,14)
         self.Draw_fonts(self.text_list["136"],20, 92)
         self.Draw_fonts(self.text_list["150"],5, 105)
         if self.enemy_crt_flug == False:
             new_enemy = Enemy(7*8, 8*8,96, 10)
             new_enemy.enemy_m = 0
             new_enemy.enemy_h = 180
             self.enemys.append(new_enemy)
             new_enemys = []
             new_enemys.append(Enemy(5*8, 12*8,96, 4))
             new_enemys.append(Enemy(7*8, 12*8,96, 4))
             new_enemys.append(Enemy(8*8, 12*8,96, 4))
             new_enemys.append(Enemy(10*8, 12*8,96, 4))
             for e in new_enemys:
                 e.enemy_m = 1
             for e2 in new_enemys:
                 self.enemys.append(e2)
             self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 339:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(0, 11)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 341:
         self.event_cnt = True
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,32,240,16,16,14)
         self.Draw_fonts(self.text_list["155"],20, 92)
         self.Draw_fonts(self.text_list["153"],5, 105)
         self.MapEvents_ctr(1, 82)
         if self.enemy_crt_flug == False:
             self.enemys.clear()
             new_enemy = Enemy(2*8, 8*8,96, 8)
             new_enemy.enemy_m = 1
             new_enemy.enemy_h = 250
             self.enemys.append(new_enemy)
             self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 3411:
         self.event_cnt = False
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,32,240,16,16,14)
         self.Draw_fonts(self.text_list["155"],20, 92)
         self.Draw_fonts(self.text_list["154"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
     #////////////////////////////////////////////////////////////////////////
         
     #AREA3///////////////////////////////////////////////////////////////////
     elif n == 342:
         pyxel.rect(0, 100, 128, 63, 0)
         tx = self.map_count_x - 1
         ty = self.map_count_y - 1
         tkey = str(tx) + "-" + str(ty)
         if tkey == "5-11":
             self.Draw_fonts(self.text_list["102"],5, 105)
             self.MapEvents_ctr(5, 11)
         elif tkey == "7-11":
             self.Draw_fonts(self.text_list["102"],5, 105)
             self.MapEvents_ctr(7, 11)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
        
     elif n == 345 or n == 346:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 70, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,48,240,16,16,14)
         self.Draw_fonts(self.text_list["307"],20, 82)
         self.Draw_fonts(self.text_list["229"],5, 94)
         self.Draw_fonts(self.text_list["229"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)        
         
     elif n == 3461:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 70, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,48,240,16,16,14)
         self.Draw_fonts(self.text_list["307"],20, 82)
         self.Draw_fonts(self.text_list["230"],5, 94)
         self.Draw_fonts(self.text_list["231"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)        
         
     elif n == 3462:
         self.MapEvents_ctr(6, 10)
         self.event_cnt = False
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 70, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,48,240,16,16,14)
         self.Draw_fonts(self.text_list["307"],20, 82)
         self.Draw_fonts(self.text_list["232"],5, 94)
         self.Draw_fonts(self.text_list["233"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)        
         
     elif n == 347:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(6, 13)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 350:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(6, 101)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 366 or n == 367:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["240"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         self.event_cnt = True
         self.n1 = 0
         self.n2 = 0
         self.n3 = 0
         self.sn = 1
         
     elif n == 3661:
         self.event_cnt = False
         if pyxel.btnp(pyxel.KEY_1):
            if self.sn == 1:
                self.n1 = 1
            elif self.sn == 2:
                self.n2 = 1
            elif self.sn == 3:
                self.n3 = 1
            self.sn += 1
         elif pyxel.btnp(pyxel.KEY_2):
            if self.sn == 1:
                self.n1 = 2
            elif self.sn == 2:
                self.n2 = 2
            elif self.sn == 3:
                self.n3 = 2
            self.sn += 1
         elif pyxel.btnp(pyxel.KEY_3):
            if self.sn == 1:
                self.n1 = 3
            elif self.sn == 2:
                self.n2 = 3
            elif self.sn == 3:
                self.n3 = 3
            self.sn += 1
         elif pyxel.btnp(pyxel.KEY_4):
            if self.sn == 1:
                self.n1 = 4
            elif self.sn == 2:
                self.n2 = 4
            elif self.sn == 3:
                self.n3 = 4
            self.sn += 1
         elif pyxel.btnp(pyxel.KEY_5):
            if self.sn == 1:
                self.n1 = 5
            elif self.sn == 2:
                self.n2 = 5
            elif self.sn == 3:
                self.n3 = 5
            self.sn += 1
         elif pyxel.btnp(pyxel.KEY_6):
            if self.sn == 1:
                self.n1 = 6
            elif self.sn == 2:
                self.n2 = 6
            elif self.sn == 3:
                self.n3 = 6
            self.sn += 1
         elif pyxel.btnp(pyxel.KEY_7):
            if self.sn == 1:
                self.n1 = 7
            elif self.sn == 2:
                self.n2 = 7
            elif self.sn == 3:
                self.n3 = 7
            self.sn += 1
         elif pyxel.btnp(pyxel.KEY_8):
            if self.sn == 1:
                self.n1 = 8
            elif self.sn == 2:
                self.n2 = 8
            elif self.sn == 3:
                self.n3 = 8
            self.sn += 1
         elif pyxel.btnp(pyxel.KEY_9):
            if self.sn == 1:
                self.n1 = 9
            elif self.sn == 2:
                self.n2 = 9
            elif self.sn == 3:
                self.n3 = 9
            self.sn += 1
         elif pyxel.btnp(pyxel.KEY_0):
            if self.sn == 1:
                self.n1 = 0
            elif self.sn == 2:
                self.n2 = 0
            elif self.sn == 3:
                self.n3 = 0
            self.sn += 1
            
         pyxel.rect(0, 40, 128, 60, 0)
         pyxel.rectb(0, 40, 128, 60, 8)
         pyxel.text(15, 60, str(self.n1), 7)
         pyxel.text(55, 60, str(self.n2), 7)
         pyxel.text(95, 60, str(self.n3), 7)
         pyxel.rectb(11+((self.sn-1)*40), 58, 10, 10, pyxel.frame_count % 16)
         pyxel.text(10, 75, "HINT", 7)
         pyxel.text(15, 85, "B1", 7)
         pyxel.blt(25,83,2,56,48,8,8,)   
         pyxel.text(55, 85, "B2", 7)
         pyxel.blt(65,83,2,64,40,8,8,)   
         pyxel.text(95, 85, "B3", 7)
         pyxel.blt(105,83,2,64,48,8,8,)   
            
     
         if self.sn == 4:
            #Check pass
            if str(str(self.n1)+str(self.n2)+str(self.n3)) == "529":
                print("ok")
                self.movie_count = 3663
                self.MapEvents_ctr(4, 14)
            else:
                print("ng")
                self.movie_count = 3662
                
         print(str(self.n1)+str(self.n2)+str(self.n3))
                 
     elif n == 3662:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["239"],5, 105)   
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 3663:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["238"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 368:
         self.event_cnt = True
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,64,240,16,16,14)
         self.Draw_fonts(self.text_list["308"],20, 92)
         self.Draw_fonts(self.text_list["309"],5, 105)
         self.MapEvents_ctr(3, 140)
         if self.enemy_crt_flug == False:
             self.enemys.clear()
             new_enemy = Enemy(2*8, 8*8, 112, 14)
             new_enemy.enemy_m = 0
             new_enemy.enemy_h = 175
             self.enemys.append(new_enemy)
             self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 3681:
         self.event_cnt = True
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,64,240,16,16,14)
         self.Draw_fonts(self.text_list["308"],20, 92)
         self.Draw_fonts(self.text_list["310"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 3682:
         self.event_cnt = False
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         pyxel.blt(2,84,1,64,240,16,16,14)
         self.Draw_fonts(self.text_list["308"],20, 92)
         self.Draw_fonts(self.text_list["311"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)

     elif n == 369 or n == 370:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items3[2] == 1:
             self.Draw_fonts(self.text_list["238"],5, 105)
             self.MapEvents_ctr(3, 121)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 371 or n == 372:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items3[3] == 1:
             self.Draw_fonts(self.text_list["238"],5, 105)
             self.MapEvents_ctr(4, 111)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 373 or n == 374:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items3[6] == 1:
             self.Draw_fonts(self.text_list["238"],5, 105)
             self.MapEvents_ctr(3, 141)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 377:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["312"],5, 105)
         self.MapEvents_ctr(5, 14)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 375 or n == 376:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["313"],5, 105)
         self.MapEvents_ctr(3, 15)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 378:
         self.MapEvents_ctr(4, 90)
         if self.enemy_crt_flug == False:
             self.enemys.clear()
             new_enemy = Enemy(7*8, 3*8, 112, 18)
             new_enemy.enemy_m = 0
             new_enemy.enemy_h = 600
             self.enemys.append(new_enemy)
             self.enemy_crt_flug = True
         self.movie_flug = False
         self.Event_save = False
     #////////////////////////////////////////////////////////////////////////
         
     #Area4///////////////////////////////////////////////////////////////////
     elif n == 427:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["400"],5, 105)
         self.MapEvents_ctr(13, 7)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)        

     elif n == 421 or n == 422:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items4[6] == 1:
             self.Draw_fonts(self.text_list["405"],5, 105)
             self.MapEvents_ctr(13, 8)
         else:
             self.Draw_fonts(self.text_list["401"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)         
         
     elif n == 578 or n == 579:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items4[2] == 1:
             self.Draw_fonts(self.text_list["405"],5, 105)
             self.MapEvents_ctr(14, 5)
         else:
             self.Draw_fonts(self.text_list["401"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                  

     elif n == 458:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items4[3] == 1:
             self.Draw_fonts(self.text_list["405"],5, 105)
             self.MapEvents_ctr(13, 4)
         else:
             self.Draw_fonts(self.text_list["401"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)             
         
     elif n == 428:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(14, 501)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)

     elif n == 430:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(14, 502)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 425:
         tx = self.map_count_x - 1
         ty = self.map_count_y - 1
         tkey = str(tx) + "-" + str(ty)
         if tkey == "13-5":         
             self.map_x = 13 * 16
             self.map_y = 4 * 16
             self.map_count_x = 14
             self.map_count_y = 5
             self.Player.update(16, 104)
             self.movie_flug = False
             self.map_ch_fl = 1         
             self.map_move = 1
         elif tkey == "15-5":         
             self.map_x = 15 * 16
             self.map_y = 4 * 16
             self.map_count_x = 16
             self.map_count_y = 5
             self.Player.update(104, 112)
             self.movie_flug = False
             self.map_ch_fl = 1         
             self.map_move = 1
         
     elif n == 426:
         tx = self.map_count_x - 1
         ty = self.map_count_y - 1
         tkey = str(tx) + "-" + str(ty)
         if tkey == "13-4":         
           self.map_x = 13 * 16
           self.map_y = 5 * 16
           self.map_count_x = 14
           self.map_count_y = 6
           self.Player.update(16, 40)
           self.movie_flug = False
           self.map_ch_fl = 1         
           self.map_move = 1         
         elif tkey == "15-4":         
           self.map_x = 15 * 16
           self.map_y = 5 * 16
           self.map_count_x = 16
           self.map_count_y = 6
           self.Player.update(104, 40)
           self.movie_flug = False
           self.map_ch_fl = 1         
           self.map_move = 1    
           
     elif n == 610:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,80,240,16,16,14)
         self.Draw_fonts(self.text_list["412"],20, 82)
         self.Draw_fonts(self.text_list["406"],5, 95)
         self.Draw_fonts(self.text_list["407"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)           
           
     elif n == 6101:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,80,240,16,16,14)
         self.Draw_fonts(self.text_list["412"],20, 82)
         self.Draw_fonts(self.text_list["408"],5, 95)
         self.Draw_fonts(self.text_list["409"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                   
         
     elif n == 6102:
         self.event_cnt = False
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,96,240,16,16,14)
         self.Draw_fonts(self.text_list["412"],20, 82)
         self.Draw_fonts(self.text_list["410"],5, 95)
         self.Draw_fonts(self.text_list["411"],5, 105)
         self.MapEvents_ctr(14, 30)
         if self.enemy_crt_flug == False:
             self.enemys.clear()
             new_enemy = Enemy(7*8, 8*8, 128, 21)
             new_enemy.enemy_m = 0
             new_enemy.enemy_h = 250
             self.enemys.append(new_enemy)
             self.enemy_crt_flug = True
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)
         
     elif n == 461 or n == 462:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["413"],5, 105)
         self.MapEvents_ctr(14, 31)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                  
         
     elif n == 437:
         pyxel.rect(0, 100, 128, 63, 0)
         #if self.enemy_crt_flug == False:
         self.o_cnt = randint(414, 418)
             #self.enemy_crt_flug = True
         self.Draw_fonts(self.text_list[str(self.o_cnt)],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)         
     #////////////////////////////////////////////////////////////////////////
     
     #Area5///////////////////////////////////////////////////////////////////
     elif n == 491:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,112,240,16,16,14)
         self.Draw_fonts(self.text_list["420"],20, 82)
         self.Draw_fonts(self.text_list["421"],5, 95)
         self.Draw_fonts(self.text_list["422"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)             
         
     elif n == 4912:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,112,240,16,16,14)
         self.Draw_fonts(self.text_list["420"],20, 82)
         self.Draw_fonts(self.text_list["423"],5, 95)
         self.Draw_fonts(self.text_list["424"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                       
         
     elif n == 4913:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,112,240,16,16,14)
         self.Draw_fonts(self.text_list["420"],20, 82)
         self.Draw_fonts(self.text_list["425"],5, 95)
         self.Draw_fonts(self.text_list["426"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                       

     elif n == 4914:
         self.event_cnt = False
         self.MapEvents_ctr(6, 60)
         if self.enemy_crt_flug == False:
             self.enemys.clear()
             new_enemy = Enemy(8*8, 8*8, 80, 24)
             new_enemy.enemy_m = 1
             new_enemy.enemy_h = 400
             self.enemys.append(new_enemy)
             self.enemy_crt_flug = True         
         pyxel.rect(0, 90, 128, 63, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,128,240,16,16,14)
         self.Draw_fonts(self.text_list["420"],20, 82)
         self.Draw_fonts(self.text_list["427"],5, 95)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                       

     elif n == 473 or n == 474:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 63, 0)
         self.Draw_fonts(self.text_list["2000"],5, 95)
         pyxel.text(7, 106, "Y = YES", 7)                        
         pyxel.text(7, 116, "N = NO", 7)     
         if pyxel.btnp(pyxel.KEY_Y):
             self.movie_count = 4741
             self.game_end = True
             self.Save_data()
         elif pyxel.btnp(pyxel.KEY_N):
             self.event_cnt = False
             self.movie_flug = False
             
     elif n == 4741:
         self.event_cnt = False
         pyxel.cls(0)
         self.Draw_fonts(self.text_list["2001"],5, 15)
         self.Draw_fonts(self.text_list["2002"],5, 35)
         self.Draw_fonts(self.text_list["2003"],5, 45)
         self.Draw_fonts(self.text_list["2004"],5, 55)
         self.Draw_fonts(self.text_list["2005"],5, 75)
         self.Draw_fonts(self.text_list["2006"],5, 85)
         pyxel.text(5, 110, "Thank you for playing!!", 
                    pyxel.frame_count % 16)              
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                
         
     elif n == 411 or n == 412:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items6[0] == 1:
             self.Draw_fonts(self.text_list["238"],5, 105)
             self.MapEvents_ctr(14, 1)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)         
         
     elif n == 381 or n == 382 or n == 413 or n == 414:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items3[5] == 1:
             self.Draw_fonts(self.text_list["428"],5, 105)
             self.MapEvents_ctr(14, 101)
         else:
             self.Draw_fonts(self.text_list["4281"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                  
         
     elif n == 445 or n == 446 or n == 477 or n == 478:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items2[5] == 1 and self.set_para == 1:
             self.Draw_fonts(self.text_list["429"],5, 105)
             self.MapEvents_ctr(14, 102)
         else:
             self.Draw_fonts(self.text_list["4291"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)               
         
     elif n == 443 or n == 444 or n == 475 or n == 476:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items4[5] == 1 and self.set_para == 2:
             self.Draw_fonts(self.text_list["430"],5, 105)
             self.MapEvents_ctr(14, 103)
         else:
             self.Draw_fonts(self.text_list["4301"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                     
         
     elif n == 571 or n == 603:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items[5] == 1 and self.set_para == 3:
             self.Draw_fonts(self.text_list["431"],5, 105)
             self.MapEvents_ctr(14, 104)
         else:
             self.Draw_fonts(self.text_list["4311"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                              
     #/////////////////////////////////////////////////////////////////////////
     
     #Area6////////////////////////////////////////////////////////////////////
     elif n == 612 or n == 611:
         pyxel.rect(0, 100, 128, 63, 0)
         if self.items2[6] == 1:
             self.Draw_fonts(self.text_list["238"],5, 105)
             self.MapEvents_ctr(13, 0)
         else:
             self.Draw_fonts(self.text_list["101"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)         
     
     elif n == 705:
         self.event_cnt = True
         self.MapEvents_ctr(14, 200)
         pyxel.rect(0, 60, 128, 83, 0)
         pyxel.rect(0, 42, 18, 20, 0)
         pyxel.rect(18, 50, 110, 10, 0)
         pyxel.blt(2,44,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 52)
         self.Draw_fonts(self.text_list["500"],5, 65)
         self.Draw_fonts(self.text_list["501"],5, 76)
         self.Draw_fonts(self.text_list["502"],5, 87)
         #self.Draw_fonts(self.text_list["422"],5, 98)
         #self.Draw_fonts(self.text_list["422"],5, 109)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)          
     
     elif n == 7051:
         self.event_cnt = True
         pyxel.rect(0, 60, 128, 83, 0)
         pyxel.rect(0, 42, 18, 20, 0)
         pyxel.rect(18, 50, 110, 10, 0)
         pyxel.blt(2,44,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 52)
         self.Draw_fonts(self.text_list["503"],5, 65)
         self.Draw_fonts(self.text_list["504"],5, 76)
         self.Draw_fonts(self.text_list["505"],5, 87)
         self.Draw_fonts(self.text_list["506"],5, 98)
         #self.Draw_fonts(self.text_list["422"],5, 109)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)               
     
     elif n == 7052:
         self.event_cnt = True
         pyxel.rect(0, 60, 128, 83, 0)
         pyxel.rect(0, 42, 18, 20, 0)
         pyxel.rect(18, 50, 110, 10, 0)
         pyxel.blt(2,44,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 52)
         self.Draw_fonts(self.text_list["507"],5, 65)
         self.Draw_fonts(self.text_list["508"],5, 76)
         self.Draw_fonts(self.text_list["509"],5, 87)
         #self.Draw_fonts(self.text_list["506"],5, 98)
         #self.Draw_fonts(self.text_list["422"],5, 109)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                   
         
     elif n == 7053:
         self.event_cnt = True
         pyxel.rect(0, 60, 128, 83, 0)
         pyxel.rect(0, 42, 18, 20, 0)
         pyxel.rect(18, 50, 110, 10, 0)
         pyxel.blt(2,44,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 52)
         self.Draw_fonts(self.text_list["510"],5, 65)
         self.Draw_fonts(self.text_list["511"],5, 76)
         #self.Draw_fonts(self.text_list["509"],5, 87)
         #self.Draw_fonts(self.text_list["506"],5, 98)
         #self.Draw_fonts(self.text_list["422"],5, 109)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                           
         
     elif n == 7054:
         self.event_cnt = True
         pyxel.rect(0, 60, 128, 83, 0)
         pyxel.rect(0, 42, 18, 20, 0)
         pyxel.rect(18, 50, 110, 10, 0)
         pyxel.blt(2,44,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 52)
         self.Draw_fonts(self.text_list["512"],5, 65)
         self.Draw_fonts(self.text_list["513"],5, 76)
         self.Draw_fonts(self.text_list["514"],5, 87)
         #self.Draw_fonts(self.text_list["506"],5, 98)
         #self.Draw_fonts(self.text_list["422"],5, 109)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)              

     elif n == 7055:
         self.event_cnt = True
         pyxel.rect(0, 60, 128, 83, 0)
         pyxel.rect(0, 42, 18, 20, 0)
         pyxel.rect(18, 50, 110, 10, 0)
         pyxel.blt(2,44,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 52)
         self.Draw_fonts(self.text_list["515"],5, 65)
         self.Draw_fonts(self.text_list["516"],5, 76)
         self.Draw_fonts(self.text_list["517"],5, 87)
         #self.Draw_fonts(self.text_list["506"],5, 98)
         #self.Draw_fonts(self.text_list["422"],5, 109)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                 
         
     elif n == 7056:
         self.event_cnt = True
         pyxel.rect(0, 60, 128, 83, 0)
         pyxel.rect(0, 42, 18, 20, 0)
         pyxel.rect(18, 50, 110, 10, 0)
         pyxel.blt(2,44,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 52)
         self.Draw_fonts(self.text_list["518"],5, 65)
         self.Draw_fonts(self.text_list["519"],5, 76)
         self.Draw_fonts(self.text_list["520"],5, 87)
         #self.Draw_fonts(self.text_list["506"],5, 98)
         #self.Draw_fonts(self.text_list["422"],5, 109)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                 

     elif n == 7057:
         self.event_cnt = True
         pyxel.rect(0, 60, 128, 83, 0)
         pyxel.rect(0, 42, 18, 20, 0)
         pyxel.rect(18, 50, 110, 10, 0)
         pyxel.blt(2,44,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 52)
         self.Draw_fonts(self.text_list["521"],5, 65)
         self.Draw_fonts(self.text_list["522"],5, 76)
         self.Draw_fonts(self.text_list["523"],5, 87)
         #self.Draw_fonts(self.text_list["506"],5, 98)
         #self.Draw_fonts(self.text_list["422"],5, 109)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                     
         
     elif n == 7058:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 83, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 82)
         self.Draw_fonts(self.text_list["524"],5, 95)
         self.Draw_fonts(self.text_list["525"],5, 106)
         #self.Draw_fonts(self.text_list["523"],5, 87)
         #self.Draw_fonts(self.text_list["506"],5, 98)
         #self.Draw_fonts(self.text_list["422"],5, 109)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                              
         
     elif n == 7059:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 83, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 82)
         self.Draw_fonts(self.text_list["526"],5, 95)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)               
         
     elif n == 7060:
         self.event_cnt = False
         pyxel.rect(0, 90, 128, 83, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 82)
         self.Draw_fonts(self.text_list["527"],5, 95)
         self.Draw_fonts(self.text_list["528"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                      
         
     elif n == 738 or n == 739 or n == 770 or n == 771:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 63, 0)
         self.Draw_fonts(self.text_list["2010"],5, 95)
         pyxel.text(7, 106, "Y = YES", 7)                        
         pyxel.text(7, 116, "N = NO", 7)     
         if pyxel.btnp(pyxel.KEY_Y):
             self.movie_count = 7700
             self.game_end = True
             #self.Save_data()
         elif pyxel.btnp(pyxel.KEY_N):
             self.movie_count = 7701
             
     elif n == 7700:
         self.event_cnt = False
         pyxel.cls(0)
         self.Draw_fonts(self.text_list["2011"],2, 15)
         self.Draw_fonts(self.text_list["2012"],2, 35)
         self.Draw_fonts(self.text_list["2013"],2, 45)
         self.Draw_fonts(self.text_list["2014"],2, 55)
         self.Draw_fonts(self.text_list["2015"],2, 65)
         self.Draw_fonts(self.text_list["2016"],2, 75)
         self.Draw_fonts(self.text_list["2017"],2, 85)
         self.Draw_fonts(self.text_list["2018"],2, 95)
         pyxel.text(5, 110, "Thank you for playing!!", 
                    pyxel.frame_count % 16)              
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)          

     elif n == 7701:
         self.event_cnt = True
         pyxel.rect(0, 90, 128, 83, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 82)
         self.Draw_fonts(self.text_list["529"],5, 95)
         self.Draw_fonts(self.text_list["530"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)        

     elif n == 7702:
         self.event_cnt = False
         self.MapEvents_ctr(14, 210)
         if self.enemy_crt_flug == False:
             self.enemys.clear()
             new_enemy = Enemy(6*8, 8*8, 64, 24)
             new_enemy.enemy_m = 1
             new_enemy.enemy_h = 400
             self.enemys.append(new_enemy)
             self.enemy_crt_flug = True              
         pyxel.rect(0, 90, 128, 83, 0)
         pyxel.rect(0, 72, 18, 20, 0)
         pyxel.rect(18, 80, 110, 10, 0)
         pyxel.blt(2,74,1,144,240,16,16,14)
         self.Draw_fonts(self.text_list["306"],20, 82)
         self.Draw_fonts(self.text_list["531"],5, 95)
         self.Draw_fonts(self.text_list["532"],5, 105)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                        
     #////////////////////////////////////////////////////////////////////////
     
     #Extra Area///////////////////////////////////////////////////////////////
     elif n == 550:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["102"],5, 105)
         self.MapEvents_ctr(0, 11)
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)     
     elif n == 442:
         pyxel.rect(0, 100, 128, 63, 0)
         self.Draw_fonts(self.text_list["157"],5, 105)
         self.MapEvents_ctr(0, 11)
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
     elif n == 357:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["142"],0, 105)
         self.Draw_fonts(self.text_list["304"],20, 92)
         self.event_cnt = True
         pyxel.blt(2,84,0,160,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3571:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["143"],0, 105)
         self.Draw_fonts(self.text_list["304"],20, 92)
         self.event_cnt = False
         pyxel.blt(2,84,0,160,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 358:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["144"],0, 105)
         self.Draw_fonts(self.text_list["304"],20, 92)
         self.event_cnt = True
         pyxel.blt(2,84,0,176,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3581:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["145"],0, 105)
         self.Draw_fonts(self.text_list["304"],20, 92)
         self.event_cnt = False
         pyxel.blt(2,84,0,176,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 360:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["146"],0, 105)
         self.Draw_fonts(self.text_list["302"],20, 92)
         self.event_cnt = True
         pyxel.blt(2,84,0,128,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3601:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["147"],0, 105)
         self.Draw_fonts(self.text_list["302"],20, 92)
         self.event_cnt = False
         pyxel.blt(2,84,0,128,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 359:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["148"],0, 105)
         self.Draw_fonts(self.text_list["303"],20, 92)
         self.event_cnt = True
         pyxel.blt(2,84,0,144,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3591:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["149"],0, 105)
         self.Draw_fonts(self.text_list["303"],20, 92)
         self.event_cnt = False
         pyxel.blt(2,84,0,144,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 361:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         if self.text_key_flug == False:
             tn = randint(2, 4)
             self.text_key = str(210 + tn)
             self.text_key_flug = True
         self.Draw_fonts(self.text_list[self.text_key],0, 105)
         self.Draw_fonts(self.text_list["305"],20, 92)
         pyxel.blt(2,84,0,208,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 362:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         if self.text_key_flug == False:
             tn = randint(2, 4)
             self.text_key = str(210 + tn)
             self.text_key_flug = True
         self.Draw_fonts(self.text_list[self.text_key],0, 105)
         self.Draw_fonts(self.text_list["305"],20, 92)
         pyxel.blt(2,84,0,192,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 363:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["216"],0, 105)
         self.Draw_fonts(self.text_list["305"],20, 92)
         self.event_cnt = True
         pyxel.blt(2,84,0,208,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3631:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["217"],0, 105)
         self.Draw_fonts(self.text_list["305"],20, 92)
         self.event_cnt = False
         pyxel.blt(2,84,0,208,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 364:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["218"],0, 105)
         self.Draw_fonts(self.text_list["305"],20, 92)
         self.event_cnt = True
         pyxel.blt(2,84,0,208,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3641:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["219"],0, 105)
         self.Draw_fonts(self.text_list["305"],20, 92)
         self.event_cnt = False
         pyxel.blt(2,84,0,208,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 365:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         if self.enemy_crt_flug == False:
             self.t_cnt = randint(1, 3)
             
         if ( (self.items5[1] == 1) or (self.items5[2] == 1) or
            (self.items5[3] == 1) ):
             if  self.items6[0] == 1:
                 self.Draw_fonts(self.text_list["254"],0, 105)
                 self.t_cnt = 4
             elif self.t_cnt == 1:
                 self.Draw_fonts(self.text_list["250"],0, 105)
             elif self.t_cnt == 2:
                 self.Draw_fonts(self.text_list["251"],0, 105)
             elif self.t_cnt == 3:
                 self.Draw_fonts(self.text_list["252"],0, 105)
         elif self.items5[0] == 1:
             self.Draw_fonts(self.text_list["224"],0, 105)
         else:
             self.Draw_fonts(self.text_list["220"],0, 105)
         self.Draw_fonts(self.text_list["306"],20, 92)
         self.enemy_crt_flug = True
         self.event_cnt = True
         pyxel.blt(2,84,0,112,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3651:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["221"],0, 105)
         self.Draw_fonts(self.text_list["306"],20, 92)
         self.event_cnt = True
         pyxel.blt(2,84,0,112,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3652:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["222"],0, 105)
         self.Draw_fonts(self.text_list["306"],20, 92)
         self.event_cnt = True
         pyxel.blt(2,84,0,112,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3653:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["223"],0, 105)
         self.Draw_fonts(self.text_list["306"],20, 92)
         self.event_cnt = False
         pyxel.blt(2,84,0,112,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
     elif n == 3654:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         if self.t_cnt == 1:
             self.Draw_fonts(self.text_list["2501"],0, 105)
         elif self.t_cnt == 2:
             self.Draw_fonts(self.text_list["2511"],0, 105)
         elif self.t_cnt == 3:
             self.Draw_fonts(self.text_list["2521"],0, 105)
         else:
             self.Draw_fonts(self.text_list["225"],0, 105)
             self.event_cnt = False
         self.Draw_fonts(self.text_list["306"],20, 92)
         pyxel.blt(2,84,0,112,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)   
         
     elif n == 3655:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["253"],0, 105)
         self.event_cnt = False
         self.Draw_fonts(self.text_list["306"],20, 92)
         pyxel.blt(2,84,0,112,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)            
         
     elif n == 3656:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["255"],0, 105)
         self.event_cnt = True
         self.Draw_fonts(self.text_list["306"],20, 92)
         pyxel.blt(2,84,0,112,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                     
         
     elif n == 3657:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["256"],0, 105)
         self.event_cnt = True
         self.Draw_fonts(self.text_list["306"],20, 92)
         pyxel.blt(2,84,0,112,208,16,16,14)  
         pyxel.text(5, 120, "Press SPACE-KEY to continue...", 
                    pyxel.frame_count % 16)                     

     elif n == 3658:
         pyxel.rect(0, 100, 128, 63, 0)
         pyxel.rect(0, 82, 18, 20, 0)
         pyxel.rect(18, 90, 110, 10, 0)
         self.Draw_fonts(self.text_list["257"],0, 105)
         self.event_cnt = False
         self.Draw_fonts(self.text_list["306"],20, 92)
         pyxel.blt(2,84,0,112,208,16,16,14)  
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
             if n == 3661:
                 self.movie_flug = True
             elif n == 3682:
                 self.b3_l = True
                 self.movie_flug = False
             elif n == 381 or n == 382 or n == 413 or n == 414:
                 if self.set_para2 == 1:
                     self.set_para = 1
                 self.movie_flug = False
             elif n == 445 or n == 446 or n == 477 or n == 478:
                 if self.set_para2 == 2:
                     self.set_para = 2
                 self.movie_flug = False           
             elif n == 443 or n == 444 or n == 475 or n == 476:
                 if self.set_para2 == 3:
                     self.set_para = 3
                 self.movie_flug = False            
             else:
                 self.movie_flug = False
             #text count reset
             self.t_cnt = 0
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
#------------------------------------------------------------------------------                
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
            elif n == 1006:
                self.movie_count = 1007                
            elif n == 1010:
                self.movie_count = 1011
            elif n == 1011:
                self.movie_count = 1012
            elif n == 1012:
                self.movie_count = 1013
            elif n == 1015:
                self.movie_count = 1016                
            elif n == 1016:
                self.movie_count = 1017    
            elif n == 1020:
                self.movie_count = 1021
            elif n == 1021:
                self.movie_count = 1022
            elif n == 1022:
                self.movie_count = 1023                
            elif n == 1030:
                self.movie_count = 1031
            elif n == 1031:
                self.movie_count = 1032
            elif n == 1032:
                self.movie_count = 1033            
            elif n == 1040:
                self.movie_count = 1041
            elif n == 1041:
                self.movie_count = 1042
            elif n == 1042:
                self.movie_count = 1043  
#------------------------------------------------------------------------------
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
            elif n == 357:
                self.movie_count = 3571
            elif n == 358:
                self.movie_count = 3581
            elif n == 360:
                self.movie_count = 3601
            elif n == 359:
                self.movie_count = 3591
            elif n == 341:
                self.movie_count = 3411
            elif n == 363:
                self.movie_count = 3631
            elif n == 364:
                self.movie_count = 3641
            elif n == 365:
                if self.t_cnt == 4:
                    self.movie_count = 3656                    
                elif self.t_cnt == 1:
                    self.movie_count = 3654
                elif self.t_cnt == 2:
                    self.movie_count = 3654
                elif self.t_cnt == 3:
                    self.movie_count = 3654
                elif self.items5[0] == 1:
                    self.movie_count = 3654
                else:
                    self.movie_count = 3651
            elif n == 3654:
                if self.t_cnt == 1:
                    self.movie_count = 3655
                elif self.t_cnt == 2:
                    self.movie_count = 3655
                elif self.t_cnt == 3:
                    self.movie_count = 3655                    
            elif n == 3651:
                self.movie_count = 3652
            elif n == 3652:
                self.movie_count = 3653
            elif n == 3656:
                self.movie_count = 3657                
            elif n == 3657:
                self.movie_count = 3658                
            elif n == 345 or n == 346:
                self.movie_count = 3461
            elif n == 3461:
                self.movie_count = 3462
            elif n == 366 or n == 367:
                self.movie_count = 3661
            elif n == 368:
                self.movie_count = 3681
            elif n == 3681:
                self.movie_count = 3682
            elif n == 610:
                self.movie_count = 6101
            elif n == 6101:
                self.movie_count = 6102
            elif n == 491:
                self.movie_count = 4912
            elif n == 4912:
                self.movie_count = 4913
            elif n == 4913:
                self.movie_count = 4914
            elif n == 705:
                self.movie_count = 7051
            elif n == 7051:
                self.movie_count = 7052
            elif n == 7052:
                self.movie_count = 7053
            elif n == 7053:
                self.movie_count = 7054
            elif n == 7054:
                self.movie_count = 7055
            elif n == 7055:
                self.movie_count = 7056
            elif n == 7056:
                self.movie_count = 7057
            elif n == 7057:
                self.movie_count = 7058
            elif n == 7058:
                self.movie_count = 7059
            elif n == 7059:
                self.movie_count = 7060                
            elif n == 7701:
               self.movie_count = 7702                           

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
     #Num select reset
         self.select_num = False
     #Camera status reset    
         #self.tile_camera_cn = 0
         #self.tile_camera_cnx = 0
         #self.tile_camera_cny = 0
     #Tirmer Start.
         if (n == 1007 or n == 1013 or n == 1017 or n == 1023 or
            n == 1033 or n == 1043):
             self.timer_f = True
    
         if n == 1050:
             self.game_over = True     
             pyxel.clip()
             pyxel.load('assets/pknights.pyxres') #Map reset

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
                 data4.append(self.set_para)
                 data4.append(self.set_para2)
                 writer.writerow(data4)
                 
                 self.save_st = 1
     except:
         self.save_st = 2
                 
 def Load_data(self, n):
     data = []
     data_file = 'DATA/data_' + str(n) + '.csv'
     try:
         with open(data_file) as f:
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
         self.Player.weapon = int(data[3][0])
         self.set_para = int(data[3][1])
         self.set_para2 = int(data[3][2])
     except:
        self.load_st = 2
        
     #urikire logic
     for u1 in range(4):
         self.shop1.urikire[u1] = self.items[u1]
         self.shop2.urikire[u1] = self.items2[u1]
         self.shop3.urikire[u1] = self.items3[u1]
         self.shop4.urikire[u1] = self.items4[u1]
         self.shop5.urikire[u1] = self.items5[u1]
         self.shop6.urikire[u1] = self.items6[u1]
    

 def Map_Change_EF(self):
    self.map_ch_cn += 6
    if self.map_ch_fl == 1: 
        n = self.map_ch_cn
        pyxel.clip(64-n, 64-n, 0+n*2, 0+n*2)
        if self.map_ch_cn > 70:
            self.map_ch_fl = 0
            self.map_ch_cn = 0
            pyxel.clip()

#Tile_Map_Conversion----------------------------------------------------------    
 def Tile_cnv(self, x, y):
     m1 = pyxel.tilemap(0).pget(x, y)
     m = m1[0] + (m1[1] * 32)         
     return m

 def Tile_cnv_set(self, x, y, t):
     t0 = t[0]
     t1 = len(t0) + 1
     t2 = int(t1 / 3)
     
     for i in range(t2):
         s1 = i * 3
         s2 = s1 + 3
         tm = t0[s1:s2]    
         tm2 = int(tm, 16)
         tm3 = int(tm2 / 32)
         tm4 = int(tm2 % 32)
         tm5 = format(tm3, 'x')
         tm6 = format(tm4, 'x')
         tmy = str(tm5).zfill(2)
         tmx = str(tm6).zfill(2)
         print(tmx)
         print(tmy)
         pyxel.tilemap(0).set(x + i, y, [tmx + tmy])         
#-----------------------------------------------------------------------------         

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
     self.last_p = [0, 0]
     self.last_p2 = [0, 0]
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
      if v2 == 1:
          self.enemy_h = 15
      elif v2 == 2:
          self.enemy_h = 30
      elif v2 == 3:
          self.enemy_h = 55
      elif v2 == 4:
          self.enemy_h = 25
      elif v2 == 5:
          self.enemy_h = 5
      elif v2 == 6:
          self.enemy_h = 50
      elif v2 == 7:
          self.enemy_h = 5
      else:
          self.enemy_h = 15
      if v2 == 12:
          self.enemy_h = 40
      else:
          self.enemy_h = 10 + v2*5
      self.enemy_d = 0
      self.enemy_da = 0
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
      elif n == 3:  
          self.price = [200,200,500,800]
      elif n == 4:  
          self.price = [400,400,800,1000]          
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