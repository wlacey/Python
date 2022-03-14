def alternate():
    while True:
        yield 1
        yield 0

alternator = alternate()
next(altenator)
