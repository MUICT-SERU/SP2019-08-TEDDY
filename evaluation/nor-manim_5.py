def get_d3_group(self):
    group = VGroup(
        self.get_d3_words(),
        self.get_d3_equation(),
    )
    group.arrange(DOWN, buff=MED_LARGE_BUFF)
    return group

