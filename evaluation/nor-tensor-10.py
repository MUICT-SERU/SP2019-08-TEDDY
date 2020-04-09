def __dir__(self):
    module = self._load()
    return dir(module)

