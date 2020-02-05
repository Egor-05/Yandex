def defractalize(fractal):
    while fractal in fractal:
        del fractal[fractal.index(fractal)]
    return fractal
