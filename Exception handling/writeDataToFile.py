from PreparingList import writingData


def Data(fname):
    data = writingData(input().split())
    with open(fname, "w") as file:
        file.writelines("\n".join(data))
    return(file)


if __name__ == "__main__":
    fname = input()
    print(Data(fname))
