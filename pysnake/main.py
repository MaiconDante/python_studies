import curses
import random

def game_loop(window):
    curses.curs_set(0)          # remove o cursor piscando
    window.nodelay(True)        # não bloqueia o getch
    window.timeout(150)         # velocidade inicial do jogo (ms)

    # Inicializa cores
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # cobra
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)    # comida

    # Cobra inicial
    snake = [
        [10, 15],
        [10, 14],
        [10, 13]
    ]
    current_direction = curses.KEY_RIGHT

    # Comida inicial
    food = [5, 5]

    while True:
        draw_screen(window)
        draw_snake(snake, window)
        # desenha comida em vermelho
        window.addch(food[0], food[1], curses.ACS_DIAMOND, curses.color_pair(2))

        # Pega direção do jogador
        direction = get_new_direction(window)
        if direction is None:
            direction = current_direction

        # Move cobra
        new_head = move_snake(snake, direction)

        # Se bateu na borda ou nela mesma -> game over
        if snake_hit_border(new_head, window) or new_head in snake:
            break

        # Verifica se comeu a comida
        if new_head == food:
            snake.insert(0, new_head)  # cresce (não remove cauda)
            # gera nova comida em posição livre
            food = None
            while food is None or food in snake:
                food = [
                    random.randint(1, window.getmaxyx()[0]-2),
                    random.randint(1, window.getmaxyx()[1]-2)
                ]
        else:
            # anda normalmente (remove cauda)
            snake.insert(0, new_head)
            snake.pop()

        current_direction = direction

    # Game over
    window.nodelay(False)
    window.clear()
    msg = "GAME OVER - pressione qualquer tecla"
    window.addstr(window.getmaxyx()[0]//2, (window.getmaxyx()[1]-len(msg))//2, msg)
    window.refresh()
    window.getch()

def draw_screen(window):
    window.clear()
    window.border(0)

def draw_snake(snake, window):
    # desenha toda a cobra com ACS_DIAMOND em verde
    for part in snake:
        window.addch(part[0], part[1], curses.ACS_DIAMOND, curses.color_pair(1))

def get_new_direction(window):
    try:
        key = window.getch()
        if key in [curses.KEY_UP, curses.KEY_RIGHT, curses.KEY_DOWN, curses.KEY_LEFT]:
            return key
    except:
        pass
    return None

def move_snake(snake, direction):
    head = snake[0].copy()
    if direction == curses.KEY_UP:
        head[0] -= 1
    elif direction == curses.KEY_DOWN:
        head[0] += 1
    elif direction == curses.KEY_LEFT:
        head[1] -= 1
    elif direction == curses.KEY_RIGHT:
        head[1] += 1
    return head

def snake_hit_border(head, window):
    height, width = window.getmaxyx()
    return (
        head[0] <= 0 or head[0] >= height-1 or
        head[1] <= 0 or head[1] >= width-1
    )

if __name__ == '__main__':
    curses.wrapper(game_loop)
    print("\n| --- VOCÊ PERDEU O JOGO --- |")
    