def compose(functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def functionsComposition(functions, x):
    return compose(map(eval, functions))(x)
