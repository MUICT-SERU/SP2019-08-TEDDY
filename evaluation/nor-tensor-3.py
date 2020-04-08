def _new__init__(self, wrapped_value, tf_should_use_helper):
  # pylint: disable=protected-access
  self._tf_should_use_helper = tf_should_use_helper
  self._tf_should_use_wrapped_value = wrapped_value