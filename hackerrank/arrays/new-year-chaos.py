import heapq
import sys


def minimumBribes_(q):
    count = 0
    for idx, num in enumerate(q):
        change = idx - num + 1
        if change < -2:
            print("Too chaotic")
            return
        if change < 0:
            count += -change
        print(change)
    print(count)


def minimumBribes_(q):
    heap = []
    for idx, num in enumerate(q):
        change = idx - num + 1
        if change < -2:
            print("Too chaotic")
            return
        heapq.heappush(heap, (num, idx))

    count = 0
    while heap:
        num, idx = heapq.heappop(heap)
        if num != idx + 1:
            for tup_idx, tup in enumerate(heap):
                if tup[1] < idx:
                    heap[tup_idx] = (tup[0], tup[1] + 1)
            count += idx - num + 1
    print(count)


def minimumBribes_(q):
    count = 0
    for i, num in enumerate(q):
        if i - num + 1 < -2:
            print("Too chaotic")
            return
        for j in range(i):
            if q[j] > num:
                count += 1
    print(count)


def minimumBribes(q):
    count = 0
    mins = [sys.maxsize, sys.maxsize]
    for i, num in reversed(list(enumerate(q))):
        if i - num + 1 < -2:
            print("Too chaotic")
            return
        elif num > mins[1]:
            count += 2
        elif num > mins[0]:
            count += 1

        if num < mins[0]:
            mins = (num, mins[0])
        elif num < mins[1]:
            mins = (mins[0], num)

    print(count)


if __name__ == "__main__":
    q_ = [2, 1, 5, 3, 4]
    minimumBribes(q_)
    print('------------------------')

    q_ = [2, 5, 1, 3, 4]
    minimumBribes(q_)
    print('------------------------')

    q_ = [1, 2, 5, 3, 7, 8, 6, 4]
    minimumBribes(q_)
