import tkinter as tk

class Window(tk.Tk):
  def __init__(self):
    super().__init__()
    self.title("Hello Tkinter")
    label = tk.Label(self, text="Hello World!")
    label.pack(fill=tk.BOTH, expand=1, padx=100, pady=50)

if __name__ == "__main__":
   window = Window()
   window.mainloop()
  
# fill: This tells the widget to take all the space in both directions
# expand: This tells the widget to expand when the window is resized
# padx: Padding (empty space) of 100 pixels in the x direction (left, right)
# pady: Padding of 50 pixels in the y direction (above, below)