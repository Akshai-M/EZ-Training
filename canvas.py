import tkinter as tk

class Circle:
    def __init__(self, canvas, x, y, radius, color='red'):
        self.canvas = canvas
        self.radius = radius
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        x0 = self.x - self.radius
        x1 = self.x + self.radius
        y0 = self.y - self.radius
        y1 = self.y + self.radius
        self.canvas.create_oval(x0, y0, x1, y1, fill=self.color)

class Application(tk.Tk):
    def __init__(self):
        super().__init__(None)  # Pass None as the screenName argument
        self.title('Circle Drawing in OOP Style')
        self.geometry('400x400')
        self.canvas = tk.Canvas(self, bg='white', width=400, height=400)
        self.canvas.pack()
        circle = Circle(self.canvas, 200, 200, 100)
        circle.draw()

if __name__ == '__main__':
    app = Application()
    app.mainloop()