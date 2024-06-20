#loading in and initiating modules
import pygame, random, pickle
pygame.init()

#creating the window
window = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("BATTLESHIP")
clock = pygame.time.Clock()


class configure:
       def __init__(self):
              global timecount, clicked, clickcount, count, stage
              #loads all essential values in
              self.alphebet = "ABCDEFGHIJ"
              self.white = (250, 250, 250)
              self.black = (0, 0, 0)
              self.red = (255, 0, 0)
              self.green = (0, 255, 0)
              self.grey = (175, 180, 189)
              self.blue = (0, 0, 255)
              self.lightblue = (90, 113, 230)
              self.bigtext = pygame.font.SysFont("arial", 35)
              self.midtext = pygame.font.SysFont("arial", 42)
              self.gianttext = pygame.font.SysFont("arial", 80)

              #loads global esential variables
              count = 0
              timecount = 0
              clicked = 0
              clickcount = 0
              stage = "MENU"
              
              #checks wether there is a previous save or not
              self.loadfromsave = False
              self.rawsavedata = [False, False]
              try:
                     savefile = open("data/saves/objects.txt", "rb")
                     self.rawsavedata[0] = pickle.load(savefile)
                     savefile.close()
              except:
                     pass

              if self.rawsavedata[0] == False:
                     self.rawsavedata[0] = False

              try:
                     savefile = open("data/saves/data.txt", "r")
                     rawsavedata = False
                     for line in savefile:
                            rawsavedata = line
                     savefile.close()
              except:
                     rawsavedata = False
              
              if rawsavedata != False:
                     self.rawsavedata[1] = rawsavedata

              if self.rawsavedata[0] != False and self.rawsavedata[1] != False:
                     self.previous_save = True

              else:
                     self.previous_save = False

              #loads in pictures
              self.nametext = self.bigtext.render("BY GEORGE SEDGWICK", 2, self.red)
              self.loadin = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
              try:
                     self.background1 = pygame.transform.scale(pygame.image.load("data\picture1.jpg"), (1200, 800))
                     self.loadin[0] = True
              except:
                     pass

              try:
                     self.background2 = pygame.transform.scale(pygame.image.load("data/background2.jpg"), (1200, 800))
                     self.loadin[1] = True
              except:
                     pass
              
              try:
                     self.background3 = pygame.transform.scale(pygame.image.load("data/background3.jpg"), (1200, 800))
                     self.loadin[2] = True
              except:
                     pass
              
              try:
                     self.background4 = pygame.transform.scale(pygame.image.load("data/background4.jpg"), (1200, 800))
                     self.loadin[3] = True
              except:
                     pass
              
              try:
                     self.battleship1 = pygame.image.load("data/battleship1.jpg")
                     self.battleship1.set_colorkey((255, 255, 255))
                     self.loadin[4] = True
              except:
                     pass

              try:
                     self.battleship2 = pygame.image.load("data/battleship2.jpg") 
                     self.battleship2.set_colorkey((255, 255, 255))
                     self.loadin[5] = True
              except:
                     pass
              
              try:
                     self.firebutton = pygame.transform.scale(pygame.image.load("data/firebutton.jpg"), (140, 130))
                     self.firebutton.set_colorkey((255, 255, 255))
                     self.loadin[6] = True
              except:
                     pass

              try:
                     self.missedhit = pygame.transform.scale(pygame.image.load("data/missedhit.png"), (45, 50))
                     self.firebutton.set_colorkey((255, 255, 255))
                     self.loadin[7] = True
              except:
                     pass

              try:
                     self.crosshair = pygame.transform.scale(pygame.image.load("data/crosshair.png"), (45, 50))
                     self.firebutton.set_colorkey((255, 255, 255))
                     self.loadin[8] = True
              except:
                     pass

              try:
                     self.burning = pygame.transform.scale(pygame.image.load("data/burning.jpg"), (45, 50))
                     self.burning.set_colorkey((255, 255, 255))
                     self.loadin[9] = True
              except:
                     pass

              try:
                     self.winnerdata = open("data/winners.txt", "r")
                     self.winner_dataraw = []
                     
                     for data in self.winnerdata:
                            self.winner_dataraw.append(data)
                     self.winnerdata.close()
                     if len(self.winner_dataraw) > 0:
                            self.loadin[10] = True
                     else:
                            self.loadin[10] = False
              except:
                     pass

              try:
                     self.backsign = pygame.transform.scale(pygame.image.load("data/backsign.png"), (100, 100))
                     self.backsign.set_colorkey((255, 255, 255))
                     self.loadin[11] = True
              except:
                     pass

              try:
                     self.savebutton = pygame.transform.scale(pygame.image.load("data/savebutton.png"), (50, 50))
                     self.savebutton.set_colorkey((255, 255, 255))
                     self.loadin[12] = True
              except:
                     pass
              
              try:
                     self.battleship3 = pygame.transform.rotate(pygame.image.load("data/battleship3.jpg"), 90)
                     self.battleship3.set_colorkey((255, 255, 255))
                     self.loadin[13] = True
              except:
                     pass

              try:
                     self.battleship4 = pygame.transform.rotate(pygame.image.load("data/battleship4.jpg"), 90)
                     self.battleship4.set_colorkey((255, 255, 255))
                     self.loadin[14] = True
              except:
                     pass


class menuclass:
       #all attributes and code needed for the menu frame
       def __init__(self):
              self.datashowing = False
              self.resumescreen = False

       def draw(self):
              #draws background
              if con.loadin[0] == True:
                     window.blit(con.background1, (0, 0, 0, 0))
              else:
                     pygame.draw.rect(window, con.blue, (0, 0, 1200, 800))

              if self.datashowing == False:
                     #creates battleship text
                     text1 = con.gianttext.render("BATTLESHIPS", 2, con.white)
                     window.blit(text1, (400, 150, 0, 0))
                     pygame.draw.rect(window, con.white, (405, 220, 420, 5))

                     #creates exit box
                     text4 = con.gianttext.render("EXIT", 2, con.red)
                     window.blit(text4, (530, 610, 0, 0))
                     pygame.draw.rect(window, con.red, (510, 605, 190, 100), 10)

                     if self.resumescreen == False:
                            #creates play text and box
                            text2 = con.gianttext.render("PLAY", 2, con.white)
                            window.blit(text2, (525, 360, 0, 0))
                            pygame.draw.rect(window, con.red, (510, 355, 190, 100), 10)

                            #creates previous winner box
                            text3 = con.midtext.render("PREVIOUS", 2, con.white)
                            window.blit(text3, (516, 485, 0, 0))
                            text4 = con.midtext.render("WINNERS", 2, con.white)
                            window.blit(text4, (525, 525, 0, 0))
                            
                            pygame.draw.rect(window, con.red, (510, 480, 190, 100), 10)
                            
                     else:
                            #creates play text and box
                            text2 = con.bigtext.render("NEW", 2, con.white)
                            window.blit(text2, (570, 364, 0, 0))
                            text3 = con.bigtext.render("GAME", 2, con.white)
                            window.blit(text3, (562, 402, 0, 0))
                            pygame.draw.rect(window, con.red, (510, 355, 190, 100), 10)

                            #creates previous winner box
                            text4 = con.midtext.render("RESUME", 2, con.white)
                            window.blit(text4, (532, 504, 0, 0))
                            pygame.draw.rect(window, con.red, (510, 480, 190, 100), 10)
                            
   
              else:
                     self.drawdata()

       def drawdata(self):
              #draws winners page
              text1 = con.gianttext.render("WINNERS:", 2, con.black)
              window.blit(text1, (100, 100, 0, 0))

              placecount = 0
              if con.loadin[10] == True:
                     for winner in con.winner_dataraw:
                            if "COMPUTER" in winner:
                                   showtext = con.midtext.render("COMPUTER WON", 2, con.red)
                            else:
                                   showtext = con.midtext.render("PLAYER WON", 2, con.green)
                            if placecount < 7:
                                   window.blit(showtext, (100, (200+(100*placecount)), 0, 0))
                            else:
                                   window.blit(showtext, (600, (100+(100*(placecount-6))), 0, 0))
                                   
                            placecount += 1
              else:
                     nodatatext = con.gianttext.render("NO DATA AVAILABLE", 2, con.red)
                     window.blit(nodatatext, (250, 400, 0, 0))

              #drawing back box
              if con.loadin[11] == True:
                     window.blit(con.backsign, (1010, 110))
              else:          
                     pygame.draw.rect(window, con.red, (1000, 100, 190, 100))
                     backtext = con.gianttext.render("BACK", 2, con.black)
                     window.blit(backtext, (1005, 110, 0, 0))
                                   
                     

class selectclass:
       #all methods needed for user to create his board
       def __init__(self, predone):
              #sets up program for user to create his grid
              self.predone = predone
              if self.predone == True:
                     self.loaddata()
              else:
                     #loads in all ships
                     self.items = [createship4(80, 100), createship3(160, 100), createship3(160, 280), createship2(240, 100), createship2(80, 330), createship2(240, 220), createship1(160, 460)
                                   , createship1(240, 350), createship1(80, 460), createship1(240, 460)]
              self.ready = False###
              self.holding = False
              self.moving = False

       def loaddata(self):
              #sets up game from previous game
              items = []
              prev_hitboxes = []

              #retrieves classes from file
              mode = "USER"
              for item in con.rawsavedata[0]:
                     if item == "1":
                            mode =  "HIT"
                     else:
                            if mode == "USER":
                                   items.append(item)
                            elif mode == "HIT":
                                   prev_hitboxes.append(item)

              self.items = []
              for item in items[0]:
                     self.items.append(item)
              self.prev_hitboxes = []
              for item in prev_hitboxes[0]:
                     self.prev_hitboxes.append(item)

              #retriving the game grids from the file
              mode = "PLAYER"
              self.player_board = [[], [], [], [], [], [], [], [], [], []]
              self.enemy_board = [[], [], [], [], [], [], [], [], [], []]
              count = 0
              for item in con.rawsavedata[1]:
                     if item == "A":
                            mode = "ENEMY"
                            count = 0
                     else:
                            if count == 10:
                                   count = 0
                            if mode == "PLAYER":
                                   self.player_board[count].append(int(item))
                            elif mode == "ENEMY":
                                   self.enemy_board[count].append(int(item))
                            count += 1

              #finding out how many ships have already been hit
              self.player_hit = 20
              self.enemy_hit = 20

              for indx in range(10):
                     for val in self.player_board[indx]:
                            if val == 3:
                                   self.player_hit -= 1

                     for val in self.player_board[indx]:
                            if val == 3:
                                   self.player_hit -= 1
                     

       def place(self, obj):
              normal = False
              pos = (obj.x, obj.y)

              #finding where the user wants to place a ship
              if pos[0] > 350 and pos[0] < 905:
                     if pos[1] > 100 and pos[1] < 705:

                            xval = (obj.x-350) / 55
                            if xval > int(str(xval)[0]):
                                   xsquare = int(str(xval)[0]) + 1
                            else:
                                   xsquare = int(str(xval)[0])

                            yval = (obj.y-100) / 50
                            if yval < 0:
                                   yval = 1 
                            if yval > int(str(yval)[0]):
                                   ysquare = int(str(yval)[0]) + 1
                            else:
                                   ysquare = int(str(yval)[0])

                            coords = [((xsquare * 55) + 295), ((ysquare * 50) + 50)]
                     else:
                            normal = True
              else:
                     normal = True

              if normal != True:
                     #checks no ships overlap and are in a valid place
                     squares  = [[xsquare, ysquare]]
                     if obj.ori == "NORMAL":
                            if (coords[1] + (obj.size*50)) > 725:
                                   normal = True

                            
                            if obj.size == 2:
                                   squares.append([xsquare, ysquare+1])
                            elif obj.size == 3:
                                   squares.append([xsquare, ysquare+1])
                                   squares.append([xsquare, ysquare+2])
                            elif obj.size == 4:
                                   squares.append([xsquare, ysquare+1])
                                   squares.append([xsquare, ysquare+2])
                                   squares.append([xsquare, ysquare+3])
                     else:
                            if (coords[0] + (obj.size*55)) > 925:
                                   normal = True
                                   
                            if obj.size == 2:
                                   squares.append([xsquare+1, ysquare])
                            elif obj.size == 3:
                                   squares.append([xsquare+1, ysquare])
                                   squares.append([xsquare+2, ysquare])
                            elif obj.size == 4:
                                   squares.append([xsquare+1, ysquare])
                                   squares.append([xsquare+2, ysquare])
                                   squares.append([xsquare+3, ysquare])

                     for item in self.items:
                            othersquares = []
                            if item.placed == True:
                                   if item.ori == "NORMAL":
                                          if item.size == 2:
                                                 othersquares.append([item.place[0], item.place[1]+1])
                                          elif item.size == 3:
                                                 othersquares.append([item.place[0], item.place[1]+1])
                                                 othersquares.append([item.place[0], item.place[1]+2])
                                          elif item.size == 4:
                                                 othersquares.append([item.place[0], item.place[1]+1])
                                                 othersquares.append([item.place[0], item.place[1]+2])
                                                 othersquares.append([item.place[0], item.place[1]+3])
                                   else:
                                          if item.size == 2:
                                                 othersquares.append([item.place[0]+1, item.place[1]])
                                          elif item.size == 3:
                                                 othersquares.append([item.place[0]+1, item.place[1]])
                                                 othersquares.append([item.place[0]+2, item.place[1]])
                                          elif item.size == 4:
                                                 othersquares.append([item.place[0]+1, item.place[1]])
                                                 othersquares.append([item.place[0]+2, item.place[1]])
                                                 othersquares.append([item.place[0]+3, item.place[1]])

                                   for square1 in squares:
                                          for square2 in othersquares:
                                                 if square1[0] == square2[0] and square1[1] == square2[1]:
                                                        normal = True

              #returns ship to defult place if placed in an invalid place
              if normal == True:
                     obj.placed = False
                     obj.x = obj.defultx
                     obj.y = obj.defulty
                     obj.ori = "NORMAL"

              #places ship where user wants
              else:
                     obj.x = coords[0]
                     obj.y = coords[1]
                     obj.placecoords = [coords]
                     obj.coords = [((xsquare * 45) + 12), ((ysquare * 50) + 100)]
                     obj.place = [xsquare, ysquare]
                     obj.placed = True

       def rotate(self, obj):
              #changes the rotation of the ship
              if obj.ori == "NORMAL":
                     obj.ori = "TILT"
              else:
                     obj.ori = "NORMAL"
              

       #draws everything in the creation frame
       def draw(self):

              #draws background
              if con.loadin[1] == True:
                     window.blit(con.background2, (0, 0, 0, 0))
              else:
                     pygame.draw.rect(window, con.blue, (0, 0, 1200, 800))
              pygame.draw.rect(window, (con.lightblue), (350, 100, 550, 500))

              #draws ships
              for obj in self.items:
                     obj.draw()

              #draws the grid
              for x in range(11):
                     pygame.draw.line(window, con.black, ((350 + (x * 55)), 100), ((350 + (x * 55), 600)), 3)
                     pygame.draw.line(window, con.black, (350, (100 + (x * 50))), (900, (100 + (x*50))), 3)

              #shows the text
              text1 = con.bigtext.render("DRAG AND DROP", 3, con.black)
              window.blit(text1, (40, 532, 0, 0))
              text2 = con.bigtext.render(" CLICK TO ROTATE", 3, con.black)
              window.blit(text2, (22, 563, 0, 0))

              #shows place button
              pygame.draw.rect(window, con.white, (540, 645, 190, 100))
              if self.ready == True:
                     text3 = con.gianttext.render("PLAY", 3, con.green)
              else:
                     text3 = con.gianttext.render("PLAY", 3, (60, 80, 80))
              window.blit(text3, (550, 650, 0, 0))

              #shows coordinates
              for place in range(len(con.alphebet)):
                     lettertext = con.bigtext.render((con.alphebet[place]), 2, con.black)
                     numbertext = con.bigtext.render((str(place + 1)), 2, con.black)

                     window.blit(lettertext, (368+(place*55), 67, 0, 0))
                     window.blit(numbertext, (902, (108+(place)*49), 0, 0))

              #drawing back box
              if con.loadin[11] == True:
                     window.blit(con.backsign, (1090, 5, 0, 0))
              else:
                     pygame.draw.rect(window, con.red, (1000, 10, 190, 80))
                     backtext = con.gianttext.render("BACK", 2, con.black)
                     window.blit(backtext, (1005, 4, 0, 0))


class playclass:
       def __init__(self, from_prev):
              global select
              #settings for actual gameplay
              self.pausecount = 0
              self.time = 0
              self.showhit = False
              self.hittime = 0
              self.roundstart = count
              self.player = 1
              if from_prev == True:
                     self.hitboxes = select.prev_hitboxes
              else:
                     self.hitboxes = []
                     
              self.pause = False
              self.hitting = False
              self.selected = False
              self.moving = False
              self.answer = True

              self.changedim()

       def changedim(self):
              #changes size of ships to fit new board
              if con.loadin[3] == True:
                     for obj in select.items:
                            obj.x = obj.coords[0]
                            obj.y = obj.coords[1]
                            
                            if obj.size == 1:
                                   obj.shipdim = (45, 42)
                            elif obj.size == 2:
                                   obj.shipdim = [42, 100]
                                   obj.rotatedshipdim = [100, 42]

                            elif obj.size == 3:
                                   obj.shipdim = [42, 140]
                                   obj.rotatedshipdim = [126, 42]

                            else:
                                   obj.shipdim = [42, 200]
                                   obj.rotatedshipdim = [185, 42]

       def hit(self, place, playerfiring):
              #fires a missile and checks wether the attacker has hit a ship
              pos = place
              self.hitboxes.append(hitbox([pos[0], pos[1]], playerfiring, True))
              
              if playerfiring == 1:
                     if enemy.board[pos[0]][pos[1]] == 1:
                            player.successfull()
                     else:
                            player.lasthit = False
                     enemy.board[pos[0]][pos[1]] = 2
                            
              self.selected = False

       def selecting(self, pos):
              #finds square user selects when he is choosing where to fire
              player.selectedagain = True
              x = pos[0]
              y = pos[1]

              xval = (x-650) / 45
              xsquare = int(str(xval)[0])

              yval = (y-150) / 50
              if yval < 0:
                     yval = 1 
              if yval > int(str(yval)[0]):
                     ysquare = int(str(yval)[0]) + 1
              else:
                     ysquare = int(str(yval)[0])
              ysquare -= 1

              if enemy.board[xsquare][ysquare] != 2:
                     self.hitting = hitbox([xsquare, ysquare], 1, False)

       def savegame(self):
              #deletes pre-existing data
              try:
                     file = open("data/saves/objects.txt", "r+")
                     file.truncate(0)
                     file.close()
                     
                     file = open("data/saves/data.txt", "r+")
                     file.truncate(0)
                     file.close()
              except:
                     #creates files if previous isnt found
                     file = open("data/saves/objects.txt", "w+")
                     file.close()

                     file = open("data/saves/data.txt", "w+")
                     file.close()

              #writes new data to file
              file = open("data/saves/objects.txt", "wb")
              all_classes = [select.items, "1", self.hitboxes]
              pickle.dump(all_classes, file)
              file.close()

              file = open("data/saves/data.txt", "a")

              #getting values from players board
              numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
              to_write = ""
              for indx in range(10):
                     for value in player.board[indx]:
                            value = str(value)
                            if value in numbers:
                                   to_write += value
              to_write += "A"

              #getting values from enemys board
              for indx in range(10):
                     for value in enemy.board[indx]:
                            value = str(value)
                            if value in numbers:
                                   to_write += value

              file.write(to_write)
              file.close()
              print(": GAME SAVE SUCCESFUL")
              
       def draw(self):
              #draws everything in the playing phase

              #draws background
              window.blit(con.background3, (0, 0, 1200, 800))

              #draws whos go it is     
              if self.player == 1:
                     gotext = con.bigtext.render("        PLAYER 1", 10, con.white)
              else:
                     gotext = con.bigtext.render("        PLAYER 2", 10, con.white)
              window.blit(gotext, (14, 12, 0, 0))

              #draws letter coordinates
              for place in range(len(con.alphebet)):
                     letter = con.bigtext.render((con.alphebet[place]), 2, con.white)
                     
                     leftcoord = 70 + (place * 45)
                     window.blit(letter, (leftcoord, 115, 0, 0))
                     
                     rightcoord = 665 + (place * 45)
                     window.blit(letter, (rightcoord, 115, 0, 0))

              #draws number coordinates
              for num in range(1, 11):
                     if num == 10:
                            number = con.bigtext.render((str(num)), 2, con.white)
                     else:
                            number = con.bigtext.render(" "+(str(num)), 2, con.white)
                            
                     coord = 105 + (num *50)
                     
                     window.blit(number, (503, coord, 0, 0))
                     window.blit(number, (620, coord, 0, 0))

              #drawing grid on left
              for x in range(11):
                     pygame.draw.line(window, con.white, (((x*45)+55), 150), (((x*45)+55), 655), 5)
              for x in range(11):
                     pygame.draw.line(window, con.white, (55, ((x*50)+150)), (505, ((x*50)+150)), 5)

              #drawing grid on right
              for x in range(11):
                     pygame.draw.line(window, con.white, (((x*45)+650), 150), (((x*45)+650), 655), 5)
              for x in range(11):
                     pygame.draw.line(window, con.white, (650, ((x*50)+150)), (1100, ((x*50)+150)), 5)

              #draws pause button
              if con.loadin[12] == True:
                     window.blit(con.savebutton, (10, 10))
              else:
                     pygame.draw.rect(window, con.black, (10, 10, 50, 50))

              #draws ships on grid while playing game
              for obj in select.items:
                     obj.draw()

              #draws all the hitboxes
              for obj in self.hitboxes:
                     obj.draw()

              #draws the box that the user is selecting
              if self.hitting != False:
                     if player.selectedagain == True:
                            self.hitting.draw()

              #draws the fire button
              if self.selected == True:
                     if con.loadin[6] == True:
                            window.blit(con.firebutton, (510, 10))
                     else:
                            pygame.draw.rect(window, con.red, (510, 10,  140, 130))

              #drawing the time
              timetext = con.gianttext.render(str(self.time), 2, con.red)
              window.blit(timetext, (1100, 20, 0, 0))

              #draws "hit ship" text
              if play.showhit == True:
                     for item in player.burninglist:
                            item.draw()
                            
                     pygame.draw.rect(window, (226, 125, 77), (452, 298, 300, 160))
                     pygame.draw.rect(window, con.black, (452, 298, 300, 160), 2)
                     hittext = con.gianttext.render("HIT SHIP!", 2, con.red)
                     window.blit(hittext, (455, 320, 0, 0))
                     

              #draws paused icon
              if play.pause == True:
                     pygame.draw.rect(window, con.black, (452, 298, 300, 160))
                     pausedtext = con.gianttext.render("PAUSED", 2, con.white)
                     window.blit(pausedtext, (465, 305, 0, 0))

                     #save game box
                     pygame.draw.rect(window, con.white, (470, 382, 260, 60), 2)
                     savetext = con.bigtext.render("SAVE GAME", 2, con.white)
                     window.blit(savetext, (515, 390, 0, 0))


class playerclass:
       #class with all settings and methods the player needs
       def __init__(self, from_prev):
              if from_prev == True:
                     self.board = select.player_board
                     self.shipshit = select.player_hit
              else:
                     self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                   ,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

                     self.shipshit = 20
                     self.plot()

              self.burninglist = []
              self.lasthit = False

       def plot(self):
              for obj in select.items:
                     
                     if obj.size == 1:
                            self.board[obj.place[0]-1][obj.place[1]-1] = 1
                            
                     elif obj.size == 2:
                            if obj.ori == "NORMAL":
                                   self.board[obj.place[0]-1][obj.place[1]-1] = 1
                                   self.board[obj.place[0]-1][obj.place[1]] = 1
                            else:
                                   self.board[obj.place[0]-1][obj.place[1]-1] = 1
                                   self.board[obj.place[0]][obj.place[1]-1] = 1
                                   
                     elif obj.size == 3:
                            if obj.ori == "NORMAL":
                                   self.board[obj.place[0]-1][obj.place[1]-1] = 1
                                   self.board[obj.place[0]-1][obj.place[1]] = 1
                                   self.board[obj.place[0]-1][obj.place[1]+1] = 1
                            else:
                                   self.board[obj.place[0]-1][obj.place[1]-1] = 1
                                   self.board[obj.place[0]][obj.place[1]-1] = 1
                                   self.board[obj.place[0]+1][obj.place[1]-1] = 1

                     elif obj.size == 4:
                            if obj.ori == "NORMAL":
                                   self.board[obj.place[0]-1][obj.place[1]-1] = 1
                                   self.board[obj.place[0]-1][obj.place[1]] = 1
                                   self.board[obj.place[0]-1][obj.place[1]+1] = 1
                                   self.board[obj.place[0]-1][obj.place[1]+2] = 1
                            else:
                                   self.board[obj.place[0]-1][obj.place[1]-1] = 1
                                   self.board[obj.place[0]][obj.place[1]-1] = 1
                                   self.board[obj.place[0]+1][obj.place[1]-1] = 1
                                   self.board[obj.place[0]+2][obj.place[1]-1] = 1


       #what happens if the user hits an enemy ship
       def successfull(self):
              enemy.shipshit -= 1
              self.lasthit = True
              play.showhit = True
              play.hittime = count

              #creates all the burning flames
              for val in range(40):
                     x = random.randint(0, 1200)
                     y = random.randint(0, 800)
                     self.burninglist.append(fireclass(x, y))
                      
          
class enemyclass:
       #class with all settings and methods the enemy ai needs
       
       def __init__(self, from_prev):
              #gets settings for ai
              if from_prev == True:
                     self.board = select.enemy_board
                     self.shipshit = select.enemy_hit
              else:
                     self.board = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                                   ,[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

                     self.shipshit = 20
                     self.plot()
              
              self.time = 0
              self.target = [0, 0]
              self.configured = False
              self.hitlast = False


       def fire(self):
              #fires at user
              x = self.target[0]
              y = self.target[1]
              
              if player.board[x][y] == 1:
                     self.configured = False
                     player.shipshit -= 1
                     player.board[x][y] = 2
                     self.hitlast = True

              else:
                     self.hitlast = False
                     
              play.hit([x, y], 2)

              if self.hitlast == False:
                     play.player = 1

       def smartplot(self):
              #will get computer to hit a coordinate close to the previous one if it previously hit a ship
              x = self.target[0]
              y = self.target[1]
              notplaced = True
              while notplaced:
                     newidentity = random.randint(1, 4)
                     if newidentity == 1:
                            if (y-1) >= 0:
                                   if player.board[x][y-1] != 2:
                                          self.target[0] = x
                                          self.target[1] = y-1
                                          notplaced = False
                                   
                     elif newidentity == 2:
                            if (x+1) <= 9:
                                   if player.board[x+1][y] != 2:
                                          self.target[0] = x+1
                                          self.target[1] = y
                                          notplaced = False

                     elif newidentity == 3:
                            if (y+1) <= 9:
                                   if player.board[x][y+1] != 2:
                                          self.target[0] = x
                                          self.target[1] = y+1
                                          notplaced = False

                     else:
                            if (x-1) >= 0:
                                   if player.board[x-1][y] != 2:
                                          self.target[0] = x-1
                                          self.target[1] = y
                                          notplaced = False
                      

       def plot(self):
              #creates the enemy board
              for x in range(4):
                     run = True
                     while run:
                            place = [random.randint(0, 9), random.randint(0, 9)]
                            if self.board[place[0]][place[1]] == 0:
                                   self.board[place[0]][place[1]] = 1
                                   run = False

              for x in range(3):
                     run = True
                     while run:
                            place = [random.randint(0, 9), random.randint(0, 9)]
                            ori = random.randint(1, 2) 
                            if ori == 1:
                                   if 9 >= place[1] + 1:
                                          if self.board[place[0]][place[1]] == 0 and self.board[place[0]][place[1]+1] == 0:
                                                 self.board[place[0]][place[1]] = 1
                                                 self.board[place[0]][place[1]+1] = 1
                                                 run = False
                            if ori == 2:
                                   if 9 >= place[0] + 1:
                                          if self.board[place[0]][place[1]] == 0 and self.board[place[0]+1][place[1]] == 0:
                                                 self.board[place[0]][place[1]] = 1
                                                 self.board[place[0]+1][place[1]] = 1
                                                 run = False

              for x in range(2):
                     run = True
                     while run:
                            place = [random.randint(0, 9), random.randint(0, 9)]
                            ori = random.randint(1, 2) 
                            if ori == 1:
                                   if 9 >= place[1] + 2:
                                          if self.board[place[0]][place[1]] == 0 and self.board[place[0]][place[1]+1] == 0 and self.board[place[0]][place[1]+2] == 0:
                                                 self.board[place[0]][place[1]] = 1
                                                 self.board[place[0]][place[1]+1] = 1
                                                 self.board[place[0]][place[1]+2] = 1
                                                 run = False
                            if ori == 2:
                                   if 9 >= place[0] + 2:
                                          if self.board[place[0]][place[1]] == 0 and self.board[place[0]+1][place[1]] == 0 and self.board[place[0]+2][place[1]] == 0:
                                                 self.board[place[0]][place[1]] = 1
                                                 self.board[place[0]+1][place[1]] = 1
                                                 self.board[place[0]+2][place[1]] = 1
                                                 run = False

              run = True
              while run:
                     place = [random.randint(0, 9), random.randint(0, 9)]
                     ori = random.randint(1, 2)
                     if ori == 1:
                            if 9 >= place[1] + 3:
                                   if self.board[place[0]][place[1]] == 0 and self.board[place[0]][place[1]+1] == 0 and self.board[place[0]][place[1]+2] == 0 and self.board[place[0]][place[1]+3] == 0:
                                          self.board[place[0]][place[1]] = 1
                                          self.board[place[0]][place[1]+1] = 1
                                          self.board[place[0]][place[1]+2] = 1
                                          self.board[place[0]][place[1]+3] = 1
                                          run = False
                     if ori == 2:
                            if 9 >= place[0] + 3:
                                   if self.board[place[0]][place[1]] == 0 and self.board[place[0]+1][place[1]] == 0 and self.board[place[0]+2][place[1]] == 0 and self.board[place[0]+3][place[1]] == 0:
                                          self.board[place[0]][place[1]] = 1
                                          self.board[place[0]+1][place[1]] = 1
                                          self.board[place[0]+2][place[1]] = 1
                                          self.board[place[0]+3][place[1]] = 1
                                          run = False


class endclass:
       def __init__(self, winner):
              #adds winner to winner file
              self.winner = winner
              if con.loadin[10] == True:
                     file = open("data/winners.txt", "a")
              else:
                     file = open("data/winners.txt", "w+")
                     
              if self.winner == 1:
                     file.write("PLAYER\n")
              else:
                     file.write("COMPUTER\n")
              file.close()

       def draw(self):
              #draws winning screen
              if con.loadin[3] == True:
                     window.blit(con.background4, (0, 0, 0, 0))
              else:
                     pygame.draw.rect(window, con.black, (0, 0, 1200, 800))

              #shows winning/loosing text
              if self.winner == 1:
                     winnertext = con.gianttext.render("YOU WON!", 2, con.white)
                     window.blit(winnertext, (410, 280))
              else:
                     winnertext = con.gianttext.render("YOU LOOSE!", 2, con.white)
                     window.blit(winnertext, (410, 280))

              #prints exit button
              pygame.draw.rect(window, con.blue, (400, 550, 400, 60))
              text2 = con.bigtext.render("EXIT", 2, con.black)
              window.blit(text2, (550, 560, 0, 0))        

class createship4:
       def __init__(self, x, y):
              #settings for size 4 ship
              self.ori = "NORMAL" 
              self.defultx = x
              self.defulty = y
              self.x = x
              self.y = y
              self.size = 4
              self.placecoords = [0, 0]
              self.coords = [0, 0]
              self.place = [0, 0]
              self.placed = False
              self.shipdim = [55, 204]
              self.rotatedshipdim = [220, 52]

       def draw(self):
              #draws the ship
              if self.ori == "NORMAL":
                     if con.loadin[14] == True:
                            window.blit(pygame.transform.scale(con.battleship4, self.shipdim), (self.x, self.y))
                     else:
                            pygame.draw.rect(window, con.grey, (self.x, self.y, 55, 100))
                            
              else:
                     if con.loadin[14] == True:
                            ship = pygame.transform.rotate(con.battleship4, 270)
                            window.blit(pygame.transform.scale(ship, self.rotatedshipdim), (self.x, self.y))
                     else:
                            pygame.draw.rect(window, con.grey, (self.x, self.y, self.rotatedshipdim[0], self.rotatedshipdim[1]))
       

class createship3:
       def __init__(self, x, y):
              #settings for size 3 ship
              self.ori = "NORMAL"
              self.defultx = x
              self.defulty = y
              self.x = x
              self.y = y
              self.size = 3
              self.placecoords = [0, 0]
              self.coords = [0, 0]
              self.place = [0, 0]
              self.placed = False
              self.shipdim = [55, 151]
              self.rotatedshipdim = [165, 52]

       def draw(self):
              #draws the ship

              if self.ori == "NORMAL":
                     if con.loadin[13] == True:
                            window.blit(pygame.transform.scale(con.battleship3, self.shipdim), (self.x, self.y))
                     else:
                            pygame.draw.rect(window, con.grey, (self.x, self.y, 55, 100))
                            
              else:
                     if con.loadin[13] == True:
                            ship = pygame.transform.rotate(con.battleship3, 270)
                            window.blit(pygame.transform.scale(ship, self.rotatedshipdim), (self.x, self.y))
                     else:
                            pygame.draw.rect(window, con.grey, (self.x, self.y, self.rotatedshipdim[0], self.rotatedshipdim[1]))


class createship2:
       def __init__(self, x, y):
              #settings for size 2 ship
              self.ori = "NORMAL"
              self.defultx = x
              self.defulty = y
              self.x = x
              self.y = y
              self.size = 2
              self.placecoords = [0, 0]
              self.coords = [0, 0]
              self.place = [0, 0]
              self.placed = False
              self.shipdim = 52, 110
              self.rotatedshipdim = 110, 50

       def draw(self):
              #draws the ship
              if self.ori == "NORMAL":
                     if con.loadin[5] == True:
              
                            window.blit(pygame.transform.scale(con.battleship2, self.shipdim), (self.x, self.y))
                     else:
                            pygame.draw.rect(window, con.grey, (self.x, self.y, 55, 100))
              else:
                     if con.loadin[5] == True:
                            window.blit(pygame.transform.scale(con.battleship2, self.rotatedshipdim), (self.x, self.y))
                     else:
                            pygame.draw.rect(window, con.grey, (self.x, self.y, 109, 52))
                     

class createship1:
       def __init__(self, x, y):
              #settings for size 1 ship
              self.ori = "NORMAL"
              self.defultx = x
              self.defulty = y
              self.x = x
              self.y = y
              self.size = 1
              self.placecoords = [0, 0]
              self.coords = [0, 0]
              self.place = [0, 0]
              self.placed = False
              self.shipdim = (45, 50)

       def draw(self):
              #draws the ship
              if con.loadin[4] == True:
                     window.blit(pygame.transform.scale(con.battleship1, self.shipdim), (self.x, self.y))
              else:
                     pygame.draw.rect(window, con.grey, (self.x, self.y, 55, 52))


class fireclass:
       #attributes for the fires shown when the user hits an enemy ship
       def __init__(self, x, y):
              self.x = x
              self.y = y

       def draw(self):
              if con.loadin[9] == True:
                     window.blit(con.burning, (self.x, self.y, 0, 0))


class hitbox:
       def __init__(self, place, playercreating, state):
              #settings for the hitbox
              self.place = place
              self.fired = state
              self.hit = False

              #checks if box is placed on a ship and gets co-ordinates.
              if playercreating == 1:
                     if self.fired == True:
                            if enemy.board[self.place[0]][self.place[1]] == 1:
                                   self.hit = True
                                   
                     self.coords = [((place[0] * 45) + 650), ((place[1] * 50) + 150)]
              else:
                     if self.fired == True:
                            if player.board[self.place[0]][self.place[1]] == 1:
                                   self.hit = True
                                   
                     self.coords = [((place[0] * 45) + 55), ((place[1] * 50) + 150)]

       def draw(self):
              #presents appropriate hitbox
              if self.fired == False:
                     if con.loadin[8] == True:
                            window.blit(con.crosshair, (self.coords[0], self.coords[1]))
                     else:
                            pygame.draw.rect(window, con.red, (self.coords[0], self.coords[1], 45, 50))
                            
              else:
                     if self.hit == True:
                            if con.loadin[9] == True:
                                   window.blit(con.burning, (self.coords[0], self.coords[1]))
                            else:
                                   pygame.draw.rect(window, con.green, (self.coords[0], self.coords[1], 45, 50))
                                   
                     else:
                            if con.loadin[7] == True:
                                   window.blit(con.missedhit, (self.coords[0], self.coords[1]))
                            else:
                                   pygame.draw.rect(window, con.red, (self.coords[0], self.coords[1], 45, 50))

                                   
def draw():
       #goes to the correct stages drawing subroutine
       if stage == "MENU":
              menu.draw()
       elif stage == "SELECT":
              select.draw()
       elif stage == "PLAY":
              play.draw()
       else:
              end.draw()

       #writing my name
       window.blit(con.nametext, (865, 765, 0, 0))

       #actually updates the screen
       pygame.display.update()


#initiates initial classes
con = configure()
menu = menuclass()

#sets time  management values
timecount = 0
clicked = 0
clickcount = 0

#starts event loop
running = True
while running:
       #manages time
       count += 1
       clock.tick(30)

       #gets all actions taken
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     running = False
       keys = pygame.key.get_pressed()
       pos = pygame.mouse.get_pos()

       if stage == "MENU":              
              if (count-clickcount) > 4:
                     if pygame.mouse.get_pressed()[0]:
                            clickcount = count
                            if menu.datashowing == False:
                                   if pos[0] > 510 and pos[0] < 700:

                                          #sees if user pressed play from the initial menu
                                          if pos[1] > 355 and pos[1] < 455:
                                                 if con.previous_save == False:
                                                        select = selectclass(False)
                                                        stage = "SELECT"
                                                        clickcount = 0
                                                 else:
                                                        #sees if the user selects to play a new game
                                                        if menu.resumescreen == True:
                                                               select = selectclass(False)
                                                               menu.resumescreen = False
                                                               stage = "SELECT"
                                                               clickcount = 0
                                                        else:
                                                               menu.resumescreen = True

                                          #sees wether the user wants to see the previous winners
                                          elif pos[1] > 480 and pos[1] < 580:
                                                 if menu.resumescreen == False:
                                                        menu.datashowing = True
                                                 else:
                                                        #sees if user selects to play from a previous game
                                                        select = selectclass(True)
                                                        con.loadfromsave = True
                                                        stage = "SELECT"
                                                        clickcount = 0

                                          #sees if user presses the exit button
                                          elif pos[1] > 605 and pos[1] < 705:
                                                 running = False
                            else:
                                   #sees if user has pressed back on the winner screen
                                   if pos[0] > 1000 and pos[0] < 1090:
                                          if pos[1] > 100 and pos[1] < 200:
                                                 menu.datashowing = False

       elif stage == "SELECT":
              #loads all values from file if needed to
              if con.loadfromsave == True:
                     play = playclass(True)
                     enemy = enemyclass(True)
                     player = playerclass(True)
                     stage = "PLAY"
                     con.loadfromsave = False         
   
              if pygame.mouse.get_pressed()[0]:
                     #checks wether use wants to go back
                     if pos[0] > 1000 and pos[0] < 1190:
                            if pos[1] > 10 and pos[1] < 90:
                                   if select.moving == False:
                                          stage = "MENU"

                     #manages drag and dropping a ship
                     select.holding = True
                     for x in range(len(select.items)):
                            if select.moving == False:
                                   obj = select.items[x]
                                   if obj.ori == "NORMAL":
                                          if pos[0] > obj.x and pos[0] < (obj.x+55):
                                                 if pos[1] > obj.y and pos[1] < obj.y+(52*obj.size):
                                                        clickcount = count
                                                        select.holding = True
                                                        select.moving = True
                                                        moveobject = obj
                                   else:
                                          if pos[0] > obj.x and pos[0] < (obj.x+(55*obj.size)):   
                                                 if pos[1] > obj.y and pos[1] < obj.y+52:
                                                        clickcount = count
                                                        select.holding = True
                                                        select.moving = True
                                                        moveobject = obj

                     if select.ready == True:
                            #starts the game when user has created their board
                            if pos[0] > 540 and pos[0] < 730:
                                   if pos[1] > 645 and pos[1] < 745:
                                          play = playclass(False)
                                          player = playerclass(False)
                                          enemy = enemyclass(False)
                                          stage = "PLAY"      

              else:
                     #rotates ship
                     if (count-clickcount) < 3:
                            clicked = count
                            select.rotate(moveobject)
                                   
                     else:
                            #places ship
                            if select.moving == True:
                                   select.place(moveobject)
                     select.holding = False
                     select.moving = False
       
              if select.moving == True:
                     #changes coordinates of moving ship
                     moveobject.x = pos[0]
                     moveobject.y = pos[1]

              #checks wether all ships have been places
              ready = True
              for obj in select.items:
                     if obj.placed == False:
                            ready = False
              if ready == True:
                     select.ready = True
              else:
                     select.ready = False                     

       elif stage == "PLAY":
              if pygame.mouse.get_pressed()[0]:
                     if (count-clickcount  > 5):
                            if pos[0] > 10 and pos[0] < 60:
                                   if pos[1] > 10 and pos[1] < 60:

                                          #checks wether user has paused and wants to save
                                          clickcount = count
                                          if play.pause == False:
                                                 play.pause = True
                                                 play.pausecount = count
                                          else:
                                                 play.pause = False
                                                 count = play.pausecount

              if play.pause == False:
                     #gets time for the counter
                     play.time = 20 - ((count - play.roundstart) // 30)

                     #manages celebrations for when user hits target successfully
                     if play.showhit == True:
                            if (count-play.hittime) > 35:
                                   play.showhit = False
                                   player.burninglist = []
                            else:
                                   for item in player.burninglist:
                                          item.y -= 5

                     #gets location of where player selects the grid
                     if play.player == 1:
                            if pygame.mouse.get_pressed()[0]:
                                   if pos[0] > 650 and pos[0] < 1100:
                                          if pos[1] > 150 and pos[1] < 655:
                                                 play.selecting(pos)
                                                 play.selected = True

                                   #manages when the user wants to fire 
                                   if pos[0] > 510 and pos[0] < 650:
                                          if pos[1] > 10 and pos[1] < 140:
                                                 if play.hitting != False:
                                                        play.roundstart = count
                                                        play.hit([play.hitting.place[0], play.hitting.place[1]], 1)
                                                        enemy.configured = False
                                                        if play.player == 1:
                                                               player.selectedagain = False
                                                               
                                                               if player.lasthit == False:
                                                                      play.player = 2
                     
                                                        
                            if play.time == 0:
                                   play.roundstart = count
                                   enemy.configured = False
                                   if play.player == 1:
                                          player.selectedagain = False
                                          play.player = 2
                                   else:
                                          play.player = 1

                            #checks wether all enemy ships are destroyed           
                            if player.shipshit <= 0:
                                   end = endclass(2)
                                   stage = "END"

                     else:
                            #creates time interval and location for enemy to hit
                            if enemy.configured == False:
                                   enemy.interval = random.randint(11, 17)
                                   if enemy.hitlast == True:
                                          enemy.smartplot()
                                          timecount = count
                                          enemy.configured = True
                                   
                                   else:
                                          picked = True
                                          
                                   while picked:
                                          #gets ai to pick target
                                          x = random.randint(0, 9)
                                          y = random.randint(0, 9)
                                          if player.board[x][y] == 0 or player.board[x][y] == 1:
                                                 enemy.target = [x, y]
                                                 enemy.configured = True
                                                 timecount = count
                                                 picked = False

                            else:
                                   if play.time == enemy.interval:
                                          play.roundstart = count
                                          enemy.fire()

                            #checks wether all enemy ships are destroyed
                            if enemy.shipshit <= 0:
                                   end = endclass(1)
                                   stage = "END"

              else:
                     #checks if user wants to save game while paused
                     if pygame.mouse.get_pressed()[0]:
                            if pos[0] > 470 and pos[0] < 730:
                                          if pos[1] > 382 and pos[1] < 442:
                                                 play.savegame()
                                          
       else:
              if pygame.mouse.get_pressed()[0]:
                     #checks if the user wants to exit the game
                     if pos[0] > 400 and pos[0] < 800:
                            if pos[1] > 500 and pos[1] < 560:
                                   running = False

       draw()


pygame.quit()
print ("THANKS FOR PLAYING!")
