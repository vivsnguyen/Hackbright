import cs1graphics as cg

def make_paper():
    paper = cg.Canvas(600, 600, bgColor="skyBlue", title="Cat")
    return paper

paper = make_paper()


class Cat:
    center_x = None
    center_y = None
    color = None

    def __init__(self, center_point_x, center_point_y, color=(158, 102, 41)):
        self.center_x = center_point_x
        self.center_y = center_point_y
        self.color = color

    def make_cat_appear(self):
        cat = cg.Circle(100, cg.Point(self.center_x, self.center_y))
        cat.setFillColor(self.color)
        eye1 = cg.Circle(10, cg.Point(self.center_x - 50, self.center_y - 25))
        eye1.setFillColor("black")
        eye2 = cg.Circle(10, cg.Point(self.center_x + 50, self.center_y - 25))
        eye2.setFillColor("black")
        ear1 = cg.Polygon(cg.Point(self.center_x + 90, self.center_y - 25), cg.Point(self.center_x + 125, self.center_y - 125), cg.Point(self.center_x + 30, self.center_y - 90))
        ear2 = cg.Polygon(cg.Point(self.center_x - 90, self.center_y - 25), cg.Point(self.center_x - 125, self.center_y - 125), cg.Point(self.center_x - 30, self.center_y - 90))
        nose = cg.Polygon(cg.Point(self.center_x - 15, self.center_y), cg.Point(self.center_x, self.center_y + 15), cg.Point(self.center_x + 15, self.center_y))
        nose_line1 = cg.Path(cg.Point(self.center_x + 15, self.center_y + 30), cg.Point(self.center_x, self.center_y + 15))
        nose_line2 = cg.Path(cg.Point(self.center_x - 15, self.center_y + 30), cg.Point(self.center_x, self.center_y + 15))
        nose.setFillColor("pink")
        ear1.setFillColor(self.color)
        ear1.setDepth(70)
        ear2.setFillColor(self.color)
        ear2.setDepth(70)
        nose.setDepth(25)
        nose_line1.setBorderWidth(2.5)
        nose_line2.setBorderWidth(2.5)
        nose_line1.setDepth(25)
        nose_line2.setDepth(25)
        paper.add(nose)
        paper.add(ear1)
        paper.add(ear2)
        paper.add(cat)
        paper.add(eye1)
        paper.add(eye2)
        paper.add(nose_line1)
        paper.add(nose_line2)


fluffy = Cat(300,300)
fluffy.make_cat_appear()
