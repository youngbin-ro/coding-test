import sys
import time
import numpy as np

from typing import List


def insertion_sort(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        key = nums[i]
        for j in reversed(range(i)):
            if nums[j] > key:
                nums[j + 1] = nums[j]
            else:
                j += 1
                break
        nums[j] = key
    return nums


def selection_sort(nums: List[int]) -> List[int]:
    for i in range(len(nums) - 1):
        least_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[least_idx]:
                least_idx = j
        if least_idx != i:
            nums[i], nums[least_idx] = nums[least_idx], nums[i]
    return nums


def bubble_sort(nums: List[int]) -> List[int]:
    for end in reversed(range(len(nums))):
        for i in range(end):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
    return nums


def quick_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    pivot = nums[int(len(nums) // 2)]
    left, mid, right = [], [], []
    for num in nums:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)
    return quick_sort(left) + mid + quick_sort(right)


def merge_sort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums

    def merge(nums1, nums2):
        new = []
        min_idx1, min_idx2 = 0, 0
        while min_idx1 < len(nums1) and min_idx2 < len(nums2):
            min1, min2 = nums1[min_idx1], nums2[min_idx2]
            if min1 <= min2:
                new.append(min1)
                min_idx1 += 1
            else:
                new.append(min2)
                min_idx2 += 1

        if min_idx1 == len(nums1):
            new += nums2[min_idx2:]
        elif min_idx2 == len(nums2):
            new += nums1[min_idx1:]

        return new

    return merge(
        merge_sort(nums[:len(nums) // 2]),
        merge_sort(nums[len(nums) // 2:])
    )


def heap_sort(nums: List[int]) -> List[int]:

    def heapify(num_list, i, n):
        left = i * 2 + 1
        right = i * 2 + 2
        largest = i
        if left < n and num_list[left] > num_list[largest]:
            largest = left
        if right < n and num_list[right] > num_list[largest]:
            largest = right
        if largest != i:
            num_list[i], num_list[largest] = num_list[largest], num_list[i]
            heapify(num_list, largest, n)

    heap = nums
    for idx in range(len(heap) // 2 - 1, -1, -1):
        heapify(heap, idx, len(nums))

    for idx in range(len(heap) - 1, 0, -1):
        heap[0], heap[idx] = heap[idx], heap[0]
        heapify(heap, 0, idx)
    return heap


if __name__ == "__main__":
    nums_ = np.random.randint(0, 1e3, size=20000).tolist()
    #nums_ = [23, 66, 2, 1, 7, 23, 4, 32, 9, 9, 81, 3, 66]

    # INSERTION SORT
    start = time.time()
    nums_sorted = insertion_sort(nums_.copy())
    print("insertion sort processing time: {:.4f}".format(time.time() - start))
    nums_.sort()
    assert nums_sorted == nums_

    # SELECTION SORT
    start = time.time()
    nums_sorted = selection_sort(nums_.copy())
    print("selection sort processing time: {:.4f}".format(time.time() - start))
    nums_.sort()
    assert nums_sorted == nums_

    # BUBBLE SORT
    start = time.time()
    nums_sorted = bubble_sort(nums_.copy())
    print("bubble sort processing time: {:.4f}".format(time.time() - start))
    nums_.sort()
    assert nums_sorted == nums_
    
    # QUICK SORT
    sys.setrecursionlimit(10000)
    start = time.time()
    nums_sorted = quick_sort(nums_.copy())
    print("quick sort processing time: {:.4f}".format(time.time() - start))
    nums_.sort()
    assert nums_sorted == nums_
    
    # MERGE SORT
    start = time.time()
    nums_sorted = merge_sort(nums_.copy())
    print("merge sort processing time: {:.4f}".format(time.time() - start))
    nums_.sort()
    assert nums_sorted == nums_

    # HEAP SORT
    start = time.time()
    nums_sorted = heap_sort(nums_.copy())
    print("heap sort processing time: {:.4f}".format(time.time() - start))
    nums_.sort()
    assert nums_sorted == nums_
