def vowelCount(name):
    vowels = "aeiou"
    vc = 0
    for character in name:
        if character.lower() in vowels:
            vc += 1
        else:
            continue
    return(vc)


if __name__ == "__main__":
    name = input()
    print(vowelCount(name))
