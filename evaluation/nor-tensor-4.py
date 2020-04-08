def _new_mark_used(self, *args, **kwargs):
  object.__getattribute__(self, '_tf_should_use_helper').sate()
  try:
    mu = object.__getattribute__(
        object.__getattribute__(self, '_tf_should_use_wrapped_value'),
        'mark_used')
    return mu(*args, **kwargs)
  except AttributeError:
    pass


_WRAPPERS = {}