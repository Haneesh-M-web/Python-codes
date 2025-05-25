import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import random

class GameOfLife:
    def _init_(self, size=50):
        self.size = size
        self.grid = np.zeros((size, size), dtype=bool)
        self.running = False
        self.fig, self.ax = plt.subplots()
        
        # Set up UI
        plt.subplots_adjust(bottom=0.2)
        self.ax_clear = plt.axes([0.3, 0.05, 0.15, 0.075])
        self.ax_start = plt.axes([0.5, 0.05, 0.15, 0.075])
        self.ax_random = plt.axes([0.7, 0.05, 0.15, 0.075])
        
        self.btn_clear = Button(self.ax_clear, 'Clear')
        self.btn_start = Button(self.ax_start, 'Start/Stop')
        self.btn_random = Button(self.ax_random, 'Random')
        
        self.btn_clear.on_clicked(self.clear_grid)
        self.btn_start.on_clicked(self.toggle_running)
        self.btn_random.on_clicked(self.random_grid)
        
        self.img = self.ax.imshow(self.grid, interpolation='nearest', cmap='binary')
        self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        
    def clear_grid(self, event=None):
        self.grid = np.zeros((self.size, self.size), dtype=bool)
        self.update_display()
        
    def random_grid(self, event=None):
        self.grid = np.random.choice([True, False], size=(self.size, self.size))
        self.update_display()
        
    def toggle_running(self, event=None):
        self.running = not self.running
        
    def on_click(self, event):
        if event.inaxes != self.ax or self.running:
            return
        x, y = int(event.xdata), int(event.ydata)
        self.grid[y, x] = not self.grid[y, x]
        self.update_display()
        
    def update_display(self):
        self.img.set_array(self.grid)
        self.fig.canvas.draw_idle()
        
    def update(self, frame):
        if not self.running:
            return self.img
        
        new_grid = self.grid.copy()
        
        for i in range(self.size):
            for j in range(self.size):
                # Count live neighbors with toroidal boundary conditions
                total = int((self.grid[i, (j-1)%self.size] + 
                            self.grid[i, (j+1)%self.size] + 
                            self.grid[(i-1)%self.size, j] + 
                            self.grid[(i+1)%self.size, j] + 
                            self.grid[(i-1)%self.size, (j-1)%self.size] + 
                            self.grid[(i-1)%self.size, (j+1)%self.size] + 
                            self.grid[(i+1)%self.size, (j-1)%self.size] + 
                            self.grid[(i+1)%self.size, (j+1)%self.size]))
                
                # Apply Conway's rules
                if self.grid[i, j]:
                    if total < 2 or total > 3:
                        new_grid[i, j] = False
                else:
                    if total == 3:
                        new_grid[i, j] = True
        
        self.grid = new_grid
        self.img.set_array(self.grid)
        return self.img
    
    def run(self):
        ani = animation.FuncAnimation(self.fig, self.update, frames=10, 
                                     interval=200, blit=True)
        plt.show()

# Run the game
if _name_ == "_main_":
    game = GameOfLife(size=50)
    game.run()