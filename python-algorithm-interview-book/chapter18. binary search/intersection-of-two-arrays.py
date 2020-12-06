from typing import List


def intersection1(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1.sort()
    nums2.sort()

    answer = set()
    p1, p2 = 0, 0
    while p1 < len(nums1) and p2 < len(nums2):
        num1, num2 = nums1[p1], nums2[p2]
        if num1 == num2:
            answer.add(num1)
            p1 += 1
            p2 += 1
        elif num1 < num2:
            p1 += 1
        else:
            p2 += 1
    return list(answer)


if __name__ == "__main__":
    nums1_, nums2_ = [1, 2, 2, 1], [2, 2]
    print(intersection(nums1_, nums2_))

    nums1_, nums2_ = [4, 9, 5], [9, 4, 9, 8, 4]
    print(intersection(nums1_, nums2_))
