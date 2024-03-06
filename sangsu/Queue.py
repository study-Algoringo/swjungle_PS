class ListQueue:
    def __init__(self):
        self.my_list = list()

    def put(self, element):
        self.my_list.append(element)

    def get(self):
        return self.my_list.pop(0)

    def qsize(self):
        return len(self.my_list)