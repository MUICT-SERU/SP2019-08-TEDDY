def text_box(self, str):
        box = TextMobject(str).scale(0.3)
        box.add(SurroundingRectangle(box, stroke_color = DARK_GREY))
        return box

