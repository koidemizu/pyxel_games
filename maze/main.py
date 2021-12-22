# -*- coding: utf-8 -*-

import pyxel

class APP:
  def __init__(self):
      pyxel.init(256, 256, title = "pyxel")
      pyxel.load('assets/assets.pyxres')
      
      self.data = []
      self.maze = []
       
      #Maze set
      for i in range(32):
          self.data = []
          for i2 in range(32):
              self.data.append(pyxel.tilemap(0).pget(i2,i))
          self.maze.append(self.data)
      
      #Player position
      self.pos = [1, 1]
      
      #Angle P=Player
      #    ^
      #    1
      #<4  P   2>
      #    3
      #    v
      #     
      self.pos_angle = 3
      
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]
      #Wall set
      for i1 in range(5):
          x1 = self.pos[1] - (1 * i1)
          if self.maze[x1][self.pos[0]] == 1:
              self.dead_end = i1      
      self.dead_end = 0
      
      pyxel.run(self.update, self.draw)
     
  def update(self): 
      
      #Wall reset
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]      
              
      #Go ahead
      if pyxel.btnp(pyxel.KEY_UP):
          self.dead_end = 0
          if self.pos_angle == 1:
              if self.maze[self.pos[1] - 1][self.pos[0]] == (0, 0):
                  self.pos[1] = self.pos[1] - 1
                  self.pos_angle = 1
          elif self.pos_angle == 2:
              if self.maze[self.pos[1]][self.pos[0] + 1] == (0, 0):
                  self.pos[0] = self.pos[0] + 1
                  self.pos_angle = 2
          elif self.pos_angle == 3:
              if self.maze[self.pos[1] + 1][self.pos[0]] == (0, 0):
                  self.pos[1] = self.pos[1] + 1
                  self.pos_angle = 3
          elif self.pos_angle == 4:
              if self.maze[self.pos[1]][self.pos[0] - 1] == (0, 0):
                  self.pos[0] = self.pos[0] - 1     
                  self.pos_angle = 4
                  

      #Turn to the back
      if pyxel.btnp(pyxel.KEY_DOWN):
          self.dead_end = 0
          if self.pos_angle == 1:
              self.pos_angle = 3
          elif self.pos_angle == 2:
              self.pos_angle = 4
          elif self.pos_angle == 3:
              self.pos_angle = 1
          elif self.pos_angle == 4:
              self.pos_angle = 2
          
      #Turn to the right
      if pyxel.btnp(pyxel.KEY_RIGHT):
          self.dead_end = 0
          if self.pos_angle == 1:
              self.pos_angle = 2
          elif self.pos_angle == 2:              
              self.pos_angle = 3
          elif self.pos_angle == 3:              
              self.pos_angle = 4
          elif self.pos_angle == 4:              
              self.pos_angle = 1
          
      #Turn to the left
      if pyxel.btnp(pyxel.KEY_LEFT):
          self.dead_end = 0
          if self.pos_angle == 1:
              self.pos_angle = 4
          elif self.pos_angle == 2:             
              self.pos_angle = 1
          elif self.pos_angle == 3:              
              self.pos_angle = 2
          elif self.pos_angle == 4:
              self.pos_angle = 3    
  
      #Wall set///////////////////////////////////////////////////////////////        
      if self.pos_angle == 1:
          for i1 in range(4):
              if self.pos[1] - i1 < 0:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] - (1 * i1)
                  p2 = self.pos[0] - 1 + (2 * i2) 
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[p1][self.pos[0]] == (1, 0):
                      if self.dead_end == 0:
                          self.dead_end = i1
                      if self.dead_end > i1:
                          self.dead_end = i1
                      
      elif self.pos_angle == 3:
          for i1 in range(4):
              if self.pos[1] + i1 > 31:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] + (1 * i1)
                  p2 = self.pos[0] + 1 - (2 * i2) 
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[p1][self.pos[0]] == (1, 0):
                      if self.dead_end == 0:
                          self.dead_end = i1
                      if self.dead_end > i1:
                          self.dead_end = i1
                      
      elif self.pos_angle == 2:
          for i1 in range(4):
              if self.pos[0] + i1 > 31:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] - 1 + (2 * i2) 
                  p2 = self.pos[0] + (1 * i1)
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[self.pos[1]][p2] == (1, 0):
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
              
                  if self.maze[self.pos[1]][p2] == (1, 0):
                      if self.dead_end == 0:
                          self.dead_end = i1
                      if self.dead_end > i1:
                          self.dead_end = i1            
      #///////////////////////////////////////////////////////////////////////

  def draw(self):
      pyxel.cls(0)
      
#Bubble draw test--------------------------------------------------------------      
      #bx = 120
      #by = 80
     
      #pyxel.circb(bx, by, 10, 6)
      #pyxel.circb(bx - 5, by - 5, 3, 6)
      #pyxel.circb(bx - 6, by - 6, 1, 7)
      
      #bx = 120
      #by = 110
     
      #pyxel.circb(bx, by, 7, 6)
      #pyxel.circb(bx - 3, by - 3, 2, 6)
      #pyxel.circb(bx - 4, by - 4, 1, 7)      
      
      
      #bx = 120
      #by = 130
     
      #pyxel.circb(bx, by, 5, 6)
      #pyxel.circb(bx - 3, by - 1, 1, 6)
      #pyxel.circb(bx - 4, by - 2, 1, 7)      
      
#------------------------------------------------------------------------------      
      
      pyxel.rectb(0, 150, 256, 106, 1)
      
#Draw wall 1------------------------------------------------------------------      
      if self.wall[0][0] == (1, 0):
          pyxel.line(0, 0, 50, 29, 6)
          pyxel.line(0, 0, 0, 150, 6)
          pyxel.line(0, 150, 50, 121, 6)
          pyxel.line(50, 29, 50, 121, 6)
      else:
          pyxel.line(0, 29, 50, 29, 6)
          pyxel.line(0, 121, 50, 121, 6)
      if self.wall[0][1] == (1, 0):       
          pyxel.line(256, 0, 205, 29, 6)
          pyxel.line(256, 150, 205, 121, 6)      
          pyxel.line(255, 0, 255, 150, 6)
          pyxel.line(205, 29, 205, 121, 6)
      else:
          pyxel.line(256, 29, 205, 29, 6)
          pyxel.line(256, 121, 205, 121, 6)
#-----------------------------------------------------------------------------          

#Draw wall 2------------------------------------------------------------------                    
      if self.wall[1][0] == (1, 0):       
          pyxel.line(50, 29, 80, 45, 12)
          pyxel.line(50, 121, 80, 105, 12)
          pyxel.line(50, 29, 50, 121, 12)
          pyxel.line(80, 45, 80, 105, 12)
      else:          
          pyxel.line(79, 45, 51, 45, 12)
          pyxel.line(79, 105, 51, 105, 12)
      if self.wall[1][1] == (1, 0):       
         pyxel.line(205, 29, 175, 45, 12)
         pyxel.line(205, 121, 175, 105, 12)
         pyxel.line(205, 29, 205, 121, 12)
         pyxel.line(175, 45, 175, 105, 12)
      else:          
          pyxel.line(176, 45, 204, 45, 12)
          pyxel.line(176, 105, 204, 105, 12)      
#----------------------------------------------------------------------------          
      
#Draw wall 3-----------------------------------------------------------------                  
      if self.wall[2][0] == (1, 0):       
          pyxel.line(80, 45, 97, 55, 5)
          pyxel.line(80, 105, 97, 95, 5)
          pyxel.line(80, 45, 80, 105, 5)
          pyxel.line(97, 55, 97, 95, 5)
      else:
          pyxel.line(97, 55, 81, 55, 5)
          pyxel.line(97, 95, 81, 95, 5)
      if self.wall[2][1] == (1, 0):       
          pyxel.line(175, 45, 158, 55, 5)
          pyxel.line(175, 105, 158, 95, 5)
          pyxel.line(175, 45, 175, 105, 5)
          pyxel.line(158, 55, 158, 95, 5)
      else:
          pyxel.line(158, 55, 174, 55, 5)
          pyxel.line(158, 95, 174, 95, 5)
#----------------------------------------------------------------------------

#Draw wall 4-----------------------------------------------------------------                  
      if self.wall[3][0] == (1, 0):       
          pyxel.line(97, 55, 108, 60, 1)
          pyxel.line(97, 95, 108, 90, 1)
          pyxel.line(97, 55, 97, 95, 1)
          pyxel.line(108, 60, 108, 90, 1)    
      if self.wall[3][1] == (1, 0):       
         pyxel.line(158, 55, 148, 60, 1)
         pyxel.line(158, 95, 148, 90, 1)  
         pyxel.line(158, 55, 158, 95, 1)
         pyxel.line(148, 60, 148, 90, 1)      
#-----------------------------------------------------------------------------      
    
#Draw Dead-End----------------------------------------------------------------
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
#-----------------------------------------------------------------------------          
          
#Draw Compass-----------------------------------------------------------------
      pyxel.rectb(14, 164, 55, 45, 13)
      for d0 in range(5):
          if self.maze[self.pos[1]-1][self.pos[0]-2+d0] == (1, 0):
              pyxel.rect(17+10*d0, 167, 9, 9, 7)
      for d1 in range(5):
          if self.maze[self.pos[1]][self.pos[0]-2+d1] == (1, 0):
              pyxel.rect(17+10*d1, 177, 9, 9, 7)
      for d2 in range(5):
          if self.maze[self.pos[1]+1][self.pos[0]-2+d2] == (1, 0):
              pyxel.rect(17+10*d2, 187, 9, 9, 7)
      for d3 in range(5):
          if self.maze[self.pos[1]+2][self.pos[0]-2+d3] == (1, 0):
              pyxel.rect(17+10*d3, 197, 9, 9, 7)              

            
      if self.pos_angle == 1:
          pyxel.tri(41, 178, 37, 185, 45, 185, 8)
      elif self.pos_angle == 2:
          pyxel.tri(45, 181, 37, 178, 37, 185, 8)
      elif self.pos_angle == 3:
          pyxel.tri(41, 185, 37, 178, 45, 178, 8)
      elif self.pos_angle == 4:
          pyxel.tri(37, 183, 45, 178, 45, 186, 8)
#-----------------------------------------------------------------------------      
      
      
      
APP()

