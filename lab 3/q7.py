class Test:

    def __init__(self):
        print("Constructor")
        
    def __del__(self):
        print("Destructor")
        
lst = [Test(), Test(), Test(), Test()]

del lst
