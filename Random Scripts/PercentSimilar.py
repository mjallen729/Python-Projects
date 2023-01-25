from collections import defaultdict

def percent_similar(base: str, compare: str) -> float:
    cache = defaultdict(set)  # key= char, val= indexes
    matches = 0
    
    for i in range(0, len(base)):
        cache[base[i]].add(i)

    for i in range(0, len(compare)):
        char = compare[i]

        if char in cache:
            if any(x in cache[char] for x in [i, i + 1, i - 1]):
                matches += 1

    return round((matches / len(compare)) * 100, 2)



if __name__ == '__main__':
    word1 = input('Enter the base word: ')
    word2 = None

    while word2 != '!end':
        word2 = input('Enter the word to compare (type !end to exit): ')
    
        ps = percent_similar(word1, word2)
    
        print(str(ps) + '% similar', end='\n\n')