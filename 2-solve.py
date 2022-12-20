def solve():
    """
    """
    values = {
        ('A','X'): 4,
        ('A','Y'): 8,
        ('A','Z'): 3,
        ('B','X'): 1,
        ('B','Y'): 5,
        ('B','Z'): 9,
        ('C','X'): 7,
        ('C','Y'): 2,
        ('C','Z'): 6,
    }
    points = 0 
    with open('2-input.txt', 'r') as f:
        for line in f:
            first, sec = line.split(" ")[0], line.split(" ")[1].replace("\n","")
            #A for Rock, B for Paper, and C for Scissors
            #X for Rock, Y for Paper, and Z for Scissors
            #1 for Rock, 2 for Paper, and 3 for Scissors
            #0 if you lost, 3 if the round was a draw, and 6 if you won
            #can have a dict for every (first, sec) tuple pair and point value
            points += values.get((first,sec))
    return points

print(solve())

def solve2():
    """
    """
    values = {
        ('A','X'): 3,
        ('A','Y'): 4,
        ('A','Z'): 8,
        ('B','X'): 1,
        ('B','Y'): 5,
        ('B','Z'): 9,
        ('C','X'): 2,
        ('C','Y'): 6,
        ('C','Z'): 7,
    }
    points = 0 
    with open('2-input.txt', 'r') as f:
        for line in f:
            first, sec = line.split(" ")[0], line.split(" ")[1].replace("\n","")
            #A for Rock, B for Paper, and C for Scissors
            #X means lose, Y means tie, Z means win
            #1 for Rock, 2 for Paper, and 3 for Scissors
            #0 if you lost, 3 if the round was a draw, and 6 if you won
            points += values.get((first,sec))
    return points

print(solve2())

