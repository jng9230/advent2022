from math import sqrt
def solve():
    """
    """
    seen = set()
    h = (0,0) #(x,y) position 
    t = (0,0)
    seen.add(t) #add initial position
    with open('9-input.txt', 'r') as f:
        for line in f:
            dir = line[0]
            steps = int(line[2:])
            for _ in range(steps):
                #move head
                h0 = h #original position of head
                if dir == "D":
                    h = (h[0], h[1] - 1)
                elif dir == "U":
                    h = (h[0], h[1] + 1)
                elif dir == "R":
                    h = (h[0] + 1, h[1])
                elif dir == "L":
                    h = (h[0] - 1, h[1])

                #move t if floor of distance > 1
                dist = abs(sqrt((h[0] - t[0])**2 + (h[1] - t[1])**2))
                if dist > sqrt(2):
                    t = h0
                seen.add(t)
            
    return len(seen)

def rope(length):
    """
    NEED TO REFACTOR B/C rope of length 2 
    is with original code is NOT generalizable to length 10.
    - diagonal motion w/ n > 2 can't be equated to
    with just having the tail take the previous head's pos (t = h0).

    - based off of u/errop_'s answer
    """
    rope = [0]*length 
    dir_dict = { #real: horizontal; imag: vertical -- easier dist. and updates later
        "U": 1j,
        "D": -1j, 
        "L": -1,
        "R": 1
    }
    seen = set(rope)
    with open('9-input.txt', 'r') as f:
        for line in f:
            dir = line[0]
            steps = int(line[2:])
            for _ in range(steps):
                rope[0] += dir_dict[dir] #update head
                for i in range(1, length): #update rest of rope
                    diff = rope[i-1] - rope[i] 
                    if abs(diff) > sqrt(2): #euclidean dist > 1 -> update
                        #update via moving by 1 in resp. directions
                        if diff.real != 0:
                            rope[i] += diff.real / abs(diff.real)
                        if diff.imag != 0:
                            rope[i] += complex(0, diff.imag) / abs(diff.imag) #need complex()
                            #   diff.imag/abs(..) is always 1; complex() gives +-1j
                            #   b/c diff.imag returns an int but we want complex nums
                seen.add(rope[-1])
    return len(seen)

if __name__ == "__main__":
    # print(solve())
    print(rope(2))
    print(rope(10))



            
