def print_matrix(N):
    matrix = []
    for i in range(N):
        row = []
        for j in range(N):
            row.append(abs(i - j) + 1)
        matrix.append(row)
    
    for row in matrix:
        print(' '.join(f"{value:3}" for value in row))
    print()  # Linha em branco após a matriz

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    orders = list(map(int, data))
    
    for N in orders:
        if N == 0:
            break
        print_matrix(N)

if __name__ == "__main__":
    main()
