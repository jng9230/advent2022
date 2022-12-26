def solve():
    important_cycles = set([20, 60, 100, 140, 180, 220])
    reg = 1 #register value
    cycle = 0
    res = 0 #result to return: sum of values at important cycles
    with open('10-input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            splits = line.split(" ")
            op = splits[0]
            add_val = 0 if len(splits) == 1 else int(splits[1])

            def update(cycle,res,reg):
                cycle += 1
                if cycle in important_cycles:
                    res += reg*cycle
                    # print(f"cycle {cycle}: SS: {reg*cycle}, reg:{reg}, val:{add_val}")
                return cycle, res, reg

            if op == "noop":
                cycle, res, reg = update(cycle,res,reg)
            elif op == "addx":
                cycle, res, reg = update(cycle,res,reg)
                cycle, res, reg = update(cycle,res,reg)
                reg += add_val

    return res


def solve2():
    important_cycles = set([40, 80, 120, 160, 200, 240])
    reg = 1 #register value
    cycle = 0
    res = "" #string to be printed
    with open('10-input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            splits = line.split(" ")
            op = splits[0]
            add_val = 0 if len(splits) == 1 else int(splits[1])
            
            def update(cycle, res, reg):
                if cycle in important_cycles:
                    res += "\n"
                if reg-1 <= cycle%40 <= reg+1:
                    res += "#"
                else:
                    res += "."
                cycle += 1
                # print(f"cycle {cycle}, reg:{reg}")
                return cycle, res, reg

            if op == "noop":
                cycle, res, reg = update(cycle, res, reg)
            elif op == "addx":
                cycle, res, reg = update(cycle, res, reg)
                cycle, res, reg = update(cycle, res, reg)
                reg += add_val

    return res

if __name__ == "__main__":
    print(solve())
    print(solve2())


            
