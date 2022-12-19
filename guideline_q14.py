def copy():
    with open('write_this.txt', 'w') as fe:
        with open('read_this.txt', 'r') as f:
            c = f.readlines()
            d = [c[x] for x in range(0, len(c), 2)]
            d = str(d)

            print(d)
        fe.writelines(d)


copy()
