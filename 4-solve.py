def solve():
    """
    find sets that fully contain others
    """
    count = 0
    with open('4-input.txt', 'r') as f:
        for line in f:
            line = line.strip()

            #skip if empty line 
            if line == "":
                continue
            
            #get the assignments for each elf
            no_commas = line.strip().split(",") 
            first = no_commas[0].split("-")
            second = no_commas[1].split("-")
            first = [int(first[0]), int(first[1])] #str to int
            second = [int(second[0]), int(second[1])]

            #compare assignments to see if one contains the other
            if (first[0] <= second[0] and first[1] >= second[1]) or\
                (first[0] >= second[0] and first[1] <= second[1]):
                    count += 1
    return count
    
def solve2():
    """
    find sets that contain any overlaps
    """
    count = 0
    with open('4-input.txt', 'r') as f:
        for line in f:
            line = line.strip()

            #skip if empty line 
            if line == "":
                continue
            
            #get the assignments for each elf
            no_commas = line.strip().split(",") 
            first = no_commas[0].split("-")
            second = no_commas[1].split("-")
            first = [int(first[0]), int(first[1])] #str to int
            second = [int(second[0]), int(second[1])]

            #compare assignments to see if one contains the other
            #   fully contains
            first_contains = first[0] <= second[0] and first[1] >= second[1]
            second_contains = first[0] >= second[0] and first[1] <= second[1]
            #   partially contains (overlaps in any way) -- symmetric
            first_includes_tail = first[0] <= second[0] and first[1] >= second[0]
            first_includes_head = first[0] <= second[1] and first[1] >= second[1]
            if (first_contains or
                second_contains or
                first_includes_tail or
                first_includes_head):
                count += 1

    return count


if __name__ == "__main__":
    print(solve())
    print(solve2())