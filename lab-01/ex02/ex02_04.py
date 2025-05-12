#tạo một danh sách rỗng để lưu kết quả 
j = []
#duyệt qua tất cả các số trong khoảng từ 2000 đến 3200, kiểm tra xem số i có chia hết cho 7 và không phải là bội của số 5 không 
for i in range (2000, 3200):
    if (i % 7 == 0 ) and (i % 5 != 0 ):
        j.append(str(i))
print (',' .join(j))