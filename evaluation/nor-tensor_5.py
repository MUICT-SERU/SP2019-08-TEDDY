def add_dispatch_support(target):
  """Decorator that adds a dispatch handling wrapper to an op."""
  def wrapper(*args, **kwargs):
    """Call target, and fall back on dispatchers if there is a TypeError."""
    try:
      return target(*args, **kwargs)
    except (TypeError, ValueError):
      # Note: convert_to_eager_tensor currently raises a ValueError, not a
      # TypeError, when given unexpected types.  So we need to catch both.
      result = dispatch(wrapper, *args, **kwargs)
      if result is not OpDispatcher.NOT_SUPPORTED:
        return result
      else:
        raise

  add_dispatch_list(wrapper)
  return tf_decorator.make_decorator(target, wrapper)

