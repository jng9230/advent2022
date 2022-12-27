from collections import deque
from math import gcd # Python versions 3.5 and above
from functools import reduce # Python version 3.x

def to_dict(text):
    """
    Converts the input to a dict with fields as such:
    key: int/monkey number:
    value: {
        "items": [int], - items that the monkey has
        "test": int, - number to be modulo'd
        "test1": int, - monkey to throw to if modulo works
        "test0": int, - monkey to throw to if module doesn't work
        "inspections": 0, - # of items monkey has seen
        "op": + or *, - operator for monkey's operation 
        "operand": int or "old"
    }
    """
    temp = {}
    for i in range(len(text)):
        monkey = text[i]
        lines = monkey.split("\n")
        name = int(lines[0][-2])
        items = lines[1].split(": ")[1].split(",")
        items = deque(list(map(lambda x: int(x), items))) #deque for poplefts
        test = int(lines[3].split(" ")[-1])
        test1 = int(lines[4][-1])
        test0 = int(lines[5][-1])
        
        #determine the operation done by the monkey
        op_splits = lines[2].split(" ")
        op = op_splits[-2]
        operand = op_splits[-1]

        temp[name] = {
            "items": items, 
            "test": test,
            "test1": test1,
            "test0": test0,
            "inspections": 0,
            "op": op,
            "operand": operand
        }
    
    return temp

def solve():
    """
    """
    with open('11-input.txt', 'r') as f:
        text = f.read()

    monkeys_in = text.split("\n\n")
    num_monkeys = len(monkeys_in)
    monkeys = to_dict(monkeys_in)
    num_rounds = 20

    #simulate the monkeys throwing 
    for r in range(num_rounds):
        for i in range(num_monkeys):
            m = monkeys[i]
            while len(m["items"]): #check only if there are items
                m["inspections"] += 1
                item = m["items"].popleft()#inspect item 
                # item1 = m["op"](item) #inspect, change worry
                # item1 = FUCK[i](item)
                rhs = item if m["operand"] == "old" else int(m["operand"])
                if m["op"] == "+":
                    item1 = item + rhs 
                else:
                    item1 = item * rhs
                item2 = item1 // 3 #drop worry b/c no damage
                if item2 % m["test"] == 0: #test and toss
                    monkeys[m["test1"]]["items"].append(item2)
                else: 
                    monkeys[m["test0"]]["items"].append(item2)

    #monkey business: the multiple of two largest inspections
    res_arr = [v["inspections"] for k,v in monkeys.items()]
    res_arr.sort(reverse=True)

    return res_arr[0] * res_arr[1]

def solve2():
    """
    keep stress from exploding via LCM modulo
    """
    with open('11-input.txt', 'r') as f:
        text = f.read()

    monkeys_in = text.split("\n\n")
    num_monkeys = len(monkeys_in)
    monkeys = to_dict(monkeys_in)
    num_rounds = 10_000

    def lcm(denominators):
        """
        https://stackoverflow.com/questions/37237954/calculate-the-lcm-of-a-list-of-given-numbers-in-python
        """
        return reduce(lambda a,b: a*b // gcd(a,b), denominators)

    LCM = lcm([v["test"] for _, v in monkeys.items()])

    #simulate the monkeys throwing 
    for _ in range(num_rounds):
        for i in range(num_monkeys):
            m = monkeys[i]
            while len(m["items"]): #check only if there are items
                m["inspections"] += 1
                item = m["items"].popleft()#inspect item 
                # item1 = m["op"](item) #inspect, change worry
                rhs = item if m["operand"] == "old" else int(m["operand"])
                if m["op"] == "+":
                    item1 = item + rhs 
                else:
                    item1 = item * rhs
                item2 = item1 % LCM
                if item2 % m["test"] == 0: #test and toss
                    monkeys[m["test1"]]["items"].append(item2)
                else: 
                    monkeys[m["test0"]]["items"].append(item2)

    #monkey business: the multiple of two largest inspections
    res_arr = [v["inspections"] for _,v in monkeys.items()]
    res_arr.sort(reverse=True)

    return res_arr[0] * res_arr[1]

if __name__ == "__main__":
    print(solve())
    print(solve2())