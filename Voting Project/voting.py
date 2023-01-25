file_name = input("Input file: ")

try:
    f = open(file_name, "r")

except:
    print("Invalid file!")
    exit()

candidates = f.readline().split()
votes = list()  # 2d array of vote nums
vote_totals = [0] * len(candidates)  # zeros
total_votes = 0  # total num of votes

for line in f:
    arr = line.split()
    votes.append(arr)

    # Add each i in votes to respective i in totals
    for i in range(len(arr)):
        vote_totals[i] += int(arr[i]) if arr[i] != None else 0
        total_votes += int(arr[i]) if arr[i] != None else 0

max_i = vote_totals.index(max(vote_totals))

print("Vote Report by Alexis\n")

for name in candidates:
    print('\t\t{}'.format(name), end='')

print('\t\tTotals')

d = 1

for row in votes:
    print('District {}'.format(d), end='')
    d += 1

    total = 0

    for n in row:
        print('\t{}'.format(n), end='\t')
        total += int(n)

    print('\t{}'.format(total))

print('Totals', end='')

for n in vote_totals:
    print('\t\t{}'.format(n), end='')

print('\t\t{}'.format(total_votes))

print("\nThe winner is {0} with {1}% of the vote!".format(
    candidates[max_i],
    round(vote_totals[max_i] / total_votes * 100, 2)
))