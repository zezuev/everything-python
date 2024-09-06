import inspect

REGISTRY = {}


def get_param_types(func):
    annotations = inspect.get_annotations(func)
    annotations.pop("return", None)
    return tuple(annotations.values())


def get_arg_types(args):
    return tuple(type(a) for a in args)


def register(func):
    param_types = get_param_types(func)
    REGISTRY.setdefault(func.__qualname__, {})[param_types] = func


def is_method(func):
    return "self" in inspect.signature(func).parameters


def create_router(func):
    if is_method(func):

        def router(self, *args):
            arg_types = get_arg_types(args)
            target = REGISTRY[func.__qualname__][arg_types]
            return target(self, *args)

    else:

        def router(*args):
            arg_types = get_arg_types(args)
            target = REGISTRY[func.__qualname__][arg_types]
            return target(*args)

    return router


def overload(func):
    register(func)
    return create_router(func)
