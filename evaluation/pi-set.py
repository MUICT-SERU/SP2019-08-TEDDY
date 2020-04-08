##PI pattern on line 33
def handle_dual_graph(self, words1, words2):
        words1.set_color("yellow")
        words2.set_color("yellow")
        connected = TextMobject("Connected")
        connected.set_color("lightgreen")
        not_connected = TextMobject("Not Connected")
        not_connected.set_color("red")
        for mob in connected, not_connected:
            mob.shift(self.points[3] + UP)

        self.play(*[
            ShowCreation(mob, run_time = 1.0)
            for mob in self.edges + self.vertices
        ])
        self.wait()
        for region in self.regions:
            self.set_color_region(region)
        self.add(words1)
        self.wait()
        self.reset_background()
        self.add(words2)

        region_pairs = it.combinations(self.graph.region_cycles, 2)
        for x in range(6):
            want_matching = (x%2 == 0)
            found = False
            while True:
                try:
                    cycle1, cycle2 = next(region_pairs)
                except:
                    return
                shared = set(cycle1).intersection(cycle2)
                if len(shared) == 2 and want_matching:
                    break
                if len(shared) != 2 and not want_matching:
                    break
            for cycle in cycle1, cycle2:
                index = self.graph.region_cycles.index(cycle)
                self.set_color_region(self.regions[index])
            if want_matching:
                self.remove(not_connected)
                self.add(connected)
                tup = tuple(shared)
                if tup not in self.graph.edges:
                    tup = tuple(reversed(tup))
                edge = deepcopy(self.edges[self.graph.edges.index(tup)])
                edge.set_color("red")
                self.play(ShowCreation(edge), run_time = 1.0)
                self.wait()
                self.remove(edge)
            else:
                self.remove(connected)
                self.add(not_connected)
                self.wait(2)
            self.reset_background()