def solve():
    """
    find largest set sum in newline-separated stream
    - newline ==> new set 
    """
    curr_sum = 0
    biggest = 0
    with open('1-input.txt', 'r') as f:
        for line in f:
            # val = line.strip()
            print(line)
            #skip and reset sum if new line
            if val == "": 
                curr_sum = 0
                continue 

            #continue sum otherwise 
            curr_sum += int(val)
            biggest = max(curr_sum, biggest)
    return biggest 


def solve2():
    """
    find 3 largest set sums in newline-separated stream
    - use a heap to maintain 3 largest 
    """
    import heapq
    heap = []
    heapq.heapify(heap)

    curr_sum = 0
    with open('1-input.txt', 'r') as f:
        for line in f:
            val = line.strip()
            #newline -> try to append new sum to heap
            if val == "": 
                heapq.heappush(heap, curr_sum)
                if len(heap) > 3: #pop if too large -- smallest val popped
                    heapq.heappop(heap)
                curr_sum = 0
                continue 
            
            curr_sum += int(val)

    return sum(heap)

if __name__ == "__main__":
    print(solve())
    print(solve2())



            
