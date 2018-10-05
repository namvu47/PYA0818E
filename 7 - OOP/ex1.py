# class HinhChuNhat
class hinhchunhat:
    def __init__(self, chieudai, chieurong):
        self.Dai = chieudai
        self.Rong = chieurong

    def chuVi(self):
        return (self.Dai+self.Rong)*2

    def dienTich(self):
        return self.Dai*self.Rong

    def showInfo(self):
        return \
            'Chieu dai: ' + str(self.Dai), \
            'Chieu rong:'+ str( self.Rong), \
            'Chu vi: ' + str(self.chuVi()), \
            'Dien tich: ' + str(self.dienTich())

    def output(self, filename):
        with open(filename, 'w+') as f:
            f.write('\n'.join(self.showInfo()))

test = hinhchunhat(4,7)
print(test.showInfo())
# test.output('hcn.txt')





