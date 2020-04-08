def add_title(self):
        square = Square(side_length=2 * self.L)
        title = TextMobject("Brownian motion")
        title.scale(1.5)
        title.next_to(square, UP)

        self.add(square)
        self.add(title)