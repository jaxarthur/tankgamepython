import math, random, pygame

window = pygame.display.get_surface()
info = pygame.display.Info()
screenW = info.current_w
screenH = info.current_h

class terrain():
    def __init__(self):
        self.terrainarray = []
        self.maxvar = 2
        for x in range(screenW):
            #first node check
            if(x > 1):
                previous = self.terrainarray[x-1][1]
                rand = 0
                while rand < 1 or rand > 250: 
                    rand = random.randint(previous-self.maxvar, previous+self.maxvar)
                
                self.terrainarray.append([x, int(rand)])
            
            else:
                self.terrainarray.append([0, 175])
    
    def draw(self):
        tempsurf = pygame.Surface((screenH, screenW))
        temp = self.terrainarray[0:]
        temp.insert(0, [0, 0])
        temp.append([screenW, 0])
        pygame.draw.polygon(tempsurf, (0,255,255), temp)
        tempsurf = pygame.transform.flip(tempsurf, False, True)
        window.blit(tempsurf, (0,0))

    def find(self, x):
        return self.terrainarray[x]
        
    def colisiondetect(self, cords):
        if self.terrainarray[cords[0]][1] > cords[1]:
            return True
        else:
            return False

    def deform(self, cords, radius):
        for i in range(radius*2):
            x = i - radius
            reletivedepresion = math.sqrt(math.pow(radius, 2) - math.pow(x, 2))
            currentheight = self.find(int(x+cords[0]))[1]
            fixeddepresion = currentheight - reletivedepresion
            if fixeddepresion < currentheight - 15:
                fixeddepresion = currentheight - 15
            if fixeddepresion < 0:
                fixeddepresion = currentheight

            self.terrainarray[int(cords[0] + x)] = [cords[0]+x, fixeddepresion]
    
    def slope(self, cords):
        temp = 0
        for i in range(11):
            x = i - 5
            temp = temp + ((self.terrainarray[x+cords[0]] - cords[1]) * x)
        
        return temp

    
land = terrain()       


            
