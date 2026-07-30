class Test:

    count = 0

    def __init__(self):
        Test.count += 1
        print("Constructor")
        
    def __del__(self):
        print("Destructor")
        
t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()

print("Reference Count:", Test.count)

del t1
del t3

print("Deleted t1 and t3")

del t2
del t4
print("Deleted t2 and t4")