def selection_sort(nums):  
    # This value of i corresponds to how many values were sorted
    for i in range(len(nums)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


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
selection_sort(random_list_of_nums)  
print(random_list_of_nums)  
#get time complexity
end = time.time()
print(end - start)

