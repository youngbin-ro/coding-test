from collections import defaultdict


def sock_merchant(arr):
    dic = defaultdict(int)
    count = 0
    for num in arr:
        dic[num] += 1
        if dic[num] % 2 == 0:
            dic[num] = 0
            count += 1
    return count


if __name__ == "__main__":
    arr_ = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    print(sock_merchant(arr_))
