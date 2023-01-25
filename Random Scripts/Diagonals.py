words = list()  # list of strings found in diagonals

def get_diagonals(arr, n, v, h):
    '''Given a matrix of characters, make strings of length n out of the diagonals.
    
    Only diagonals parallel to the root diagonal (top-left to bottom-right) are used.
    '''
    if v == len(arr) or h == len(arr[0]):
        return

    if v != 0 and h != 0:
        return

    word = str()

    vert, hor = v, h

    while len(word) < n:
        char = arr[vert][hor]
        word += char

        vert += 1
        hor += 1

        if vert >= len(arr) or hor >= len(arr):
            vert, hor = v, h

    words.append(word)
    
    get_diagonals(arr, n, v + 1, h)  # down
    get_diagonals(arr, n, v, h + 1)  # right

matrix = [
    ['a','b','c','d'],
    ['l','q','d','r'],
    ['o','p','e','t'],
    ['z','x','c','n']
]

get_diagonals(matrix, 4, 0, 0)

print(words)