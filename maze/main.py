# -*- coding: utf-8 -*-

import pyxel

class APP:
  def __init__(self):
      pyxel.init(256, 256, title = "pyxel")
      
      self.maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],
                   [1, 0, 0, 0, 0, 1, 1, 0, 1, 1,],
                   [1, 0, 1, 1, 0, 1, 1, 0, 1, 1,],
                   [1, 0, 1, 1, 0, 0, 0, 0, 0, 1,],
                   [1, 0, 1, 1, 0, 1, 1, 0, 1, 1,],
                   [1, 0, 0, 0, 0, 1, 1, 1, 1, 1,],
                   [1, 1, 1, 1, 0, 1, 1, 1, 1, 1,],
                   [1, 1, 1, 1, 0, 1, 0, 1, 1, 1,],
                   [1, 1, 1, 1, 0, 0, 0, 1, 1, 1,],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1,],]
      
      self.pos = [4, 4]
      self.pos_angle = 1
      
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]

      for i1 in range(5):
          x1 = self.pos[1] - (1 * i1)
          if self.maze[x1][self.pos[0]] == 1:
              self.dead_end = i1      
      self.dead_end = 0
      
      pyxel.run(self.update, self.draw)
     
  def update(self): 
      
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]      
              
      if pyxel.btnp(pyxel.KEY_UP):
          self.dead_end = 0
          if self.pos_angle == 1:
              if self.maze[self.pos[1] - 1][self.pos[0]] == 0:
                  self.pos[1] = self.pos[1] - 1
                  self.pos_angle = 1
          elif self.pos_angle == 2:
              if self.maze[self.pos[1]][self.pos[0] + 1] == 0:
                  self.pos[0] = self.pos[0] + 1
                  self.pos_angle = 2
          elif self.pos_angle == 3:
              if self.maze[self.pos[1] + 1][self.pos[0]] == 0:
                  self.pos[1] = self.pos[1] + 1
                  self.pos_angle = 3
          elif self.pos_angle == 4:
              if self.maze[self.pos[1]][self.pos[0] - 1] == 0:
                  self.pos[0] = self.pos[0] - 1     
                  self.pos_angle = 4
                  

          
      if pyxel.btnp(pyxel.KEY_DOWN):
          self.dead_end = 0
          if self.pos_angle == 1:
              if self.maze[self.pos[1] + 1][self.pos[0]] == 0:
                  self.pos[1] = self.pos[1] + 1
                  self.pos_angle = 3
          elif self.pos_angle == 2:
              if self.maze[self.pos[1]][self.pos[0] - 1] == 0:
                  self.pos[0] = self.pos[0] - 1     
                  self.pos_angle = 4
          elif self.pos_angle == 3:
              if self.maze[self.pos[1] - 1][self.pos[0]] == 0:
                  self.pos[1] = self.pos[1] - 1
                  self.pos_angle = 1
          elif self.pos_angle == 4:
              if self.maze[self.pos[1]][self.pos[0] + 1] == 0:
                  self.pos[0] = self.pos[0] + 1
                  self.pos_angle = 2
          
      if pyxel.btnp(pyxel.KEY_RIGHT):
          self.dead_end = 0
          if self.pos_angle == 1:
              if self.maze[self.pos[1]][self.pos[0] + 1] == 0:
                  self.pos[0] = self.pos[0] + 1
                  self.pos_angle = 2
          elif self.pos_angle == 2:
              if self.maze[self.pos[1] + 1][self.pos[0]] == 0:
                  self.pos[1] = self.pos[1] + 1
                  self.pos_angle = 3
          elif self.pos_angle == 3:
              if self.maze[self.pos[1]][self.pos[0] - 1] == 0:
                  self.pos[0] = self.pos[0] - 1     
                  self.pos_angle = 4
          elif self.pos_angle == 4:
              if self.maze[self.pos[1] - 1][self.pos[0]] == 0:
                  self.pos[1] = self.pos[1] - 1
                  self.pos_angle = 1
          
      if pyxel.btnp(pyxel.KEY_LEFT):
          self.dead_end = 0
          if self.pos_angle == 1:
              if self.maze[self.pos[1]][self.pos[0] - 1] == 0:
                  self.pos[0] = self.pos[0] - 1     
                  self.pos_angle = 4
          elif self.pos_angle == 2:
              if self.maze[self.pos[1] - 1][self.pos[0]] == 0:
                  self.pos[1] = self.pos[1] - 1
                  self.pos_angle = 1
          elif self.pos_angle == 3:
              if self.maze[self.pos[1]][self.pos[0] + 1] == 0:
                  self.pos[0] = self.pos[0] + 1
                  self.pos_angle = 2
          elif self.pos_angle == 4:
              if self.maze[self.pos[1] + 1][self.pos[0]] == 0:
                  self.pos[1] = self.pos[1] + 1
                  self.pos_angle = 3    
  
          
      if self.pos_angle == 1:
          for i1 in range(4):
              if self.pos[1] - i1 < 0:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] - (1 * i1)
                  p2 = self.pos[0] - 1 + (2 * i2) 
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[p1][self.pos[0]] == 1:
                      if self.dead_end == 0:
                          self.dead_end = i1
                      if self.dead_end > i1:
                          self.dead_end = i1
                      
      elif self.pos_angle == 3:
          for i1 in range(4):
              if self.pos[1] + i1 > 9:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] + (1 * i1)
                  p2 = self.pos[0] + 1 - (2 * i2) 
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[p1][self.pos[0]] == 1:
                      if self.dead_end == 0:
                          self.dead_end = i1
                      if self.dead_end > i1:
                          self.dead_end = i1
                      
      elif self.pos_angle == 2:
          for i1 in range(4):
              if self.pos[0] + i1 > 9:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] - 1 + (2 * i2) 
                  p2 = self.pos[0] + (1 * i1)
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[self.pos[1]][p2] == 1:
                      if self.dead_end == 0:
                          self.dead_end = i1
                      if self.dead_end > i1:
                          self.dead_end = i1             
                          
      elif self.pos_angle == 4:
          for i1 in range(4):
              if self.pos[0] - i1 < 0:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] + 1 - (2 * i2) 
                  p2 = self.pos[0] - (1 * i1)
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[self.pos[1]][p2] == 1:
                      if self.dead_end == 0:
                          self.dead_end = i1
                      if self.dead_end > i1:
                          self.dead_end = i1            


  def draw(self):
      pyxel.cls(0)
      
      pyxel.rectb(0, 150, 256, 106, 1)
#--------------------------------------------------------------      
      if self.wall[0][0] == 1:
          pyxel.line(0, 0, 50, 29, 6)
          pyxel.line(0, 0, 0, 150, 6)
          pyxel.line(0, 150, 50, 121, 6)
          pyxel.line(50, 29, 50, 121, 6)
      else:
          pyxel.line(0, 29, 50, 29, 6)
          pyxel.line(0, 121, 50, 121, 6)
      if self.wall[0][1] == 1:       
          pyxel.line(256, 0, 205, 29, 6)
          pyxel.line(256, 150, 205, 121, 6)      
          pyxel.line(255, 0, 255, 150, 6)
          pyxel.line(205, 29, 205, 121, 6)
      else:
          pyxel.line(256, 29, 205, 29, 6)
          pyxel.line(256, 121, 205, 121, 6)
#---------------------------------------------------------------          

#---------------------------------------------------------------                    
      if self.wall[1][0] == 1:       
          pyxel.line(50, 29, 80, 45, 12)
          pyxel.line(50, 121, 80, 105, 12)
          pyxel.line(50, 29, 50, 121, 12)
          pyxel.line(80, 45, 80, 105, 12)
      else:          
          pyxel.line(80, 45, 50, 45, 12)
          pyxel.line(80, 105, 50, 105, 12)
      if self.wall[1][1] == 1:       
         pyxel.line(205, 29, 175, 45, 12)
         pyxel.line(205, 121, 175, 105, 12)
         pyxel.line(205, 29, 205, 121, 12)
         pyxel.line(175, 45, 175, 105, 12)
      else:          
          pyxel.line(175, 45, 205, 45, 12)
          pyxel.line(175, 105, 205, 105, 12)      
#---------------------------------------------------------------          
      
#---------------------------------------------------------------                  
      if self.wall[2][0] == 1:       
          pyxel.line(80, 45, 97, 55, 5)
          pyxel.line(80, 105, 97, 95, 5)
          pyxel.line(80, 45, 80, 105, 5)
          pyxel.line(97, 55, 97, 95, 5)
      else:
          pyxel.line(97, 55, 80, 55, 5)
          pyxel.line(97, 95, 80, 95, 5)
      if self.wall[2][1] == 1:       
          pyxel.line(175, 45, 158, 55, 5)
          pyxel.line(175, 105, 158, 95, 5)
          pyxel.line(175, 45, 175, 105, 5)
          pyxel.line(158, 55, 158, 95, 5)
      else:
          pyxel.line(158, 55, 175, 55, 5)
          pyxel.line(158, 95, 175, 95, 5)
#---------------------------------------------------------------

#---------------------------------------------------------------                  
      if self.wall[3][0] == 1:       
          pyxel.line(97, 55, 108, 60, 1)
          pyxel.line(97, 95, 108, 90, 1)
          pyxel.line(97, 55, 97, 95, 1)
          pyxel.line(108, 60, 108, 90, 1)    
      if self.wall[3][1] == 1:       
         pyxel.line(158, 55, 148, 60, 1)
         pyxel.line(158, 95, 148, 90, 1)  
         pyxel.line(158, 55, 158, 95, 1)
         pyxel.line(148, 60, 148, 90, 1)      
#-------------------------------------------------------------      
      

 
      if self.dead_end == 0:
          pass
      elif self.dead_end == 1:
          pyxel.rect(50, 29, 156, 93, 0)
          pyxel.rectb(50, 29, 156, 93, 6)
      elif self.dead_end == 2:
          pyxel.rect(80, 45, 96, 61, 0)
          pyxel.rectb(80, 45, 96, 61, 12)
      elif self.dead_end == 3:
          pyxel.rect(97, 55, 62, 41, 0)
          pyxel.rectb(97, 55, 62, 41, 5)
      elif self.dead_end == 4:
          pyxel.rect(108, 60, 41, 30, 0)
          pyxel.rectb(108, 60, 41, 30, 1)
          
      for d in range(3):
          pyxel.text(30+10*d, 180, str(self.maze[self.pos[1]]
                                  [self.pos[0]-1+d]), 7)
      for d2 in range(3):
          pyxel.text(30+10*d2, 190, str(self.maze[self.pos[1]+1]
                                  [self.pos[0]-1+d2]), 7)
      for d3 in range(3):
          pyxel.text(30+10*d3, 170, str(self.maze[self.pos[1]-1]
                                  [self.pos[0]-1+d3]), 7)          
      pyxel.rect(40, 180, 10, 10, 0)
      if self.pos_angle == 1:
          pyxel.tri(41, 178, 37, 185, 45, 185, 8)
      elif self.pos_angle == 2:
          pyxel.tri(45, 181, 37, 178, 37, 185, 8)
      elif self.pos_angle == 3:
          pyxel.tri(41, 185, 37, 178, 45, 178, 8)
      elif self.pos_angle == 4:
          pyxel.tri(37, 183, 45, 178, 45, 186, 8)
      
      
      
      
APP()

