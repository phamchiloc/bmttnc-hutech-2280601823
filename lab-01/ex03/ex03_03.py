def tao_tuple_tu_list(lst):
    return tuple(lst)


#nhập danh sách từ người dùng và chuỗi xử lý chuỗi
input_list = input ("nhập danh sách các số, cách nhau bằng dấu phẩy:")
numbers = list(map (int, input_list.split(',')))

# sử dụng hàm và in kết quả
my_tuple = tao_tuple_tu_list(numbers) 
print ("list :", numbers)
# in ra tuple
print ("tuple tu list:", my_tuple) 