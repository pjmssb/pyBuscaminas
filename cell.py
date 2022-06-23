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
            self.show_cell()

    def show_cell(self):
        pass
    
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