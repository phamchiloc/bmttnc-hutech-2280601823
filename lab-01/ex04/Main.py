from QuanLySinhVien import QuanLySinhVien


qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("***********************MENU***********************")
    @app.route('/api/vigenere/decrypt', methods = ['POST'])
    def Vigenere_decrypt():
        data = request.json
        cipher_text = data['cipher_text']
        key = data['key']
        decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
        return jsonify({'encrypted_text': decrypted_text})  # Sai key name    print("1.thêm sinh viên                               ***")
    print("2.cập nhật thông tin sinh viên bởi ID          ***")
    print("3.xóa sinh viên bơi ID                         ***")
    print("4.tìm kiếm sinh viên theo tên                  ***") 
    print("5.sắp xếp danh sách sinh viên theo điểm trung bình")
    print("6.sắp xếp danh sách sinh viên theo chuyên ngành***")
    print("7.hiển thị danh sách sinh viên                 ***")
    print("0.thoát  chương trình                          ***") 
    print("**************************************************")  



    key = int(input("nhập lựa chọn của bạn: "))
    if (key == 1):
        print("thêm sinh viên")
        qlsv.NhapSinhVien()
        print("thêm sinh viên thành công")
    elif (key == 2):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n2. cập nhật thông tin  sinh viên")
            print("nhập ID")
            ID = int(input())
            qlsv.updateSinhVien(ID)
        else:
            print("không có sinh viên nào trong danh sách")
    elif (key == 3):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n3. xóa sinh viên")
            print("nhập ID")
            ID = int(input())
            if (qlsv.deleteSinhVien(ID)):
                print("\n sinh viên có id = ", ID, " đã được xóa")
            else:
                print("\n sinh viên có id = ", ID, " không tồn tại")
        else:
            print("không có sinh viên nào trong danh sách")


    elif (key == 4):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n4. tìm kiếm sinh viên theo tên")
            print ("nhập tên sinh viên cần tìm: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("không có sinh viên nào trong danh sách")
    elif (key == 5):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n5. sắp xếp danh sách sinh viên theo điểm trung bình(GPA)")
            qlsv.sortbyDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("không có sinh viên nào trong danh sách")


    elif (key == 6):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n6. sắp xếp danh sách sinh viên theo tên")
            qlsv.sortbyName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("không có sinh viên nào trong danh sách")

    elif (key == 7):
        if (qlsv.SoLuongSinhVien() > 0):
            print("\n7. hiển thị danh sách sinh viên")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("không có sinh viên nào trong danh sách")

    elif (key == 0):
        print("thoát chương trình")
        break
    else:
        print("nhập không hợp lệ, vui lòng nhập lại")
        print("hãy chọn lại chức năng trong menu")
