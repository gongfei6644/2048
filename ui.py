import tkinter
from bll import *


# game_over_flag = False

list_2048_now = []

class ViewModel(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(393, 580)
        self.minsize(393, 580)
        self.title("2048")
        self.control = LogicControlModel()
        self.game_over_flag = False
        self.game_start(False)


    def game_start(self, flag=True):
        if flag:
            self.frame.grid_forget()

            self.control.data_save(str(self.control.list_2048))
            self.game_over_flag = False

        self.frame = tkinter.Frame(self, relief="ridge", borderwidth=0)
        self.frame.grid(row=0, column=0)

        self.start_label1 = tkinter.Label(self.frame, text='      ', font=("宋体", 20))
        self.start_label2 = tkinter.Label(self.frame, text="2048", fg="black", font=("宋体", 80))
        self.start_label3 = tkinter.Label(self.frame, text='', font=("宋体", 30))

        self.start_btn1 = tkinter.Button(self.frame, text="继续游戏", bg="#D6D6D6", fg="black", font=("宋体", 40),
                                         command=self.load_map)
        self.start_label4 = tkinter.Label(self.frame, text='', font=("宋体", 10))
        self.start_btn2 = tkinter.Button(self.frame, text="重新开始", bg="#D6D6D6", fg="black", font=("宋体", 40),
                                         command=self.game_reset)
        self.start_label5 = tkinter.Label(self.frame, text='', font=("宋体", 10))
        self.start_btn3 = tkinter.Button(self.frame, text="退出游戏", bg="#D6D6D6", fg="black", font=("宋体", 40),
                                         command=self.game_exit)

        self.start_label1.grid(row=0, column=0)
        self.start_label2.grid(row=1, column=2)
        self.start_label3.grid(row=2, column=2)
        self.start_btn1.grid(row=3, column=2)
        self.start_label4.grid(row=4, column=2)
        self.start_btn2.grid(row=5, column=2)
        self.start_label5.grid(row=6, column=2)
        self.start_btn3.grid(row=7, column=2)

    def load_map(self,reset=False):

        self.frame.grid_forget()

        # global game_over_flag

        # if game_over_flag:
        #     self.control.list_2048 = self.control.map_init()
        #     game_over_flag = False
        if reset:
            self.control.list_2048 = self.control.map_init()
        global list_2048_now
        list_2048_now = self.control.list_2048

        self.frame = tkinter.Frame(self, relief="ridge", borderwidth=0)
        self.frame.grid(row=0, column=0)
        self.list_map = []
        for r in range(4):
            list_row = []
            for c in range(4):

                self.label = tkinter.Label(self.frame, text=self.control.list_2048[r][c],
                                           width=6, height=3, bg="#F0F090",
                                           fg="white", font=("黑体", 20))
                self.label.grid(row=r, column=c, padx=2, pady=2)
                list_row.append(self.label)
            self.list_map.append(list_row)
        self.elem_color()
        self.occupied = tkinter.Label(self.frame, text='', height=1)
        self.reset = tkinter.Button(self.frame, text="重新开始", width=8, height=1,
                                    fg="black", font=("黑体", 10), command=self.game_reset)
        self.exit = tkinter.Button(self.frame, text="退出游戏", width=8, height=1,
                                   fg="black", font=("黑体", 10), command=self.game_start)

        self.occupied.grid(row=4)
        self.reset.grid(row=5, column=1)
        self.exit.grid(row=5, column=2)

        self.key_event()

    def key_event(self):
        """监听上下左右键盘键"""
        self.bind("<KeyPress-Left>", self.left_key_down)
        self.bind("<KeyPress-Right>", self.right_key_down)
        self.bind("<KeyPress-Up>", self.up_key_down)
        self.bind("<KeyPress-Down>", self.down_key_down)

    def left_key_down(self, event):
        if self.game_over_flag == False:
            flag = self.control.move_left()
            if flag:
                self.control.random_elem_insert()
                self.control.random_elem_insert()
                self.up_date()

    def right_key_down(self, event):
        if self.game_over_flag == False:
            flag = self.control.move_right()
            if flag:
                self.control.random_elem_insert()
                self.control.random_elem_insert()
                self.up_date()

    def up_key_down(self, event):
        if self.game_over_flag == False:
            flag = self.control.move_up()
            if flag:
                self.control.random_elem_insert()
                self.control.random_elem_insert()
                self.up_date()

    def down_key_down(self, event):
        if self.game_over_flag == False:
            flag = self.control.move_down()
            if flag:
                self.control.random_elem_insert()
                self.control.random_elem_insert()
                self.up_date()

    def up_date(self):
        global game_over_flag
        for r in range(4):
            for c in range(4):
                if self.list_map[r][c]["text"] != self.control.list_2048[r][c]:
                    self.list_map[r][c].config(text=self.control.list_2048[r][c])

        self.elem_color()
        global list_2048_now
        list_2048_now = self.control.list_2048

        game = self.control.game_over_judge()
        if game:
            self.line1 = tkinter.Label(self.frame, text="Game Over", width=17,
                                       height=2, fg="red", font=("黑体", 30))
            self.line1.grid(row=0, column=0, rowspan=4, columnspan=4)

            list_2048_now=self.control.map_init()
            self.game_over_flag = True

    def elem_color(self):

        # 设置游戏中每个数据对应色块的颜色
        self.mapcolor = {
            0: ("#cdc1b4", "#776e65"),
            2: ("#eee4da", "#776e65"),
            4: ("#ede0c8", "#776e65"),
            8: ("#f2b179", "#f9f6f2"),
            16: ("#f59563", "#f9f6f2"),
            32: ("#f67c5f", "#f9f6f2"),
            64: ("#f65e3b", "#f9f6f2"),
            128: ("#edcf72", "#f9f6f2"),
            256: ("#edcc61", "#f9f6f2"),
            512: ("#e4c02a", "#f9f6f2"),
            1024: ("#e2ba13", "#f9f6f2"),
            2048: ("#ecc400", "#f9f6f2"),
            4096: ("#ae84a8", "#f9f6f2"),
            8192: ("#b06ca8", "#f9f6f2"),
            # ----其它颜色都与8192相同---------
            2 ** 14: ("#b06ca8", "#f9f6f2"),
            2 ** 15: ("#b06ca8", "#f9f6f2"),
            2 ** 16: ("#b06ca8", "#f9f6f2"),
            2 ** 17: ("#b06ca8", "#f9f6f2"),
            2 ** 18: ("#b06ca8", "#f9f6f2"),
            2 ** 19: ("#b06ca8", "#f9f6f2"),
            2 ** 20: ("#b06ca8", "#f9f6f2"),
        }
        for r in range(4):
            for c in range(4):
                number = self.list_map[r][c]['text']
                if number != '':
                    self.list_map[r][c]['bg'] = self.mapcolor[number][0]
                    self.list_map[r][c]['fg'] = self.mapcolor[number][1]
                if number == 0:
                    self.list_map[r][c]['text'] = ''

    def game_reset(self):
        self.game_over_flag = False

        self.frame.grid_forget()

        self.load_map(True)

    def game_exit(self):

        # global game_over_flag

        # if game_over_flag:
        # self.control.list_2048 = self.control.map_init()

        self.control.data_save(str(self.control.list_2048))
        self.quit()


root = ViewModel()

root.mainloop()

v =ViewModel()
if list_2048_now !=[]:
    v.control.data_save(str(list_2048_now))


