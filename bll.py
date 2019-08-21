from model import *
import random


class LogicControlModel():
    def __init__(self):
        self.list_2048 = Model().read()

    def map_init(self):
        """
        初始化地图
        :return:
        """
        self.list_2048 = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.random_elem_insert()
        self.random_elem_insert()

        return self.list_2048

    def data_save(self,list_data):
        """数据存储"""
        Model().write(list_data)


    def game_over_judge(self):
        """游戏结束判定,return True 时游戏结束"""
        global game
        for r in range(4):
            for c in range(4):
                if self.list_2048[r][c] == 0:
                    return False
                if c < 3 and self.list_2048[r][c] == self.list_2048[r][c+1]:
                    return False
                if r < 3 and self.list_2048[r][c] == self.list_2048[r+1][c]:
                    return False

        return True

    def game_next(self):
        """
        继续游戏
        :return:
        """
        m = Model()
        self.list_2048 = eval(m.read())


    def move_left(self):
        """左移：先把0移至末尾；再相等的元素相加；再次把0移至末尾"""
        # 判断是否有元素移动旗标 Ture:有元素移动 False:无元素移动
        flag = False
        flag = self.zero_to_end(flag)
        flag = self.add(flag)
        flag = self.zero_to_end(flag)

        return flag

    def move_right(self):
        """右移：先反转每一行元素；再左移；再反转回来"""
        self.reverse_elem()
        flag =self.move_left()
        self.reverse_elem()

        return flag

    def move_up(self):
        """上移：先把列表每一列逆时针倒转成行，第一列成第一行；再左移；行转回列"""
        self.up_to_left()
        flag = self.move_left()
        self.left_to_up()

        return flag

    def move_down(self):
        """下移：先把列表每一列逆时针倒转成行；再右移；再把行转回列"""
        self.up_to_left()
        flag = self.move_right()
        self.left_to_up()

        return flag

    def random_num(self):
        """随机生成2(90%)或4(10%)"""
        num = random.randint(1,10)
        if num>1:
            num = 2
        else:
            num = 4
        return num

    def random_elem_insert(self):
        """遍历2048列表，如果有元素=0，把该元素的下标添加到一个新列表，
        遍历完后在新列表中随机取一组值，作为2048列表下标，将该元素的值改成随机生成的数字"""
        num = self.random_num()

        list_insert = []
        for r in range(4):
            for c in range(4):
                if self.list_2048[r][c] == 0:
                    list_insert.append([r,c])
        if list_insert:
            elem = random.randint(0,len(list_insert)-1)
            self.list_2048[list_insert[elem][0]][list_insert[elem][1]] = num

        else:
            return

    def zero_to_end(self,flag):
        """把0移动至每一行的末尾"""
        for r in range(4):
            for c in range(3, -1, -1):
                if (c > 0) and (self.list_2048[r][c-1] ==0 ) and (self.list_2048[r][c] !=0):
                    flag = True

                if self.list_2048[r][c] == 0:
                    del self.list_2048[r][c]
                    self.list_2048[r].append(0)

        return flag

    def add(self,flag):
        """把每一行相等的元素相加"""
        for r in range(4):
            for c in range(3):
                if self.list_2048[r][c] == self.list_2048[r][c + 1] and self.list_2048[r][c]!=0:
                    self.list_2048[r][c] *= 2
                    self.list_2048[r][c + 1] = 0
                    flag = True
        return flag

    def reverse_elem(self):
        """反转每一行的元素"""
        for r in range(4):
            self.list_2048[r].reverse()


    def up_to_left(self):
        """把向上移动变成向左移动，即把每一列的元素逆方向倒转成行"""
        list_new = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        for r in range(4):
            for c in range(4):
                 list_new[r][c]=self.list_2048[c][r]

        self.list_2048 = list_new

    def left_to_up(self):
        """移动后把行元素顺方向倒转回列元素"""
        list_new = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        for r in range(4):
            for c in range(4):
                list_new[c][r] = self.list_2048[r][c]
        self.list_2048 = list_new










if __name__ == '__main__':
    l = LogicControlModel()
    # l.list_2048 = [
    #     [4, 0, 0, 0],
    #     [2, 2, 0, 0],
    #     [4, 2, 2, 0],
    #     [4, 4, 2, 8]
    # ]
    # l.zero_to_end()
    # print(l.list_2048)
    #
    # l.add()
    # print(l.list_2048)
    #
    # l.zero_to_end()
    # print(l.list_2048)

    # 左移：
    # l.move_left()
    # print(l.list_2048)

    # 右移：
    # l.move_right()
    # print(l.list_2048)

    # 上移：
    # l.move_up()
    # print(l.list_2048)

    # 下移：
    # l.move_down()
    # print(l.list_2048)

    # 随机数：
    # l.random_elem()

    while True:
        test = input("输入：")
        if test == "1":
            l.move_left()
            l.random_elem_insert()
            l.random_elem_insert()
        if test == "2":
            l.move_right()
            l.random_elem_insert()
            l.random_elem_insert()
        if test == "3":
            l.move_up()
            l.random_elem_insert()
            l.random_elem_insert()
        if test == "4":
            l.move_down()
            l.random_elem_insert()
            l.random_elem_insert()
        print(l.list_2048)