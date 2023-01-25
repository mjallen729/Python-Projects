"""Landfinder LeetCode challenge/Twitch interview question.

Given an arbitrarily sized array of 0 (water) and 1 (land), find the
total number of islands.
"""

landgraph = [
    [1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1]
]

# loop through array
# when 1 is found, call recursive flood fill changing connected 1s to 0s
# increment island count


def find_land(arr):
    island_count = 0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                _recursive_search(arr, i, j)
                island_count += 1

    return island_count


def _recursive_search(arr, i, j):
    if i >= len(arr) or i < 0 or j >= len(arr[0]) or j < 0:  # if out of bounds
        return

    if arr[i][j] == 0:
        return

    arr[i][j] = 0

    _recursive_search(arr, i - 1, j)  # up
    _recursive_search(arr, i + 1, j)  # down
    _recursive_search(arr, i, j + 1)  # right
    _recursive_search(arr, i, j - 1)  # left
    _recursive_search(arr, i + 1, j + 1)  # down-right
    _recursive_search(arr, i + 1, j - 1)  # down-left
    _recursive_search(arr, i - 1, j + 1)  # up-right
    _recursive_search(arr, i - 1, j - 1)  # up-left


if __name__ == "__main__":
    print(find_land(landgraph))
