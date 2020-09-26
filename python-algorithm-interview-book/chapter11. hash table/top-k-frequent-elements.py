import collections


def first_solution(nums, k):
    count = sorted(collections.Counter(nums).items(),
                   key=lambda x: x[1], reverse=True)
    return [count[i][0] for i in range(k)]


def second_solution(nums, k):
    return list(zip(*collections.Counter(nums).most_common(k)))[0]


if __name__ == "__main__":
    nums1, k1 = [1, 1, 1, 2, 2, 3], 2
    print(second_solution(nums1, k1))

    nums2, k2 = [1], 1
    print(second_solution(nums2, k2))
