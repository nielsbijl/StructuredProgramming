def randomAlgorithm():
    import random
    code = []
    for x in range(4):
        code += random.choice(['r', 'b', 'g', 'p', 'z', 'w'])
    return code