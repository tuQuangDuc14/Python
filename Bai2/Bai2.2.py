class Ngay:
    def __init__(self, gtri_date, gtri_moth, gtri_year):
        self.ngay = gtri_date
        self.thang = gtri_moth
        self.nam = gtri_year

    #xac dinh so ngay cua thang
    @staticmethod
    def soNgayCuaThang(thang,nam):
        if(thang in [1,3,5,7,8,10,12]):
            return 31
        elif (thang in [4,6,9,11]):
            return 30
        elif(thang ==2):
            if(nam%400==0 or (nam%4==0 and nam%100 !=0)):
                return 28
            else:
                return 29

    def ngayTrongnam(self):
        gtringaytrongnam=0
        for x in range(1,self.thang):
            gtringaytrongnam += self.soNgayCuaThang(x,self.nam)
        gtringaytrongnam += self.ngay
        return gtringaytrongnam

ngaymuontim = Ngay(12,4,2012)
print(ngaymuontim.ngayTrongnam)