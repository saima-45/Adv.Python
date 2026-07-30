class Test:

    count = 0

    def __init__(self):
        Test.count += 1


t1 = Test()
t2 = Test()
t3 = Test()

print("Objects Created:", Test.count)