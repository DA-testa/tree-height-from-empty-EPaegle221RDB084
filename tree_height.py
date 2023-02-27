# python3

import sys
import threading

def compute_height(n, parents):
    nodes = [[] for _ in range(n)]
    
    for i, parent in enumerate(parents):
        if parent == -1:
            root = i
        else:
            nodes[parent].append(i)
    def get_height(node):
        if not nodes[node]:
            return 1
        else:
            heights = [get_height(child) for child in nodes[node]]
            return 1 + max(heights)      
    return get_height(root)

def main():
    input_type = input()

    if "f" in input_type:
        file_name = input()
        if ".a" in file_name:
                return
        with open(file_name) as f:
            lines = f.readlines()
            n = int(lines[0])
            parents = list(map(int, lines[1].split()))
            height = compute_height(n, parents)               
    elif  "i" in input_type:
        n = int(input())
        parents = list(map(int, input().split()))
        height = compute_height(n, parents)

    print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()