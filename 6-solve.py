def solve(n):
    """
    Returns the index at which there exists n unique preceeding characters
    """
    with open('6-input.txt', 'r') as f:
        text = f.read()

    for i in range(len(text)):
        seen = set()
        for j in range(n):
            seen.add(text[i+j])
        if len(seen) == n: #len of n -> n unique chars seen
            return i+n

if __name__ == "__main__":
    print(solve(4))
    print(solve(14))