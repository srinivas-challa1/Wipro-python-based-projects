from datetime import datetime


def SecretCode(file):
    lines = file.readlines()
    NumOfLines = str(len(lines))
    getTime = ''
    if (len(NumOfLines) > 2):
        getTime = NumOfLines[:2]+":"+NumOfLines[2:]
    elif(len(NumOfLines) == 2):
        getTime = NumOfLines[:2]+":"+"00"
    else:
        getTime = "0"+NumOfLines+":"+"00"
    words = [word for line in lines for word in line.split()]
    Meeting_place = max(words, key=words.count)+" Street"
    d = datetime.strptime(getTime, "%H:%M")
    Meeting_time = d.strftime("%I:%M %p")
    print("Meeting time:{}".format(Meeting_time))
    print("Meeting place:{}".format(Meeting_place))


if __name__ == "__main__":
    fname = input()
    file = open(fname, "r")
    SecretCode(file)
