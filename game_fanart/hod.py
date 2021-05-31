# -*- coding: utf-8 -*-
import pyxel
from random import randint, randrange

class App:
 def __init__(self):
     #bullet
     self.blt = 6
     
     #Player Life
     self.p_lf = 4
     
     #Enemy
     self.znb = []
     new_z = []
     for n in range(randint(1,3)):
         new_z.append(ZNB(randint(5+(40*n),25+(40*n)),
                              randint(15,35),
                              1, randint(0, 1)))
     for i2 in range(len(new_z)):
         self.znb.append(new_z[i2])
         
     #Effect controll
     self.r_ef = 0
     self.b_ef = []
     self.p_dm_r = 0
     
     #Game status
     self.game_st = 0
     
     #Image read
     pyxel.init(128,128, caption="hod", scale=5,
                fps = 30,)
     pyxel.load('assets/znb.pyxres')
     pyxel.run(self.update, self.draw)
 
 def update(self):
     #Game start logic
     if self.game_st == 0:
         if pyxel.btnp(pyxel.KEY_S):
             self.game_st= 1
     elif self.game_st == 1:
         self.game_starting() #Main logic
         
     #Debug
     if pyxel.btnp(pyxel.KEY_R):
         self.znb = []
         new_z = []
         for n in range(randint(1,3)):
             new_z.append(ZNB(randint(5+(40*n),25+(40*n)),
                              randint(15,35),
                              1, randint(0, 1)))
         for i2 in range(len(new_z)):
             self.znb.append(new_z[i2])
         self.p_lf = 4
         
 def game_starting(self):
     #Reload effect controll
     self.r_ef = 0
     
     #Damage effect controll
     if self.p_dm_r > 0:
         self.p_dm_r -= 1
     
     #Enemy controll
     for z in range(len(self.znb)):
         #Enemy update
         self.znb[z].update()
         
         #Enemy line change
         if self.znb[z].mv_cn <= 0:
             self.znb[z].lnch()
             self.znb[z].mv_cn = 100
             
         #Enemy attack
         if self.znb[z].atk_cn <= 0 and self.p_dm_r <= 0:
             self.p_lf -= 1
             self.p_dm_r = 60
             
         #Hit check for back line
         if self.znb[z].pos_z == 1:
             for x in range(len(self.b_ef)):
                 if self.b_ef[x].t < 2 and self.b_ef[x].v == 1:
                     for i1 in range(randint(2, 5)):
                         a1=self.znb[z].hit_ch1(self.b_ef[x].pos_x,
                                               self.b_ef[x].pos_y)
                     if a1 == 1:
                         self.b_ef.append(Ef(self.b_ef[x].pos_x,
                                             self.b_ef[x].pos_y,2))
                         del self.b_ef[x]
                     break
         #Hit check for forward lone
         elif self.znb[z].pos_z == 2:
             for x2 in range(len(self.b_ef)):
                 if self.b_ef[x2].t < 2 and self.b_ef[x2].v == 1:
                     for i2 in range(randint(2, 5)):
                         a2=self.znb[z].hit_ch2(self.b_ef[x2].pos_x,
                                               self.b_ef[x2].pos_y)
                     if a2 == 1:
                         self.b_ef.append(Ef(self.b_ef[x2].pos_x,
                                             self.b_ef[x2].pos_y,2))
                         del self.b_ef[x2]
                         break
            
     #Enemy delete
     for z2 in range(len(self.znb)):
         if self.znb[z2].hp <= 0:
             del self.znb[z2]
             break
         
     #Reload
     if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
         if self.blt > 0:
             self.blt -= 1
             self.b_ef.append(Ef(pyxel.mouse_x,pyxel.mouse_y,1))
            
     #Shoot
     if pyxel.btnp(pyxel.MOUSE_RIGHT_BUTTON):
         self.blt = 6
         self.r_ef = 1
 
 def draw(self):
     pyxel.cls(0)
     if self.game_st == 0:
         self.title_draw()
     elif self.game_st == 1:
         self.game_draw()
         
 def title_draw(self):
     pyxel.blt(0,15,1,0,0,128,80)
     pyxel.text(28, 100, "Press \"S\" to start.", 7)
     
 def game_draw(self):
     #Draw tilemap
     pyxel.bltm(0,0,0,0,0,16,16)
     
     #Draw enemy line1
     for z1 in range(len(self.znb)):
         if self.znb[z1].pos_z == 1:
             self.znb[z1].draw1()
             
     #Draw enemy line2
     for z2 in range(len(self.znb)):
         if self.znb[z2].pos_z == 2:
             self.znb[z2].draw2()
     
     #Draw effect
     for e in range(len(self.b_ef)):
         self.b_ef[e].update()
         self.b_ef[e].draw()
         if self.b_ef[e].t < 0:
             del self.b_ef[e]
             break
     
     #Draw player life
     for l in range(self.p_lf):
         pyxel.blt(10+l*8,115,2,0,0,8,8,14)
         
     #Draw bullet
     for b in range(self.blt):
         pyxel.blt(1+b*7,100,2,8,0,8,8,14)
         
     if self.blt == 0:
         pyxel.text(2, 105, "RELOAD", 0)
         pyxel.text(3, 105, "RELOAD", 8)
         
     pyxel.text(0, 117, "1P", 0)
     pyxel.text(1, 117, "1P", 8)
     
     #Draw damage effect
     if self.p_dm_r > 30:
         pyxel.blt(50,50,2,208,0,24,40,14)
         
     #Draw mouse point
     pyxel.blt(pyxel.mouse_x-3,pyxel.mouse_y-4,2,16,0,16,16,14)
     
     if self.r_ef > 0:
         pyxel.cls(7)
         
     

class ZNB:
 def __init__(self,x,y,z,v):    
     self.pos_x = x
     self.pos_y = y     
     self.pos_z = z
     self.v = v
     self.yure = randint(0, 3)
     self.yuref = 0
     self.hp = 100
     self.atk_cn = randrange(400,800,100)
     self.atk_fl = False
     self.atk_r = 0
     self.atk_l = 0
     self.mv_cn = randrange(400,1200,100)
     
 def update(self):
     #Attack count reset
     if self.atk_cn <= 0:
         self.atk_cn = randrange(400,800,100)
         self.atk_r = 0
         self.atk_l = 0
         self.atk_fl = False
     
     #Line change count update
     if self.pos_z == 1:
         self.mv_cn -= randint(1, 15)
    
     #Attack action
     if self.pos_z == 2:
         self.atk_cn -= randint(1, 10)
         if self.atk_cn < 150 and self.atk_fl == False:
             self.atk_fl = True
             a = randint(1, 3)
             if a == 1:
                 self.atk_r = 1
             elif a == 2:
                 self.atk_l = 1
             elif a == 3:
                 self.atk_r = 1
                 self.atk_l = 1
     
     #Yure
     if self.yuref == 0:
         self.yure += 0.5
         if self.yure > 4:
             self.yuref = 1
     else:
         self.yure -= 0.5
         if self.yure < 0:
             self.yuref = 0
             
 def hit_ch1(self,x, y):
     #Head
     if ((self.pos_x+(self.yure/2) <= x <= self.pos_x+(self.yure/2) + 8) and
         (self.pos_y <= y <= self.pos_y + 8)):
         self.hp -= 100
         return 1
     #Body
     if ((self.pos_x-4+(self.yure/4)<= x <=self.pos_x-4+(self.yure/4)+16) and
         (self.pos_y+7+(self.yure/4)<= y <=self.pos_y+7+(self.yure/4) + 16)):
         self.hp -= 10
         return 1
     #Arm R
     if ((self.pos_x-10+(self.yure/2)<=x<=self.pos_x-10+(self.yure/2)+8) and
         (self.pos_y+8 <= y <= self.pos_y+24)):
         self.hp -= 5
         return 1
     #Arm L
     if ((self.pos_x+10+(self.yure/2)<=x<=self.pos_x+10+(self.yure/2)+8) and
         (self.pos_y+8 <= y <= self.pos_y+24)):
         self.hp -= 5
         return 1
     #Leg R
     if ((self.pos_x-3-(self.yure/4) <= x <= self.pos_x-3-(self.yure/4)+8) and
         (self.pos_y+22 <= y <= self.pos_y+38)):
         self.hp -= 5
         return 1
     #Leg L
     if ((self.pos_x+3-(self.yure/4) <= x <= self.pos_x+3-(self.yure/4)+8) and
         (self.pos_y+22 <= y <= self.pos_y+38)):
         self.hp -= 5
         return 1

 def hit_ch2(self,x, y):
     #Head
     if ((self.pos_x+(self.yure/2) <= x <= self.pos_x+(self.yure/2) + 16) and
         (self.pos_y <= y <= self.pos_y + 16)):
         self.hp -= 100
         return 1
     #Body
     if ((self.pos_x-3+(self.yure/3)<= x <=self.pos_x-3+(self.yure/3)+24) and
         (self.pos_y+14+(self.yure/3)<= y <=self.pos_y+14+(self.yure/3)+40)):
         self.hp -= 10
         return 1
     #Arm R
     if self.atk_r == 1:
         if ((self.pos_x-8+(self.yure/2)<=x<=self.pos_x-8+(self.yure/2)+8) and
             (self.pos_y-4 <= y <= self.pos_y-4+24)):
             self.hp -= 50
             return 1     
     else:
         if ((self.pos_x-11+(self.yure/2)<=x<=self.pos_x-11
              +(self.yure/2)+8)and
             (self.pos_y+17 <= y <= self.pos_y+17+24)):
             self.hp -= 5
             return 1
     #Arm L
     if self.atk_l == 1:
         if ((self.pos_x+16+(self.yure/2)<=x<=self.pos_x+16+(self.yure/2)+8) and
             (self.pos_y-4 <= y <= self.pos_y-4+24)):
             self.hp -= 50
             return 1
     else:
         if ((self.pos_x+19+(self.yure/2)<=x<=self.pos_x+19
              +(self.yure/2)+8) and
             (self.pos_y+17 <= y <= self.pos_y+17+24)):
             self.hp -= 5
             return 1
     #Leg R
     if ((self.pos_x-1-(self.yure/4) <= x <= self.pos_x-1-(self.yure/4)+8) and
         (self.pos_y+45 <= y <= self.pos_y+45+32)):
         self.hp -= 5
         return 1
     #Leg L
     if ((self.pos_x+11-(self.yure/4)<= x <=self.pos_x+11-(self.yure/4)+8)and
         (self.pos_y+45 <= y <= self.pos_y+45+32)):
         self.hp -= 5
         return 1
             
 def lnch(self):
     #Enemy line change
     if self.pos_z == 1:
         self.pos_z = 2
         self.pos_y += 20
     else:
         self.pos_z = 1
         self.pos_y -= 20
     
 def draw1(self):
     #Head
     pyxel.blt(self.pos_x+(self.yure/2),self.pos_y,0,0+40*self.v,16,8,8,14)
     #Body
     pyxel.blt(self.pos_x-4+(self.yure/4),self.pos_y+7+(self.yure/4),0,
               0+40*self.v,24,16,16,14)
     #Arm_R
     pyxel.blt(self.pos_x-10+(self.yure/2),self.pos_y+8,0,0+40*self.v,
               0,8,16,14)
     #Arm_L
     pyxel.blt(self.pos_x+10+(self.yure/2),self.pos_y+8,0,8+40*self.v,0,
               8,16,14)

     #Leg_R
     pyxel.blt(self.pos_x-3-(self.yure/4),self.pos_y+22,0,0+40*self.v,
               40,8,24,14)
     #Leg_L
     pyxel.blt(self.pos_x+5-(self.yure/4),self.pos_y+22,0,8+40*self.v,
               40,8,24,14)
     
 def draw2(self):
     #Head
     pyxel.blt(self.pos_x+(self.yure/2),self.pos_y,0,16+40*self.v,24,16,16,14)
     #Body
     pyxel.blt(self.pos_x-3+(self.yure/3),self.pos_y+14+(self.yure/3),0,
               16+40*self.v,40,24,32,14)
     #Arm_R
     if self.atk_r == 1:
         pyxel.blt(self.pos_x-8+(self.yure/2),self.pos_y-4,0,16+40*self.v,
                   0,8,-24,14)
     else:
         pyxel.blt(self.pos_x-11+(self.yure/2),self.pos_y+17,0,16+40*self.v,
                   0,8,24,14)
     #Arm_L
     if self.atk_l == 1:
         pyxel.blt(self.pos_x+16+(self.yure/2),self.pos_y-4,0,24+40*self.v,
                   0,8,-24,14)
     else:
         pyxel.blt(self.pos_x+19+(self.yure/2),self.pos_y+17,0,24+40*self.v,
                   0,8,24,14)

     #Leg_R
     pyxel.blt(self.pos_x+1-(self.yure/4),self.pos_y+45,0,16+40*self.v,
               72,8,32,14)
     #Leg_L
     pyxel.blt(self.pos_x+11-(self.yure/4),self.pos_y+45,0,24+40*self.v,
               72,8,32,14)
     
class Ef:
 def __init__(self,x,y,v):    
     self.pos_x = x
     self.pos_y = y     
     self.v = v
     self.t = 3
 def update(self):
     if self.v == 1:
         self.t -= 0.5
     elif self.v == 2:
         self.t -= 0.5
         self.pos_x += randint(-10,10)/5
         self.pos_y -= randint(-10,10)/5 
 def draw(self):
     if self.v == 1: 
         #bullet
         if self.t < 2:
             c = 7
         else:
             c = 10
         pyxel.circ(self.pos_x, self.pos_y, self.t, c)
     elif self.v == 2: 
         #blood
         pyxel.circ(self.pos_x, self.pos_y, self.t, 3)
     
App()

