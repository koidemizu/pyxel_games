import pyxel

class APP:
  def __init__(self):
      pyxel.init(32, 48, caption="BD",scale=10)
      
      pyxel.load('1stBD.pyxres')
      
      pyxel.mouse(False)
      
      self.view_pos = 0
      self.txt_pos = 0
      self.st = 0
      
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
         "!":[152,16],
         "?":[160,16],
         "-":[168,16],
         ".":[176,16],
         ",":[184,16],
         }
      
      self.text_list = {
         "0":["HA","SA","MI",],
         "1":["O","KA","NE"],
         "2":["HO","NN"],
         "3":["BO","-","RU",],
         "4":["PA","SO","KO","NN",],
         "5":["GA","tu","KI",],
      }
      
      pyxel.run(self.update, self.draw)
     
  def update(self):
      if pyxel.btnp(pyxel.KEY_SPACE):
          self.view_pos += 16
          self.txt_pos += 1
          if self.view_pos >80:
              self.view_pos = 0
              self.txt_pos = 0
              
      if self.st == 1:
          self.view_pos += 16
          self.txt_pos += 1
          if self.view_pos >80:
              self.view_pos = 0
              self.txt_pos = 0
              
      if pyxel.btnp(pyxel.KEY_S):
          if self.st == 0:
              self.st = 1
          else:
              self.st = 0
      

  def draw(self):
      pyxel.cls(0)
      
      pyxel.rect(0, 0, 32, 23, 7)
      pyxel.rectb(0, 0, 32, 23, self.view_pos / 16 + 8)
      self.Draw_fonts(self.text_list[str(self.txt_pos)],1, 28)
      pyxel.blt(8,4,0,self.view_pos,0,16,16,14)
      
  def Draw_fonts(self,txt,x,y):  
     txt_count = len(txt)      
     for i in range(txt_count):
         #Key check
         font_xy = self.font_list[txt[i]]
       
         fontx = font_xy[0]
         fonty = font_xy[1]
         pyxel.blt(x + 8 * i,y,1,fontx,fonty,8,8,14)
      

                  
APP()