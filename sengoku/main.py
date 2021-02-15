#main.py

import pyxel
import csv
from random import randint
from module import Fontlist, Text_list, Game_status

class App:
 def __init__(self):
     #Font set
     self.font_list = Fontlist.text_j()
     #Text list set
     self.text_list = Text_list.text_get()
     #Costs set
     self.costs = Game_status.costs_get()
     #System status
     self.craft = Craft()
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
     self.roryoku = 100
     #Daimyo status
     self.dst1 = Game_status.oda()
     self.daimyo1 = Daimyo(self.dst1["kome"],self.dst1["sikin"],
                                self.dst1["heisi"],self.dst1["sei"],
                                self.dst1["mei"],self.dst1["msg"],0)
     self.dst2 = Game_status.imagawa()
     self.daimyo2 = Daimyo(self.dst2["kome"],self.dst2["sikin"],
                                self.dst2["heisi"],self.dst2["sei"],
                                self.dst2["mei"],self.dst2["msg"],20)
     self.daimyo_flug = 0
     #Gaiko status
     self.answer_list = []
     self.answer_tgt = 0
     self.msg_num = 0
     
     #Base window create
     pyxel.init(128,128, caption="sengoku", scale=5)
     
     #Mouse visivle
     pyxel.mouse(True)

     #Image read
     pyxel.load('assets/assets.pyxres')
     
     pyxel.run(self.update, self.draw)
     
 def update(self):
             
     #Main window
     if self.window_ctr == 0:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             x2 = int(x/8)
             y2 = int(y/8)
             v = pyxel.tilemap(0).get(x2, y2)
             self.craft.get_pos(x2, y2, v)
             if v == 6:
                 self.window_ctr = 99
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
                 elif self.txt_ctr == 8:
                     self.update_tgt = 17
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
                 t = str(self.update_tgt)
                 c = self.costs[t]
                 if self.roryoku >= c:
                     self.craft.update_pos(self.update_tgt, c)
                     self.roryoku = self.roryoku - c
                     self.window_ctr = 0
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
                 if ((self.daimyo1.event_flug == True) and
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
     #Title
     elif self.window_ctr == 999:
         if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON):
             x = pyxel.mouse_x
             y = pyxel.mouse_y
             if ((64 < x < 128)  and (114 < y < 128)):
                 self.window_ctr = 0
 
 def draw(self):
     #Draw tilemap
     pyxel.bltm(0,0,0,0,0,16,16)
     #Status window
     if  0 < self.window_ctr < 90 :
         pyxel.rect(25, 0, 103, 60, 0)
         pyxel.rectb(25, 0, 103, 60, 7)
         self.Draw_fonts(self.text_list["96"], 30, 5)
         pyxel.text(75, 5, str(self.sikin), 7)
         self.Draw_fonts(self.text_list["97"], 30, 15)
         pyxel.text(75, 15, str(self.kome), 7)
         self.Draw_fonts(self.text_list["95"], 30, 25)
         pyxel.text(75, 25, str(self.heisi), 7)
         self.Draw_fonts(self.text_list["98"], 30, 35)
         pyxel.text(75, 35, str(self.roryoku), 7)
         
     #Status window2
     if  self.window_ctr == 99 :
         pyxel.rect(25, 0, 103, 70, 0)
         pyxel.rectb(25, 0, 103, 70, 7)
         pyxel.text(30, 5, str(self.turn), 7)
         self.Draw_fonts(self.text_list["106"], 45, 5)
         self.Draw_fonts(self.text_list["96"], 30, 15)
         pyxel.text(75, 15, str(self.sikin), 7)
         self.Draw_fonts(self.text_list["97"], 30, 25)
         pyxel.text(75, 25, str(self.kome), 7)
         self.Draw_fonts(self.text_list["95"], 30, 35)
         pyxel.text(75, 35, str(self.heisi), 7)
         self.Draw_fonts(self.text_list["98"], 30, 45)
         pyxel.text(75, 45, str(self.roryoku), 7)
         
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
             self.update_list = [17,18]
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
                 c = self.costs[str(self.update_list[i])]
                 pyxel.text(90,56+10*i,str(c),7)
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
         self.Draw_fonts(self.text_list["99"], 5, 105)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["101"], 69, 117)
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
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
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
     #Title
     elif self.window_ctr == 999:
         pyxel.rect(0, 100, 128, 26, 0)
         pyxel.rectb(0, 100, 128, 26, 7)
         pyxel.rect(0, 114, 64, 14, 0)
         pyxel.rectb(0, 114, 64, 14, 7)
         pyxel.rect(64, 114, 64, 14, 0)
         pyxel.rectb(64, 114, 64, 14, 7)
         self.Draw_fonts(self.text_list["113"], 69, 117)
         
 def Draw_fonts(self,txt,x,y):  
     txt_count = len(txt)      
     for i in range(txt_count):
         #Key check
         font_xy = self.font_list[txt[i]]
        
         fontx = font_xy[0]
         fonty = font_xy[1]
         pyxel.blt(x + 8 * i,y,1,fontx,fonty,8,8,14)
         
 def Turn_change(self):
     r = 0
     for i in range(16):
         for i2 in range(16):
             m = pyxel.tilemap(0).data[i][i2]
             if m == 0:
                 self.kome = self.kome + 50
                 r = r + 1
             elif m == 1:
                 self.sikin = self.sikin + 50
                 r = r + 1
             elif m == 2:
                 self.heisi = self.heisi + 15
                 r = r + 1
             elif m == 32:
                 self.kome = self.kome + 100
                 r = r + 1
             elif m == 33:
                 self.sikin = self.sikin + 75
                 r = r + 1
             elif m == 34:
                 self.heisi = self.heisi + 25
                 r = r + 1
             elif m == 64:
                 self.kome = self.kome + 200
                 r = r + 1
             elif m == 65:
                 self.sikin = self.sikin + 100
                 r = r + 1
             elif m == 66:
                 self.heisi = self.heisi + 50
                 r = r + 1
             
                 
     #hyoro
     self.kome = self.kome - int(self.heisi*0.5)
     if self.kome < 0:
         self.heisi = self.heisi - abs(self.kome*3)
         self.heisi = self.heisi - 100
         if self.heisi < 0:
             self.heisi = 0
         self.kome = 0
         
     self.roryoku = self.roryoku + int(r*20)
     self.turn = self.turn + 1
     
     #Daimyo
     self.daimyo1.Turn_change(1)
     self.daimyo2.Turn_change(2)
     
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
                 writer.writerow(data3)
                 data4 = []
                 data4.append(self.daimyo1.kome)
                 data4.append(self.daimyo1.sikin)
                 data4.append(self.daimyo1.heisi)
                 data4.append(self.daimyo1.yuko)
                 data4.append(self.daimyo1.event_cnt)
                 writer.writerow(data4)
                 data5 = []
                 data5.append(self.daimyo2.kome)
                 data5.append(self.daimyo2.sikin)
                 data5.append(self.daimyo2.heisi)
                 data5.append(self.daimyo2.yuko)
                 data5.append(self.daimyo2.event_cnt)
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
         self.daimyo1.kome = int(data[17][0])
         self.daimyo1.sikin = int(data[17][1])
         self.daimyo1.heisi = int(data[17][2])
         self.daimyo1.yuko = int(data[17][3])
         self.daimyo1.event_cnt = int(data[17][4])
         self.daimyo2.kome = int(data[18][0])
         self.daimyo2.sikin = int(data[18][1])
         self.daimyo2.heisi = int(data[18][2])
         self.daimyo2.yuko = int(data[18][3])
         self.daimyo2.event_cnt = int(data[18][4])
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
    def Turn_change(self,d):
        if d == 1:
            self.kome += 300
            self.sikin += 200
            self.heisi += 100
        elif d == 2:
            self.kome += 500
            self.sikin += 500
            self.heisi += 200
        self.event_cnt += randint(5, 10)
        if self.event_cnt >= randint(51, 100):
            self.event_flug = True
            
        
App()
