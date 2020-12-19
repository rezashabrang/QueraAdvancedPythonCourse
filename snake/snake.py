import consts


class Snake:

    def __init__(self, keys, game, pos, color, direction):
        self.keys=keys
        self.game=game
        self.pos=pos
        self.color=color
        self.direction=direction
        self.cells=[pos]
        self.game.add_snake(self)

    def get_head(self):
        return (self.cells[len(self.cells)-1][0],self.cells[len(self.cells)-1][1])

    def next_move(self):
        if self.game.turn!=0:
            if self.direction=="UP":
                if self.pos[1]!=1:
                    self.pos=(self.pos[0],self.pos[1]-1)
                else:
                    self.pos=(self.pos[0],consts.table_size)
            elif self.direction=="DOWN":
                if self.pos[1]!=consts.table_size:
                    self.pos=(self.pos[0],self.pos[1]+1)
                else:
                    self.pos=(self.pos[0],1)
            elif self.direction=="LEFT":
                if self.pos[0]!=1:
                    self.pos=(self.pos[0]-1,self.pos[1])
                else:
                    self.pos=(consts.table_size,self.pos[1])
            elif self.direction=="RIGHT":
                if self.pos[0]!=consts.table_size:
                    self.pos=(self.pos[0]+1,self.pos[1])
                else:
                    self.pos=(1,self.pos[1])


            for i in self.game.snakes:
                if self.pos in i.cells:
                    for j in self.cells:
                        self.game.del_cell_moving.append([j[0],j[1]])
                    self.game.kill(self)
            if [self.pos[0],self.pos[1]] in consts.block_cells:
                for i in self.cells:
                    self.game.del_cell_moving.append([i[0],i[1]])
                self.game.kill(self)
            elif [self.pos[0],self.pos[1]] in self.game.fruit:
                self.cells.append(self.pos)
                self.game.fruit.remove([self.pos[0],self.pos[1]])
            else:
                self.cells.append(self.pos)
                self.game.del_cell_moving.append([self.cells[0][0],self.cells[0][1]])
                self.cells.remove(self.cells[0])


    def handle(self, keys):
        if self.game.turn!=0:
            for i in range(len(keys)):
                if keys[i] in self.keys and self.keys[keys[i]]=="UP" and self.direction!="DOWN":
                    self.direction="UP"
                    break
                if keys[i] in self.keys and self.keys[keys[i]]=="DOWN" and self.direction!="UP":
                    self.direction="DOWN"
                    break
                if keys[i] in self.keys and self.keys[keys[i]]=="RIGHT" and self.direction!="LEFT":
                    self.direction="RIGHT"
                    break
                if keys[i] in self.keys and self.keys[keys[i]]=="LEFT" and self.direction!="RIGHT":
                    self.direction="LEFT"
                    break