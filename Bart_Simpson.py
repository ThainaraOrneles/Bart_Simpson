import turtle # biblioteca turtle 

tela = turtle.Screen() # cria a janela do turtle
pen = turtle.Turtle() # cria a caneta ou lapis
tela.bgcolor("white") # coloca a cor de fundo
tela.setup(650,650) #define tamanho da janela
pen.hideturtle() # esconde o turtle
#pen.pen(pencolor = "white", fillcolor = "black", pensize = 3, speed = 10) # define cor da caneta, preechimento, tamanho e velocidade

#função que faz uma curva para esquerda definido pelo angulo, tamanho da linha desenhada e a quantidade de repetições
def curva_esquerda(ang,anda,tam): 
    for i in range(tam): 
        pen.left(ang) 
        pen.forward(anda)
        
#função que faz uma curva para direita definido pelo angulo, tamanho da linha desenhada e a quantidade de repetições
def curva_direita(ang,anda,tam): 
    for i in range(tam): 
        pen.right(ang) 
        pen.forward(anda)

#move o turtle(caneta) para a posição x y definida no código onde chama a fução
def move(x,y):
    pen.penup()
    pen.goto(x,y)
    pen.pendown()

#Desenha um circulo com preenchimento na cor branca o tamanho e definido no código onde chama a fução
def circulo_vazio(tam):
    pen.begin_fill()
    pen.pen(pencolor = "black", fillcolor = "white", pensize = 3, speed = 10)
    pen.circle(tam)
    pen.end_fill()
        
#Desenha um circulo com preenchimento na cor preta
def circulo_Preenchido(tam):
    pen.begin_fill()
    pen.pen(pencolor = "white", fillcolor = "black", pensize = 3, speed = 10)
    pen.circle(tam)
    pen.end_fill()

move(80,-160)
#define a fonte, o tamanho e a formatação
fonte = ("Comic Sans", 20, "normal")
pen.write("@itzme_atinara", False, "center", fonte)
pen.forward(40)
move(0,0)
#desenha os olhos
circulo_vazio(50)
move(80,0)
circulo_vazio(50)
move(0,40)
circulo_Preenchido(10)
move(85,40)
circulo_Preenchido(10)

#Sombracelha
pen.pencolor("black")
move(-30,90)
pen.right(200)
curva_direita(7,1.5,20)

#cabeça e cabelo
pen.left(70)
pen.forward(120)
pen.right(24)

for i in range(8):
    pen.right(130)
    pen.forward(30)
    pen.left(130)    
    pen.forward(30)

pen.right(140)
pen.forward(30)
pen.right(28)
curva_esquerda(2,18,10)
curva_esquerda(1,18,7)


pen.penup()
    
#parte da boca

pen.home()
move(-18,5)
    
pen.right(90)
curva_direita(2,12,5)
curva_esquerda(20,5,4)
pen.left(5)
curva_esquerda(8,38,4)
move(-18,5)

pen.penup()
pen.home()
pen.left(90)
  
move(40,20)
pen.left(90)
    

pen.begin_fill()
pen.pendown()
pen.pen(pencolor = "black", fillcolor = "white", pensize = 3, speed = 0.8)
curva_direita(1,5,10)
curva_esquerda(4,1,45)
pen.forward(10)
curva_esquerda(1,5,5)
pen.end_fill()

#parte debaixo da boca
pen.right(20)
move(120,-50)
curva_esquerda(2,3,9)

    
move(50,-75)
pen.right(70)
curva_esquerda(1,3,4)
curva_esquerda(8,2,10)
curva_direita(8,3,10)

#orelha
    
pen.left(120)
move(165,12)
pen.begin_fill()
pen.pen(pencolor = "black", fillcolor = "white", pensize = 3, speed = 0.8)
curva_direita(15,5,18)
pen.end_fill()

move(170,-1)
pen.right(90)
pen.pen(pencolor = "black",pensize = 2, speed = 0.8)
curva_direita(10,3,3)
curva_direita(15,3,3)

move(178,1)
curva_direita(15,3,4)

tela.mainloop()
