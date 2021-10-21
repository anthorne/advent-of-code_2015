# Advent of Code 2015 - day 2

fileobj = open("2015_d2_input.txt")
presents = []
paper_needed = 0

for row in fileobj:
    l = int(row.strip().split("x")[0])
    w = int(row.strip().split("x")[1])
    h = int(row.strip().split("x")[2])
    surface = 2 * l * w + 2 * w * h + 2 * h * l
    current = [l, w, h]
    current.sort()
    smallest = current[0] * current[1]
    paper_needed += surface + smallest

    presents.append([l, w, h])

    # print('smallest: ' + str(smallest[0]) + ' then..: ' + str(smallest[1]) + ' and highest: ' + str(smallest[2]))

# length, width, height
# print(presents)

print("The elves should order " + str(paper_needed) + ' square feet of wrapping paper!')
