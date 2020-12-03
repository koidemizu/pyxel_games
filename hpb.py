# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:56:29 2020

@author: koshiba0824
"""

import pyxel
from random import randint

class APP:
  def __init__(self):
      self.Game_ctr = 0
      self.Stage_count = 0
      self.Stage_time = 0
      self.Mato = []
      self.Cara = []
      self.bangs = []
      self.hit_flug = 0
      self.score = 0
      self.Movie_flug = False
      pyxel.init(100, 100, caption="hpb")
      pyxel.load("assets/hpb.pyxres")
      pyxel.mouse(False)  
      pyxel.run(self.update, self.draw)

  def update(self):
      
    if self.Game_ctr == 0:
        if pyxel.btnp(pyxel.KEY_S):
              self.Game_ctr = 1
              self.Stage_count = 1
              self.Mato = []
              
    elif self.Game_ctr == 1:
        if pyxel.frame_count % 60 == 0:
            mato_s = randint(1, 4)
            for i in range(mato_s):
                new_mato = mato(randint(10, 90), 
                                randint(10, 75),
                                randint(1, 4), 5, 5)
                self.Mato.append(new_mato)
        
        if len(self.bangs) > 0:
            self.hit_flug += 1
            if self.hit_flug > 5:
                del self.bangs[0]
                self.hit_flug = 0
                
        for c1 in self.Cara:
            c1.update()
        for c2 in self.Cara:
            if ((c2.pos_x > 100) or (c2.pos_x < 0) or
               (c2.pos_y) > 100 or (c2.pos_y < 0)):
                del c2
                break
            
        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON)==True:
           mouse_x = pyxel.mouse_x
           mouse_y = pyxel.mouse_y
           mato_count = len(self.Mato)
           #self.shot_flug = self.shot_flug + 1
           for e in range (mato_count):
               if ((self.Mato[e].pos_x <= mouse_x 
                  <= self.Mato[e].pos_x + 16)and(self.Mato[e].pos_y 
                  <= mouse_y <= self.Mato[e].pos_y + 16)):
                   
                   new_bang = Bang(self.Mato[e].pos_x, 
                                     self.Mato[e].pos_y, self.Mato[e].v)
                   self.bangs.append(new_bang)
                   
                   new_cara = Cara(self.Mato[e].pos_x, 
                                     self.Mato[e].pos_y,
                                     randint(1, 4))
                   self.Cara.append(new_cara)
                   
                   #self.hit_flug = 0
                   if self.Mato[e].v == 1:
                       self.score += 10
                   elif self.Mato[e].v == 2:
                       self.score += 20
                   elif self.Mato[e].v == 3:
                       self.score += 30
                   elif self.Mato[e].v == 4:
                       self.score += 50
                   del self.Mato[e]
                   #self.score = self.score + 100
                   break#敵に当たったらbreak
               
        self.Stage_time += 1
        if self.Stage_time >= 700:
            self.Game_ctr = 2
            self.Stage_time = 0
            
    elif self.Game_ctr == 2:
        self.Stage_time += 1
        self.Mato = []
        self.Cara = []
        self.Movie_flug = True
        if self.Stage_time >= 100:
            self.Stage_time = 0
            self.Movie_flug = False
            self.Game_ctr = 3

    elif self.Game_ctr == 3:
        self.Stage_count += 1
        self.Game_ctr = 1
        if self.Stage_count == 5:
            self.Game_ctr = 99
            
    elif self.Game_ctr == 99:
        print("Game end.")
        
  def draw(self):
    pyxel.cls(0)
    if self.Game_ctr == 0:
        #Title screen
        pyxel.rect(0, 0, 100, 50, 6)
        for im in range (8):
            pyxel.blt(10+16*(im-1),15,1,144,0,16,79,6)
        pyxel.rect(0, 88, 100, 12, 13)
        pyxel.blt(5,18,1,112,0,32,72,6)
        pyxel.blt(60,18,1,112,0,32,72,6)
        pyxel.blt(23,45,1,64,16,48,48,6)
        pyxel.blt(31,28,1,72,64,32,24,6)
        
        pyxel.text(11, 94, "Press S-key to start", 0)
        pyxel.text(12, 94, "Press S-key to start", 9)
        
    elif self.Game_ctr == 1:
        if self.Stage_count == 1:
            pyxel.blt(0,0,2,0,0,100,100)
        elif self.Stage_count == 2:
            pyxel.blt(0,0,2,100,0,100,100)
        elif self.Stage_count == 3:
            pyxel.blt(0,0,2,0,100,100,100)
        elif self.Stage_count == 4:
            pyxel.blt(0,0,2,100,100,100,100)
            
        v = self.Stage_count
        for m in self.Mato:
             pyxel.blt(m.pos_x, m.pos_y, 
                       0, 16*(m.v-1), 16*(v-1), 16, 16, 14)
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 1, 16, 0, 8, 8, 6) 
        
        for i in self.bangs:
           pyxel.blt(i.bang_x, i.bang_y, 0, 
                     16*(i.bang_v - 1), 16*(self.Stage_count-1)+64,
                     16, 16, 14) 
        
        for c in self.Cara:
           pyxel.blt(c.pos_x, c.pos_y, 1, 16*(c.v1-1), self.Stage_count*16,
                     16, 16, 6) 
           
        pyxel.rect(37, 91, 25, 9, 7)
        pyxel.rectb(36, 90, 27, 10, 0)
        pyxel.text(38, 93, str(self.score), pyxel.frame_count % 16)
    elif self.Game_ctr == 2:
        if self.Stage_count == 1:
            pyxel.blt(0,0,2,0,0,100,100)
        elif self.Stage_count == 2:
            pyxel.blt(0,0,2,100,0,100,100)
        elif self.Stage_count == 3:
            pyxel.blt(0,0,2,0,100,100,100)
        elif self.Stage_count == 4:
            pyxel.blt(0,0,2,100,100,100,100)
        if self.Movie_flug == True:
           pyxel.blt(23, 45, 1, 32, 0, 48, 16, 6)
           pyxel.blt(50, 60, 1, 0, self.Stage_count*16,
                     16, 16, 6)  
           pyxel.text(25, 49, "Next Stage!", pyxel.frame_count % 16)
    elif self.Game_ctr == 99:
        pyxel.cls(1)
        pyxel.text(17, 5, "Happy Birthday!!", pyxel.frame_count % 16)
        pyxel.text(17, 15, "Score: " + str(self.score), pyxel.frame_count % 16)
        pyxel.blt(60, 15, 0, 0, 48, 16, 16, 14) 
        for v in range(4):
            for c in range(5):
                pyxel.blt(16*c, 50+((v-1)*16), 1, 0+((c-1)*16), 32+((v-1)*16),
                          16, 16, 6) 

class mato:
    def __init__(self, x, y, v, m1, m2):
        self.pos_x = x
        self.pos_y = y
        self.v = v
        self.m_1 = m1
        self.m_2 = m2

class Bang:
 def __init__(self, x, y, v):
     self.bang_x = x
     self.bang_y = y   
     self.bang_v = v   
     
class Cara:
 def __init__(self, x, y, v1):
     self.pos_x = x
     self.pos_y = y
     self.time = 0
     self.v1 = v1
     self.v2 = 1
 def update(self):
     self.time += 1
     if self.time % 15 == 0:
         if self.v2 == 1:
            self.v2 = 2
         elif self.v2 == 2:
             self.v2 = 1
     if self.v1 == 1:
         if self.v2 == 1:
           self.pos_x += 1
           self.pos_y += 1
         if self.v2 == 2:
           self.pos_x += 1
           self.pos_y -= 1
     elif self.v1 == 2:
         if self.v2 == 1:
           self.pos_x -= 1
           self.pos_y += 1
         if self.v2 == 2:
           self.pos_x -= 1
           self.pos_y -= 1
     elif self.v1 == 3:
         if self.v2 == 1:
           self.pos_x += 1
           self.pos_y += 1
         if self.v2 == 2:
           self.pos_x -= 1
           self.pos_y += 1
     elif self.v1 == 4:
         if self.v2 == 1:
           self.pos_x += 1
           self.pos_y -= 1
         if self.v2 == 2:
           self.pos_x -= 1
           self.pos_y -= 1
             
     
     
     
     
     
     
     
     
     
     
        
          
APP()