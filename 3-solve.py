def solve():
    val_sum = 0
    with open('3-input.txt', 'r') as f:
        for line in f:
            #split lines in half
            line = list(line)
            first = line[:int(len(line)/2)] #doesn't matter if non-whole int
            second = line[int(len(line)/2):]

            #find the item that occurs twice 
            temp = ""
            for i in first:
                if i in second:
                    temp = i
                    break 

            #ord: A-65, Z-90, a-97, z-122
            #want: A-Z: 27-52, a-z: 1-26
            if ord(temp) >= 97:
                temp = ord(temp) - 96
            else:
                temp = ord(temp) - 38
            val_sum += temp

    return val_sum

def solve2():
    val_sum = 0
    with open('3-input.txt', 'r') as f:
        temp_lines = []#arr to hold 3 lines at a time 
        for line in f:
            #add new line to temp holder 
            if len(temp_lines) == 3: #reset if too long
                temp_lines = []
            temp_lines.append(list(line))

            #don't proceed if not of length
            if len(temp_lines) != 3:
                continue 

            #of length -> try to find the badge that occurs thrice
            badge = ""
            for i in temp_lines[0][:-1]: #newline is at end -- skip
                if i in temp_lines[1] and i in temp_lines[2]:
                    badge = i

            #ord: A-65, Z-90, a-97, z-122
            #want: A-Z: 27-52, a-z: 1-26
            if ord(badge) >= 97:
                badge = ord(badge) - 96
            else:
                badge = ord(badge) - 38
            val_sum += badge
            
    return val_sum

if __name__ == "__main__":
    print(solve())
    print(solve2())