def cross_out_assumption(self):
    cross = Cross(self.assumption)
    cross.set_color(GREY)
    self.bar_chart.save_state()

    self.play(ShowCreation(cross))
    self.play(self.bar_chart.fade, 0.7)
    self.wait(2)
    self.play(self.bar_chart.restore)

