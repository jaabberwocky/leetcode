'''
Python implementation of MergeSort algorithm for learning purposes. Sorts integers in ascending order.
'''

import unittest
import math


class mergeSort:

    @staticmethod
    def sort(arr):
        '''
        Sorts an array using the MergeSort algorithm. Returns the sorted array.
        '''
        assert len(arr) > 0

        if len(arr) == 1:
            return arr
        else:
            return mergeSort.merge(mergeSort.sort(arr[:math.ceil(len(arr)/2)]), mergeSort.sort(arr[math.ceil(len(arr)/2):]))

    @staticmethod
    def isSorted(a):
        val = None
        for i in a:
            if val is None:
                val = i
            if i > val:
                val = i
            elif i == val:
                continue
            else:
                return False
        return True

    @staticmethod
    def merge(a, b):
        '''
        Merges two non-empty and sorted arrays a and b. Returns the merged and sorted array.
        '''

        assert len(a) > 0 and len(b) > 0
        assert mergeSort.isSorted(a) and mergeSort.isSorted(b)

        new = [None] * (len(a) + len(b))

        # i : index position for a
        # j : index position for b
        # k : index position for new
        i, j, k = 0, 0, 0

        while k < len(new):

            # check if i or j are exhausted
            # if so: populate the rest of the array with the non-exhausted array
            if i == len(a):
                new[k] = b[j]
                j += 1

            elif j == len(b):
                new[k] = a[i]
                i += 1

            # run the merge
            else:
                if a[i] < b[j]:
                    new[k] = a[i]
                    i += 1
                elif a[i] > b[j]:
                    new[k] = b[j]
                    j += 1
                else:
                    # always use array a when tied
                    new[k] = a[i]
                    i += 1
            k += 1
        return new


class TestMergeSort(unittest.TestCase):

    def testIsSorted(self):
        a = [1, 2, 3, 4, 5]
        self.assertTrue(mergeSort.isSorted(a))

    def testIsSorted2(self):
        a = [2, 6, 4, 1]
        self.assertFalse(mergeSort.isSorted(a))

    def testMerge1(self):
        a = [1, 4, 5]
        b = [2, 3, 6]
        self.assertEqual(mergeSort.merge(a, b), [1, 2, 3, 4, 5, 6])

    def testMerge2(self):
        a = [1]
        b = [2, 3, 4, 5]
        self.assertEqual(mergeSort.merge(a, b), [1, 2, 3, 4, 5])

    def testMerge3(self):
        a = [-1]
        b = [2, 3, 4, 5]
        self.assertEqual(mergeSort.merge(a, b), [-1, 2, 3, 4, 5])

    def testMerge4(self):
        a = [5, 6, 7]
        b = [2, 3, 4, 5]
        self.assertEqual(mergeSort.merge(a, b), [2, 3, 4, 5, 5, 6, 7])

    def testMerge5(self):
        a = [1, 1, 1]
        b = [1, 1, 1]
        self.assertEqual(mergeSort.merge(a, b), [1, 1, 1, 1, 1, 1])

    def testSort1(self):
        a = [1, 2, 3, 4, 5]
        self.assertEqual(mergeSort.sort(a), [1, 2, 3, 4, 5])

    def testSort2(self):
        a = [5, 4, 3, 2, 1]
        self.assertEqual(mergeSort.sort(a), [1, 2, 3, 4, 5])

    def testSort3(self):
        a = [5, 4, 3, 3, 2, 1]
        self.assertEqual(mergeSort.sort(a), [1, 2, 3, 3, 4, 5])

    def testSort4(self):
        a = [1, 1, 1, 1, 1, 1]
        self.assertEqual(mergeSort.sort(a), [1, 1, 1, 1, 1, 1])

    def testSort5(self):
        a = [6, 1, 3, 4, 5, 2]
        self.assertEqual(mergeSort.sort(a), [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
