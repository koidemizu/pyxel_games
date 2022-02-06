# -*- coding: utf-8 -*-

import pyxel
from random import choice

class APP:
  def __init__(self):
      pyxel.init(256, 256, title = "pyxel")
      pyxel.load('assets/assets.pyxres')             
      
      #Maze set
      self.data = []
      self.maze = []
      
      for i in range(32):
          self.data = []
          for i2 in range(32):
              self.data.append(pyxel.tilemap(0).pget(i2,i))
          self.maze.append(self.data)
      
      #Player status--------------------------------------------------
      #Player position
      self.pos = [1, 1]
      #Move permission tile list      
      self.move_permit = [(0, 0), (0, 1)]
      #Paint Can count
      self.paint_cnt = 5
      
      self.key_flag = False
      
      self.move_flag = False
      
      #Angle P=Player
      #    ^
      #    1
      #<4  P   2>
      #    3
      #    v
      #     
      self.pos_angle = 3
      
      #----------------------------------------------------------------
      
      #Wall set
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]
      
      for i1 in range(5):
          x1 = self.pos[1] - (1 * i1)
          if self.maze[x1][self.pos[0]] == 1:
              self.dead_end[0] = i1      
      self.dead_end = [0, (0, 0)]
      
      self.wall_list = [(1, 0), (1, 1), (2, 1)]
      
      #Floor
      self.floor = [0, 0, 0, 0]
      
      #Bubble
      self.bubbles = [] 
      self.bubble_cnt = 0      
      #Bubble color list
      self.bub_c = (1, 5, 6, 12)
      
      #Enemy
      self.enemys = []
      self.enemy_set =[
                      (1, 10),
                      (7, 5),
                      (8, 26),
                      (24, 22),
                      (17, 17),
                      (22, 6),
                      ]
      for e in self.enemy_set:
          self.enemys.append(Enemy(e[0], e[1], self.maze, self.move_permit))      
      self.enemy_pos = 9
      pyxel.mouse(True)
      
      #System
      self.game_over = False
      self.e_msg = "Enemies nearby: X"      
      self.e_msg_c = 0
      self.e_msg_F = False
      
      self.game_msg = GameMsg()      
      pyxel.run(self.update, self.draw)
     
  def reset(self):        
      #Player position
      self.pos = [1, 1]     
      
      self.paint_cnt = 5
      self.move_flag = False      
      self.pos_angle = 3
      self.key_flag = False
      
      #Wall set
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]
      
      for i1 in range(5):
          x1 = self.pos[1] - (1 * i1)
          if self.maze[x1][self.pos[0]] == 1:
              self.dead_end[0] = i1      
      self.dead_end = [0, (0, 0)]
      
      #Floor
      self.floor = [0, 0, 0, 0]
      
      #Bubble
      self.bubbles = [] 
      self.bubble_cnt = 0      
      #Bubble color list
      self.bub_c = (1, 5, 6, 12)
      
      #Enemy
      self.enemys = []      
      
      for e in self.enemy_set:
          self.enemys.append(Enemy(e[0], e[1], self.maze, self.move_permit))            
      self.enemy_pos = 9
      
      #System
      self.game_over = False
      self.e_msg = "Enemies nearby: X"      
      self.e_msg_c = 0
      self.e_msg_F = False
      
      self.game_msg = GameMsg()      
      
  def update(self): 
      print(self.enemy_pos)
      #print(pyxel.mouse_x, pyxel.mouse_y)
      #Bubble generate test---------------------------------------------------
      if pyxel.btnp(pyxel.KEY_B):
          c = choice(self.bub_c)
          x = pyxel.rndi(0, 256)
          y = pyxel.rndi(160, 220)
          v = pyxel.rndi(0, 2)
          s1 = pyxel.rndi(1, 2)
          s2 = pyxel.rndi(1, 9) / 10
          s = s1 + s2
          new_bubble = Bubble(x, y, v, c, s)
          self.bubbles.append(new_bubble)
      #-----------------------------------------------------------------------
      
      if pyxel.btnp(pyxel.KEY_M):
          self.game_msg.update("Test M", 3)
          
      #Game Over Move---------------------------------------------------------    
      if self.game_over == True and pyxel.btnp(pyxel.KEY_R):
          self.reset()
      if self.game_over == True and pyxel.btnp(pyxel.KEY_Q):
          pyxel.quit()
      #-----------------------------------------------------------------------          

      #New bubble create------------------------------------------------------
      if self.bubble_cnt == 0:
          self.bubble_cnt = pyxel.rndi(200, 400)
          b_num = pyxel.rndi(2, 10)
          for bn in range(b_num):
              c = choice(self.bub_c)
              x = pyxel.rndi(30, 220)
              y = pyxel.rndi(160, 220)
              v = pyxel.rndi(0, 2)
              s1 = pyxel.rndi(1, 2)
              s2 = pyxel.rndi(1, 9) / 10
              s = s1 + s2
              new_bubble = Bubble(x, y, v, c, s)
              self.bubbles.append(new_bubble)
              
      #Bubble update----------------------------------------------------------      
      b_mi = pyxel.rndi(1, 10)
      self.bubble_cnt -= b_mi
      for b in self.bubbles:
          b.update()
          if b.bub_y < 0:
              del b              
       #----------------------------------------------------------------------      
      if self.game_over == True:
          pass
      else:
          self.Game_update()
          
  def Game_update(self):                           
      #Wall reset
      self.wall = [[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],]      
      self.floor = [0, 0, 0, 0]
      
      #Enemy reset
      self.enemy_pos = 9      
              
      #Player Controll--------------------------------------------------------
      self.move_flag = False
      #Go ahead
      if pyxel.btnp(pyxel.KEY_UP):          
          self.dead_end[0] = 0
          if self.pos_angle == 1:
              if self.maze[self.pos[1] - 1][self.pos[0]] in self.move_permit:
                  self.move_flag = True
                  self.e_msg_F = False
                  self.pos[1] = self.pos[1] - 1
                  self.pos_angle = 1
              #Tile Check(Start position)
              elif self.maze[self.pos[1] - 1][self.pos[0]] == (1, 1):
                  self.game_msg.update("Start position", 3)
                  self.game_msg.update("Find out the secret information!", 10)                  
              #Tile Check(Goal position)
              elif self.maze[self.pos[1] - 1][self.pos[0]] == (2, 1):
                  print("Goal position")                  
          elif self.pos_angle == 2:
              if self.maze[self.pos[1]][self.pos[0] + 1] in self.move_permit:
                  self.move_flag = True
                  self.e_msg_F = False
                  self.pos[0] = self.pos[0] + 1
                  self.pos_angle = 2
              #Tile Check(Start position)
              elif self.maze[self.pos[1]][self.pos[0] + 1] == (1, 1):
                  self.game_msg.update("Start position", 3)
                  self.game_msg.update("Find out the secret information!", 10)                                    
              #Tile Check(Goal position)
              elif self.maze[self.pos[1]][self.pos[0] + 1] == (2, 1):
                  print("Goal position")                                    
          elif self.pos_angle == 3:
              if self.maze[self.pos[1] + 1][self.pos[0]] in self.move_permit:
                  self.move_flag = True
                  self.e_msg_F = False
                  self.pos[1] = self.pos[1] + 1
                  self.pos_angle = 3
              #Tile Check(Start position)
              elif self.maze[self.pos[1] + 1][self.pos[0]] == (1, 1):
                  self.game_msg.update("Start position", 3)
                  self.game_msg.update("Find out the secret information!", 10)                                    
              #Tile Check(Goal position)
              elif self.maze[self.pos[1] + 1][self.pos[0]] == (2, 1):
                  print("Goal position")                                    
          elif self.pos_angle == 4:
              if self.maze[self.pos[1]][self.pos[0] - 1] in self.move_permit:
                  self.move_flag = True
                  self.e_msg_F = False
                  self.pos[0] = self.pos[0] - 1     
                  self.pos_angle = 4
              #Tile Check(Start position)
              elif self.maze[self.pos[1]][self.pos[0] - 1] == (1, 1):
                  self.game_msg.update("Start position", 3)
                  self.game_msg.update("Find out the secret information!", 10)                                    
              #Tile Check(Goal position)
              elif self.maze[self.pos[1]][self.pos[0] - 1] == (2, 1):
                  print("Goal position")                                    

          #Enemy action
          self.e_msg_c = 0          
          for e in self.enemys:
              if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                  self.enemy_pos = 0                  
                  self.game_over = True
                  
              if self.enemy_pos > 0:
                  if self.move_flag == True:
                      e.update()                  
                  x = abs(self.pos[0] - e.ene_x) 
                  y = abs(self.pos[1] - e.ene_y) 
                  if x < 5 and y < 5:                      
                      self.e_msg_c += 1
                  if x < 3 and y < 3:
                      self.e_msg_F = True            
                  self.e_msg = "Enemies nearby: " + str(self.e_msg_c)
                  
              if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                  self.enemy_pos = 0     
                  self.bubble_cnt = 0
                  self.game_over = True
                      
      #Turn to the back
      if pyxel.btnp(pyxel.KEY_DOWN):
          self.dead_end[0] = 0
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
          self.dead_end[0] = 0
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
          self.dead_end[0] = 0
          if self.pos_angle == 1:
              self.pos_angle = 4
          elif self.pos_angle == 2:             
              self.pos_angle = 1
          elif self.pos_angle == 3:              
              self.pos_angle = 2
          elif self.pos_angle == 4:
              self.pos_angle = 3    
      #-----------------------------------------------------------------------
  
      #Wall-Floor set & Enemy-serch-------------------------------------------      
      if self.pos_angle == 1:
          for i1 in range(4):
              if self.pos[1] - i1 < 0:
                  break           
              for i2 in range(2):
                  p1 = self.pos[1] - (1 * i1)
                  p2 = self.pos[0] - 1 + (2 * i2) 
              
                  self.wall[i1][i2] = self.maze[p1][p2]
                               
                  if self.maze[p1][self.pos[0]] in self.wall_list:                      
                      if self.dead_end[0] == 0:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[p1][self.pos[0]]
                      if self.dead_end[0] > i1:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[p1][self.pos[0]]                                                                    
                  elif self.maze[p1][self.pos[0]] == (0, 1):
                          self.floor[i1] = 1
                          
                  for e in self.enemys:
                      if p1 == e.ene_y and self.pos[0]  == e.ene_x:
                          self.enemy_pos = i1        
                          if self.enemy_pos > i1:                            
                              self.enemy_pos = i1       
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0                  
                          self.bubble_cnt = 0
                          self.game_over = True                               
                         
                        
      elif self.pos_angle == 3:
          for i1 in range(4):
              if self.pos[1] + i1 > 31:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] + (1 * i1)
                  p2 = self.pos[0] + 1 - (2 * i2) 
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[p1][self.pos[0]] in self.wall_list:                      
                      if self.dead_end[0] == 0:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[p1][self.pos[0]]
                      if self.dead_end[0] > i1:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[p1][self.pos[0]]
                  elif self.maze[p1][self.pos[0]] == (0, 1):
                      self.floor[i1] = 1                          
                      
                  for e in self.enemys:
                      if p1 == e.ene_y and self.pos[0]  == e.ene_x:
                          if self.enemy_pos > i1:                                         
                              self.enemy_pos = i1         
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0        
                          self.bubble_cnt = 0
                          self.game_over = True                                                             
                      
                      
      elif self.pos_angle == 2:
          for i1 in range(4):
              if self.pos[0] + i1 > 31:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] - 1 + (2 * i2) 
                  p2 = self.pos[0] + (1 * i1)
              
                  self.wall[i1][i2] = self.maze[p1][p2]                  
              
                  if self.maze[self.pos[1]][p2] in self.wall_list:                                            
                      if self.dead_end[0] == 0:
                          self.dead_end[0] = i1
                          self.dead_end[1] = self.maze[self.pos[1]][p2]
                      if self.dead_end[0] > i1:
                          self.dead_end[0] = i1             
                          self.dead_end[1] = self.maze[self.pos[1]][p2]
                  elif self.maze[self.pos[1]][p2] == (0, 1):
                      self.floor[i1] = 1                          
                          
                  for e in self.enemys:
                      if p2 == e.ene_x and self.pos[1]  == e.ene_y:
                          if self.enemy_pos > i1:                            
                              self.enemy_pos = i1              
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0        
                          self.bubble_cnt = 0
                          self.game_over = True                                                             
                              
      elif self.pos_angle == 4:
          for i1 in range(4):
              if self.pos[0] - i1 < 0:
                  break
              for i2 in range(2):
                  p1 = self.pos[1] + 1 - (2 * i2) 
                  p2 = self.pos[0] - (1 * i1)
              
                  self.wall[i1][i2] = self.maze[p1][p2]
              
                  if self.maze[self.pos[1]][p2] in self.wall_list:                      
                      if self.dead_end[0] == 0:
                          self.dead_end[0] = i1                   
                          self.dead_end[1] = self.maze[self.pos[1]][p2]
                      if self.dead_end[0] > i1:
                          self.dead_end[0] = i1        
                          self.dead_end[1] = self.maze[self.pos[1]][p2]
                  elif self.maze[self.pos[1]][p2] == (0, 1):
                      self.floor[i1] = 1                       
                      
                  for e in self.enemys:
                      if p2 == e.ene_x and self.pos[1]  == e.ene_y:
                          if self.enemy_pos > i1:                            
                              self.enemy_pos = i1            
                      if e.ene_x == self.pos[0] and e.ene_y == self.pos[1]:
                          self.enemy_pos = 0          
                          self.bubble_cnt = 0
                          self.game_over = True                                                             
      #-----------------------------------------------------------------------
      
      #Paint floor action-----------------------------------------------------
      if pyxel.btnp(pyxel.KEY_SPACE):
          if self.paint_cnt > 0:
              if self.maze[self.pos[1]][self.pos[0]] == (0, 1):
                  pass
              else:
                  self.maze[self.pos[1]][self.pos[0]] = (0, 1)                        
                  self.paint_cnt -= 1
      #-----------------------------------------------------------------------
      
          

  def draw(self):
      pyxel.cls(0)                        
      
#Draw wall 1------------------------------------------------------------------      
      if self.wall[0][0] == (1, 0):
          pyxel.line(0, 0, 50, 29, 6)
          pyxel.line(0, 0, 0, 150, 6)
          pyxel.line(0, 150, 50, 121, 6)
          pyxel.line(50, 29, 50, 121, 6)
      elif self.wall[0][0] == (1, 1):
          pyxel.line(0, 0, 50, 29, 9)
          pyxel.line(0, 0, 0, 150, 9)
          pyxel.line(0, 150, 50, 121, 9)
          pyxel.line(50, 29, 50, 121, 9)          
      elif self.wall[0][0] == (2, 1):
          pyxel.line(0, 0, 50, 29, 10)
          pyxel.line(0, 0, 0, 150, 10)
          pyxel.line(0, 150, 50, 121, 10)
          pyxel.line(50, 29, 50, 121, 10)               
      else:
          pyxel.line(0, 29, 50, 29, 6)
          pyxel.line(0, 121, 50, 121, 6)
          
      if self.wall[0][1] == (1, 0):       
          pyxel.line(256, 0, 205, 29, 6)
          pyxel.line(256, 150, 205, 121, 6)      
          pyxel.line(255, 0, 255, 150, 6)
          pyxel.line(205, 29, 205, 121, 6)
      elif self.wall[0][1] == (1, 1):       
          pyxel.line(256, 0, 205, 29, 9)
          pyxel.line(256, 150, 205, 121, 9)      
          pyxel.line(255, 0, 255, 150, 9)
          pyxel.line(205, 29, 205, 121, 9)
      elif self.wall[0][1] == (2, 1):       
          pyxel.line(256, 0, 205, 29, 10)
          pyxel.line(256, 150, 205, 121, 10)      
          pyxel.line(255, 0, 255, 150, 10)
          pyxel.line(205, 29, 205, 121, 10)          
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
      elif self.wall[1][0] == (1, 1):       
          pyxel.line(50, 29, 80, 45, 9)
          pyxel.line(50, 121, 80, 105, 9)
          pyxel.line(50, 29, 50, 121, 9)
          pyxel.line(80, 45, 80, 105, 9)
      elif self.wall[1][0] == (2, 1):       
          pyxel.line(50, 29, 80, 45, 10)
          pyxel.line(50, 121, 80, 105, 10)
          pyxel.line(50, 29, 50, 121, 10)
          pyxel.line(80, 45, 80, 105, 10)          
      else:          
          pyxel.line(79, 45, 51, 45, 12)
          pyxel.line(79, 105, 51, 105, 12)
          
      if self.wall[1][1] == (1, 0):       
         pyxel.line(205, 29, 175, 45, 12)
         pyxel.line(205, 121, 175, 105, 12)
         pyxel.line(205, 29, 205, 121, 12)
         pyxel.line(175, 45, 175, 105, 12)
      elif self.wall[1][1] == (1, 1):       
         pyxel.line(205, 29, 175, 45, 9)
         pyxel.line(205, 121, 175, 105, 9)
         pyxel.line(205, 29, 205, 121, 9)
         pyxel.line(175, 45, 175, 105, 9)
      elif self.wall[1][1] == (2, 1):       
         pyxel.line(205, 29, 175, 45, 10)
         pyxel.line(205, 121, 175, 105, 10)
         pyxel.line(205, 29, 205, 121, 10)
         pyxel.line(175, 45, 175, 105, 10)         
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
      elif self.wall[2][0] == (1, 1):       
          pyxel.line(80, 45, 97, 55, 9)
          pyxel.line(80, 105, 97, 95, 9)
          pyxel.line(80, 45, 80, 105, 9)
          pyxel.line(97, 55, 97, 95, 9)
      elif self.wall[2][0] == (2, 1):       
          pyxel.line(80, 45, 97, 55, 10)
          pyxel.line(80, 105, 97, 95, 10)
          pyxel.line(80, 45, 80, 105, 10)
          pyxel.line(97, 55, 97, 95, 10)          
      else:
          pyxel.line(97, 55, 81, 55, 5)
          pyxel.line(97, 95, 81, 95, 5)
          
      if self.wall[2][1] == (1, 0):       
          pyxel.line(175, 45, 158, 55, 5)
          pyxel.line(175, 105, 158, 95, 5)
          pyxel.line(175, 45, 175, 105, 5)
          pyxel.line(158, 55, 158, 95, 5)
      elif self.wall[2][1] == (1, 1):       
          pyxel.line(175, 45, 158, 55, 9)
          pyxel.line(175, 105, 158, 95, 9)
          pyxel.line(175, 45, 175, 105, 9)
          pyxel.line(158, 55, 158, 95, 9)
      elif self.wall[2][1] == (2, 1):       
          pyxel.line(175, 45, 158, 55, 10)
          pyxel.line(175, 105, 158, 95, 10)
          pyxel.line(175, 45, 175, 105, 10)
          pyxel.line(158, 55, 158, 95, 10)          
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
      elif self.wall[3][0] == (1, 1):       
          pyxel.line(97, 55, 108, 60, 9)
          pyxel.line(97, 95, 108, 90, 9)
          pyxel.line(97, 55, 97, 95, 9)
          pyxel.line(108, 60, 108, 90, 9)              
      elif self.wall[3][0] == (2, 1):       
          pyxel.line(97, 55, 108, 60, 10)
          pyxel.line(97, 95, 108, 90, 10)
          pyxel.line(97, 55, 97, 95, 10)
          pyxel.line(108, 60, 108, 90, 10)    
          
      if self.wall[3][1] == (1, 0):       
         pyxel.line(158, 55, 148, 60, 1)
         pyxel.line(158, 95, 148, 90, 1)  
         pyxel.line(158, 55, 158, 95, 1)
         pyxel.line(148, 60, 148, 90, 1)      
      elif self.wall[3][1] == (1, 1):       
         pyxel.line(158, 55, 148, 60, 9)
         pyxel.line(158, 95, 148, 90, 9)  
         pyxel.line(158, 55, 158, 95, 9)
         pyxel.line(148, 60, 148, 90, 9)      
      elif self.wall[3][1] == (2, 1):       
         pyxel.line(158, 55, 148, 60, 10)
         pyxel.line(158, 95, 148, 90, 10)  
         pyxel.line(158, 55, 158, 95, 10)
         pyxel.line(148, 60, 148, 90, 10)               
#-----------------------------------------------------------------------------      
    
#Draw Floor paint-------------------------------------------------------------
      if self.floor[0] == 1:
          pyxel.line(67, 145, 178, 130, 8)
          pyxel.line(70, 130, 178, 145, 8)
      if self.floor[1] == 1:
          pyxel.line(95, 117, 155, 107, 8)
          pyxel.line(95, 107, 155, 117, 8)
      if self.floor[2] == 1:
          pyxel.line(110, 104, 140, 97, 1)
          pyxel.line(110, 97, 140, 104, 1)        
      if self.floor[3] == 1:
          pyxel.line(115, 92, 135, 95, 1)
          pyxel.line(115, 95, 135, 92, 1)    
      
#-----------------------------------------------------------------------------      



#Draw Dead-End----------------------------------------------------------------
      #print(self.dead_end[1])
      if self.dead_end[0] == 0:
          pass
      elif self.dead_end[0] == 1:
          if self.dead_end[1] == (1, 0):
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 6)
          elif self.dead_end[1] == (1, 1):
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 9)              
          elif self.dead_end[1] == (2, 1):
              pyxel.rect(50, 29, 156, 93, 0)
              pyxel.rectb(50, 29, 156, 93, 10)                  
      elif self.dead_end[0] == 2:
          if self.dead_end[1] == (1, 0):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 12)
          elif self.dead_end[1] == (1, 1):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 9)              
          elif self.dead_end[1] == (2, 1):
              pyxel.rect(80, 45, 96, 61, 0)
              pyxel.rectb(80, 45, 96, 61, 10)                    
      elif self.dead_end[0] == 3:
          if self.dead_end[1] == (1, 0):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 5)
          elif self.dead_end[1] == (1, 1):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 9)              
          elif self.dead_end[1] == (2, 1):
              pyxel.rect(97, 55, 62, 41, 0)
              pyxel.rectb(97, 55, 62, 41, 10)                      
      elif self.dead_end[0] == 4:
          if self.dead_end[1] == (1, 0):
              pyxel.rect(108, 60, 41, 30, 0)
              pyxel.rectb(108, 60, 41, 30, 1)
          elif self.dead_end[1] == (1, 1):
              pyxel.rect(108, 60, 41, 30, 0)
              pyxel.rectb(108, 60, 41, 30, 9)              
          elif self.dead_end[1] == (2, 1):
              pyxel.rect(108, 60, 41, 30, 0)
              pyxel.rectb(108, 60, 41, 30, 10)                      
#-----------------------------------------------------------------------------     

          
      
#Bubble draw 1--------------------------------------------------------------     
      bn = len(self.bubbles)
      for b in range(bn) :
          bx = self.bubbles[b].bub_x
          by = self.bubbles[b].bub_y
          bc = self.bubbles[b].bub_c
          bv = self.bubbles[b].bub_v
          
          if b % 2 == 0:
              if bv == 0:
                  pyxel.circb(bx, by, 10, bc)
                  pyxel.circb(bx - 5, by - 5, 3, bc)
                  pyxel.circb(bx - 6, by - 6, 1, 7)
              elif bv == 1:     
                  pyxel.circb(bx, by, 7, 6)
                  pyxel.circb(bx - 3, by - 3, 2, bc)
                  pyxel.circb(bx - 4, by - 4, 1, bc)      
              elif bv == 2:
                  pyxel.circb(bx, by, 5, 6)
                  pyxel.circb(bx - 3, by - 1, 1, bc)
                  pyxel.circb(bx - 4, by - 2, 1, bc)      
      
#------------------------------------------------------------------------------      


#Draw Game Over text----------------------------------------------------------
      if self.game_over == True:
          pyxel.circ(124, 87, 45, 0)
          pyxel.text(105, 70, "GAME OVER!!", 8)
          pyxel.text(105, 90, "R: RETRY", 8)
          pyxel.text(105, 100, "Q: QUIT", 8)
#-----------------------------------------------------------------------------          
          
          
#Draw enemy------------------------------------------------------------------
       
      if ((self.enemy_pos == 3 and self.enemy_pos < self.dead_end[0])
         or (self.enemy_pos == 3 and self.dead_end[0] == 0)) : 
       #Pos 1------------------------------------------------------------------
          ex = 117
          ey = 75
          pyxel.circ(ex, ey, 1, 9)
          pyxel.circ(ex - 1, ey + 1, 1, 9)
          pyxel.circ(ex + 16, ey, 1, 9)
          pyxel.circ(ex + 16 + 1, ey + 1, 1, 9)
          
      elif ((self.enemy_pos == 2 and self.enemy_pos < self.dead_end[0])
            or (self.enemy_pos == 2 and self.dead_end[0] == 0)): 
       #Pos 2------------------------------------------------------------------
          ex = 114
          ey = 70
          pyxel.circ(ex, ey, 2, 9)
          pyxel.circ(ex - 1, ey + 1, 2, 9)
          pyxel.circ(ex + 26, ey, 2, 9)
          pyxel.circ(ex + 26 + 1, ey + 1, 2, 9)      
          
      elif ((self.enemy_pos == 1 and self.enemy_pos < self.dead_end[0])
            or (self.enemy_pos == 1 and self.dead_end[0] == 0)):
      #Pos 3-------------------------------------------------------------------
          ex = 109
          ey = 65
          pyxel.circ(ex, ey, 3, 9)
          pyxel.circ(ex - 1, ey + 1, 3, 9)
          pyxel.circ(ex + 36, ey, 3, 9)
          pyxel.circ(ex + 36 + 1, ey + 1, 3, 9)
          pyxel.circ(ex - 1, ey + 1, 2, 10)
          pyxel.circ(ex + 36 + 1, ey + 1, 2, 10)
      
      #teeth 1----------------------------------------------------------------
          x = 105
          x2 = 110
          y = 100
          x3 = x + ((x2 - x) / 2)
          y3 = 90
            
          for i in range(5):
              vx =  i * 4.3
              vy =  i * 5
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 1)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 7)    
      
      #teeth 2-----------------------------------------------------------------
          x = 145
          x2 = 150
          y = 100
          x3 = x + ((x2 - x) / 2)
          y3 = 90
       
          for i in range(5):
              vx =  i * 4.3
              vy =  i * 5
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 1)              
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 7)              
      
      #teeth 3----------------------------------------------------------------
          x = 105
          x2 = 110
          y = 87
          x3 = x + ((x2 - x) / 2)
          y3 = 97
      
          for i in range(5):
              vx =  i * 4.3
              vy =  i * -5          
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 7)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 1)     
      
      #teeth 4----------------------------------------------------------------
          x = 145
          x2 = 150
          y = 87
          x3 = x + ((x2 - x) / 2)
          y3 = 97
      
          for i in range(5):
              vx =  i * 4.3
              vy =  i * -5
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 7)      
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 1)      
     #------------------------------------------------------------------------
      elif self.enemy_pos == 0:
      #Pos 4-------------------------------------------------------------------
          ex = 85
          ey = 30
          pyxel.circ(ex, ey, 4, 9)
          pyxel.circ(ex - 1, ey + 1, 4, 9)
          pyxel.circ(ex + 80, ey, 4, 9)      
          pyxel.circ(ex + 80 + 1, ey + 1, 4, 9)
          pyxel.circ(ex + 80 + 1, ey + 1, 3, 10)
          pyxel.circ(ex - 1, ey + 1, 3, 10)  
      
      #teeth 1----------------------------------------------------------------
          x = 75
          x2 = 85
          y = 110
          x3 = x + ((x2 - x) / 2)
          y3 = 90
            
          for i in range(5):
              vx =  i * 10
              vy =  i * 8
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 1)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 7)    
      
      #teeth 2-----------------------------------------------------------------
          x = 165
          x2 = 175
          y = 110
          x3 = x + ((x2 - x) / 2)
          y3 = 90
      
          for i in range(5):
              vx =  i * 10
              vy =  i * 8
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 1)              
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 7)              
      
      #teeth 3----------------------------------------------------------------
          x = 75
          x2 = 85
          y = 50
          x3 = x + ((x2 - x) / 2)
          y3 = 90
      
          for i in range(5):
              vx =  i * 10
              vy =  i * - 8          
              pyxel.tri(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 7)      
              pyxel.trib(x+vx, y+vy, x2+vx, y+vy, x3+vx, y3+vy, 1)     
      
      #teeth 4----------------------------------------------------------------
          x = 165
          x2 = 175
          y = 50
          x3 = x + ((x2 - x) / 2)
          y3 = 90
      
          for i in range(5):
              vx =  i * 10
              vy =  i * - 8
              pyxel.tri(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 7)      
              pyxel.trib(x-vx, y+vy, x2-vx, y+vy, x3-vx, y3+vy, 1)      
#-----------------------------------------------------------------------------

#Bubble draw 2--------------------------------------------------------------     
      bn = len(self.bubbles)
      for b in range(bn) :
          bx = self.bubbles[b].bub_x
          by = self.bubbles[b].bub_y
          bc = self.bubbles[b].bub_c
          bv = self.bubbles[b].bub_v
          
          if b % 2 == 1:
              if bv == 0:
                  pyxel.circb(bx, by, 10, bc)
                  pyxel.circb(bx - 5, by - 5, 3, bc)
                  pyxel.circb(bx - 6, by - 6, 1, 7)
              elif bv == 1:     
                  pyxel.circb(bx, by, 7, 6)
                  pyxel.circb(bx - 3, by - 3, 2, bc)
                  pyxel.circb(bx - 4, by - 4, 1, bc)      
              elif bv == 2:
                  pyxel.circb(bx, by, 5, 6)
                  pyxel.circb(bx - 3, by - 1, 1, bc)
                  pyxel.circb(bx - 4, by - 2, 1, bc)      
      
#------------------------------------------------------------------------------      

#Draw Compass-----------------------------------------------------------------
      pyxel.ellib(-50, -10, 360, 170, 5)
      pyxel.fill(0, 1, 0)
      pyxel.rect(3, 2, 15, 7, 0)
      pyxel.fill(0, 140, 0)
      pyxel.rect(0, 141, 17, 15, 0)
      pyxel.fill(255, 9, 0)
      pyxel.rect(242, 0, 15, 9, 0)
      pyxel.fill(255, 141, 0)
      pyxel.rect(242, 141, 15, 9, 0)
      
      pyxel.rectb(0, 0, 256, 151, 1)      
      
      pyxel.rect(0, 150, 256, 106, 0)
      pyxel.rectb(0, 150, 256, 106, 1)     
      pyxel.rectb(110, 150, 146, 106, 1)           
      pyxel.rectb(114, 154, 137, 97, 5)       
        
      #Wall
      for d0 in range(5):
          if (self.pos[1]-1 < 0 or 
              self.pos[0]-2+d0 < 0 or self.pos[0]-2+d0 > 31):
              pyxel.rect(17+10*d0, 167, 9, 9, 7)
          elif self.maze[self.pos[1]-1][self.pos[0]-2+d0] in self.wall_list:
              pyxel.rect(17+10*d0, 167, 9, 9, 7)
          elif self.maze[self.pos[1]-1][self.pos[0]-2+d0] == (2, 0):
              pyxel.rect(17+10*d0, 167, 9, 9, 3)              
          elif self.maze[self.pos[1]-1][self.pos[0]-2+d0] == (0, 1):
              pyxel.rectb(17+10*d0, 167, 9, 9, 8)              
      for d1 in range(5):
          if self.pos[0]-2+d1 < 0 or self.pos[0]-2+d1 > 31:
              pyxel.rect(17+10*d1, 177, 9, 9, 7)
          elif self.maze[self.pos[1]][self.pos[0]-2+d1] in self.wall_list:
              pyxel.rect(17+10*d1, 177, 9, 9, 7)
          elif self.maze[self.pos[1]][self.pos[0]-2+d1] == (2, 0):
              pyxel.rect(17+10*d1, 177, 9, 9, 3)              
          elif self.maze[self.pos[1]][self.pos[0]-2+d1] == (0, 1):
              pyxel.rectb(17+10*d1, 177, 9, 9, 8)              
      for d2 in range(5):
          if (self.pos[1]+1 > 31 or
              self.pos[0]-2+d2 < 0 or self.pos[0]-2+d2 > 31):
              pyxel.rect(17+10*d2, 187, 9, 9, 7)
          elif self.maze[self.pos[1]+1][self.pos[0]-2+d2] in self.wall_list:
              pyxel.rect(17+10*d2, 187, 9, 9, 7)
          elif self.maze[self.pos[1]+1][self.pos[0]-2+d2] == (2, 0):
              pyxel.rect(17+10*d2, 187, 9, 9, 3)              
          elif self.maze[self.pos[1]+1][self.pos[0]-2+d2] == (0, 1):
              pyxel.rectb(17+10*d2, 187, 9, 9, 8)              
      for d3 in range(5):
          if (self.pos[1]+2 > 31 or
              self.pos[0]-2+d3 < 0 or self.pos[0]-2+d3 > 31):
              pyxel.rect(17+10*d3, 197, 9, 9, 7)      
          elif self.maze[self.pos[1]+2][self.pos[0]-2+d3] in self.wall_list:
              pyxel.rect(17+10*d3, 197, 9, 9, 7)              
          elif self.maze[self.pos[1]+2][self.pos[0]-2+d3] == (2, 0):
              pyxel.rect(17+10*d3, 197, 9, 9, 3)                            
          elif self.maze[self.pos[1]+2][self.pos[0]-2+d3] == (0, 1):
              pyxel.rectb(17+10*d3, 197, 9, 9, 8)                            
            
      #Prayer
      if self.pos_angle == 1:
          pyxel.tri(41, 178, 37, 185, 45, 185, 1)
      elif self.pos_angle == 2:
          pyxel.tri(45, 181, 37, 178, 37, 185, 1)
      elif self.pos_angle == 3:
          pyxel.tri(41, 185, 37, 178, 45, 178, 1)
      elif self.pos_angle == 4:
          pyxel.tri(37, 183, 45, 178, 45, 186, 1)
          
      pyxel.circb(40, 185, 27, 5)   
      pyxel.circb(40, 185, 32, 1)   
      pyxel.fill(18, 168, 0)
      pyxel.fill(64, 168, 0)
      pyxel.fill(63, 202, 0)
      pyxel.fill(18, 204, 0)
      
      #Enemy message
      pyxel.ellib(12, 220, 90, 20, 5)
      pyxel.rectb(12, 220, 90, 20, 1)
      #pyxel.fill(42, 228, 3)
      if self.e_msg_F == False:
          c = 3
      else:
          c = 8
      pyxel.text(23, 228, self.e_msg, c)            
      
      #Paint count
      pyxel.blt(74, 160, 1, 0, 0, 16, 16, 15)
      pyxel.text(90, 170, "x  " + str(self.paint_cnt), 7)
      
      #Message
      for m in range(len(self.game_msg.msg)):
          pyxel.text(120, 160 + m * 10, self.game_msg.msg[m][0], 
                     self.game_msg.msg[m][1])
                
#-----------------------------------------------------------------------------      


class Bubble:
  def __init__(self, x, y, v, c, s):
      self.bub_x = x
      self.bub_y = y
      self.bub_v = v
      self.bub_c = c      
      self.bub_s = s
  def update(self):
      self.bub_y -= self.bub_s
  
class Enemy:
  def __init__(self, x, y, m, p):
      self.ene_x = x
      self.ene_y = y      
      self.ene_m = 1
      self.maze = m
      self.move_permit = p
      self.move_c = 0
  def update(self):
      if self.maze[self.ene_y - 1][self.ene_x] in self.move_permit:
          self.move_c += 1
      if self.maze[self.ene_y + 1][self.ene_x] in self.move_permit:
          self.move_c += 1
      if self.maze[self.ene_y][self.ene_x + 1] in self.move_permit:
          self.move_c += 1
      if self.maze[self.ene_y][self.ene_x - 1] in self.move_permit:
          self.move_c += 1
          
      if self.move_c > 2:
          self.ene_m = pyxel.rndi(1, 4)
          
      #ene_m = Angle E=Enemy
      #    ^
      #    1
      #<4  E   2>
      #    3
      #    v
      #     
      if self.ene_m == 1:
          if self.maze[self.ene_y - 1][self.ene_x] in self.move_permit:
              self.ene_y = self.ene_y - 1
              self.ene_m = 1
          else:
              self.ene_m = pyxel.rndi(1, 4)
      elif self.ene_m == 3:
          if self.maze[self.ene_y + 1][self.ene_x] in self.move_permit:
              self.ene_y = self.ene_y + 1
              self.ene_m = 3
          else:
              self.ene_m = pyxel.rndi(1, 4)
      if self.ene_m == 2:
          if self.maze[self.ene_y][self.ene_x + 1] in self.move_permit:
              self.ene_x = self.ene_x + 1
              self.ene_m = 2
          else:
              self.ene_m = pyxel.rndi(1, 4)
      if self.ene_m == 4:
          if self.maze[self.ene_y][self.ene_x - 1] in self.move_permit:
              self.ene_x = self.ene_x - 1
              self.ene_m = 4
          else:
              self.ene_m = pyxel.rndi(1, 4)           
              
      self.move_c = 0

class GameMsg:
  def __init__(self):
      self.msg = [
                 ["test1",3],
                 ["test2",5],
                 ["test3",6],
                 ["test4",7],
                 ["test5",8],
                 ["test6",9],
                 ["test7",10],
                 ["test8",11],
                 ["test9",12],                 
                 ]    
  def update(self, msg, c):
      self.msg.pop(0)
      self.msg.append([msg, c])

      
APP()

