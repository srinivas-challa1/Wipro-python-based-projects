from collections import namedtuple


def writingData(categories):
    #categories = input().split()
    Items = namedtuple("Items", categories)
    ItemList = []
    for _ in range(int(input("Number of items:"))):
        item = Items._make(input().split())
        ItemList.append(item)
    ItemL = []
    for item in ItemList:
        ItemL.append(item._asdict())
    itemData = [" ".join(i.values()) for i in ItemL]
    return(itemData)


if __name__ == "__main__":
    categories = input().split()
    print(writingData(categories))
