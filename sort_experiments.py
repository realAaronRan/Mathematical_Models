#!/usr/bin/python3

# -*- coding:utf-8 -*-
# @Time     : 2019/9/7 13:30
# @Author   : Aaron Ran
# @Email    : aaronran07@outlook.com
# @File     : sort_experiments.py
# @Software : PyCharm


from utils import profile

import random


# def heapify(arr: list, index: int) -> None:
#     """
#     Heapify the sub-array in the given array, which specified by index.
#
#     :param arr:
#     :param index:
#     :return:
#     """
#     root = index
#     left = 2*index+1
#     right = 2*(index+1)
#     length = len(arr)
#
#     max_num = arr[index]
#     if left < length and max_num < arr[left]:
#         max_num = arr[left]
#         root = left
#
#     if right < length and max_num < arr[right]:
#         max_num = arr[right]
#         root = right
#     arr[index], arr[root] = max_num, arr[index]
#     if root != index:
#         heapify(arr, root)
#
#
# def build_heap(arr):
#     for i in range(len(arr)//2-1, -1, -1):
#         heapify(arr, i)
#
#
# @profile
# def heap_sort(arr: list) -> list:
#     """
#     Sort the specified array by heap-sort method.
#
#     :param arr: input array to be sorted.
#     :return: sorted array
#     """
#     # build heap
#     build_heap(arr)
#     result = []
#     len_ = len(arr)
#     for i in range(len_-1):
#         arr[0], arr[-1] = arr[-1], arr[0]
#         result.append(arr.pop(-1))
#         heapify(arr, 0)
#     result.append(arr[0])
#     return result
def heapify(arr, index):
    left = 2*index + 1
    right = 2*(index + 1)
    max_num = arr[index]
    root = index

    if left < len(arr) and max_num < arr[left]:
        max_num = arr[left]
        root = left


    if right < len(arr) and max_num < arr[right]:
        max_num = arr[right]
        root = right

    if root != index:
        arr[index], arr[root] = max_num, arr[index]
        heapify(arr, root)


def bulid_heap(arr):
    length = len(arr)
    for i in range(length//2-1, -1, -1):
        heapify(arr, i)


def heap_sort(arr):
    bulid_heap(arr)
    result = []
    for i in range(len(arr)-1):
        arr[0], arr[-1] = arr[-1], arr[0]
        result.append(arr.pop(-1))
        heapify(arr, 0)
    result.append(arr[0])
    return result


def partion(arr, p, q):
    x = arr[q]
    i = p - 1
    for j in range(p, q):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[q] = arr[q], arr[i+1]
    return i+1


def quick_sort(arr, p, q):
    # if arr is None:
    #     return arr
    if p < q:
        m = partion(arr, p, q)
        quick_sort(arr, p, m-1)
        quick_sort(arr, m+1, q)


@profile
def foo(arr):
    quick_sort(arr, 0, len(arr)-1)
    return None


if __name__ == '__main__':
    # arr = [1, 7, 36, 10, 2, 74, 8, 3, 9, 13, 2, 7, 91, 4, 23]
    arr = list(range(1000))
    random.seed(100)
    random.shuffle(arr)
    # arr_1 = [2, 7, 10, 3, 4, 3, 5]
    # heapify(arr_1, 0)
    # print(arr_1)
    # heapify(arr, 2)
    # build_heap(arr)
    # result = heap_sort(arr)
    # foo(arr)
    result = heap_sort(arr)
    print(result)
