from datetime import datetime


def SecretCode(file):
    NumOfLines = str(len(file.readlines()))
    getTime = ''
    if (len(NumOfLines) > 2):
        getTime = NumOfLines[:2]+":"+NumOfLines[2:]
    elif(len(NumOfLines) == 2):
        getTime = NumOfLines[:2]+":"+"00"
    d = datetime.strptime(getTime, "%H:%M")
    Meeting_time = d.strftime("%I:%M %p")
    Meeting_place = max((file.txt).split(), key=(file.txt).count)
    print("Meeting time:".format(Meeting_time))
    print("Meeting place:".format(Meeting_place))


if __name__ == "__main__":
    fname = input()
    file = open(fname, "r")
    print(SecretCode(file))
