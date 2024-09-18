def print_matrix(N, matrix):
    for row in matrix:
        print("".join(str(x) for x in row))
    print()  

def generate_matrix(N):
    matrix = [[0] * N for _ in range(N)]

    center = N // 2
    third = N // 3

    for i in range(N):
        matrix[i][i] = 2  
        matrix[i][N - 1 - i] = 3  

    for i in range(third, N - third):
        for j in range(third, N - third):
            matrix[i][j] = 1

    matrix[center][center] = 4

    return matrix

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    for number in data:
        N = int(number)
        if N == 0:
            break
        matrix = generate_matrix(N)
        print_matrix(N, matrix)

if __name__ == "__main__":
    main()
