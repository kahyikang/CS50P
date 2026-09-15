def main():
    inp = shorten(input("Input: ").strip())
    print("Output:", inp)


def shorten(word):
    vowel = ["a","e","i","o","u","A","E","I","O","U"]
    for i in word:
        if i in vowel:
            word = word.replace(i,"")
    return word


if __name__ == "__main__":
    main()
