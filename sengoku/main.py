# -*- coding: utf-8 -*-
#main.py

import pyxel
import csv
from random import randint
from module import Fontlist, Text_list, Game_status, Text_list_en

class App:
 def __init__(self):
     #Language set
     self.lng = "none"
     
     #Font set
     self.font_list = Fontlist.text_j()
     
     #Costs set
     self.costs = Game_status.costs_get()
     
     #System status
     self.craft = Craft()
     self.window_ctr = -1
     self.txt_ctr = 0
     self.inf_ctr = 999
     self.update_list = []
     self.update_tgt = 0
     self.turn = 1
     self.map_ch_cn = 0
     self.map_ch_fl = 0
     
     #Player status
     self.kome = 0
     self.sikin = 0
     self.heisi = 0
     self.roryoku = 500
     self.rend = 1
     self.gankyo = 1
     self.samurai = 0
     self.gaiko = 0
     self.ninjya = 0
     self.syonin = 0
     
     #Gaiko status
     self.answer_list = []
     self.answer_tgt = 0
     self.msg_num = 0
     
     #Kassen status
     self.k_cnt = 0
     self.k_end = False
     self.k_end_msg = 0
     self.k_kome = 0
     self.k_sikin = 0
     self.k_hei = 0
     self.k_hei2 = 0
     self.enemy_tgt = 0
     
     #Ending status
     self.end_num = 0
     self.end_flug = False
     
     #Base window create
     pyxel.init(128,128, caption="sengoku", scale=5,quit_key=pyxel.KEY_NONE)
     
     #Mouse visivle
     pyxel.mouse(True)

     #Image read
     pyxel.load('assets/assets.pyxres')
     
     pyxel.run(self.update, self.draw)
     
 def update(self):
     
     #Select language
     if self.window_ctr == -1:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((0 < x < 63)  and (114 < y < 128)):
                 #Text list set
                 if self.lng == "none":
                     self.text_list = Text_list.text_get()
                     self.lng = "ja"
             elif ((64 < x < 128)  and (114 < y < 128)):
                 if self.lng == "none":
                     self.text_list = Text_list_en.text_get()
                     self.lng = "en"
                  #Daimyo status
             self.dst1 = Game_status.oda(self.lng)
             self.daimyo1 = Daimyo(self.dst1["kome"],self.dst1["sikin"],
                                self.dst1["heisi"],self.dst1["sei"],
                                self.dst1["mei"],self.dst1["msg"],0)
             self.dst2 = Game_status.imagawa(self.lng)
             self.daimyo2 = Daimyo(self.dst2["kome"],self.dst2["sikin"],
                                self.dst2["heisi"],self.dst2["sei"],
                                self.dst2["mei"],self.dst2["msg"],30)
             self.daimyo_flug = 0
             self.window_ctr = 999
                 
     #Main window
     elif self.window_ctr == 0:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             x2 = int(x/8)
             y2 = int(y/8)
             v = pyxel.tilemap(0).get(x2, y2)
             self.craft.get_pos(x2, y2, v)
             if v == 6:
                 self.window_ctr = 99
             #elif v == 10:
              #   self.window_ctr = 95
            # elif v == 17:
             #    self.window_ctr = 97
             else:
                 self.window_ctr = 1
             self.txt_ctr = v
     #Craft window
     elif self.window_ctr == 1:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((0 < x < 64)  and (114 < y < 128)):
                 if ((self.txt_ctr < 3) or (self.txt_ctr == 5) or
                  (32 <= self.txt_ctr <= 34)) :
                    self.update_tgt = 0
                    self.window_ctr = 2
                 elif ((self.txt_ctr == 3) or (64 <= self.txt_ctr <= 66)) :
                     self.update_tgt = 5
                     self.window_ctr = 2
                 #Target = Jyounai
                 elif self.txt_ctr == 8:
                     if self.samurai == 0:
                         self.update_tgt = 17
                         self.window_ctr = 2
                     elif self.gaiko == 0:
                         self.update_tgt = 18
                         self.window_ctr = 2
                     elif self.ninjya == 0:
                         self.update_tgt = 19
                         self.window_ctr = 2
                     elif self.syonin == 0:
                         self.update_tgt = 20
                         self.window_ctr = 2
                     else:
                         self.window_ctr = 3
                #Target = Jyoumon
                 elif self.txt_ctr == 10:
                     self.update_tgt = 171
                     self.window_ctr = 2 
                #Target = Samuraidaisyo
                 elif self.txt_ctr == 17:
                     self.update_tgt = 1271
                     self.window_ctr = 2 
                #Target = Gaikokan
                 elif self.txt_ctr == 18:
                     self.update_tgt = 133
                     self.window_ctr = 2
                 #Target = Ninja
                 elif self.txt_ctr == 19:
                     self.update_tgt = 150
                     self.window_ctr = 2
                 #Target = Shounin
                 elif self.txt_ctr == 20:
                     self.update_tgt = 140
                     self.window_ctr = 2
                 else:
                     self.window_ctr = 3
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 0
     #Craft window2
     elif self.window_ctr == 2:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             l = len(self.update_list)
             for i in range(l):
                 if ((0 < x < 64)  and (55+i*10 < y < 65+i*10)):
                     self.update_tgt = self.update_list[i]
             if ((0 < x < 64)  and (100 < y < 114)):
                 #Jyoumon
                 if self.txt_ctr == 10:
                     if self.update_tgt == 171:
                         self.enemy_tgt = 1
                     elif self.update_tgt == 172:
                         self.enemy_tgt = 2    
                     elif self.update_tgt == 173:
                         self.enemy_tgt = 9
                     
                     t = str(self.update_tgt)
                     c = self.costs[t]
                     if self.roryoku >= c:
                         self.roryoku = self.roryoku - c
                         self.k_cnt = 1000
                         self.inf_ctr = 179
                         self.window_ctr = 100
                     else:
                         self.window_ctr = 4
                 #Syonin
                 elif self.txt_ctr == 20:
                     t = str(self.update_tgt)
                     c = self.costs[t]
                     if self.sikin >= c:
                         self.sikin = self.sikin - c
                         if self.update_tgt == 140:
                             self.kome += randint(500, 2000)
                             self.inf_ctr = 1402
                         elif self.update_tgt == 141:
                             self.kome += randint(2500, 5000)
                             self.inf_ctr = 1402
                         elif self.update_tgt == 142:
                             self.heisi += randint(250, 1500)
                             self.inf_ctr = 1401
                         elif self.update_tgt == 143:
                             self.heisi += randint(1500, 5000)
                             self.inf_ctr = 1401
                         self.window_ctr = 100
                     else:
                         self.inf_ctr = 1403
                         self.window_ctr = 100
                 #Ninja
                 elif self.txt_ctr == 19:
                     t = str(self.update_tgt)
                     c = self.costs[t]
                     if self.roryoku >= c:
                         self.roryoku = self.roryoku - c
                         self.inf_ctr = 159
                         self.window_ctr = 100
                     else:
                         self.window_ctr = 4
                 #Samuraidaisyo
                 elif self.txt_ctr == 17:
                     t = str(self.update_tgt)
                     c = self.costs[t] * int((self.rend+self.gankyo)/2)
                     if self.roryoku >= c:
                         self.roryoku = self.roryoku - c
                         if self.update_tgt == 1272:
                             self.gankyo = self.gankyo + randint(1, 5)
                         elif self.update_tgt == 1271:
                             self.rend = self.rend + randint(1, 5)
                         self.inf_ctr = 128
                         self.window_ctr = 100
                     else:
                         self.window_ctr = 4
                 else:
                     t = str(self.update_tgt)
                     c = self.costs[t]
                     if self.roryoku >= c:
                         #Gaikokan#################################
                         if self.update_tgt == 133:
                             self.roryoku = self.roryoku - c
                             self.daimyo1.yuko += randint(3, 10)
                             self.inf_ctr = 134
                             self.window_ctr = 100
                         elif self.update_tgt == 1331:
                             self.roryoku = self.roryoku - c
                             self.daimyo2.yuko += randint(3, 10)
                             self.inf_ctr = 134
                             self.window_ctr = 100
                         ##########################################
                         else:
                             self.craft.update_pos(self.update_tgt, c)
                             self.roryoku = self.roryoku - c
                             self.window_ctr = 0
                             if self.update_tgt == 17:
                                 self.samurai = 1
                             if self.update_tgt == 18:
                                 self.gaiko = 1
                             if self.update_tgt == 19:
                                 self.ninjya = 1
                             if self.update_tgt == 20:
                                 self.syonin = 1
                     else:
                         self.window_ctr = 4
             if ((64 < x < 128)  and (100 < y < 114)):
                 self.window_ctr = 0
     #Cannot craft1
     elif self.window_ctr == 3:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 0
     #Cannot craft2
     elif self.window_ctr == 4:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 0
                 
     #Turn change
     elif self.window_ctr == 98:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 if self.k_cnt >= 999:
                     self.window_ctr = 201
                 elif ((self.daimyo1.event_flug == True) and
                    (self.daimyo2.event_flug == True)):
                     self.daimyo_flug = randint(1, 2)
                     self.window_ctr = 101
                     self.msg_num = randint(1, 3)
                 elif self.daimyo1.event_flug == True:
                     self.daimyo_flug = 1
                     self.window_ctr = 101
                     self.msg_num = randint(1, 3)
                 elif self.daimyo2.event_flug == True:
                     self.daimyo_flug = 2
                     self.window_ctr = 101
                     self.msg_num = randint(1, 3)
                 elif self.k_cnt >= 35:
                     self.enemy_tgt = 9
                     self.window_ctr = 201
                 else:
                     self.window_ctr = 0
     #Siro
     elif self.window_ctr == 99:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 0
             if ((0 < x < 64)  and (114 < y < 128)):
                 self.map_ch_fl = 1
                 self.Turn_change()
                 self.window_ctr = 98
                 #self.window_ctr = 0
             if ((0 < x < 64)  and (100 < y < 114)):
                 self.Save_data()
                 self.window_ctr = 100
             if ((64 < x < 128)  and (100 < y < 114)):
                 self.Load_data()
                 self.window_ctr = 100
     #Information window
     elif self.window_ctr == 100:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 0
                 self.inf_ctr = 999
     #Gaiko
     elif self.window_ctr == 101:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 102
                 self.answer_tgt = 116
     #Gaiko2
     elif self.window_ctr == 102:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             l = len(self.answer_list)
             for i in range(l):
                 if ((0 < x < 64)  and (73+i*10 < y < 83+i*10)):
                     self.answer_tgt = self.answer_list[i]
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 103
                 #Daimyo1
                 if self.daimyo_flug == 1:
                     if self.msg_num == 1:
                         if self.answer_tgt == 116:
                             h = int(self.kome*0.2)
                             if h > 0:
                                 self.daimyo1.yuko += 10
                                 self.daimyo2.yuko -= 2
                             self.kome -= h
                             self.daimyo1.kome += h
                             if self.kome <= 0:
                                 self.kome = 0
                         elif self.answer_tgt == 117:
                             self.daimyo1.yuko -= 5
                     elif self.msg_num == 2:
                         if self.answer_tgt == 116:
                             h = int(self.sikin*0.2)
                             if h > 0:
                                 self.daimyo1.yuko += 10
                                 self.daimyo2.yuko -= 2
                             self.sikin -= h
                             self.daimyo1.sikin += h
                             if self.sikin <= 0:
                                 self.sikin = 0
                         elif self.answer_tgt == 117:
                             self.daimyo1.yuko -= 5
                     elif self.msg_num == 3:
                         if self.answer_tgt == 116:
                             h = int(self.heisi*0.2)
                             if h > 0:
                                 self.daimyo1.yuko += 10
                                 self.daimyo2.yuko -= 2
                             self.heisi -= h
                             self.daimyo1.heisi += h
                             if self.heisi <= 0:
                                 self.heisi = 0
                         elif self.answer_tgt == 117:
                             self.daimyo1.yuko -= 5
                 #Daimyo2
                 elif self.daimyo_flug == 2:   
                     if self.msg_num == 1:
                         if self.answer_tgt == 116:
                             h = int(self.kome*0.2)
                             if h > 0:
                                 self.daimyo2.yuko += 10
                                 self.daimyo1.yuko -= 2
                             self.kome -= h
                             self.daimyo2.kome += h
                             if self.kome <= 0:
                                 self.kome = 0
                         elif self.answer_tgt == 117:
                             self.daimyo2.yuko -= 5
                     elif self.msg_num == 2:
                         if self.answer_tgt == 116:
                             h = int(self.sikin*0.2)
                             if h > 0:
                                 self.daimyo2.yuko += 10
                                 self.daimyo1.yuko -= 2
                             self.sikin -= h
                             self.daimyo2.sikin += h
                             if self.sikin <= 0:
                                 self.sikin = 0
                         elif self.answer_tgt == 117:
                             self.daimyo2.yuko -= 5
                     elif self.msg_num == 3:
                         if self.answer_tgt == 116:
                             h = int(self.heisi*0.2)
                             if h > 0:
                                 self.daimyo2.yuko += 10
                                 self.daimyo1.yuko -= 2
                             self.heisi -= h
                             self.daimyo2.heisi += h
                             if self.heisi <= 0:
                                 self.heisi = 0
                         elif self.answer_tgt == 117:
                             self.daimyo2.yuko -= 5
     #Gaiko3
     elif self.window_ctr == 103:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 0
                 if self.daimyo_flug == 1:
                     self.daimyo1.event_cnt = 0
                     self.daimyo1.event_flug = False
                 elif self.daimyo_flug == 2:
                     self.daimyo2.event_cnt = 0
                     self.daimyo2.event_flug = False
                 self.daimyo_flug = 0

     #Kassen1
     elif self.window_ctr == 201:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 if self.enemy_tgt == 9:
                     k2 = int(self.turn * 50) + randint(5, 20) * self.turn
                     if k2 > 50000:
                         k2 = 50000
                 elif self.enemy_tgt == 1:
                     k2 = k2 = self.daimyo1.heisi
                     
                 elif self.enemy_tgt == 2:
                     k2 = self.daimyo2.heisi
                    
                 else:
                     k2 = 1000
                 self.k_hei = k2
                 self.k_hei2 = k2
                 self.window_ctr = 202
     #Kassen2
     elif self.window_ctr == 202:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.Kassen(self.heisi, self.k_hei)
                 if self.k_end == True:
                     self.window_ctr = 203                
                 else:
                     self.window_ctr = 202
     #Kassen3
     elif self.window_ctr == 203:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 204
                 #self.window_ctr = 0
     #Kassen4
     elif self.window_ctr == 204:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.kome = self.kome + self.k_kome
                 self.sikin = self.sikin + self.k_sikin
                 #Oda
                 if self.enemy_tgt == 1:
                     self.daimyo1.kome += self.k_kome
                     self.daimyo1.sikin += self.k_sikin
                     self.daimyo1.yuko = 10
                     self.daimyo2.yuko += 10
                     if self.daimyo2.yuko > 100:
                         self.daimyo2.yuko = 100
                 #Imagawa
                 elif self.enemy_tgt == 2:
                     self.daimyo2.kome += self.k_kome
                     self.daimyo2.sikin += self.k_sikin
                     self.daimyo2.yuko = 10
                     self.daimyo1.yuko += 10
                     if self.daimyo1.yuko > 100:
                         self.daimyo1.yuko = 100
                 if self.kome < 0:
                     self.kome = 0
                 if self.sikin < 0:
                     self.sikin = 0
                 #if self.k_cnt > 0:
                 self.k_cnt = 0
                 self.k_end = False
                 self.k_end_msg = 0
                 self.k_kome = 0
                 self.k_sikin = 0
                 self.k_hei = 0
                 self.k_hei2 = 0
                 self.enemy_tgt = 0
                 if self.end_flug == True:
                     if self.end_num == 1:
                         self.window_ctr = 1000
                     elif self.end_num == 2:
                         self.window_ctr = 1000
                 else:
                     self.window_ctr = 0
     #Introduction1
     elif self.window_ctr == 998:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 997
     #Introduction2
     elif self.window_ctr == 997:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 0
     #Title
     elif self.window_ctr == 999:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((0 < x < 63)  and (114 < y < 128)):
                 self.window_ctr = 998
             elif ((64 < x < 128)  and (114 < y < 128)):
                 self.Load_data()
                 self.window_ctr = 100
                 self.map_ch_fl = 1
     #End 1
     elif self.window_ctr == 1000:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 #Reset Game##################################################
                 pyxel.load('assets/assets.pyxres') #Map reset
                 #System status
                 self.window_ctr = 999
                 self.txt_ctr = 0
                 self.inf_ctr = 999
                 self.update_list = []
                 self.update_tgt = 0
                 self.turn = 1
     
                 #Player status
                 self.kome = 0
                 self.sikin = 0
                 self.heisi = 0
                 self.roryoku = 500
                 self.rend = 1
                 self.gankyo = 1
                 self.samurai = 0
                 self.gaiko = 0
                 self.ninjya = 0
                 self.syonin = 0
     
                 #Daimyo status
                 del self.daimyo1
                 self.daimyo1 = Daimyo(self.dst1["kome"],self.dst1["sikin"],
                                self.dst1["heisi"],self.dst1["sei"],
                                self.dst1["mei"],self.dst1["msg"],0)
                 del self.daimyo2
                 self.daimyo2 = Daimyo(self.dst2["kome"],self.dst2["sikin"],
                                self.dst2["heisi"],self.dst2["sei"],
                                self.dst2["mei"],self.dst2["msg"],30)
                 self.daimyo_flug = 0
     
                 #Gaiko status
                 self.answer_list = []
                 self.answer_tgt = 0
                 self.msg_num = 0
     
                 #Kassen status
                 self.k_cnt = 0
                 self.k_end = False
                 self.k_end_msg = 0
                 self.k_kome = 0
                 self.k_sikin = 0
                 self.k_hei = 0
                 self.k_hei2 = 0
                 self.enemy_tgt = 0
     
                 #Ending status
                 self.end_num = 0
                 self.end_flug = False
                 #############################################################
 
 def draw(self):
     pyxel.cls(0)
     
     if self.map_ch_fl > 0:
         self.Map_Change_EF()
         
     #Draw tilemap
     pyxel.bltm(0,0,0,0,0,16,16)
     #Select language
     if self.window_ctr == -1:
         pyxel.cls(0)
         pyxel.rect(0, 100, 128, 26, 0)
         pyxel.rectb(0, 100, 128, 26, 7)
         pyxel.rectb(0, 83, 128, 18, 7)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(["GE","NN","GO","WO","E","RA","NN","DE","KU","DA",
                          "SA","I"], 5, 88)
         pyxel.text(5, 104, "Please select lunguage.", 7)
         self.Draw_fonts(["NI","HO","NN","GO",], 5, 117)
         pyxel.text(68, 118, "English", 7)

     #Status window
     if  0 < self.window_ctr <= 99 :
         pyxel.rect(25, 0, 103, 80, 0)
         pyxel.rectb(25, 0, 103, 80, 7)
         pyxel.text(30, 5, str(self.turn), 7)
         self.Draw_fonts(self.text_list["106"], 45, 5)
         self.Draw_fonts(self.text_list["96"], 30, 15)
         pyxel.text(75, 15, str(self.sikin), 7)
         self.Draw_fonts(self.text_list["97"], 30, 25)
         pyxel.text(75, 25, str(self.kome), 7)
         self.Draw_fonts(self.text_list["95"], 30, 35)
         pyxel.text(75, 35, str(self.heisi), 7)
         self.Draw_fonts(self.text_list["94"], 30, 45)
         pyxel.text(75, 45, str(self.rend), 7)
         self.Draw_fonts(self.text_list["93"], 30, 55)
         pyxel.text(75, 55, str(self.gankyo), 7)
         self.Draw_fonts(self.text_list["98"], 30, 65)
         pyxel.text(75, 65, str(self.roryoku), 7)
         
     #Craft window
     if self.window_ctr == 1:
         pyxel.rect(0, 100, 128, 26, 0)
         pyxel.rectb(0, 100, 128, 26, 7)
         key = str(self.txt_ctr)
         self.Draw_fonts(self.text_list[key], 5, 105)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         if self.txt_ctr == 8:
             self.Draw_fonts(self.text_list["100_1"], 5, 117)
         elif 17 <= self.txt_ctr <= 20 or self.txt_ctr == 10:
             self.Draw_fonts(self.text_list["100_2"], 5, 117)
         else:
             self.Draw_fonts(self.text_list["100"], 5, 117)
         self.Draw_fonts(self.text_list["101"], 69, 117)

     #Craft window2  
     elif self.window_ctr == 2:
         
         pyxel.rect(0, 50, 128, 64, 0)
         pyxel.rectb(0, 50, 128, 64, 7)
         #Target = TANBO,MATI,BUKEYASIKI,HEITI
         if ((self.txt_ctr < 3) or (self.txt_ctr == 5) or
             (32 <= self.txt_ctr <= 34)) :
             self.update_list = [0,1,2]
             if ((self.txt_ctr < 3) or (32 <= self.txt_ctr <= 34)) :
                 self.update_list.append(80)
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
                 c = self.costs[str(self.update_list[i])]
                 pyxel.text(90,56+10*i,str(c),7)
         #Target = KI
         elif ((self.txt_ctr == 3) or (64 <= self.txt_ctr <= 66)) :
             self.update_list = [5]
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
                 c = self.costs[str(self.update_list[i])]
                 pyxel.text(90,56+10*i,str(c),7)
         #Target = JIYOUNAI
         elif self.txt_ctr == 8 :
             self.update_list = [17,18,19,20,]
             if self.samurai == 1:
                 self.update_list.remove(17)    
             if self.gaiko == 1:
                 self.update_list.remove(18)    
             if self.ninjya == 1:
                 self.update_list.remove(19)    
             if self.syonin == 1:
                 self.update_list.remove(20)    
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
                 c = self.costs[str(self.update_list[i])]
                 pyxel.text(105,56+10*i,str(c),7)
         #Target = Jyomon
         elif self.txt_ctr == 10:
             self.update_list = [171,172,173]
             l = len(self.update_list)
             pyxel.rect(0, 35, 128, 16, 0)
             pyxel.rectb(0, 35, 128, 16, 7)
             self.Draw_fonts(self.text_list["170"], 10, 40)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
                 c = self.costs[str(self.update_list[i])]
                 pyxel.text(105,56+10*i,str(c),7)
         #Target = Samuraidaisyo
         elif self.txt_ctr == 17:
             self.update_list = [1271, 1272]
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
                 c = self.costs[str(self.update_list[i])] * int((self.rend \
                                                            +self.gankyo)/2)
                 pyxel.text(105,56+10*i,str(c),7)
         #Target = GAIKOKAN
         elif self.txt_ctr == 18:
             self.update_list = [133, 1331]
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
                 c = self.costs[str(self.update_list[i])]
                 pyxel.text(105,56+10*i,str(c),7)
         #Target = Ninja
         elif self.txt_ctr == 19:
             self.update_list = [150]
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
                 c = self.costs[str(self.update_list[i])]
                 pyxel.text(105,56+10*i,str(c),7)
         #Target = Shounin
         elif self.txt_ctr == 20:
             self.update_list = [140,141,142,143]
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
                 c = self.costs[str(self.update_list[i])]
                 pyxel.text(105,56+10*i,str(c),7)
                 self.Draw_fonts(self.text_list["1400"],
                                 82, 56+10*i)
         pyxel.rect(0, 100, 64, 14, 0)
         pyxel.rectb(0, 100, 64, 14, 7)
         pyxel.rect(64, 100, 64, 14, 0)
         pyxel.rectb(64, 100, 64, 14, 7)
         self.Draw_fonts(self.text_list["102"], 5, 103)
         self.Draw_fonts(self.text_list["101"], 69, 103)
         
         s = self.update_list.index(self.update_tgt)
         pyxel.circb(5, 59+10*s, 2, 7)
     #Cannot craft1
     elif self.window_ctr == 3:
         pyxel.rect(0, 100, 128, 26, 0)
         pyxel.rectb(0, 100, 128, 26, 7)
         if self.txt_ctr == 8:
             self.Draw_fonts(self.text_list["99_1"], 5, 105)
         else:
             self.Draw_fonts(self.text_list["99"], 5, 105)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["107"], 69, 117)
     #Cannot craft2
     elif self.window_ctr == 4:
         pyxel.rect(0, 100, 128, 26, 0)
         pyxel.rectb(0, 100, 128, 26, 7)
         self.Draw_fonts(self.text_list["108"], 5, 105)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["107"], 69, 117)

     #Turn change
     elif self.window_ctr == 98:
         pyxel.rect(0, 100, 128, 26, 0)
         pyxel.rectb(0, 100, 128, 26, 7)
         pyxel.text(10, 105, str(self.turn), 7)
         self.Draw_fonts(self.text_list["106"], 25, 105)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["107"], 69, 117)
     #Siro
     elif self.window_ctr == 99:
         pyxel.rect(0, 86, 128, 26, 0)
         pyxel.rectb(0, 86, 128, 26, 7)
         pyxel.rect(0, 100, 128, 26, 0)
         pyxel.rectb(0, 100, 128, 26, 7)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         pyxel.rect(0, 100, 64, 14, 0)
         pyxel.rectb(0, 100, 64, 14, 7)
         pyxel.rect(64, 100, 64, 14, 0)
         pyxel.rectb(64, 100, 64, 14, 7)
         key = str(self.txt_ctr)
         self.Draw_fonts(self.text_list[key], 5, 91)
         self.Draw_fonts(self.text_list["101"], 69, 117)
         self.Draw_fonts(self.text_list["103"], 5, 103)
         self.Draw_fonts(self.text_list["104"], 69, 103)
         self.Draw_fonts(self.text_list["105"], 5, 117)
     #Information window
     elif self.window_ctr == 100:
         pyxel.rect(0, 100, 128, 26, 0)
         pyxel.rectb(0, 100, 128, 26, 7)
         t = str(self.inf_ctr)
         self.Draw_fonts(self.text_list[t], 5, 105)
         #if self.inf_ctr == 134:
          #   pyxel.rect(40, 50, 64, 32, 0)
           #  pyxel.rectb(40, 50, 64, 32, 7)
            # pyxel.blt(40, 50, 0, 0, 0, 64, 32)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         #Ninja
         if self.txt_ctr == 19:
             pyxel.rect(0, 0, 128, 100, 0)
             pyxel.rectb(0, 0, 128, 100, 7)
             if self.update_tgt == 150:
                 for dai in range(2):
                     if dai == 0:
                         dai2 = self.daimyo1
                     else:
                         dai2 = self.daimyo2
                     self.Draw_fonts(dai2.sei, 15+(60*dai), 5)
                     self.Draw_fonts(self.text_list["97"], 4+(60*dai), 15)
                     pyxel.text(30+(60*dai),15,str(dai2.kome), 7)
                     self.Draw_fonts(self.text_list["96"], 4+(60*dai), 30)
                     pyxel.text(30+(60*dai),30,str(dai2.sikin), 7)
                     self.Draw_fonts(self.text_list["95"], 4+(60*dai), 45)
                     pyxel.text(38+(60*dai),45,str(dai2.heisi) ,7)
                     self.Draw_fonts(self.text_list["94"], 4+(60*dai), 60)
                     pyxel.text(45+(60*dai),60,str(dai2.rend) ,7)
                     self.Draw_fonts(self.text_list["93"], 4+(60*dai), 75)
                     pyxel.text(45+(60*dai),75,str(dai2.gankyo) ,7)
                     self.Draw_fonts(self.text_list["160"], 4+(60*dai), 90)
                     pyxel.text(45+(60*dai),90,str(dai2.yuko), 7)
             else:
                 pass
         self.Draw_fonts(self.text_list["107"], 69, 117)
     #Gaiko
     elif self.window_ctr == 101:
         pyxel.rect(0, 80, 128, 46, 0)
         pyxel.rectb(0, 80, 128, 46, 7)
         if self.daimyo_flug == 1:
             sei = self.daimyo1.sei
             mei = self.daimyo1.mei
             self.Draw_fonts(sei, 5, 85)
             self.Draw_fonts(mei, 30, 85)
         elif self.daimyo_flug == 2:
             sei = self.daimyo2.sei
             mei = self.daimyo2.mei
             self.Draw_fonts(sei, 5, 85)
             self.Draw_fonts(mei, 45, 85)    
         self.Draw_fonts(self.text_list["114"], 85, 85)
         self.Draw_fonts(self.text_list["115"], 5, 95)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["107"], 69, 117)
     #Gaiko2
     elif self.window_ctr == 102:
         pyxel.bltm(0,0,0,240,0,16,16)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         if self.daimyo_flug == 1:
             sei = self.daimyo1.sei
             mei = self.daimyo1.mei
             self.Draw_fonts(mei, 85, 52)
             pyxel.blt(81,7,2,0,208,40,32,2)
             #Msg
             if self.msg_num == 1:
                 if self.daimyo1.yuko >= 80:
                     self.Draw_fonts(self.daimyo1.msg["0-1"], 10, 10)   
                     self.Draw_fonts(self.daimyo1.msg["3-1"], 10, 40)   
                 elif self.daimyo1.yuko <= 20:
                     self.Draw_fonts(self.daimyo1.msg["0-3"], 10, 10)   
                     self.Draw_fonts(self.daimyo1.msg["3-3"], 10, 40)   
                 else:
                     self.Draw_fonts(self.daimyo1.msg["0-2"], 10, 10)   
                     self.Draw_fonts(self.daimyo1.msg["3-2"], 10, 40)   
                 self.Draw_fonts(self.daimyo1.msg["1-1"], 10, 20)
                 self.Draw_fonts(self.daimyo1.msg["2"], 10, 30)   
             elif self.msg_num == 2:
                 if self.daimyo1.yuko >= 80:
                     self.Draw_fonts(self.daimyo1.msg["0-1"], 10, 10)   
                     self.Draw_fonts(self.daimyo1.msg["3-1"], 10, 40)   
                 elif self.daimyo1.yuko <= 20:
                     self.Draw_fonts(self.daimyo1.msg["0-3"], 10, 10)   
                     self.Draw_fonts(self.daimyo1.msg["3-3"], 10, 40)   
                 else:
                     self.Draw_fonts(self.daimyo1.msg["0-2"], 10, 10)   
                     self.Draw_fonts(self.daimyo1.msg["3-2"], 10, 40)   
                 self.Draw_fonts(self.daimyo1.msg["1-2"], 10, 20)
                 self.Draw_fonts(self.daimyo1.msg["2"], 10, 30)   
             elif self.msg_num == 3:
                 if self.daimyo1.yuko >= 80:
                     self.Draw_fonts(self.daimyo1.msg["0-1"], 10, 10)   
                     self.Draw_fonts(self.daimyo1.msg["3-1"], 10, 40)   
                 elif self.daimyo1.yuko <= 20:
                     self.Draw_fonts(self.daimyo1.msg["0-3"], 10, 10)   
                     self.Draw_fonts(self.daimyo1.msg["3-3"], 10, 40)   
                 else:
                     self.Draw_fonts(self.daimyo1.msg["0-2"], 10, 10)   
                     self.Draw_fonts(self.daimyo1.msg["3-2"], 10, 40)   
                 self.Draw_fonts(self.daimyo1.msg["1-3"], 10, 20)
                 self.Draw_fonts(self.daimyo1.msg["2"], 10, 30)  
         elif self.daimyo_flug == 2:
             sei = self.daimyo2.sei
             mei = self.daimyo2.mei
             self.Draw_fonts(mei, 85, 52)
             pyxel.blt(81,7,2,40,208,40,32,2)
             #Msg
             if self.msg_num == 1:
                 if self.daimyo2.yuko >= 80:
                     self.Draw_fonts(self.daimyo2.msg["0-1"], 10, 10)   
                     self.Draw_fonts(self.daimyo2.msg["3-1"], 10, 40)   
                 elif self.daimyo2.yuko <= 20:
                     self.Draw_fonts(self.daimyo2.msg["0-3"], 10, 10)   
                     self.Draw_fonts(self.daimyo2.msg["3-3"], 10, 40)   
                 else:
                     self.Draw_fonts(self.daimyo2.msg["0-2"], 10, 10)   
                     self.Draw_fonts(self.daimyo2.msg["3-2"], 10, 40)   
                 self.Draw_fonts(self.daimyo2.msg["1-1"], 10, 20)
                 self.Draw_fonts(self.daimyo2.msg["2"], 10, 30)   
             elif self.msg_num == 2:
                 if self.daimyo2.yuko >= 80:
                     self.Draw_fonts(self.daimyo2.msg["0-1"], 10, 10)   
                     self.Draw_fonts(self.daimyo2.msg["3-1"], 10, 40)   
                 elif self.daimyo2.yuko <= 20:
                     self.Draw_fonts(self.daimyo2.msg["0-3"], 10, 10)   
                     self.Draw_fonts(self.daimyo2.msg["3-3"], 10, 40)   
                 else:
                     self.Draw_fonts(self.daimyo2.msg["0-2"], 10, 10)   
                     self.Draw_fonts(self.daimyo2.msg["3-2"], 10, 40)   
                 self.Draw_fonts(self.daimyo2.msg["1-2"], 10, 20)
                 self.Draw_fonts(self.daimyo2.msg["2"], 10, 30)   
             elif self.msg_num == 3:
                 if self.daimyo2.yuko >= 80:
                     self.Draw_fonts(self.daimyo2.msg["0-1"], 10, 10)   
                     self.Draw_fonts(self.daimyo2.msg["3-1"], 10, 40)   
                 elif self.daimyo2.yuko <= 20:
                     self.Draw_fonts(self.daimyo2.msg["0-3"], 10, 10)   
                     self.Draw_fonts(self.daimyo2.msg["3-3"], 10, 40)   
                 else:
                     self.Draw_fonts(self.daimyo2.msg["0-2"], 10, 10)   
                     self.Draw_fonts(self.daimyo2.msg["3-2"], 10, 40)   
                 self.Draw_fonts(self.daimyo2.msg["1-3"], 10, 20)
                 self.Draw_fonts(self.daimyo2.msg["2"], 10, 30)   
             #
         #Answer
         self.answer_list = [116,117]
         r = len(self.answer_list)
         for a in range(r):
             k = str(self.answer_list[a])
             self.Draw_fonts(self.text_list[k], 20, 73+(10*a))
         #
         s = self.answer_list.index(self.answer_tgt)
         pyxel.circb(12, 76+10*s, 2, 7)
         self.Draw_fonts(self.text_list["118"], 69, 117)
     #Gaiko3
     elif self.window_ctr == 103:
         pyxel.bltm(0,0,0,240,0,16,16)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         if self.daimyo_flug == 1:
             sei = self.daimyo1.sei
             mei = self.daimyo1.mei
             self.Draw_fonts(mei, 85, 52)
             pyxel.blt(81,7,2,0,208,40,32,2)
             #Msg
             if self.answer_tgt == 116:
                 self.Draw_fonts(self.daimyo1.msg["4"], 10, 10)   
             else:
                 self.Draw_fonts(self.daimyo1.msg["5"], 10, 10)
                 self.Draw_fonts(self.daimyo1.msg["6"], 10, 20)   
                 self.Draw_fonts(self.daimyo1.msg["7"], 10, 30)   
             #
         elif self.daimyo_flug == 2:
             sei = self.daimyo2.sei
             mei = self.daimyo2.mei
             self.Draw_fonts(mei, 85, 52)
             pyxel.blt(81,7,2,40,208,40,32,2)
             #Msg
             if self.answer_tgt == 116:
                 self.Draw_fonts(self.daimyo2.msg["4"], 10, 10)   
             else:
                 self.Draw_fonts(self.daimyo2.msg["5"], 10, 10)
                 self.Draw_fonts(self.daimyo2.msg["6"], 10, 20)   
                 self.Draw_fonts(self.daimyo2.msg["7"], 10, 30)   
             #
                 
         self.Draw_fonts(self.text_list["107"], 69, 117) 
     #Kassen1
     elif self.window_ctr == 201:
         pyxel.rect(0, 80, 128, 46, 0)
         pyxel.rectb(0, 80, 128, 46, 7)
         if self.k_cnt < 100:
             if self.enemy_tgt == 1:
                 self.Draw_fonts(self.text_list["171"], 5, 85)
             elif self.enemy_tgt == 2:
                 self.Draw_fonts(self.text_list["172"], 5, 85)
             elif self.enemy_tgt == 9:
                 self.Draw_fonts(self.text_list["120"], 5, 85)
                 
             self.Draw_fonts(self.text_list["114"], 85, 85)
             self.Draw_fonts(self.text_list["119"], 5, 95)
         else:
             if self.enemy_tgt == 1:
                 self.Draw_fonts(self.text_list["171"], 5, 85)
             elif self.enemy_tgt == 2:
                 self.Draw_fonts(self.text_list["172"], 5, 85)
             elif self.enemy_tgt == 9:
                 self.Draw_fonts(self.text_list["120"], 5, 85)
             self.Draw_fonts(self.text_list["131"], 85, 85)
             self.Draw_fonts(self.text_list["132"], 5, 95)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["107"], 69, 117)
     #Kassen2
     elif self.window_ctr == 202:
         pyxel.bltm(0,0,0,240,16,16,16)
         h1 = self.heisi // 100
         if h1 < 1 and self.heisi > 0:
             h1 = 1
         for h2 in range(h1):
             h3 = h2 // 7
             if h3 < 7:
                 h4 = ((h2 * 8) - (h3 * 56 ))
                 if self.rend >= 40:
                     pyxel.blt(8 + (h3 * 8),8 + h4,2,24,248,8,8,9)
                 else:
                     pyxel.blt(8 + (h3 * 8),8 + h4,2,24,240,8,8,9)
         h5 = self.k_hei // 100
         if h5 < 1 and self.k_hei > 0:
             h5 = 1
         for h6 in range(h5):
             h7 = h6 // 7
             if h7 < 7:
                 h8 = ((h6 * 8) - (h7 * 56))
                 if self.enemy_tgt == 9:
                     pyxel.blt(113 - (h7 * 8), 8 + h8,2,32,240,8,8,9)
                 elif self.enemy_tgt == 1:
                     if self.daimyo1.rend > 50:
                         pyxel.blt(113 - (h7 * 8), 8 + h8,2,40,248,8,8,9)
                     else:
                         pyxel.blt(113 - (h7 * 8), 8 + h8,2,40,240,8,8,9)
                 elif self.enemy_tgt == 2:
                     if self.daimyo2.rend > 50:
                         pyxel.blt(113 - (h7 * 8), 8 + h8,2,40,248,8,8,9)
                     else:
                         pyxel.blt(113 - (h7 * 8), 8 + h8,2,40,240,8,8,9)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["125"], 10, 75)      
         self.Draw_fonts(self.text_list["95"], 10, 85)      
         pyxel.text(37,86,str(self.heisi),7)
         if self.enemy_tgt == 9:
             self.Draw_fonts(self.text_list["120"], 68, 75)
         elif self.enemy_tgt == 1:
             self.Draw_fonts(self.text_list["1201"], 68, 75)
         elif self.enemy_tgt == 2:
             self.Draw_fonts(self.text_list["1202"], 68, 75)
         self.Draw_fonts(self.text_list["95"], 68, 85)      
         pyxel.text(95,86,str(self.k_hei),7)
         self.Draw_fonts(self.text_list["124"], 69, 117)         
     #Kassen3
     elif self.window_ctr == 203:
         pyxel.rect(0, 100, 128, 26, 0)
         pyxel.rectb(0, 100, 128, 26, 7)
         t = str(self.k_end_msg)
         self.Draw_fonts(self.text_list[t], 5, 105)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["107"], 69, 117)
     #Kassen4
     elif self.window_ctr == 204:
         pyxel.rect(0, 50, 128, 65, 0)
         pyxel.rectb(0, 50, 128, 65, 7)
         self.Draw_fonts(self.text_list["126"], 5, 53)
         self.Draw_fonts(self.text_list["97"], 5, 64)
         self.Draw_fonts(self.text_list["96"], 5, 74)
         if self.k_kome < 0:
             pyxel.text(35,65,str(self.k_kome),7)
             pyxel.text(35,75,str(self.k_sikin),7)
         else:
             pyxel.text(35,65,"+" + str(self.k_kome),7)
             pyxel.text(35,75,"+" + str(self.k_sikin),7)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["107"], 69, 117)
     #Introduction1
     elif self.window_ctr == 998:
         pyxel.cls(0)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["o1"], 5, 5)
         self.Draw_fonts(self.text_list["o2"], 5, 15)
         self.Draw_fonts(self.text_list["o3"], 5, 35)
         self.Draw_fonts(self.text_list["o4"], 5, 45)
         self.Draw_fonts(self.text_list["o5"], 5, 55)
         self.Draw_fonts(self.text_list["o6"], 5, 65)
         self.Draw_fonts(self.text_list["o7"], 5, 75)
         self.Draw_fonts(self.text_list["ox"], 69, 117)
     #Introduction2
     elif self.window_ctr == 997:
         pyxel.cls(0)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["o8"], 5, 5)
         self.Draw_fonts(self.text_list["o9"], 5, 15)
         self.Draw_fonts(self.text_list["o10"], 5, 25)
         self.Draw_fonts(self.text_list["o11"], 5, 35)
         self.Draw_fonts(self.text_list["o12"], 5, 45)
         self.Draw_fonts(self.text_list["o13"], 5, 65)
         self.Draw_fonts(self.text_list["o14"], 5, 75)
         self.Draw_fonts(self.text_list["ox"], 69, 117)
     #Title
     elif self.window_ctr == 999:
         pyxel.cls(0)
         pyxel.blt(0,28,0,0,0,128,84)
         pyxel.blt(4,10,2,0,176,64,16)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         pyxel.text(5, 30, "Better be the head of a pike ", 7)
         pyxel.text(5, 40, "than the tail of", 7)
         pyxel.text(5, 50, "a sturgeon.", 7)
         self.Draw_fonts(self.text_list["113"], 6, 117)
         self.Draw_fonts(self.text_list["1131"], 69, 117)
         
     #End 1
     elif self.window_ctr == 1000:
         pyxel.cls(0)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["180"], 5, 5)
         self.Draw_fonts(self.text_list["182"], 5, 15)
         self.Draw_fonts(self.text_list["97"], 29, 15)
         pyxel.text(75, 15, str(self.kome), 7)
         self.Draw_fonts(self.text_list["182"], 5, 25)
         self.Draw_fonts(self.text_list["96"], 29, 25)
         pyxel.text(75, 25, str(self.sikin), 7)
         self.Draw_fonts(self.text_list["182"], 5, 35)
         self.Draw_fonts(self.text_list["95"], 29, 35)
         pyxel.text(75, 35, str(self.heisi), 7)
         self.Draw_fonts(self.text_list["182"], 5, 45)
         self.Draw_fonts(self.text_list["98"], 29, 45)
         pyxel.text(75, 45, str(self.roryoku), 7)
         self.Draw_fonts(self.text_list["183"], 5, 55)
         kei = self.kome+self.sikin+self.heisi+self.roryoku
         pyxel.text(75, 55, str(kei), 7)
         self.Draw_fonts(self.text_list["184"], 5, 65)
         pyxel.text(60, 65, str(self.turn), 7)
         kei_mai = self.turn * 500
         self.Draw_fonts(self.text_list["185"], 5, 75)
         pyxel.text(60, 75, str(self.turn)+"x500="+str(kei_mai), 7)
         #rank check
         self.Draw_fonts(self.text_list["186"], 5, 95)
         kei_g = kei - kei_mai
         if kei_g > 99999:
             rank = "S"
             pyxel.text(75, 95, rank, 8)
         elif kei_g > 79999:
             rank = "A"
             pyxel.text(75, 95, rank, 9)
         elif kei_g > 49999:
             rank = "B"
             pyxel.text(75, 95, rank, 10)
         elif kei_g > 19999:
             rank = "C"
             pyxel.text(75, 95, rank, 3)
         elif kei_g > 9999:
             rank = "D"
             pyxel.text(75, 95, rank, 6)
         else:
             rank = "Z"
             pyxel.text(75, 95, rank, 7)
         self.Draw_fonts(self.text_list["181"], 69, 117)
         
 def Draw_fonts(self,txt,x,y):  
     txt_count = len(txt)      
     if ((self.lng == "ja") or (self.lng == "none")):
         for i in range(txt_count):
             #Key check
             font_xy = self.font_list[txt[i]]
        
             fontx = font_xy[0]
             fonty = font_xy[1]
             pyxel.blt(x + 8 * i,y,1,fontx,fonty,8,8,14)
     elif  self.lng == "en":
         pyxel.text(x, y, txt, 7)
         
 def Turn_change(self):
     r = 0
     for i in range(16):
         for i2 in range(16):
             m = pyxel.tilemap(0).data[i][i2]
             if m == 0:
                 self.kome = self.kome + 100
                 r = r + 1
             elif m == 1:
                 self.sikin = self.sikin + 100
                 r = r + 1
             elif m == 2:
                 self.heisi = self.heisi + 50
                 r = r + 1
             elif m == 32:
                 self.kome = self.kome + 250
                 r = r + 2
             elif m == 33:
                 self.sikin = self.sikin + 200
                 r = r + 2
             elif m == 34:
                 self.heisi = self.heisi + 100
                 r = r + 2
             elif m == 64:
                 self.kome = self.kome + 500
                 r = r + 3
             elif m == 65:
                 self.sikin = self.sikin + 300
                 r = r + 3
             elif m == 66:
                 self.heisi = self.heisi + 150
                 r = r + 3
             
     if self.kome > 99999:
         self.kome = 99999
     if self.sikin > 99999:
         self.sikin = 99999
     if self.heisi > 99999:
         self.heisi = 99999
            
     #hyoro
     self.kome = self.kome - int(self.heisi*0.25)
     if self.kome < 0:
         self.heisi = self.heisi - abs(self.kome)
         self.heisi = self.heisi - 100
         if self.heisi < 0:
             self.heisi = 0
         self.kome = 0
         
     self.roryoku = self.roryoku + int(r*20)
     self.turn = self.turn + 1
     
     #Daimyo
     self.daimyo1.Turn_change(1)
     self.daimyo2.Turn_change(2)
     
     #Kassen
     k1 = int(self.turn * 0.5)
     if k1 > 5:
         k1 = randint(2, 5)
     self.k_cnt = self.k_cnt + k1
     
 def Kassen(self, p, e):
     #Player status
     pr = int(1 + (self.rend * 0.1))
     pr2 = int(pr / 2)
     if pr2 < 1:
         pr2 = 1
     pl = int(self.gankyo / 2)
     if pl < 1:
         pl = 1
         
     #Enemy status
     if self.enemy_tgt == 9:
         es = int(self.turn - randint(5, 50) + 1) 
         if es > 50:
             es = 50
         elif es < 1:
             es = 1
         er = randint(1, es)
         er2 = 1
         el = 1
         el2 = 1
     elif self.enemy_tgt == 1:
         es = self.daimyo1.rend
         if es < 1:
             es = 1
         er = es
         er2 = int(er / 2)
         if er2 < 1:
             er2 = 1
         el = self.daimyo1.gankyo
         el2 = int(el / 2)
         if el2 < 1:
             el2 = 1
     elif self.enemy_tgt == 2:
         es = self.daimyo2.rend
         if es < 1:
             es = 1
         er = es
         er2 = int(er / 2)
         if er2 < 1:
             er2 = 1
         el = self.daimyo2.gankyo
         el2 = int(el / 2)
         if el2 < 1:
             el2 = 1
         
     p_atk = int(int(p * (randint(pr2, pr) * 0.02)) * \
             (1 - (randint(el2, el ) * 0.01)))
     if p_atk < 1:
         p_atk = 1
         
     e_atk = int(int(e * (randint(er2, er) * 0.02)) * \
             (1 - (randint(pl, self.gankyo) * 0.01)))
     if e_atk < 1:
         e_atk = 1
         
     self.heisi = self.heisi - e_atk
     self.k_hei = self.k_hei - p_atk
     if self.heisi <= 0 and self.k_hei <= 0:
         self.heisi = 0 
         self.k_hei = 0
         self.k_end = True
         self.k_end_msg = 123
         self.k_kome = 0
         self.k_sikin = 0
     elif self.heisi <= 0:
         self.heisi = 0 
         self.k_end = True
         self.k_end_msg = 122
         self.k_kome = randint(100, self.k_hei) * -1
         self.k_sikin = randint(100, self.k_hei) * -1
         self.k_cnt = -25
     elif self.k_hei <= 0:
         self.k_end = True
         self.k_end_msg = 121
         self.k_kome = randint(100, self.k_hei2) 
         self.k_sikin = randint(100, self.k_hei2) 
         if self.enemy_tgt == 1:
             self.end_flug = True
             self.end_num = 1
         elif self.enemy_tgt == 2:
             self.end_flug = True
             self.end_num = 2
     
     if self.enemy_tgt == 1:
         self.daimyo1.heisi = self.k_hei
         if self.daimyo1.heisi <= 0:
             self.daimyo1.heisi = 0
     elif self.enemy_tgt == 2:
         self.daimyo2.heisi = self.k_hei
         if self.daimyo2.heisi <= 0:
             self.daimyo2.heisi = 0
         
 def Map_Change_EF(self):
     self.map_ch_cn += 4
     if self.map_ch_fl == 1: 
         n = self.map_ch_cn
         pyxel.clip(64-n, 64-n, 0+n*2, 0+n*2)
         if self.map_ch_cn > 70:
             self.map_ch_fl = 0
             self.map_ch_cn = 0
             pyxel.clip()

 def Save_data(self):
     #Save data
     data2 = []
     for i in range(16):
         data = []
         for i2 in range(16):
             data.append(pyxel.tilemap(0).data[i][i2])
         data2.append(data)
     try:
         with open('DATA/data.csv', 'w', newline="") as f:
                 writer = csv.writer(f)
                 for i3 in range(16):
                     writer.writerow(data2[i3])
                 data3 = []
                 data3.append(self.turn)
                 data3.append(self.sikin)
                 data3.append(self.roryoku)
                 data3.append(self.heisi)
                 data3.append(self.kome)
                 data3.append(self.rend)
                 data3.append(self.gankyo)
                 data3.append(self.k_cnt)
                 data3.append(self.samurai)
                 data3.append(self.gaiko)
                 data3.append(self.ninjya)
                 data3.append(self.syonin)
                 data3.append(self.enemy_tgt)
                 writer.writerow(data3)
                 data4 = []
                 data4.append(self.daimyo1.kome)
                 data4.append(self.daimyo1.sikin)
                 data4.append(self.daimyo1.heisi)
                 data4.append(self.daimyo1.yuko)
                 data4.append(self.daimyo1.event_cnt)
                 data4.append(self.daimyo1.rend)
                 data4.append(self.daimyo1.gankyo)
                 writer.writerow(data4)
                 data5 = []
                 data5.append(self.daimyo2.kome)
                 data5.append(self.daimyo2.sikin)
                 data5.append(self.daimyo2.heisi)
                 data5.append(self.daimyo2.yuko)
                 data5.append(self.daimyo2.event_cnt)
                 data5.append(self.daimyo2.rend)
                 data5.append(self.daimyo2.gankyo)
                 writer.writerow(data5)
                 self.inf_ctr = 109
     except:
         self.inf_ctr = 112
         
 def Load_data(self):
     #Load data
     data = []
     data2 = []
     data3 = []
     try:
         with open('DATA/data.csv') as f:
             reader = csv.reader(f)
             for row in reader:
                 data.append(row)
         for i in range(16):
             data2 = []
             for i2 in range(16):
                 a = format(int(data[i][i2]), 'x')
                 data2.append(str(format(a, '0>3')))
             data3.append(data2)
         for i2 in range(16):
             d = ""
             d = "".join(data3[i2])
             pyxel.tilemap(0).set(0, 0+i2, [d]) 
         self.turn = int(data[16][0])
         self.sikin = int(data[16][1])
         self.roryoku = int(data[16][2])
         self.heisi = int(data[16][3])
         self.kome = int(data[16][4])
         self.rend = int(data[16][5])
         self.gankyo = int(data[16][6])
         self.k_cnt = int(data[16][7])
         self.samurai = int(data[16][8])
         self.gaiko = int(data[16][9])
         self.ninjya = int(data[16][10])
         self.syonin = int(data[16][11])
         self.enemy_tgt = int(data[16][12])
         self.daimyo1.kome = int(data[17][0])
         self.daimyo1.sikin = int(data[17][1])
         self.daimyo1.heisi = int(data[17][2])
         self.daimyo1.yuko = int(data[17][3])
         self.daimyo1.event_cnt = int(data[17][4])
         self.daimyo1.rend = int(data[17][5])
         self.daimyo1.gankyo = int(data[17][6])
         self.daimyo2.kome = int(data[18][0])
         self.daimyo2.sikin = int(data[18][1])
         self.daimyo2.heisi = int(data[18][2])
         self.daimyo2.yuko = int(data[18][3])
         self.daimyo2.event_cnt = int(data[18][4])
         self.daimyo2.rend = int(data[18][5])
         self.daimyo2.gankyo = int(data[18][6])
         self.inf_ctr = 110
     except:
        self.inf_ctr = 111
         
class Craft:
    def __init__(self):
        self.tgt_x = 0
        self.tgt_y = 0
        self.tgt_v = 0
    def get_pos(self, x, y, v):
        self.tgt_x = x
        self.tgt_y = y
        self.tgt_v = v
    def update_pos(self, v, c):
        x = self.tgt_x
        y = self.tgt_y
        #Taget point check
        if v == 80:
            v2 = pyxel.tilemap(0).get(x, y)
            if v2 == 0:
                v = 32
            elif v2 == 32:
                v = 64
            elif v2 == 1:
                v = 33
            elif v2 == 33:
                v = 65
            elif v2 == 2:
                v = 34
            elif v2 == 34:
                v = 66
                
        tile = format(v, 'x')
        tile2 = str(format(tile, '0>3'))
        #Update tilemap
        pyxel.tilemap(0).set(x, y, [tile2]) 
        
class Daimyo:
    def __init__(self,a,b,c,d,e,m,v):
        self.kome = a
        self.sikin = b
        self.heisi = c
        self.yuko = 50
        self.sei = d
        self.mei = e
        self.msg = m
        self.event_cnt = v
        self.event_flug = False
        self.rend = 5
        self.gankyo = 5
    def Turn_change(self,d):
        if d == 1:
            self.kome += 300 * randint(1, 5)
            self.sikin += 200 * randint(1, 5)
            self.heisi += 150 * randint(1, 5)
            self.rend += randint(2, 4)
            self.gankyo += randint(2, 4)
            if self.kome > 999999:
                self.kome = 999999
            if self.sikin > 999999:
                self.sikin = 999999
            if self.heisi > 999999:
                self.heisi = 999999
            if self.rend > 100:
                self.rend = 100
            if self.gankyo > 100:
                self.gankyo = 100
        elif d == 2:
            self.kome += 500 * randint(1, 10)
            self.sikin += 500 * randint(1, 10)
            self.heisi += 200 * randint(1, 10)
            self.rend += randint(1, 3)
            self.gankyo += randint(1, 3)
            if self.kome > 999999:
                self.kome = 999999
            if self.sikin > 999999:
                self.sikin = 999999
            if self.heisi > 999999:
                self.heisi = 999999
            if self.rend > 100:
                self.rend = 100
            if self.gankyo > 100:
                self.gankyo = 100
        self.event_cnt += randint(5, 10)
        if self.event_cnt >= randint(51, 100):
            self.event_flug = True
            
        
App()
