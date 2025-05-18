from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if len(self.listSinhVien) > 0:
            maxId = self.listSinhVien[0]._id
            for i in self.listSinhVien:
                if (maxId < i._id):
                    maxId = i._id
            maxId += 1
        return maxId
    
    def SoLuongSinhVien(self):
        return self.listSinhVien.__len__()


    def NhapSinhVien(self):
        id = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(id, name, sex, major, diemTB)
        self.XepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        sv: SinhVien = self.findbyID(ID)
        if (sv != None):
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input ("Nhap nganh hoc sinh vien: ")
            diemTB = float(input("Nhap diem trung binh sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.XepLoaiHocLuc(sv)
        else:
            print("sinh viên có ID ={} không tồn tại : ",format(ID))

    def sortbyID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False) 
    
    def sortbyName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)
    

    def sortbyDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        searchResult = None
        if (self.SoLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult
    
    def findByName(self, keyword):
        listSV = []
        if (self.SoLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if(keyword.upper() in sv._name.upper()):
                    listSV.append(sv)
        return listSV
    

    def deleteSinhVien(self, ID):
        isDeleted = False
        sv = self.findByID(ID)
        if (sv != None):
            self.listSinhVien.remove(sv)
            isDeleted = True
        return isDeleted
    
    def XepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._HocLuc = "Gioi"
        elif (sv._diemTB >= 6.5):
            sv._HocLuc = "Kha"
        elif (sv._diemTB >= 5):
            sv._HocLuc = "Trung Binh"
        else:
            sv._HocLuc = "Yeu"


    def showSinhVien(self, listSV):
         print ("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format("ID", "Name", "sex", "major", "diemTB", "HocLuc"))

         if(listSV.__len__() > 0):
            for sv in listSV:
                print ("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._HocLuc))
                print("\n")
    
    def getListSinhVien(self):
        return self.listSinhVien

            