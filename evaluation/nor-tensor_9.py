def __getattr__(self, item):
    module = self._load()
    return getattr(module, item)

