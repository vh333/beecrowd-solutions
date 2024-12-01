while True:
    try:
        dados = list(map(int, input().split()))
        r1 = dados[0]
        x1 = dados[1]
        y1 = dados[2]
        r2 = dados[3]
        x2 = dados[4]
        y2 = dados[5]
        dist = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5
        if dist <= r1 - r2:
            print("RICO")
        else:
            print("MORTO")
    except EOFError:
        break
