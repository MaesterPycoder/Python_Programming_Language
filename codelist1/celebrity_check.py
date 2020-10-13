import random as rd
def celeb_check(matrix):
    n=len(matrix)
    for i in range(n):
        eliminated=False
        for j in range(n):
            if not eliminated:
                if i==j:
                    continue
                if matrix[i][j] or not matrix[j][i]:
                    eliminated=True
        if not eliminated:
            return i+1


def main():
    matrix=[[rd.randint(0,1)]*5 for i in range(5)]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i==j:
                matrix[i][j]=1
            else:
                matrix[i][j]=rd.randint(0,1)
                matrix[j][i]=int(not matrix[i][j])
    for i in range(len(matrix)):
        print(matrix[i])
    celeb=celeb_check(matrix)
    if celeb:print(f"{celeb} is celebrity")
    else:print("No celebrity")

if __name__ == '__main__':
    for _ in range(50):
        main()
        print()
