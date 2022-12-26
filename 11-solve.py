from collections import deque
import heapq
from math import gcd # Python versions 3.5 and above
from functools import reduce # Python version 3.x

def to_dict(text):
    """
    Converts the input to a dict 
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
        rhs = op_splits[-1]
        if op == "+":
            func = lambda x : x + (int(rhs) if rhs != "old" else x)
        else:
            func = lambda x : x * (int(rhs) if rhs != "old" else x)

        # print(f"name: {name}")
        # print(func(2))
        # print(f"items: {items}")
        # print(f"test: {test}")
        # print(f"test1: {test1}")
        # print(f"test0: {test0}\n\n")
        temp[name] = {
            "items": items, 
            "test": test,
            "test1": test1,
            "test0": test0,
            "inspections": 0,
            "test_op": func(2),
            "op": func
        }
    
    return temp

FUCK1 = [
    lambda x : x * 19,
    lambda x : x + 6, 
    lambda x : x * x,
    lambda x : x + 3
]

FUCK = [
    lambda x : x * 3,
    lambda x : x + 8,
    lambda x : x * x,
    lambda x : x + 2,
    lambda x : x + 3,
    lambda x : x * 17, 
    lambda x : x + 6,
    lambda x : x + 1
]


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
                item1 = FUCK[i](item)
                item2 = item1 // 3 #drop worry b/c no damage
                if item2 % m["test"] == 0: #test and toss
                    monkeys[m["test1"]]["items"].append(item2)
                else: 
                    monkeys[m["test0"]]["items"].append(item2)

    #monkey business: the multiple of two largest inspections
    res_arr = []
    for i in range(num_monkeys):
        res_arr.append(monkeys[i]["inspections"])
    heapq.heapify(res_arr)
    while len(res_arr) != 2:
        heapq.heappop(res_arr) 

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

    thing = []
    for i in range(num_monkeys):
        thing.append(monkeys[i]["test"])
    LCM = lcm(thing)

    #simulate the monkeys throwing 
    for r in range(num_rounds):
        for i in range(num_monkeys):
            m = monkeys[i]
            while len(m["items"]): #check only if there are items
                m["inspections"] += 1
                item = m["items"].popleft()#inspect item 
                # item1 = m["op"](item) #inspect, change worry
                item1 = FUCK[i](item)
                item2 = item1 % LCM
                if item2 % m["test"] == 0: #test and toss
                    monkeys[m["test1"]]["items"].append(item2)
                else: 
                    monkeys[m["test0"]]["items"].append(item2)

    res_arr = []
    for i in range(num_monkeys):
        res_arr.append(monkeys[i]["inspections"])
    heapq.heapify(res_arr)
    while len(res_arr) != 2:
        heapq.heappop(res_arr) 

    return res_arr[0] * res_arr[1]

if __name__ == "__main__":
    print(solve())
    print(solve2())