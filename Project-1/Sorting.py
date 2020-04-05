def rearrange(colors):
    return("-".join(sorted(colors)))


if __name__ == "__main__":
    colors = list(map(str, input().split("-")))
    print(rearrange(colors))
