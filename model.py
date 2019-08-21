import os


class Model():
    def __init__(self):
        self.list_2048_data = []

    def read(self):
        if os.path.exists("data_2048.txt"):
            try:
                f = open("data_2048.txt", "r")
                self.list_2048_data = eval(f.read())
                f.close()
                return self.list_2048_data
            except:
                self.list_2048_data = [
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0],
                    [0, 0, 0, 0]
                ]

                return self.list_2048_data
        else:
            self.list_2048_data = [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ]
            return self.list_2048_data

    def write(self, list_update):
        file = open("data_2048.txt", "w")
        file.write(list_update)
        file.close()


if __name__ == '__main__':
    m = Model()
    test = m.read()
    print(test)
    print(test[2])
    test_list = [
        [2, 3, 2, 2],
        [0, 0, 0, 0],
        [3, 3, 3, 3],
        [0, 0, 0, 0]
    ]
    m.write(str(test_list))
