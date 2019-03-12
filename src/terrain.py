import math, random, pygame

window = pygame.display.get_surface()
info = pygame.display.Info()
screenW = info.current_w
screenH = info.current_h

class terrain():
    def __init__(self):
        self.terrainarray = [[0, random.randint(50,100)]]
        self.maxvar = 2
        generating = True
        while generating:
            lastpoint = self.terrainarray[-1]
            
            x = random.randint(lastpoint[0]+50, lastpoint[0]+60)
            
            y = random.randint(lastpoint[1]-30, lastpoint[1]+30)
            if y < 50:
                y = 50
            elif y > 150:
                y = 150
            
            if x > screenW:
                x = screenW
                generating = False

            self.terrainarray.append([x, y])
        
        self.smooth()

    def draw(self):
        tempsurf = pygame.Surface((screenH, screenW))
        temp = self.terrainarray[0:]
        temp.insert(0, [0, 0])
        temp.append([screenW, 0])
        pygame.draw.polygon(tempsurf, (0,255,255), temp)
        tempsurf = pygame.transform.flip(tempsurf, False, True)
        window.blit(tempsurf, (0,0))

    def find(self, x):
        i = 0
        x = int(x)
        px = 0
        while x > px:
            i = i + 1
            px = self.terrainarray[i][0]
        
        point1 = self.terrainarray[i-1]
        point2 = self.terrainarray[i]

        try:
            slope = (point2[1] - point1[1])/(point2[0] - point1[0])
        except:
            print(point1, point2)

        height = point1[1] + (slope * (x - point1[0]))

        return int(height)
        
    def slope(self, x):
        i = 0
        px = 0
        while x < px:
            i = i + 1
            px = self.terrainarray[i][0]
        
        point1 = self.terrainarray[i-1]
        point2 = self.terrainarray[i]

        
        slope = (point2[1] - point1[1])/(point2[0] - point1[0])
    
        return slope
    
    def colisiondetect(self, cords):
        if self.find(cords[0]) > cords[1]:
            return True
        else:
            return False

    def deform(self, cords):
        replaced = False
        
        for i in self.terrainarray:
            if i[0] == cords[0]:
                i = [cords[0], cords[1]-10]
                replaced = True
        
        if replaced == False:
            #remove nearby points
            for i in self.terrainarray:
                if i[0] > cords[0] - 10 and i[0] < cords[0] + 10:
                    self.terrainarray.remove(i)
            
            #insert new point
            i = 0
            px = 0
            x = cords[0]
            while x > px:
                i = i + 1
                px = self.terrainarray[i][0]
            
            self.terrainarray.insert(i, [cords[0], cords[1]-10])
            self.smooth()
    
    def smooth(self):
        runningsmooth = True
        while runningsmooth:
            ran = False
            for i in self.terrainarray:
                if self.slope(i[0]+1) > 1:
                    i[1] = i[1]-1
                    ran = True
                elif self.slope(i[0]+1) < -1:
                    i[1] = i[1]+1
                    ran = True
            if ran == False:
                runningsmooth = False


land = terrain()       


            
