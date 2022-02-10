# черные b
# белые w
# пешка p
# королева f
# слон s
# ладья l 
# конь h
# король k 
import pygame
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
        self.click_check=False
        self.white_color=255,255,255
        self.black_color=0,0,0
        self.side=True
        self.load_bp_img =  self.resize_figure(pygame.image.load("chess_game/img/bp.png"))
        self.load_wp_img = self.resize_figure(pygame.image.load("chess_game/img/wp.png"))
    def draw_table(self):
        pass

    def create_figures(self):
        for i in range(0,8):
            self.table[1][i]="bp"

        for i in range(0,8):
            self.table[6][i]="wp"
        
    def member_chose(self,mouse_pos):
        if self.click_check is False:
            self.check_figure(mouse_pos)
            print(self.click_check)
        elif self.click_check is True:   
            self.figure_move(mouse_pos)
            print(self.click_check)


    def check_figure(self,mouse_pos):
        if self.table[mouse_pos["y"]][mouse_pos["x"]] =="*":
            self.click_check = False

        else:
            self.figure_chosen = mouse_pos
            self.click_check = True

    def write_figure_on_desk(self,text,x1,y1,y2,x2):
        self.table[y1][x1]="*"
        self.table[y2][x2]=f"{text}"
        if self.side is False:
            self.side = True
        else:
            self.side = False

    def figure_move(self,mouse_pos):
        print("OK")

        self.click_check=False
        y1 = self.figure_chosen['y']
        x1 = self.figure_chosen['x']
        y2 = mouse_pos['y']
        x2 = mouse_pos['x']
        print(x1)
        if self.side == False:
            if "bp" in self.table[y1][x1] :

                if (x2 == x1 and  y1 < y2 <= y1+2 
                        and self.table[y2][x2] == '*' and 1 == y1):
                    self.write_figure_on_desk("bp",x1,y1,y2,x2)

                if (x2 == x1 and  y1 < y2 <= y1+1 
                        and self.table[y2][x2] == '*'):
                    self.write_figure_on_desk("bp",x1,y1,y2,x2)

                elif ((x1-1 == x2 or x2 == x1+1) and y1 < y2 <= y1+1 and 
                        "bp" != self.table[y2][x2]  != "*"):
                    self.write_figure_on_desk("bp",x1,y1,y2,x2)

        if self.side == True:
            if "wp" in self.table[y1][x1] :

                if (x2 == x1 and  y1 > y2 >= y1-2 
                        and self.table[y2][x2] == '*' and 6 == y1):
                    self.write_figure_on_desk("wp",x1,y1,y2,x2)

                if (x2 == x1 and  y1 > y2 >= y1-1 
                        and self.table[y2][x2] == '*'):
                    self.write_figure_on_desk("wp",x1,y1,y2,x2)

                elif ((x1-1 == x2 or x2 == x1+1) and y1 > y2 >= y1-1 and 
                        "wp" != self.table[y2][x2]  != "*"):
                    self.write_figure_on_desk("wp",x1,y1,y2,x2)
                
    def resize_figure(self,figure):
        return pygame.transform.scale(figure, (100, 100))
        
    def draw_figures(self,screen):
        white=0,0,255
        color_switch=False
        for i in range(0,8):
            for g in range(0,8): 
                if not color_switch :
                    color=(234,205,174)
                    color_switch=True
                else:
                    color=(189,109,60)
                    color_switch=False

                    pygame.draw.rect(
                        surface=screen,
                        color = color,
                        rect =(g*100,i*100,100,100)
                    )
                if g==7 and color_switch == False:
                    color_switch=True
                elif g==7 and color_switch == True:
                    color_switch=False
                    


        for i in range(0,8):
            for g in range(0,8):
                if self.table[i][g] != "*":
                    pos=((g*100)+100 -100 ,i*100+100-100)
                    
                    if "w" in self.table[i][g]:
                        side= self.load_wp_img

                    else:
                        side= self.load_bp_img

                    
                    screen.blit(side, self.load_bp_img.get_rect(topleft=pos))
                    #pygame.draw.circle(
                    #    surface = screen,
                    #    color = color,
                    #    center  = pos,
                    #    radius = 50
                    #)
        

a=Game()
a.create_figures()