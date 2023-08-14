class UIELEMENT:
    def __init__(self, object, string, pos):
        self.object = object
        self.rawstring=string
        self.pos = pos
        self.w=LOAD("WIDTH", "config.txt")
        self.h=LOAD("HEIGHT", "config.txt")
        self.string = font.render(string, True, black)
        self.str=self.string.get_size()
        self.x1=self.w/2-self.str[0]/2-5
        self.x2=self.w/2-self.str[0]/2-5+self.str[0]+10
        self.y1=self.h/9*(self.pos-1)-self.str[1]/2+5+20
        self.y2=self.h/9*(self.pos-1)-self.str[1]/2+5+self.str[1]+10+20
        if self.object=="mode":
            self.x1=self.w-self.str[0]-25
            self.x2=self.w-10
            self.y1=10
            self.y2=self.str[1]+10+10
        left, middle, right = pygame.mouse.get_pressed()
        mouse= mouse_position()
        if self.x1<mouse[0]<self.x2 and self.y1<mouse[1]<self.y2:
            self.state="hover"
            if left:
                self.state="click"
        else: 
            self.state="idle"
        if self.state == "idle":
            self.color = black
            self.colorx = blue
            self.colory = red
        else:
            self.color = grey
            self.colorx = light_blue
            self.colory = light_red
        self.string = font.render(string, True, self.color)
    
    def button(self):
        pygame.draw.rect(screen,self.colorx, pygame.Rect(self.x1, self.y1, self.str[0]+10, self.str[1]+10))
        pygame.draw.rect(screen,self.colory, pygame.Rect(self.x1, self.y1, self.str[0]+10, self.str[1]+10),2)
        screen.blit(self.string, (self.w/2-self.str[0]/2,self.h/9*(self.pos-1)+20))
        if self.state=="click":
            return 1
        return 0
    
    def text(self):
        string = font.render(self.rawstring, True, black)
        screen.blit(string, (20,20+self.h/9*(self.pos-1)))
    
    def mode(self):
        pygame.draw.rect(screen,self.colorx, pygame.Rect(self.x1, self.y1, self.str[0]+10, self.str[1]+10))
        pygame.draw.rect(screen,self.colory, pygame.Rect(self.x1, self.y1, self.str[0]+10, self.str[1]+10),2)
        screen.blit(self.string, (self.w-self.str[0]-20,20))
        if self.state=="click":
            return 1
        return 0