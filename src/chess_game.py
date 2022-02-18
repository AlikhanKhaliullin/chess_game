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
            ["bl","bh","bs","bq","bk","bs","bh","bl"],#0
            ["*","*","*","*","*","*","*","*"],#1
            ["*","*","*","*","*","*","*","*"],#2
            ["*","*","*","*","*","*","*","*"],#3
            ["*","*","*","*","wk","*","*","*"],#4
            ["*","*","*","*","*","*","*","*"],#5
            ["*","*","*","*","*","*","*","*"],#6
            ["wl","wh","ws","wq","wk","ws","wh","wl"],#7
        ]
        self.figure_chosen = None
        self.click_check = False
        self.white_color = 255,255,255
        self.black_color = 0,0,0
        self.side = True


    def check_figure(self, mouse_pos):
        if self.table[mouse_pos["y"]][mouse_pos["x"]] == "*":
            self.click_check = False

        else:
            self.figure_chosen = mouse_pos
            self.click_check = True

    
       
    def write_figures(self):
        for i in range(0,8):
            self.table[1][i] = "bp"

        for i in range(0,8):
            self.table[6][i] = "wp"

    def free_fire(self, mouse_pos):
        y1, x1, y2, x2= self.pos_fig(mouse_pos)
        if self.table[y1][x1][0] in self.table[y2][x2]:
            self.click_check = False
            return False
        return True

    def member_chose(self, mouse_pos):
        if self.click_check is False:
            self.check_figure(mouse_pos)
            print(self.click_check)
            
        elif self.click_check is True:
            if self.free_fire(mouse_pos):
                self.figure_move(mouse_pos)
            print(self.click_check)

    def figure_move(self, mouse_pos):
            self.click_check=False
            if "p" in self.table[self.figure_chosen['y']][self.figure_chosen['x']]:
                self.p_rules(mouse_pos)

            if "l" in self.table[self.figure_chosen['y']][self.figure_chosen['x']]:
                self.l_rules(mouse_pos,"l")

            if "h" in self.table[self.figure_chosen['y']][self.figure_chosen['x']]:
                self.h_rules(mouse_pos)

            if "s" in self.table[self.figure_chosen['y']][self.figure_chosen['x']]:
                self.s_rules(mouse_pos, "s")
            
            if "q" in self.table[self.figure_chosen['y']][self.figure_chosen['x']]:
                self.q_rules(mouse_pos, "q")

            if "k" in self.table[self.figure_chosen['y']][self.figure_chosen['x']]:
                self.k_rules(mouse_pos, "k")

#---------------------RulesPart---------------------------------------
    def write_figure_on_desk(self, text, x1, y1, y2, x2):
        self.table[y1][x1] = "*"
        self.table[y2][x2] = f"{text}"
        if self.side is False:
            self.side = True

        else:
            self.side = False

    def pos_fig(self, mouse_pos):
        y1 = self.figure_chosen['y']
        x1 = self.figure_chosen['x']
        y2 = mouse_pos['y']
        x2 = mouse_pos['x']
        return y1, x1, y2, x2

    def p_rules(self, mouse_pos):
        y1, x1, y2, x2= self.pos_fig(mouse_pos)

        if self.side == False:
            if "bp" in self.table[y1][x1] :
                if (x2 == x1 and  y1 < y2 <= y1+2 
                        and self.table[y2][x2] == '*' and 1 == y1):
                    self.write_figure_on_desk("bp", x1, y1, y2, x2)

                if (x2 == x1 and  y1 < y2 <= y1+1 
                        and self.table[y2][x2] == '*'):
                    self.write_figure_on_desk("bp", x1, y1, y2, x2)

                elif ((x1-1 == x2 or x2 == x1+1) and y1 < y2 <= y1+1 and 
                        "bp" != self.table[y2][x2]  != "*"):
                    self.write_figure_on_desk("bp", x1, y1, y2, x2)

        if self.side == True:
            if "wp" in self.table[y1][x1] :
                if (x2 == x1 and  y1 > y2 >= y1-2 
                        and self.table[y2][x2] == '*' and 6 == y1):
                    self.write_figure_on_desk("wp", x1, y1, y2, x2)

                if (x2 == x1 and  y1 > y2 >= y1-1 
                        and self.table[y2][x2] == '*'):
                    self.write_figure_on_desk("wp", x1, y1, y2, x2)

                elif ((x1-1 == x2 or x2 == x1+1) and y1 > y2 >= y1-1 and 
                        "wp" != self.table[y2][x2]  != "*"):
                    self.write_figure_on_desk("wp", x1, y1, y2, x2)

    def l_rules(self, mouse_pos, text):
        y1,x1,y2,x2= self.pos_fig(mouse_pos)
        if self.side == False:
            if f"b{text}" in self.table[y1][x1] :
                self.rule_l_for_both_side(mouse_pos, f"b{text}")

        elif self.side == True:
            if f"w{text}" in self.table[y1][x1] :
                self.rule_l_for_both_side(mouse_pos, f"w{text}")
            
    def q_rules(self, mouse_pos, text):
        y1, x1, y2, x2= self.pos_fig(mouse_pos)
        
        if self.side == False:
            if f"b{text}" in self.table[y1][x1] :
                self.rule_l_for_both_side(mouse_pos, f"b{text}")
                self.rule_s_for_both_side(mouse_pos, f"b{text}")


        elif self.side == True:
            if f"w{text}" in self.table[y1][x1] :
                self.rule_l_for_both_side(mouse_pos, f"w{text}")
                self.rule_s_for_both_side(mouse_pos, f"w{text}")

    def k_rules(self, mouse_pos, text):
        y1, x1, y2, x2= self.pos_fig(mouse_pos)

        if self.side == True:
            print("OK")
            if "wk" in self.table[y1][x1] and "w" not in  self.table[y2][x2]:
                if (x1 <= x2 <= x1 + 1 or x1 >= x2 >= x2 - 1) and (y1 <= y2 <= y1 + 1 or y1 >=  y2 >= y1 -1 ):
                    self.write_figure_on_desk(f"w{text}", x1, y1, y2, x2)
            
        if self.side == False:
            if "bk" in self.table[y1][x1] and "b" not in  self.table[y2][x2]:
                if (x1 <= x2 <= x1 + 1 or x1 >= x2 >= x2 - 1) and (y1 <= y2 <= y1 + 1 or y1 >=  y2 >= y1 -1 ):
                    self.write_figure_on_desk(f"b{text}", x1, y1, y2, x2)


    def rule_l_for_both_side(self,mouse_pos,text):
        y1, x1, y2, x2= self.pos_fig(mouse_pos)

        if x1==x2 or y1==y2:
            if y2>y1:
                for i in range(y1+1, y2+1):
                    print(y1,y2,i)
                    if self.table[i][x1] != "*" and i==y2:
                        self.write_figure_on_desk(text, x1, y1, y2, x2)
                        break

                    if self.table[i][x1] != "*":
                        break

                    if i == y2:
                        self.write_figure_on_desk(text, x1, y1, y2, x2)
                     
            elif x2>x1:
                for i in range(x1+1, x2+1):
                    print(x1, x2, i)
                    if self.table[y1][i] != "*" and i==x2:
                        self.write_figure_on_desk(text, x1, y1, y2, x2)
                        break

                    if self.table[y1][i] != "*":
                        break

                    if i == x2:
                        self.write_figure_on_desk(text, x1, y1, y2, x2)
            elif y1>y2:
                g = y1
                while g > 0:
                    g-=1
                    if self.table[g][x1] != "*" and g==y2:
                        self.write_figure_on_desk(text, x1, y1, y2, x2)
                        break

                    if self.table[g][x1] != "*":
                        break

                    if g == y2:
                        self.write_figure_on_desk(text, x1, y1, y2, x2)
                     
            elif x1>x2:
                g = x1
                while g > 0:
                    g-=1
                    if self.table[y1][g] != "*" and g==x2:
                        self.write_figure_on_desk(text, x1, y1, y2, x2)
                        break

                    if self.table[y1][g] != "*":
                        break

                    if g == x2:
                        self.write_figure_on_desk(text, x1, y1, y2, x2)

    def h_rules(self,mouse_pos):
        y1,x1,y2,x2= self.pos_fig(mouse_pos)

        if self.side == True:
            if "wh" in self.table[y1][x1] and "w" not in  self.table[y2][x2]:
                if (y2 == y1+2 or y2 == y1-2) and (x2 == x1+1 or x2 == x1-1):
                    self.write_figure_on_desk("wh", x1, y1, y2, x2)

                elif (x2 == x1-2 or  x2 == x1+2) and (y2 == y1+1 or y2 == y1-1):
                    self.write_figure_on_desk("wh", x1, y1, y2, x2)

        elif self.side == False:
            if "bh" in self.table[y1][x1] and "b" not in self.table[y2][x2]:
                if (y2 == y1+2 or y2 == y1-2) and (x2 == x1+1 or x2 == x1-1):
                    self.write_figure_on_desk("bh", x1, y1, y2, x2)

                elif (x2 == x1-2 or  x2 == x1+2) and (y2==y1+1 or y2 == y1-1):
                    self.write_figure_on_desk("bh", x1, y1, y2, x2)

    def s_rules(self,mouse_pos,text):
        y1, x1, y2, x2= self.pos_fig(mouse_pos)
        if self.side == False:
            if f"b{text}" in self.table[y1][x1] :
                self.rule_s_for_both_side(mouse_pos, f"b{text}")

        elif self.side == True:
            if f"w{text}" in self.table[y1][x1] :
                self.rule_s_for_both_side(mouse_pos, f"w{text}")

    def rule_s_for_both_side(self,mouse_pos,text):
        y1,x1,y2,x2= self.pos_fig(mouse_pos)
        if abs(x1 - x2) == abs(y1 - y2):
            if x1 < x2 and y1 < y2:
                while x1<x2:
                    y1 += 1
                    x1 += 1
                    if x1 == x2: 
                        self.write_figure_on_desk(text, 
                            x1 = self.figure_chosen["x"],
                            y1 = self.figure_chosen["y"],
                            y2 = y2,
                            x2 = x2)

                    if self.table[y1][x1] != "*":
                        break

            if x1 < x2 and y1 > y2:
                while x1<x2:
                    y1-=1
                    x1+=1
                    if x1 == x2: 
                        self.write_figure_on_desk(text, 
                            x1 = self.figure_chosen["x"],
                            y1 = self.figure_chosen["y"],
                            y2 = y2,
                            x2 = x2)

                    if self.table[y1][x1] != "*":
                        break
            
            if x1 > x2 and y1 > y2:
                print("1")
                while x2<x1:
                    y1-=1
                    x1-=1
                    if x1 == x2: 
                        self.write_figure_on_desk(text, 
                            x1 = self.figure_chosen["x"],
                            y1 = self.figure_chosen["y"],
                            y2 = y2,
                            x2 = x2)

                    if self.table[y1][x1] != "*":
                        break

            if x1 > x2 and y1 < y2:
                while x2<x1:
                    y1+=1
                    x1-=1
                    if x1 == x2: 
                        self.write_figure_on_desk(text, 
                            x1 = self.figure_chosen["x"],
                            y1 = self.figure_chosen["y"],
                            y2 = y2,
                            x2 = x2)

                    if self.table[y1][x1] != "*":
                        break
#---------------------VisiblePart----------------------------------------
    def draw_figures(self,screen):        
        self.draw_desk(screen)
        self.drawfigures_on_desk(screen)
        if self.click_check == True:
            self.draw_help_cyrcles(screen)

    def draw_help_cyrcles(self,screen):
        x = self.figure_chosen["x"]
        y = self.figure_chosen["y"]
        if "p" in self.table[y][x]:
            self.draw_p(screen,x,y)

        if "l" in self.table[y][x]:
            self.draw_l(screen, x, y)

        if "s" in self.table[y][x]:    
            self.draw_s(screen, x, y)
        
        if "h" in self.table[y][x]:    
            self.draw_h(screen, x, y)

        if "q" in self.table[y][x]:    
            self.draw_l(screen, x, y)
            self.draw_s(screen, x, y)
        if "k" in self.table[y][x]: 
            self.draw_k(screen, x, y)
    def draw_cyrcles(self, screen, color, pos):
        pygame.draw.circle(screen, color, pos, 10)
#----------------------------------------------------------------
    def draw_k(self, screen, x, y):
        if "b" in self.table[y][x]:
            for i in range(y+1,y+2):
                pos = (x*100+50, i*100+50)
                if self.table[i][x] != "*":
                    if "w" in self.table[i][x]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)
            
            for i in range(y-1,y-2,-1):
                pos = (x*100+50, i*100+50)
                if self.table[i][x] != "*":
                    if "w" in  self.table[i][x]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)

            for i in range(x+1,x+2):
                pos = (i*100+50, y*100+50)
                if self.table[y][i] != "*":
                    if "w" in self.table[y][i]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)

            for i in range(x-1,x-2,-1):
                pos = (i*100+50, y*100+50)
                if self.table[y][i] != "*":
                    if "w" in self.table[y][i]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)
            
        if "w" in self.table[y][x]:
            for i in range(y+1,y+2):
                pos = (x*100+50, i*100+50)
                if self.table[i][x] != "*":
                    if "b" in self.table[i][x]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)
            
            for i in range(y-1,y-2,-1):
                pos = (x*100+50, i*100+50)
                if self.table[i][x] != "*":
                    if "b" in  self.table[i][x]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)

            for i in range(x+1,x+2):
                pos = (i*100+50, y*100+50)
                if self.table[y][i] != "*":
                    if "b" in self.table[y][i]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)

            for i in range(x-1,x-2,-1):
                pos = (i*100+50, y*100+50)
                if self.table[y][i] != "*":
                    if "b" in self.table[y][i]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)
            

    def draw_p(self,screen,x,y):
        if "w" in self.table[y][x]:
            if y == 6 and self.table[y-1][x] == "*":
                for i in range(y-1,y-3,-1):
                    pos = (x*100+50, i*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)

            try:
                if ("b" in self.table[y-1][x+1] !=  "*" ):
                    pos = ((x+1)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass

            try:
                if ("b" in self.table[y-1][x-1] != "*"):
                    pos = ((x-1)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass

            if self.table[y-1][x] == "*":
                    pos = (x*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
        
        if "b" in self.table[y][x]:
            print(y)
            if y == 1 and self.table[y+1][x] == "*":
                for i in range(y+1,y+3,1):
                    pos = (x*100+50, i*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)

            try:
                if ("w" in self.table[y+1][x+1] !=  "*" ):
                    pos = ((x+1)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
            
            try:
                if ("w" in self.table[y+1][x-1] != "*"):
                    pos = ((x-1)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass

            if self.table[y+1][x] == "*":
                    pos = (x*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)

    def draw_l(self,screen, x, y):
        if "b" in self.table[y][x]:
            for i in range(y+1,8):
                pos = (x*100+50, i*100+50)
                if self.table[i][x] != "*":
                    if "w" in self.table[i][x]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)
            
            for i in range(y-1,0,-1):
                pos = (x*100+50, i*100+50)
                if self.table[i][x] != "*":
                    if "w" in  self.table[i][x]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)

            for i in range(x+1,8):
                pos = (i*100+50, y*100+50)
                if self.table[y][i] != "*":
                    if "w" in self.table[y][i]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)

            for i in range(x-1,-1,-1):
                pos = (i*100+50, y*100+50)
                if self.table[y][i] != "*":
                    if "w" in self.table[y][i]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)
        
        if "w" in self.table[y][x]:
            for i in range(y+1,8):
                pos = (x*100+50, i*100+50)
                if self.table[i][x] != "*":
                    if "b" in self.table[i][x]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)
            
            for i in range(y-1,0,-1):
                pos = (x*100+50, i*100+50)
                if self.table[i][x] != "*":
                    if "b" in  self.table[i][x]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)

            for i in range(x+1,8):
                pos = (i*100+50, y*100+50)
                if self.table[y][i] != "*":
                    if "b" in self.table[y][i]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)

            for i in range(x-1,-1,-1):
                pos = (i*100+50, y*100+50)
                if self.table[y][i] != "*":
                    if "b" in self.table[y][i]:
                        self.draw_cyrcles(screen, (255,0,0), pos)
                    break
                
                self.draw_cyrcles(screen, (255,255,0), pos)

    def draw_s(self, screen, x, y):
        x1 = x
        y1 = y
        if "b" in self.table[y][x]:
            while True:
                x1 += 1
                y1 += 1
                pos = (x1*100+50, y1*100+50)
                if x1 == 8 :
                    break
                try:
                    if self.table[y1][x1] != "*" :
                        if "w" in self.table[y1][x1]:
                           self.draw_cyrcles(screen, (255,0,0), pos)
                        break
                except:
                    break
                self.draw_cyrcles(screen, (255,255,0), pos)
            x1 = x
            y1 = y
            while True:
                x1 += 1
                y1 -= 1
                pos = (x1*100+50, y1*100+50)
                if x1 == 8 :
                    break

                try:
                    if self.table[y1][x1] != "*" :
                        if "w" in self.table[y1][x1]:
                           self.draw_cyrcles(screen, (255,0,0), pos)
                        break
                except:
                    break
                self.draw_cyrcles(screen, (255,255,0), pos)

            x1 = x
            y1 = y
            while True:
                x1 -= 1
                y1 -= 1
                pos = (x1*100+50, y1*100+50)
                if x1 == 8 :
                    break

                try:
                    if self.table[y1][x1] != "*" :
                        if "w" in self.table[y1][x1]:
                           self.draw_cyrcles(screen, (255,0,0), pos)
                        break
                except:
                    break
                self.draw_cyrcles(screen, (255,255,0), pos)
            
            x1 = x
            y1 = y
            while True:
                x1 -= 1
                y1 += 1
                pos = (x1*100+50, y1*100+50)
                if x1 == 8 :
                    break

                try:
                    if self.table[y1][x1] != "*" :
                        if "w" in self.table[y1][x1]:
                           self.draw_cyrcles(screen, (255,0,0), pos)
                        break
                except:
                    break
                self.draw_cyrcles(screen, (255,255,0), pos)

        if "w" in self.table[y][x]:
            while True:
                x1 += 1
                y1 += 1
                pos = (x1*100+50, y1*100+50)
                if x1 == 8 :
                    break
                try:
                    if self.table[y1][x1] != "*" :
                        if "b" in self.table[y1][x1]:
                           self.draw_cyrcles(screen, (255,0,0), pos)
                        break
                except:
                    break
                self.draw_cyrcles(screen, (255,255,0), pos)
            x1 = x
            y1 = y
            while True:
                x1 += 1
                y1 -= 1
                pos = (x1*100+50, y1*100+50)
                if x1 == 8 :
                    break

                try:
                    if self.table[y1][x1] != "*" :
                        if "b" in self.table[y1][x1]:
                           self.draw_cyrcles(screen, (255,0,0), pos)
                        break
                except:
                    break
                self.draw_cyrcles(screen, (255,255,0), pos)

            x1 = x
            y1 = y
            while True:
                x1 -= 1
                y1 -= 1
                pos = (x1*100+50, y1*100+50)
                if x1 == 8 :
                    break

                try:
                    if self.table[y1][x1] != "*" :
                        if "b" in self.table[y1][x1]:
                           self.draw_cyrcles(screen, (255,0,0), pos)
                        break
                except:
                    break
                self.draw_cyrcles(screen, (255,255,0), pos)
            
            x1 = x
            y1 = y
            while True:
                x1 -= 1
                y1 += 1
                pos = (x1*100+50, y1*100+50)
                if x1 == 8 :
                    break

                try:
                    if self.table[y1][x1] != "*" :
                        if "b" in self.table[y1][x1]:
                           self.draw_cyrcles(screen, (255,0,0), pos)
                        break
                except:
                    break
                self.draw_cyrcles(screen, (255,255,0), pos)

    def draw_h(self, screen, x, y):
        if "b" in self.table[y][x]:
            
            try:
                if self.table[y+2][x-1]  == "*":
                    pos = ((x-1)*100+50, (y+2)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass

            try:
                if self.table[y+2][x+1]  == "*":
                    pos = ((x+1)*100+50, (y+2)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass

            try:
                if self.table[y-2][x-1]  == "*":
                    pos = ((x-1)*100+50, (y-2)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass

            try:
                if self.table[y-2][x+1]  == "*":
                    pos = ((x+1)*100+50, (y-2)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass
            
            try:
                if self.table[y-1][x+2]  == "*":
                    pos = ((x+2)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass
            
            try:
                if self.table[y+1][x+2]  == "*":
                    pos = ((x+2)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass
            
            try:
                if self.table[y-1][x-2]  == "*":
                    pos = ((x-2)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass
            
            try:
                if self.table[y+1][x-2]  == "*":
                    pos = ((x-2)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass

            try:
                if "w" in self.table[y+2][x-1]:
                    pos = ((x-1)*100+50, (y+2)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass


            try:
                if "w" in self.table[y+2][x+1]:
                    pos = ((x+1)*100+50, (y+2)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass


            try:
                if "w" in self.table[y-2][x-1]:
                    pos = ((x-1)*100+50, (y-2)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass


            try:
                if "w" in self.table[y-2][x+1]:
                    pos = ((x+1)*100+50, (y-2)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
 
            
            try:
                if "w" in self.table[y-1][x+2]:
                    pos = ((x+2)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
 
            
            try:
                if "w" in self.table[y+1][x+2]:
                    pos = ((x+2)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
 
            
            try:
                if "w" in self.table[y-1][x-2]:
                    pos = ((x-2)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
 
            
            try:
                if "w" in self.table[y+1][x-2]:
                    pos = ((x-2)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
        
        if "w" in self.table[y][x]:
            
            try:
                if self.table[y+2][x-1]  == "*":
                    pos = ((x-1)*100+50, (y+2)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass

            try:
                if self.table[y+2][x+1]  == "*":
                    pos = ((x+1)*100+50, (y+2)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass

            try:
                if self.table[y-2][x-1]  == "*":
                    pos = ((x-1)*100+50, (y-2)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass

            try:
                if self.table[y-2][x+1]  == "*":
                    pos = ((x+1)*100+50, (y-2)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass
            
            try:
                if self.table[y-1][x+2]  == "*":
                    pos = ((x+2)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass
            
            try:
                if self.table[y+1][x+2]  == "*":
                    pos = ((x+2)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass
            
            try:
                if self.table[y-1][x-2]  == "*":
                    pos = ((x-2)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass
            
            try:
                if self.table[y+1][x-2]  == "*":
                    pos = ((x-2)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,255,0), pos)
            except:
                pass

            try:
                if "b" in self.table[y+2][x-1]:
                    pos = ((x-1)*100+50, (y+2)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass


            try:
                if "b" in self.table[y+2][x+1]:
                    pos = ((x+1)*100+50, (y+2)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass


            try:
                if "b" in self.table[y-2][x-1]:
                    pos = ((x-1)*100+50, (y-2)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass


            try:
                if "b" in self.table[y-2][x+1]:
                    pos = ((x+1)*100+50, (y-2)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
 
            
            try:
                if "b" in self.table[y-1][x+2]:
                    pos = ((x+2)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
 
            
            try:
                if "b" in self.table[y+1][x+2]:
                    pos = ((x+2)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
 
            
            try:
                if "b" in self.table[y-1][x-2]:
                    pos = ((x-2)*100+50, (y-1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass
 
            
            try:
                if "b" in self.table[y+1][x-2]:
                    pos = ((x-2)*100+50, (y+1)*100+50)
                    self.draw_cyrcles(screen, (255,0,0), pos)
            except:
                pass



#----------------------------------------------------------------
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
                    side, rect = self.load_img(self.table[i][g], pos)
                    
                    screen.blit(side, rect)
a = Game()
a.write_figures()