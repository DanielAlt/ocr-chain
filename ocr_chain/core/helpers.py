def updateConfig(args, kwargs):
    for arg in args:
        if arg in kwargs.keys():
            args[arg] = kwargs[arg]
    return (args)
