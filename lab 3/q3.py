class FOS:

    class BCA_Dept:

        def total_admission(self):
            print("Department: BCA")
            print("Admission: 240")
            
        def BCA_info(self):
            print("Students: 240")
            print("Faculties: 10")
            
    class Chemistry_Dept:

        def total_admission(self):
            print("Department: Chemistry")
            print("Admission: 200")
            
    class Maths_Dept:

        def total_admission(self):
            print("Department: Maths")
            print("Admission: 150")
            
            
b = FOS.BCA_Dept()
c = FOS.Chemistry_Dept()
m = FOS.Maths_Dept()

b.total_admission()
c.total_admission()
m.total_admission()

b.BCA_info()