from tkinter import Button 
import random
import settings

class Cell:

    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text = ""
        )
        btn.bind('<Button-1>', self.left_click_action)
        btn.bind('<Button-3>', self.right_click_action)
        self.cell_btn_object = btn
    
    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            #if self.surrounded_cells_mines_length == 0:
            #    for cell_obj in self.surrounded_cells:
            #        cell_obj.show_cell()
            self.show_cell()


    def get_cell_by_axis(self, x, y):
        #Return a cell object
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x-1, self.y-1),
            self.get_cell_by_axis(self.x-1, self.y),
            self.get_cell_by_axis(self.x-1, self.y+1),
            self.get_cell_by_axis(self.x, self.y-1),
            self.get_cell_by_axis(self.x, self.y+1),
            self.get_cell_by_axis(self.x+1, self.y-1),
            self.get_cell_by_axis(self.x+1, self.y),
            self.get_cell_by_axis(self.x+1, self.y+1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
        print(f'{self.x},{self.y} -> {self.surrounded_cells_mines_length}')
        if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.cell_btn_object.configure(text=cell_obj.surrounded_cells_mines_length)
                    if cell_obj.surrounded_cells_mines_length == 0:
                        print ('Recursión')
                        cell_obj.show_cell()
        
    
    def show_mine(self):
        #A logic to interrup game
        #Message lost game
        self.cell_btn_object.configure(bg='red')
    
        
    def right_click_action(self, event):
        print(event)
        print('I am right clicked!')
    
    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell(x={self.x}, y={self.y}, is_mine={self.is_mine})"