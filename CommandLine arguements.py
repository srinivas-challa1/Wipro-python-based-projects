from sys import argv


def Count(n):
    c = 0
    k = n[-1].split("-")
    for v in k:
        if v in n[0].split("-"):
            c += 1
        elif v in n[1].split("-"):
            c -= 1
    return("Final happiness {}".format(c))


if __name__ == "__main__":
    n = argv[1:]
    print(Count(n))
