class Utils:

    def assertTextfromList(self, mylist, target):
        for item in mylist:
            print(item.text)
            assert (item.text == target or item.text == "")
            print("assert passed")
