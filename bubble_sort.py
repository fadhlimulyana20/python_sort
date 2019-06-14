#function bubble sort
def bubble_sort(nums):  
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True

# import modules
import xlrd
import time

#parse data from xlsx
random_list_of_nums = []
work_book = xlrd.open_workbook("random_data.xlsx")
sheet = work_book.sheet_by_index(1) 
for i in range(sheet.nrows) :
    random_list_of_nums.append(sheet.cell_value(i, 0))
print(random_list_of_nums)
     

#get initial start time
start = time.time()

# excecute function
bubble_sort(random_list_of_nums)  
print(random_list_of_nums)

#get time complexity
end = time.time()
print(end - start)
