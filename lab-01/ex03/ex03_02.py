def dao_nguoc_list(lst):
    return lst[::-1]

#nhập danh sách từ người dùng và chuỗi xử lý chuỗi
input_list = input ("nhập danh sách các số, cách nhau bằng dấu phẩy:")
numbers = list(map (int, input_list.split(',')))

# sử dụng hàm và in kết quả
list_dao_nguoc = dao_nguoc_list(numbers)
print ("list sau khi đảo ngược :", list_dao_nguoc)