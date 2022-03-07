import sys

count = int(sys.stdin.readline())
tile = [0] * (count+1)

if count <=2:
    print(1 if count==1 else 2)

else:

    tile[1] = 1
    tile[2] = 2


    for i in range(3, count+1):
        tile[i] = tile[i - 2] + tile[i - 1]

    print(tile[count]%10007)