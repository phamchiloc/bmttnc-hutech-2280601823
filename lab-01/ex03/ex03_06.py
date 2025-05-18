def xoa_phan_tu(dictionary, key):
    """
    Xoa phan tu co key tu dictionary
    :param dictionary: dictionary
    :param key: key
    :return: dictionary
    """
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
    
    
    #su dung ham va in ket qua
    my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    key_to_delete = 'b'
    result = xoa_phan_tu(my_dict, key_to_delete)
    if result:
        print("phần tử đã được xóa từ dictionary.", my_dict)
    else:
        print("không tìm thấy phần tử cần xóa trong dictionary.") 

    print("dictionary sau khi xóa:", my_dict)


