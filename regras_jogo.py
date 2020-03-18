from abc import ABC
import turtle
class RegrasJogo(ABC):
    """ Interface mínima para implementar um jogo interativo e modular. Não
    tente instanciar objetos dessa classe, ela deve ser herdada e seus métodos
    abstratos sobrecarregados.
    """
    # Setando o Mapa do Labirinto
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("Labirinto")
    wn.setup(700, 700)
    wn.tracer(0)
    # Registrando os GIFS
    turtle.register_shape("person.gif")
    turtle.register_shape("wall.gif")
    turtle.register_shape("finish.gif")

class Pen(turtle.Turtle):
   def __init__(self):
    turtle.Turtle.__init__(self)
    self.shape("square")
    self.color("black")
    self.penup()
    self.speed(0)
class Player(turtle.Turtle):
    def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("person.gif")
            self.color("blue")
            self.penup()
            self.speed(0)
            self.gold = 0

    def subir(self):
        mover_para_x = player.xcor()
        mover_para_y = player.ycor() + 24
        if (mover_para_x, mover_para_y) not in walls:
            self.goto(self.xcor(), self.ycor() + 24)
            self.gold += 1

    def descer(self):
        mover_para_x = player.xcor()
        mover_para_y = player.ycor() - 24
        if (mover_para_x, mover_para_y) not in walls:
            self.goto(self.xcor(), self.ycor() - 24)
            self.gold += 1

    def esquerda(self):
        mover_para_x = player.xcor() - 24
        mover_para_y = player.ycor()
        if (mover_para_x, mover_para_y) not in walls:
            self.goto(self.xcor() - 24, self.ycor())
            self.gold += 1

    def direita(self):
        mover_para_x = player.xcor() + 24
        mover_para_y = player.ycor()
        if (mover_para_x, mover_para_y) not in walls:
            self.goto(self.xcor() + 24, self.ycor())
            self.gold += 1

    levels = [""]

    level_1 = [
        "XXXXXXXXXXXXXXXXXXXXXXX",
        "XP   X                X",
        "XXXX X		XXXX X  X     X",
        "X    XXXXXXX    X  X  X",
        "XXXX       X  XXX     X",
        "X  X  X    X  X   XXXXX",
        "X  XXXX   XX  X X     X",
        "X  X    X   X X X     X",
        "X  X    XXX X X XXX   X",
        "X      XX          X  X",
        "XXXX X  X   XXXXX  X  X",
        "X    X    X           X",
        "XXXXXXXXXXXXXXXXXXXXCXX"
    ]



class Checkpoint(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("finish.gif")
            self.color("red")
            self.penup()
            self.speed(0)

class Treasure(turtle.Turtle):
        def __int__(self, x, y):
            turtle.Turtle.__init__(self)
            self.shape("circle")
            self.color("gold")
            self.penup()
            self.speed(0)
            self.gold = 100
            self.goto(x, y)

        def destroy(self):
            self.goto(2000, 2000)
            self.hideturtle()
levels = [""]

level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXX",
    "XP   X                X",
    "XXXX X		XXXX X  X     X",
    "X    XXXXXXX    X  X  X",
    "XXXX       X  XXX     X",
    "X  X  X    X  X   XXXXX",
    "X  XXXX   XX  X X     X",
    "X  X    X   X X X     X",
    "X  X    XXX X X XXX   X",
    "X      XX          X  X",
	  "XXXX X  X   XXXXX  X  X",
	  "X    X    X           X",
    "XXXXXXXXXXXXXXXXXXXXCXX"
]

treasures = []

levels.append(level_1)
player = Player()




turtle.listen()
turtle.onkey(player.esquerda, "Left")
turtle.onkey(player.direita, "Right")
turtle.onkey(player.subir, "Up")
turtle.onkey(player.descer, "Down")

def registrarAgenteJogador():
        """ Cria ou recupera id de um elemento de jogo agente.
        """
        Player()
        elemAgente = 'JOGADOR_PADRAO'
        return elemAgente
    
    #@abstractmethod
def isFim(self):
        """ Boolean indicando fim de jogo em True.
        """
        #player = Player()
        #if (player.xcor() == 192 and player.ycor() == 0):
        return True
        #else:
           # return False

    #@abstractmethod
def gerarCampoVisao(self, idAgente):
        """ Retorna um EstadoJogoView para ser consumido por um agente
        específico. Objeto deve conter apenas descrição de elementos visíveis
        para este agente.

        EstadoJogoView é um objeto imutável ou uma cópia do jogo, de forma que
        sua manipulação direta não tem nenhum efeito no mundo de jogo real.
        """
        return

    #@abstractmethod
def registrarProximaAcao(self, id_jogador, acao):
        """ Informa ao jogo qual a ação de um jogador especificamente.
        Neste momento, o jogo ainda não é transformado em seu próximo estado,
        isso é feito no método de atualização do mundo.
        """
        return
    
    #@abstractmethod
def atualizarEstado(diferencial_tempo):
        """ Apenas neste momento o jogo é atualizado para seu próximo estado
        de acordo com as ações de cada jogador registradas anteriormente.
        """
        return

walls = []

def construir_jogo(level):
    """ Método factory para uma instância Jogavel arbitrária, de acordo com os
    paraâmetros. Pode-se mudar à vontade a assinatura do método.
    """

    class Pen(turtle.Turtle):
        def __init__(self):
            turtle.Turtle.__init__(self)
            self.shape("square")
            self.color("black")
            self.penup()
            self.speed(0)

    pen = Pen()
    player = Player()
    checkpoing = Checkpoint()
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)
            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.shape("wall.gif")
                pen.stamp()
                #Condição de coordenadas para travar as paredes
                walls.append((screen_x, screen_y))
            if character == "P":
                player.goto(screen_x, screen_y)
            if character == "C":
                checkpoing.goto(screen_x, screen_y)
            if character == "T":
                treasures.append(Treasure(screen_x, screen_y))
    pass