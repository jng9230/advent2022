class Node:
    """
    Class to represent files in a file system. 
    Each node has a name and parent node.
    """
    def __init__(self, name, size, parent):
        self.name = name 
        self.parent = parent 
        self.size = size

class File(Node):
    """
    A file is a node without children
    """
    def __init__(self, name, size, parent:Node = None):
        super().__init__(name, size, parent)

class Directory(Node):
    """
    A directory is a node with children
    """
    def __init__(self, name, size, parent:Node = None):
        super().__init__(name, size, parent)
        self.children = [] 


def to_tree(text):
    """
    converts the given text input into a tree and returns the root node
    """
    text = text.split("\n")
    root = Directory("/", 0, None)
    curr = root #current directory
    ls = False #flag marking if we're looking at a ls statement
    for line in text:
        # print(line)
        if line[0] == "$": #command to execute 
            splits = line.split(" ")
            if splits[1] == "cd":
                ls = False
                name = splits[2] 
                if name == "/": #do nothing for root
                    continue
                elif name == "..": #bubble up for ..
                    curr = curr.parent
                else: #make new directory on cd
                    new_node = Directory(name, 0, curr)
                    curr.children.append(new_node)
                    curr = new_node 
            elif splits[1] == "ls":
                ls = True
        elif ls: #start adding file sizes
            splits = line.split(" ")
            if splits[0] == "dir": #only make nodes on cd
                continue 
            
            #file -> make new file, update sizes, update dir children
            new_file = File(splits[1],int(splits[0]), curr)
            update_file_sizes(new_file)
            curr.children.append(new_file)
        else:
            raise Exception("how did we get here", curr.name, ls)

    return root

def update_file_sizes(node:Node):
    """
    bubbles up from the given node and updates file sizes
    for directories
    """
    curr = node 
    size_to_add = node.size 
    while curr.parent:
        curr.parent.size += size_to_add
        curr = curr.parent

def sum_cutoff_files(root:Directory, cutoff:int):
    """
    given a root `node`, returns the sum of sizes of nodes with 
    file sizes <= cutoff
    """
    curr = root 
    res = 0
    buffer = []
    for i in root.children:
        if isinstance(i, Directory):
            buffer.append(i)

    while buffer:
        curr = buffer.pop()
        if curr.size <= cutoff:
            res += curr.size

        for i in curr.children:
            if isinstance(i, Directory):
                buffer.append(i)

    return res

def solve():
    """
    """
    with open('7-input.txt', 'r') as f:
        text = f.read()

    root = to_tree(text)
    return sum_cutoff_files(root, 100000)


def closest_cutoff(root):
    """
    returns the directory that, once deleted, frees up enough space
    to add a file of certain size
    """
    min_space = root.size
    space_avail = 70_000_000 - root.size
    space_needed = 30_000_000 - space_avail
    curr = root 
    buffer = []
    for i in root.children:
        if isinstance(i, Directory):
            buffer.append(i)
    
    while buffer:
        curr = buffer.pop()
        if curr.size >= space_needed:
            min_space = min(curr.size, min_space)
        for i in curr.children:
            if isinstance(i, Directory):
                buffer.append(i)

    return min_space

def solve2():
    """
    """
    with open('7-input.txt', 'r') as f:
        text = f.read()

    root = to_tree(text)
    return closest_cutoff(root)
    

if __name__ == "__main__":
    print(solve())
    print(solve2())