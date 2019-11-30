import pygame as pg
from sympy import *

def output(f,g):
    a,b,c,x = symbols('a,b,c,x')
    f=f; g=g;

    # Using sympy.div() method 
    q, r = div(f, g, domain ='QQ')
    #q, r = div(f, g, x) 

    print(q) 
    print(r)
    return q,r

pg.init()

screen = pg.display.set_mode((640, 480))
font = pg.font.Font(None, 32)
clock = pg.time.Clock()
dividend_box = pg.Rect(280, 85, 350, 35)
divisor_box = pg.Rect(280, 170, 350, 35)

dividend_box1 = pg.Rect(150, 85, 200, 35)
divisor_box1 = pg.Rect(150, 170, 200, 35)

divide_box=pg.Rect(450, 260,80, 35)

quotient_box=pg.Rect(175, 330,300, 35)

reminder_box=pg.Rect(175, 390,300, 35)

divide_box1=pg.Rect(450, 260,80, 35)

quotient_box1=pg.Rect(25, 330,300, 35)

reminder_box1=pg.Rect(25, 390,300, 35)

divide_active = False

color_inactive = pg.Color('lightskyblue3')
color_active = pg.Color('dodgerblue2')
color_dividend = color_inactive
color_divisor = color_inactive
dividend_active = False
divide_active = False

divisor_active = False

dividend = ''
divisor = ''
q_text=''
r_text=''

pg.display.set_caption('PolyDivision')

done = False

while not done:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if dividend_box.collidepoint(event.pos):
                    # Toggle the active variable.
                   dividend_active = True
                else:
                    dividend_active = False
                # Change the current color of the input box.
                color_dividend = color_active if dividend_active else color_inactive

                if divisor_box.collidepoint(event.pos):
                   divisor_active = True
                else:
                    divisor_active = False
                # Change the current color of the input box.
                color_divisor = color_active if divisor_active else color_inactive

                if divide_box.collidepoint(event.pos):
                    # Toggle the active variable.
                   divide_active = True
                 
                else:
                    divide_active = False
                    
            if event.type == pg.KEYDOWN:
                if dividend_active:
                    if event.key == pg.K_RETURN:
                        print(dividend)
        
                    elif event.key == pg.K_BACKSPACE:
                        dividend = dividend[:-1]
                    else:
                        dividend += event.unicode
                        
                if divisor_active:
                    if event.key == pg.K_RETURN:
                        print(divisor)
            
                    elif event.key == pg.K_BACKSPACE:
                        divisor = divisor[:-1]
                    else:
                        divisor += event.unicode
                        
            if divide_active:
                
                    print('divide active')
                    divide_active = False
                    
                    q,r = output(str(dividend), str(divisor))
                    
                    q_text=str(q); r_text=str(r);
                                        
                    quotient_text = font.render(q_text, True, (255,255,255))
                                                                                    
                    reminder_text = font.render(r_text, True, (255,255,255))
                    screen.blit(quotient_text, (quotient_box.x+5, quotient_box.y+5))
                    screen.blit(reminder_text, (reminder_box.x+5, reminder_box.y+5))

                 
        #screen.fill((30, 30, 30))
        
        # Render the current text.
        dividend_surface = font.render(dividend, True, color_dividend)
        divisor_surface  = font.render(divisor, True, color_divisor)
##        # Resize the box if the text is too long.
##        width = max(200, txt_surface.get_width()+10)
##        input_box.w = width
##        # Blit the text.
        screen.blit(dividend_surface, (dividend_box.x+5, dividend_box.y+5))
        screen.blit(divisor_surface, (divisor_box.x+5, divisor_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color_dividend, dividend_box, 2)
        pg.draw.rect(screen, color_divisor, divisor_box, 2)

        dividend_text = font.render('Dividend', True, (155,255,155))
        divisor_text = font.render('Divisor', True, (155,255,155))
        screen.blit(dividend_text, (dividend_box1.x+5, dividend_box1.y+5))
        screen.blit(divisor_text, (divisor_box1.x+5, divisor_box1.y+5))

        divide_text = font.render('Divide', True, (0,0,0),(155,255,155))
        
        screen.blit(divide_text, (divide_box.x+5, divide_box.y+5))
        pg.draw.rect(screen, (255,255,255), divide_box, 2)

        pg.draw.rect(screen, (255,255,255), quotient_box, 2)

        pg.draw.rect(screen, (255,255,255), reminder_box, 2)
        
        q_text = font.render('Quotient', True, (155,255,155))
        
        screen.blit(q_text, (quotient_box1.x+5, quotient_box1.y+5))

        r_text = font.render('Reminder', True, (155,255,155))
        
        screen.blit(r_text, (reminder_box1.x+5, reminder_box1.y+5))
        
        pg.display.flip()
        clock.tick(30)



    
   



