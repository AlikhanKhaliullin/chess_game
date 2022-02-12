# черные b
# белые w
# пешка p
# королева q
# слон s
# ладья l 
# конь h
# король k  
import pygame
class Game:
    def __init__(self):
        self.table= [
            # 0   1   2   3   4   5   6   7 
            ["bh","*","*","*","*","*","*","bh"],#0
            ["*","*","*","*","*","*","*","*"],#1
            ["*","*","*","*","*","*","*","*"],#2
            ["*","*","*","*","*","*","*","*"],#3
            ["*","bl","*","*","wl","*","*","*"],#4
            ["*","*","*","*","*","*","*","*"],#5
            ["*","*","*","*","*","*","*","*"],#6
            ["wh","*","*","*","*","*","*","wh"],#7
        ]
        self.figure_chosen=None
        self.click_check=False
        self.white_color=255,255,255
        self.black_color=0,0,0
        self.side=True


    def check_figure(self,mouse_pos):
        if self.table[mouse_pos["y"]][mouse_pos["x"]] =="*":
            self.click_check = False

        else:
            self.figure_chosen = mouse_pos
            self.click_check = True

    
       
    def write_figures(self):
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

    def figure_move(self,mouse_pos):
            self.click_check=False
            self.p_rules(mouse_pos)
            self.l_rules(mouse_pos)
            self.h_rules(mouse_pos)

#---------------------RulesPart---------------------------------------
    def write_figure_on_desk(self,text,x1,y1,y2,x2):
        self.table[y1][x1]="*"
        self.table[y2][x2]=f"{text}"
        if self.side is False:
            self.side = True
        else:
            self.side = False

    def p_rules(self,mouse_pos):
        y1 = self.figure_chosen['y']
        x1 = self.figure_chosen['x']
        y2 = mouse_pos['y']
        x2 = mouse_pos['x']

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

    def l_rules(self,mouse_pos):
        y1 = self.figure_chosen['y']
        x1 = self.figure_chosen['x']
        if self.side == False:
            if "bl" in self.table[y1][x1] :
                self.rule_l_for_both_side(mouse_pos,"bl")

        elif self.side == True:
            if "wl" in self.table[y1][x1] :
                self.rule_l_for_both_side(mouse_pos,"wl")
            

    def rule_l_for_both_side(self,mouse_pos,text):
        y1 = self.figure_chosen['y']
        x1 = self.figure_chosen['x']
        y2 = mouse_pos['y']
        x2 = mouse_pos['x']
        if x1==x2 or y1==y2:
            if y2>y1:
                for i in range(y1+1,y2+1):
                    print(y1,y2,i)
                    if self.table[i][x1] != "*" and i==y2:
                        self.write_figure_on_desk(text,x1,y1,y2,x2)
                        break
                    if self.table[i][x1] != "*":
                        break
                    if i == y2:
                        self.write_figure_on_desk(text,x1,y1,y2,x2)
                     
            elif x2>x1:
                for i in range(x1+1,x2+1):
                    print(x1,x2,i)
                    if self.table[y1][i] != "*" and i==x2:
                        self.write_figure_on_desk(text,x1,y1,y2,x2)
                        break
                    if self.table[y1][i] != "*":
                        break
                    if i == x2:
                        self.write_figure_on_desk(text,x1,y1,y2,x2)
            elif y1>y2:
                g = y1
                while g > 0:
                    g-=1
                    if self.table[g][x1] != "*" and g==y2:
                        self.write_figure_on_desk(text,x1,y1,y2,x2)
                        break
                    if self.table[g][x1] != "*":
                        break
                    if g == y2:
                        self.write_figure_on_desk(text,x1,y1,y2,x2)
                     
            elif x1>x2:
                g = x1
                while g > 0:
                    g-=1
                    if self.table[y1][g] != "*" and g==x2:
                        self.write_figure_on_desk(text,x1,y1,y2,x2)
                        break
                    if self.table[y1][g] != "*":
                        break
                    if g == x2:
                        self.write_figure_on_desk(text,x1,y1,y2,x2)

    def h_rules(self,mouse_pos):
        y1 = self.figure_chosen['y']
        x1 = self.figure_chosen['x']
        y2 = mouse_pos['y']
        x2 = mouse_pos['x']
        if self.side == True:
            if "wh" in self.table[y1][x1]:
                if (y2 == y1+2 or y2 == y1-2) and (x2==x1+1 or x2 ==x1-1):
                    self.write_figure_on_desk("wh",x1,y1,y2,x2)
                elif (x2 == x1-2 or  x2 == x1+2) and (y2==y1+1 or y2 == y1-1):
                    self.write_figure_on_desk("wh",x1,y1,y2,x2)
        elif self.side == False:
            if "bh" in self.table[y1][x1]:
                if (y2 == y1+2 or y2 == y1-2) and (x2==x1+1 or x2 ==x1-1):
                    self.write_figure_on_desk("bh",x1,y1,y2,x2)
                elif (x2 == x1-2 or  x2 == x1+2) and (y2==y1+1 or y2 == y1-1):
                    self.write_figure_on_desk("bh",x1,y1,y2,x2)
#---------------------VisiblePart----------------------------------------
    def draw_figures(self,screen):
        self.draw_desk(screen)
        self.drawfigures_on_desk(screen)

    def resize_figure(self,figure):
        return pygame.transform.scale(figure, (100, 100))

    def draw_desk(self,screen):
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
    def load_img(self,name,pos):
        loaded_img = self.resize_figure(pygame.image.load(f"chess_game/img/{name}.png"))
        pos = loaded_img.get_rect(topleft=pos)
        return loaded_img , pos
    def drawfigures_on_desk(self,screen):
        for i in range(0,8):
            for g in range(0,8):
                if self.table[i][g] != "*":
                    pos=((g*100)+100 -100 ,i*100+100-100)
                    side, rect = self.load_img(self.table[i][g],pos )
                    

                    screen.blit(side,rect)
a=Game()
a.write_figures()