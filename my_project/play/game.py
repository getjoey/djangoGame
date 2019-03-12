import random

class Map:
    def __init__(self,sizex,sizey,seed):

        self.sizex = sizex
        self.sizey = sizey
        self.seed = seed

        self.map = []
        self.buildEmpty()
        self.randomize()
        self.padIt()

    def buildEmpty(self):
        self.map = [] * self.sizex
        for i in range(self.sizex):
            line = [0] * self.sizey
            self.map.append(line)

    def randomize(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                if(random.randint(0,10) > 8):
                    self.map[x][y]=1

                if(x == 0 or y==0 or x == self.sizex-1 or y ==self.sizey-1):
                    self.map[x][y] = 1

    def padIt(self):
        paddedmap = [] * (self.sizex + 40)

        for i in range(self.sizex+40):
            line = [0] * (self.sizey + 40)
            paddedmap.append(line)


        for xx in range(len(self.map)):
            for yy in range(len(self.map[xx])):
                paddedmap[xx+20][yy+20] = self.map[xx][yy]

        self.map = paddedmap


    def buildOffSeed(self):
        seed = self.seed
        #TO DO


class Display:
    def __init__(self, x, y, map):
        self.x = x
        self.y = y
        self.map = map

        #how many cubes to display
        self.displayx = 32
        self.displayy = 24

        self.displayedMap = []
        self.buildEmpty()
        self.fillIt()

    def buildEmpty(self):
        self.displayedMap = [] * self.displayx
        for i in range(self.displayx):
            line = [0] * self.displayy
            self.displayedMap.append(line)

    def fillIt(self):
        for xx in range(len(self.displayedMap)):
            for yy in range(len(self.displayedMap[xx])):
                try:
                    self.displayedMap[xx][yy] = self.map.map[xx+self.x-((int)(self.displayx/2))][yy+self.y-((int)(self.displayy/2))]
                except:
                    self.displayedMap[xx][yy] == 1
                    pass


    def update(self,x,y):
        self.map.map[self.x][self.y] = 0
        self.x = x
        self.y = y
        self.map.map[self.x][self.y] = 2
        self.fillIt()
