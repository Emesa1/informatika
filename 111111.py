for i in range(1, 200):
    n2 =  bin(i)[2:]
    if i % 2 == 0:
        n2 = n2 + "00"
    else:
        n2 = n2 + "11"
    r = int(n2, 2)
    if r > 115:
        print(i)
        break