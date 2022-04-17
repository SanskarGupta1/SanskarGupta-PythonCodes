import pygame
import random
import os


if os.path.exists("The high score of the best snake game in the world.txt"):
    pass
else:
    open("The high score of the best snake game in the world.txt", 'w+')

    with open("The high score of the best snake game in the world.txt", 'w') as writter:
        writter.write('0')

pygame.init()

Screen_width = 1250
Screen_height = 600

SGTech = pygame.display.set_mode((Screen_width, Screen_height))
pygame.display.set_caption("SGTech")


def BackGround(image):
    Background_image = pygame.image.load(image)
    Background_image = pygame.transform.scale(
        Background_image, (Screen_width, Screen_height))

    SGTech.blit(Background_image, [0, 0])


def Snake_length_increase(color, Snake_l, Size):
    for x, y in Snake_l:
        pygame.draw.rect(SGTech, color, [x, y, Size, Size])


def High_score(Chs, cs):
    if cs > Chs:
        with open("The high score of the best snake game in the world.txt", 'w') as writer:
            writer.write(f'{cs}')


Clock = pygame.time.Clock()

Fonts = pygame.font.SysFont("None", 55)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)


def Text(text, font, color, GameWindow, Pos_x, Pos_y):
    Font = pygame.font.SysFont(font, 65)

    Display_text = Font.render(text, True, color)
    GameWindow.blit(Display_text, [Pos_x, Pos_y])


Exit = False


def Game():

    global Exit

    Snake_list = []

    Exit = False

    score = 0

    Velocity_X = 0
    Velocity_Y = 0

    Pos_X = Screen_width / 2
    Pos_Y = Screen_height / 2

    Size = 20
    Snake_length = 1

    Rand_X = random.randint(30, (Screen_width - 100))
    Rand_Y = random.randint(30, (Screen_height - 100))

    while not Exit:
        with open("The high score of the best snake game in the world.txt", 'r') as reader:
            Get_score = reader.read()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Exit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    Velocity_Y = -5
                    Velocity_X = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    Velocity_Y = 5
                    Velocity_X = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    Velocity_Y = 0
                    Velocity_X = 5
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    Velocity_Y = 0
                    Velocity_X = -5
                elif event.key == pygame.K_q:
                    Exit = True


        if Pos_X <= 0 or Pos_X >= Screen_width or Pos_Y <= 0 or Pos_Y >= Screen_height:
            EndScreen(score)
            Exit = True

        Pos_X += Velocity_X
        Pos_Y += Velocity_Y

        SGTech.fill(black)
        BackGround("The perfect snake.jpg")

        head = [Pos_X, Pos_Y]
        Snake_list.append(head)

        if abs(Rand_X - Pos_X) < 22 and abs(Rand_Y - Pos_Y) < 22:
            Rand_X = random.randint(30, (Screen_width - 100))
            Rand_Y = random.randint(30, (Screen_height - 100))

            Snake_length += 7
            score += 10

        High_score(int(Get_score), int(score))
        Snake_length_increase(green, Snake_list, Size)

        if len(Snake_list) > Snake_length:
            del Snake_list[0]

        if head in Snake_list[:-1]:
            EndScreen(score)
            Exit = True

        Text(f"Score: {score}", None, blue, SGTech, 10, 10)
        Text(f"high score: {Get_score}", None, red, SGTech, 10, 50)

        pygame.draw.rect(SGTech, red, [Rand_X, Rand_Y, Size, Size])
        pygame.draw.rect(SGTech, green, [Pos_X, Pos_Y, Size, Size])

        Clock.tick(75)
        pygame.display.update()


def Home_screen():

    global Exit

    Exit = False

    pygame.mixer.music.load(r'Born a rockstar.mp3')
    pygame.mixer.music.play(True)
    pygame.mixer.music.set_volume(.7)

    while not Exit:
        for action in pygame.event.get():
            if action.type == pygame.KEYDOWN:
                if action.key == pygame.K_SPACE:
                    Game()
                    Exit = True
            elif action.type == pygame.QUIT:
                Exit = True

        SGTech.fill(black)
        BackGround(r"Snake.jpg")

        Text("Welcome to the snakes game.",
             'vivaldi', (255, 24, 24), SGTech, 10, 50)
        Text('Please press spacebar to start.',
             'vivaldi', (255, 24, 24), SGTech, 60, 100)

        pygame.display.update()


def EndScreen(score):

    global Exit

    Exit = False

    SGTech.fill(black)
    BackGround(r"Red Snake.jpg")

    while not Exit:
        for L_actions in pygame.event.get():
            if L_actions.type == pygame.KEYDOWN:
                if L_actions.key == pygame.K_q:
                    Exit = True
                else:
                    Game()

        Text("You lose the game!", 'vivaldi', (60, 255, 0),
             SGTech, 10, Screen_height / 2 - 190)
        Text(f"The score you made was {score}", 'vivaldi',
             (60, 255, 0), SGTech, 40, Screen_height / 2 - 140)
        Text("Press any key to re-start or q to quit.", 'vivaldi',
             (60, 255, 0), SGTech, 70, Screen_height / 2 - 90)

        pygame.display.update()


if __name__ == '__main__':
    Home_screen()
