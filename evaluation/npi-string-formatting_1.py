##NPI pattern on line 6,8
def report_error(self, e):
    original = getattr(e, "original_exception", None)

    if original is not None:
        return "wrapped " + type(original).__name__

    return "direct " + type(e).__name__
