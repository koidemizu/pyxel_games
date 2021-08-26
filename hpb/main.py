# -*- coding: utf-8 -*-

import pyxel

class App:
   def __init__(self):
       
       #Player status
       self.Player = Player(56, 56)
       self.player_move = 0    
       self.atc_flug = False   
       self.atc_count = 0      
       self.p_atc_x = 0      
       self.p_atc_y = 0        
       
       #Map status
       self.stage_flug = 1     
       self.map_count_x = 8   
       self.map_count_y = 14 
       self.game_start = False 
       self.map_x = 7*16
       self.map_y = 13*16
       self.map_move = 0
       
       pyxel.init(128,128)

       #Image read
       pyxel.load('assets/assets.pyxres')
       
       pyxel.run(self.update, self.draw)
       
   def update(self):
       if pyxel.btnp(pyxel.KEY_S):
         self.game_start = True
       if pyxel.btnp(pyxel.KEY_Q):
           pyxel.quit()
                   
       #Player controll
       self.Player_ctr()
     
   def draw(self):
       pyxel.cls(0)
       
       #Draw tilemap
       pyxel.bltm(0,0,0,0 + self.map_x,0 + self.map_y,16,16)
   
       #Draw player
       if self.Player.player_m == 0: #Player situation is right
           pyxel.blt(self.Player.player_x,self.Player.player_y,
                 0,0,0+self.Player.player_m2*8,8,8,14)
       elif self.Player.player_m == 1: #Player situation is left
           pyxel.blt(self.Player.player_x,self.Player.player_y,
                 0,8,0+self.Player.player_m2*8,8,8,14)
       elif self.Player.player_m == 2: #Player situation is up
           pyxel.blt(self.Player.player_x,self.Player.player_y,
                 0,16,0+self.Player.player_m2*8,8,8,14)
       elif self.Player.player_m == 3: #Player situation is down
               pyxel.blt(self.Player.player_x,self.Player.player_y,
                 0,24,0+self.Player.player_m2*8,8,8,14)
       
       #Draw title text
       if self.game_start == False:
          pyxel.cls(0)
          pyxel.text(35, 40, "PYXEL KNIGHTS", 7)
          pyxel.text(45, 70, "S = START ", 7)
          pyxel.text(45, 80, "Q = QUIT ", 7)
          

   
   def Player_ctr(self):
       
       #Get map coordinate
       x = 16*(self.map_count_x-1)
       y = 16*(self.map_count_y-1)

       #Get player coordinate        
       move_map_x = int(self.Player.player_x / 8 + x)
       move_map_y = int(self.Player.player_y / 8 + y)
       
       #Plyer move
       self.player_move = self.player_move + 1
       if self.player_move > 6:
       
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
                   if (self.Player.player_y - 8) < 0: #When map change
                       self.map_y = self.map_y - 16
                       self.Player.update(56, 120)
                       self.map_count_y = self.map_count_y - 1
                       self.map_move = 1
       
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
                       self.Player.update(56, 8)
                       self.map_count_y = self.map_count_y + 1
                       self.map_move = 1
               
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
                       self.Player.update(8, 56)
                       self.map_count_x = self.map_count_x + 1
                       self.map_move = 1
       
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
                   if (self.Player.player_x - 8) < 0: #When map change
                       self.map_x = self.map_x - 16
                       self.Player.update(120, 56)
                       self.map_count_x = self.map_count_x - 1
                       self.map_move = 1
       
       
   
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
       
       
   
App()