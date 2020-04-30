def get_stroke_rgbas(self, vmobject, background=False):
        return self.modified_rgbas(
            vmobject, vmobject.get_stroke_rgbas(background)
        )

