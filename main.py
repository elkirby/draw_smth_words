import enchant
import numbers
import sys

def get_permutations(letters):
    permutations = []
    if len(letters) == 2:
        return [letters, letters[::-1]]
    
    for i in range(len(letters)):
        first = letters[i]
        test_letters = letters[:i] + letters[i+1:]
        substrings = get_permutations(test_letters)
        for s in substrings:
            permutations.append(first + s)
    return permutations
    

def get_words(letters, length):
    permutations = [p[:length] for p in get_permutations(letters)]
    d = enchant.Dict('en_US')
    
    return set(w for w in filter(lambda x: d.check(x), permutations))

def main():
    l = len(sys.argv)
    try:
        letters, length = sys.argv[l-2], sys.argv[l-1]
        length = int(length)

    except TypeError:
        length, letters = letters, length
        length = int(length)

    finally:
        words = get_words(letters, length)
        for word in words:
            print(word)


if __name__ == '__main__':
    main()
