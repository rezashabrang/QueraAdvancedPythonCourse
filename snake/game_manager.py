import consts

from cell import Cell


class GameManager:

    def __init__(self, size, screen, sx, sy, block_cells):
        self.size=size
        self.screen=screen
        self.sx=sx
        self.sy=sy
        self.block_cells=block_cells
        self.turn=0
        self.snakes=[]
        self.cells=[[] for i in range(size)]
        for i in range(size):
            for j in range(size):
                self.cells[i].append((sx+i*consts.cell_size,sy+j*consts.cell_size))

        self.fruit=[]
        self.del_cell_moving=[]
        self.accu_cells=[]
        self.free_cells=[[]for i in range(size)]
        self.cells_class_build=[[0 for i in range(size)] for i in range(size)]


        for i in range(size):
            for j in range(size):
                self.cells_class_build[i][j]=Cell(screen, self.cells[i][j][0], self.cells[i][j][1], consts.back_color)

        for i in range(len(block_cells)):
            self.cells_class_build[block_cells[i][0]-1][block_cells[i][1]-1].set_color(consts.block_color)



    def add_snake(self,snake):
        self.snakes.append(snake)

    def get_cell(self, pos):
        if pos[0] in list(range(1,self.size+1,1)) and pos[1] in list(range(1,self.size+1,1)):
            return pos
        else:
            return None

    def kill(self,killed_snake):
        self.snakes.remove(killed_snake)


    def handle(self, keys):

        for zingil in self.snakes:
            zingil.handle(keys)
            zingil.next_move()

        self.turn+=1

        for i in self.snakes:
            for j in range(len(i.cells)):
                self.cells_class_build[i.cells[j][0]-1][i.cells[j][1]-1].set_color(i.color)

        for i in (self.del_cell_moving):
            self.cells_class_build[i[0] - 1][i[1] - 1].set_color(consts.back_color)

        for i in self.fruit:
            self.cells_class_build[i[0]-1][i[1]-1].set_color(consts.fruit_color)

        self.del_cell_moving=[]

        if self.turn%10==0:
            for i in range(self.size):
                for j in range(self.size):
                    if self.cells_class_build[i][j].color!=consts.back_color:
                        self.accu_cells.append([i+1,j+1])
            for k in range(self.size):
                for i in range(len(self.accu_cells)):
                    if [self.accu_cells[i][0]-1,self.accu_cells[i][1]-1] not in self.accu_cells and 0<self.accu_cells[i][0]-1<21 and 0<self.accu_cells[i][1]-1<21:
                        self.accu_cells.append([self.accu_cells[i][0]-1,self.accu_cells[i][1]-1])
                    if [self.accu_cells[i][0],self.accu_cells[i][1]-1] not in self.accu_cells and 0<self.accu_cells[i][0]<21 and 0<self.accu_cells[i][1]-1<21:
                        self.accu_cells.append([self.accu_cells[i][0],self.accu_cells[i][1]-1])
                    if [self.accu_cells[i][0]+1,self.accu_cells[i][1]-1] not in self.accu_cells and 0<self.accu_cells[i][0]+1<21 and 0<self.accu_cells[i][1]-1<21:
                        self.accu_cells.append([self.accu_cells[i][0]+1,self.accu_cells[i][1]-1])
                    if [self.accu_cells[i][0]-1,self.accu_cells[i][1]] not in self.accu_cells and 0<self.accu_cells[i][0]-1<21 and 0<self.accu_cells[i][1]<21:
                        self.accu_cells.append([self.accu_cells[i][0]-1,self.accu_cells[i][1]])
                    if [self.accu_cells[i][0]+1,self.accu_cells[i][1]] not in self.accu_cells and 0<self.accu_cells[i][0]+1<21 and 0<self.accu_cells[i][1]<21:
                        self.accu_cells.append([self.accu_cells[i][0]+1,self.accu_cells[i][1]])
                    if [self.accu_cells[i][0]-1,self.accu_cells[i][1]+1] not in self.accu_cells and 0<self.accu_cells[i][0]-1<21 and 0<self.accu_cells[i][1]+1<21:
                        self.accu_cells.append([self.accu_cells[i][0]-1,self.accu_cells[i][1]+1])
                    if [self.accu_cells[i][0],self.accu_cells[i][1]+1] not in self.accu_cells and 0<self.accu_cells[i][0]<21 and 0<self.accu_cells[i][1]+1<21:
                        self.accu_cells.append([self.accu_cells[i][0],self.accu_cells[i][1]+1])
                    if [self.accu_cells[i][0]+1,self.accu_cells[i][1]+1] not in self.accu_cells and 0<self.accu_cells[i][0]+1<21 and 0<self.accu_cells[i][1]+1<21:
                        self.accu_cells.append([self.accu_cells[i][0]+1,self.accu_cells[i][1]+1])
                for h in range(self.size):
                    for j in range(self.size):
                        if [h+1,j+1] not in self.accu_cells:
                            self.free_cells[k].append((h+1,j+1))
                if self.free_cells[k]==[]:
                    self.fruit.append([min(self.free_cells[k-1])[0],min(self.free_cells[k-1])[1]])
                    self.accu_cells=[]
                    self.free_cells=[[]for i in range(self.size)]
                    break
