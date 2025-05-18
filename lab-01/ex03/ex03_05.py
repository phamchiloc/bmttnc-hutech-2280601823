def dem_so_lan_xuat_hien(list):
    """
    Dem so luong xuat hien cua cac phan tu trong list
    :param list: list
    :return: dict
    """
    count_dict = {}
    for item in list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    return count_dict

# Nhap tuple tu nguoi dung
input_string = input("Nhap danh sach cac tu bang cach nhau bang dau phay: ")
word_list = input_string.split()


#su dung ham va in ket qua

so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print("So luong xuat hien cua cac phan tu trong list:", so_lan_xuat_hien)