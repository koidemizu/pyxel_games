# -*- coding: utf-8 -*-

import pyxel

class App:
   def __init__(self): 
       self.move_r = 0 
       self.move_l = 0 
       self.atk_flug = 0 
       self.up_flug = 0 
       self.atk_count = 0 
       self.Player = Player(15, 19) 
       self.Hadou = []
       self.music_flug = False
       
       pyxel.init(64,35)

       pyxel.load('assets/sf.pyxres')
       
       pyxel.run(self.update, self.draw)
       
   def update(self):
       #BGM_Ctr
       if self.music_flug == False:
         pyxel.playm(0, loop=True)
         self.music_flug = True
       
       if pyxel.btnp(pyxel.KEY_Q):
           pyxel.quit()
           
       #Attack_action    
       if self.atk_flug == 0: 
           #Hado
           if pyxel.btnp(pyxel.KEY_SPACE): 
               if (self.move_r == 0 )and(self.move_l == 0):
                   if len(self.Hadou) < 1: 
                       self.atk_flug = 1
                       self.atk_count = 1
                       pyxel.play(1,10,loop=False)
                       new_Hadou = Hadou(self.Player.player_x + 8,
                                         self.Player.player_y + 3)
                       self.Hadou.append(new_Hadou)
           #Syoryu
           if pyxel.btnp(pyxel.KEY_V): 
               if (self.move_r == 0 )and(self.move_l == 0):
                   self.atk_flug = 1
                   self.atk_count = 1
                   self.up_flug = 1
                   pyxel.play(1,11,loop=False)
           #Move_right        
           if pyxel.btn(pyxel.KEY_RIGHT): 
               if self.Player.player_x < 51:
                   self.move_r = 1
                   self.Player.update(self.Player.player_x + 0.5,
                                    self.Player.player_y)
           else:
               self.move_r = 0
           #Move_left
           if pyxel.btn(pyxel.KEY_LEFT): 
               if self.Player.player_x > 0:
                   self.move_l = 1
                   self.Player.update(self.Player.player_x - 0.5,
                                            self.Player.player_y)
           else:
               self.move_l = 0
       else: 
           self.atk_count = self.atk_count + 1 
           if self.atk_count > 18: 
               self.atk_flug = 0
               self.atk_count = 0
               self.up_flug = 0
               
       #Hadou_move
       if len(self.Hadou) >= 1: 
           if self.Hadou[0].hadou_x < 70:
               x = self.Hadou[0].hadou_x + 1.5
               y = self.Hadou[0].hadou_y
               self.Hadou[0].update(x, y)
           else:
               del self.Hadou[0]

   def draw(self):
       pyxel.cls(13)
       
       #Draw tilemap
       pyxel.bltm(0,0,0,0,0,8,5)
       
       #Draw_player
       if self.move_r == 1:
           pyxel.blt(self.Player.player_x,self.Player.player_y,
                     0,0,16,16,16,3)
       elif self.move_l == 1:
           pyxel.blt(self.Player.player_x,self.Player.player_y,
                     0,16,16,16,16,3)
       elif self.atk_flug == 1:
           #Draw_upper
           if self.up_flug == 1:
               if self.atk_count < 9:
                   s = self.atk_count + 2
                   pyxel.blt(self.Player.player_x+0.1,self.Player.player_y-s,
                             0,0,32,16,20,3)
               else:
                   s = 18 - self.atk_count
                   pyxel.blt(self.Player.player_x,self.Player.player_y-s,
                             0,16,32,16,20,3)
           else:
               pyxel.blt(self.Player.player_x,self.Player.player_y,
                         0,16,0,16,16,3)
       else:
           pyxel.blt(self.Player.player_x,self.Player.player_y,0,0,0,16,16,3)
       
       #Draw_hadou
       if len(self.Hadou) >= 1:
           pyxel.blt(self.Hadou[0].hadou_x,self.Hadou[0].hadou_y,
                     0,32,0,8,8,3)
       
       
       
class Player:
   def __init__(self, x, y):
       self.player_x = x
       self.player_y = y
   def update(self, x, y):
       self.player_x = x
       self.player_y = y
       
class Hadou:
   def __init__(self, x, y):
       self.hadou_x = x
       self.hadou_y = y
   def update(self, x, y):
       self.hadou_x = x
       self.hadou_y = y

       
App()