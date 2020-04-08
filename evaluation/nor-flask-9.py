def is_null_session(self, obj):
        """Checks if a given object is a null session.  Null sessions are
        not asked to be saved.
        This checks if the object is an instance of :attr:`null_session_class`
        by default.
        """
        return isinstance(obj, self.null_session_class)