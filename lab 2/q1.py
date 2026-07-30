class Test:

    def average(self, lst):
        avg = sum(lst) / len(lst)
        print("Average:", avg)
        return avg


t = Test()
t.average([10, 20, 30, 40, 50])