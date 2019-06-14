def insertion_sort(nums):  
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert


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
insertion_sort(random_list_of_nums)  
print(random_list_of_nums)  

#get time complexity
end = time.time()
print(end - start)
 
