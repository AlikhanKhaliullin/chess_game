# черные b
# белые w
# пешка p
# королева f
# слон s
# ладья l 
# конь h
# король k 
class Game:
    def __init__(self):
        self.table= [
            # 0   1   2   3   4   5   6   7 
            ["*","*","*","*","*","*","*","*"],#0
            ["*","*","*","*","*","*","*","*"],#1
            ["*","*","*","*","*","*","*","*"],#2
            ["*","*","*","*","*","*","*","*"],#3
            ["*","*","*","*","*","*","*","*"],#4
            ["*","*","*","*","*","*","*","*"],#5
            ["*","*","*","*","*","*","*","*"],#6
            ["*","*","*","*","*","*","*","*"],#7
        ]
        self.figure_chosen=None

    def draw_table(self):
        pass

    def create_figures(self):
        for i in range(0,8):
            self.table[1][i]="bp"

        for i in range(0,8):
            self.table[6][i]="wp"
        
    def member_chose(self,mouse_pos):
        
        if self.table[mouse_pos["y"]][mouse_pos["x"]] =="*":
            pass
        print(self.table[mouse_pos["y"]][mouse_pos["x"]] )
        self.figure_chosen = mouse_pos

    def member_move(self,x1,y1):
        
        if self.table[y1][x1] =="*":
            pass

        if "bp" in self.table[y1][x1] :
            if x2 == x1 and  y2 <= y1+2:
                print("yes")
                self.table[y1][x1]="*"
                self.table[y2][x2]="bp"
    
        if "wp" in self.table[y1][x1] :
            if x2 == x1 and  y2 >= y1-2:
                print("yes")
                self.table[y1][x1]="*"
                self.table[y2][x2]="wp"
        print(*self.table)
        
        

a=Game()
a.create_figures()