def Repeatchar(word):
    size = len(word)
    print(size)
    count = [0] * 256
    print(count)
    for i in range(size):
        if count[ord(word[i])] == 1:
            print(word[i])
            break
        else:
            count[ord(word[i])] += 1

    if i == size-1:
        print("no repeated character")


if __name__ == '__main__':
    word = "abcaefgh"
    Repeatchar(word)
