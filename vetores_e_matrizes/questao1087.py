def min_moves_dama(x1, y1, x2, y2):
    if x1 == x2 and y1 == y2:
        return 0
    elif x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
        return 1
    else:
        return 2

import sys
input = sys.stdin.read

def main():
    data = input().strip().split()
    index = 0
    results = []
    while True:
        x1 = int(data[index])
        y1 = int(data[index + 1])
        x2 = int(data[index + 2])
        y2 = int(data[index + 3])
        if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
            break
        results.append(min_moves_dama(x1, y1, x2, y2))
        index += 4
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
