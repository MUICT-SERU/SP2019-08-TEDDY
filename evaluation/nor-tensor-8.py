def __init__(self, local_name, parent_module_globals, name, warning=None):  # pylint: disable=super-on-old-class
    self._local_name = local_name
    self._parent_module_globals = parent_module_globals
    self._warning = warning

    super(LazyLoader, self).__init__(name)