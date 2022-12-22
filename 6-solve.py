def solve():
    """
    find the index at which there exists 4 unique preceeding characters
    """
    with open('6-input.txt', 'r') as f:
        text = f.read()

    for i in range(len(text)):
        seen = set()
        for j in range(4):
            seen.add(text[i+j])
        if len(seen) == 4: #len of 4 -> 4 unique chars seen
            return i+4

def solve2():
    """
    find the index at which there exists 14 unique preceeding characters
    """
    with open('6-input.txt', 'r') as f:
        text = f.read()

    for i in range(len(text)):
        seen = set()
        for j in range(14):
            seen.add(text[i+j])
        if len(seen) == 14:
            return i+14        


if __name__ == "__main__":
    print(solve())
    print(solve2())