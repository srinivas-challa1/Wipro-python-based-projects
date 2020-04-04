def ispalindrome(name):
    return(name == name[::-1])


if __name__ == "__main__":
    name = input()
    print(ispalindrome(name))
