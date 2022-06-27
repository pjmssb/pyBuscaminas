from tkinter import Button, Label 
import random
import settings

class Cell:

    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_shown = False
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
    
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label (
            location,            
            bg="black", fg="white",
            width = 12,
            height = 4,
            font = ("",30),
            text=f"Cells left: {settings.CELL_COUNT}"
        )
        Cell.cell_count_label_object = lbl

    def left_click_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
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
        if not self.is_shown:
            Cell.cell_count -= 1    
            print(f'Quedan: {Cell.cell_count}')
        self.is_shown = True
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
        print(f'{self.x},{self.y} -> {self.surrounded_cells_mines_length}')
        if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.cell_btn_object.configure(text=cell_obj.surrounded_cells_mines_length)
                    if cell_obj.surrounded_cells_mines_length == 0 and not cell_obj.is_shown:
                        print ('Recursión')
                        cell_obj.show_cell()
                    else:
                        cell_obj.is_shown = True
                        Cell.cell_count -= 1
        if Cell.cell_count_label_object:
                 Cell.cell_count_label_object.configure(text=f'Cells left: {Cell.cell_count}') 
        
    
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