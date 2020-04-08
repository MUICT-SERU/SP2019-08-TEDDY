def view(*args, **kwargs):
    self = view.view_class(*class_args, **class_kwargs)
    return self.dispatch_request(*args, **kwargs)