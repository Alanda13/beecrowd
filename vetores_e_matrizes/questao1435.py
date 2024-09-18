#Matriz quadrada I

def main():
    while True:
        x = int(input())
        if (x==0) : break

        for i in range(0, x):
            for j in range(0, x):

              if(i < x-i-1):
                  distL = i
              else:
                  distL = x-i-1

              if(j < x-j-1):
                  distC = j
              else:
                  distC = x - j - 1

              if(distC < distL):
                  dist = distC
              else:
                  dist = distL
              print("%3d" %(dist+1), end="")
              if (j != x-1):
                  print(end = " ")

            print()

        print()

main()