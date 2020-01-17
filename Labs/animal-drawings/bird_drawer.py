import cs1graphics as cg

def make_paper():
    paper = cg.Canvas(600, 600, bgColor="skyBlue", title="Bird")
    return paper

paper = make_paper()


class Bird:
    center_x = None
    center_y = None
    color = None

    def __init__(self, center_point_x, center_point_y, color):
        self.center_x = center_point_x
        self.center_y = center_point_y
        self.color = color

    def make_bird_appear(self):
        bird = cg.Circle(100, cg.Point(self.center_x, self.center_y))
        bird.setFillColor(self.color)
        eye1 = cg.Circle(10, cg.Point(self.center_x - 50, self.center_y - 25))
        eye1.setFillColor("black")
        eye2 = cg.Circle(10, cg.Point(self.center_x + 50, self.center_y - 25))
        eye2.setFillColor("black")
        nose = cg.Polygon(cg.Point(self.center_x - 25, self.center_y - 25), cg.Point(self.center_x, self.center_y), cg.Point(self.center_x + 25, self.center_y - 25))
        nose.setFillColor("yellow")
        nose.setDepth(25)
        paper.add(nose)
        paper.add(bird)
        paper.add(eye1)
        paper.add(eye2)


fluffy = Bird(300,300, "Blue")
fluffy.make_bird_appear()
