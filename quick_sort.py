# There are different ways to do a Quick Sort partition, this implements the
# Hoare partition scheme. Tony Hoare also created the Quick Sort algorithm.
def partition(nums, low, high):  
    # We select the middle element to be the pivot. Some implementations select
    # the first element or the last element. Sometimes the median value becomes
    # the pivot, or a random one. There are many more strategies that can be
    # chosen or created.
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If an element at i (on the left of the pivot) is larger than the
        # element at j (on right right of the pivot), then swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):  
    # Create a helper function that will be called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)

# import modules
import xlrd
import time

#parse data from xlsx
random_list_of_nums = []
work_book = xlrd.open_workbook("random_data.xlsx")
sheet = work_book.sheet_by_index(0) 
for i in range(sheet.nrows) :
    random_list_of_nums.append(sheet.cell_value(i, 0))
print(random_list_of_nums)
     

#get initial start time
start = time.time()

# excecute function
quick_sort(random_list_of_nums)  
print(random_list_of_nums) 

#get time complexity
end = time.time()
print(end - start)

