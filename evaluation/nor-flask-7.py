def get(self, key, default=None):
        self.accessed = True
        return super(SecureCookieSession, self).get(key, default)