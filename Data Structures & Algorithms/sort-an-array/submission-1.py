import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def partition(arr, low, high):
            rand_idx = random.randint(low, high)
            arr[rand_idx], arr[high] = arr[high], arr[rand_idx]
            
            pivot = arr[high]
            i = low - 1

            for j in range(low, high):
                if arr[j] < pivot:
                    i += 1
                    swap(arr, i, j)
            
            swap(arr, i + 1, high)
            return i + 1
        
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
        
        def quick_sort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)

                quick_sort(arr, low, pi - 1)
                quick_sort(arr, pi + 1, high)
        
        quick_sort(nums, 0, len(nums) - 1)
        return nums