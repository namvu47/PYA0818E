# Managing Students

import statistics

class HocVien:
    def __init__(self, studentcode, name, mathgrade, physicsgrade, chemisgrade):
        self.studencode = studentcode
        self.name = name
        self.mathgrade = mathgrade
        self.physicsgrade = physicsgrade
        self. chemisgrade = chemisgrade

    def average(self):
       return  'Diem trung binh: ' + str(statistics.mean([self.mathgrade, self.physicsgrade, self.chemisgrade]))

    def tostring (self):
        return \
            'Ma hoc vien: ' + str(self.studencode), \
            'Ho ten: ' + str(self.name), \
            'Diem Toan: ' + str(self.mathgrade), \
            "Diem Ly: " + str (self.physicsgrade), \
            "Diem Hoa: " + str (self.chemisgrade)

    def output (self, filename):
        with open (filename, 'w+') as f:
            f.write ('\n'.join(self.tostring()))


hv1 = HocVien ('test1', 'Nguyen Van A', 9, 8, 8.5)
print (hv1.tostring(),'\n', hv1.average())
hv1.output('hocvien.txt')

