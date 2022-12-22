import re
from collections import deque

def get_stacks(text):
    """
    returns a 2d array, with each subarray representing one stack
    """
    text = text.split("\n")

    #remove spaces and find # of stacks needed
    stacks = [[] for _ in range(len(text[-1].replace(" ", "")))] 

    #iterate through and append to stacks as fit 
    for row in text[:-1]: 
        no_brackets = re.sub(r'[\[\]]'," ", row)#drop brackets
            #keep spaces to maintain length of lines for indexing
        for i, char in enumerate(no_brackets):
            if char != " ":
                stacks[(i-1)/4].append(char)#3 spaces between chars

    #reverse stacks to correct order
    for i in range(len(stacks)):
        stacks[i].reverse()
    return stacks

def get_steps(text):
    """
    returns a list of dicts containing the instructions 
    - each dict will have key:value as such:
        {
            "move": i,
            "from": j, 
            "to": k
        }
    where i,j,k are all ints.
    """
    text = text.split("\n")
    steps = []
    for step in text:
        step = re.sub(r'\s+', '', step)
        move = int(step.split("move")[1].split("from")[0])
        from1 = int(step.split("from")[1].split("to")[0])-1 #-1 as python lists are 0-based
        to = int(step.split("to")[1])-1
        steps.append({
            "move": move,
            "from": from1, 
            "to": to
        })
    return steps

def parse_input(text):
    splits = text.split("\n\n")
    stacks = get_stacks(splits[0])
    steps = get_steps(splits[1])
    return stacks, steps

def solve():
    """
    - move around blocks in stacks
    - find the block at the top of each stack after all steps
    """
    with open('5-input.txt', 'r') as f:
        text = f.read()
        stacks, steps = parse_input(text)
        
    #work through the steps
    for step in steps:
        for _ in range(step.get("move")):
            popped = stacks[step.get("from")].pop()
            stacks[step.get("to")].append(popped)

    temp = ""
    for stack in stacks:
        temp += stack.pop()
    return temp
    

def solve2():
    """
    - move around blocks in stacks via slicing (NOT popping)
    - find the block at the top of each stack after all steps
    """
    with open('5-input.txt', 'r') as f:
        text = f.read()
        stacks, steps = parse_input(text)
        
    #work through the steps
    for step in steps:
        temp_stack = deque([]) #list to prepend to
        for _ in range(step.get("move")):
            popped = stacks[step.get("from")].pop()
            temp_stack.appendleft(popped)

        stacks[step.get("to")] += temp_stack
        
    temp = ""
    for stack in stacks:
        temp += stack.pop()
    return temp

if __name__ == "__main__":
    print(solve())
    print(solve2())