class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw_line(self):
        self.p1.draw_point()
        self.p2.draw_point()
