def calculate(fname):
    try:
        with open(fname, "r") as file:
            totalAmount = 0
            FreeItems = 0
            Discount = 0
            ItemsPurchased = 0
            FinalAmount = 0
            flst = file.readlines()
            for line in flst:
                if (not line.isspace()):
                    line = line.rstrip("\n")
                    if(not line.startswith("Discount")):
                        ItemsPurchased += 1
                        if(line[line.find(' ')+1:] != "Free"):
                            totalAmount += int(line[line.find(' ')+1:])
                        elif(line[line.find(' ')+1:] == "Free"):
                            FreeItems += 1
                    elif(line.startswith("Discount")):
                        Discount += int(line[line.find(' ')+1:])
            FinalAmount = totalAmount-Discount

    except IOError:
        print("File doesn't exist cannot perform operations on the file")

    else:
        print("No of items purchased:{}".format(ItemsPurchased))
        print("No of free items:{}".format(FreeItems))
        print("Amount to pay:{}".format(totalAmount))
        print("Discount given:{}".format(Discount))
        print("Final Amount paid:{}".format(FinalAmount))


if __name__ == "__main__":
    fname = input()
    calculate(fname)
