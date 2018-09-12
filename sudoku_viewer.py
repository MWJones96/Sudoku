from tkinter import *
from tkinter.colorchooser import askcolor
import random

class SudokuComponent:
	def __init__(self):
		self.root = Tk()
		self.canvases = [SudokuCell(self.root)]*81
		self.root.mainloop()

class SudokuCell:
	def __init__(self, root):
		self.c = Canvas(root, bg='white', width=640, height=640)
		self.c.grid(row=9, columnspan=9)
		self.setup()

	def setup(self):
		self.old_x = None
		self.old_y = None
		self.c.bind('<B1-Motion>', self.draw)
		self.c.bind('<ButtonRelease-1>', self.release_draw)

	def draw(self, event):
		if self.old_x and self.old_y:
			self.c.create_line(self.old_x, self.old_y, event.x, event.y,
						width=5, fill='black',
						capstyle=ROUND, smooth=TRUE, splinesteps=36)
		self.old_x = event.x
		self.old_y = event.y

	def release_draw(self, event):
		self.old_x, self.old_y = None, None
		self.c.delete("all")

		rand_int = random.randint(0, 9)

		self.c.create_text(100, 100, fill="black",font="Times 200 bold",
		                text=str(rand_int))
		print('release')


if __name__ == '__main__':
	SudokuComponent()