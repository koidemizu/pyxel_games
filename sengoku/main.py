#main.py

import pyxel
import csv
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
     self.window_ctr = 0
     self.txt_ctr = 0
     self.inf_ctr = 999
     self.update_list = []
     self.update_tgt = 0
     self.turn = 1
     #Player status
     self.sikin = 0
     self.roryoku = 100
     self.heisi = 0
     self.kome = 0
     
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
                 if self.txt_ctr < 3 or self.txt_ctr == 5:
                    self.update_tgt = 0
                    self.window_ctr = 2
                 elif self.txt_ctr == 3:
                     self.update_tgt = 5
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
         if self.txt_ctr < 3 or self.txt_ctr == 5:
             self.update_list = [0,1,2]
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
         #Target = KI
         elif self.txt_ctr == 3:
             self.update_list = [5]
             l = len(self.update_list)
             for i in range(l):
                 self.Draw_fonts(self.text_list[str(self.update_list[i])],
                                 12, 56+10*i)
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
         
 def Draw_fonts(self,txt,x,y):  
     txt_count = len(txt)      
     for i in range(txt_count):
         #Key check
         font_xy = self.font_list[txt[i]]
        
         fontx = font_xy[0]
         fonty = font_xy[1]
         pyxel.blt(x + 8 * i,y,1,fontx,fonty,8,8,14)
         
 def Turn_change(self):
     for i in range(16):
         for i2 in range(16):
             m = pyxel.tilemap(0).data[i][i2]
             if m == 0:
                 self.kome = self.kome + 100
             elif m == 1:
                 self.sikin = self.sikin + 100
             elif m == 2:
                 self.heisi = self.heisi + 100
     self.roryoku = self.roryoku + 100
     self.turn = self.turn + 1
     
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
        #Taget point check
        tile = format(v, 'x')
        tile2 = str(format(tile, '0>3'))
        x = self.tgt_x
        y = self.tgt_y
        #Update tilemap
        pyxel.tilemap(0).set(x, y, [tile2]) 
        
App()
