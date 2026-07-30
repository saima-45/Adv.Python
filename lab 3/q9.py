class BCA:

    def __init__(self, students):
        self.students = students
        
    def __add__(self, other):
        return BCA(self.students + other.students)
    
    def __str__(self):
        return "Total Students: " + str(self.students)
    
fybca = BCA(249)
sybca = BCA(240)
tybca = BCA(240)

print(fybca + sybca)
print(fybca + sybca + tybca)