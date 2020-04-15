def _load_unlocked(self):
        __traceback_hide__ = True  # noqa: F841
        self._app = rv = self.loader()
        self._bg_loading_exc_info = None
        return rv

