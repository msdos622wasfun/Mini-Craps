####################################
#
# Mini Craps
# A game of Craps written in Python.
# Copyleft 2020 by Erich Kohl
# Version 1.00
#
# https://github.com/msdos622wasfun
#
####################################

import os, sys, random, appdirs, configparser, pygame

# Globals

win = None
run = None
diceTitle = []
diceGame = []
fontCasino125 = None
fontAtariClassicSmooth25 = None
fontAtariClassicSmooth40 = None
balance = None
balanceStart = None
appdataFolder = None

def get_appdata_folder():
    # Variables_begin
    global appdataFolder
    # Variables_end
    try:
        appdataFolder = appdirs.user_data_dir("Mini Craps", "Erich Kohl")
        if os.path.isdir(appdataFolder) == False:
            os.makedirs(appdataFolder)
    except:
        pass


def balance_read():
    # Variables_begin
    global appdataFolder
    global balance
    config = None
    # Variables_end
    try:
        balance = 1000
        config = configparser.ConfigParser()
        config.read(appdataFolder + "\\Mini Craps.ini")
        balance = int(config["SCORES"]["balance"])
        if balance < -99999:
            balance = -99999
        elif balance > 99999:
            balance = 99999
    except:
        pass
        
    
def balance_write():
    # Variables_begin
    global appdataFolder
    config = None
    configFile = None
    # Variables_end
    try:
        config = configparser.ConfigParser()
        config["SCORES"] = {}
        config["SCORES"]["Balance"] = str(balance)
        with open(appdataFolder + "\\Mini Craps.ini", "w") as configFile:
            config.write(configFile)
        configFile.close()
    except:
        pass


def balance_reset():
    # Variables_begin
    global balance
    # Variables_end
    balance = 1000
    balance_write()


def screen_title():
    # Variables_begin
    global win
    global run
    global fontCasino125
    global fontAtariClassicSmooth25
    global fontAtariClassicSmooth40
    diceTop = []
    diceBottom = []
    diceLeft = []
    diceRight = []
    text = None
    a = None
    x = None
    event = None
    # Variables_end
    for a in range(1, 21):
        diceTop.append(diceTitle[random.randint(0, 35)])
        diceBottom.append(diceTitle[random.randint(0, 35)])
        if a <= 16:
            diceLeft.append(diceTitle[random.randint(0, 35)])
            diceRight.append(diceTitle[random.randint(0, 35)])
    while run:
        win.fill((0, 0, 255))
        for a in range(0, 20):
            win.blit(pygame.transform.scale(diceTop[a], (50, 50)), (a * 50, 0))
            win.blit(pygame.transform.scale(diceBottom[a], (50, 50)), (a * 50, 750))
            if a <= 15:
                win.blit(pygame.transform.scale(diceLeft[a], (50, 50)), (0, a * 50))
                win.blit(pygame.transform.scale(diceRight[a], (50, 50)), (950, a * 50))
        text = fontCasino125.render("MINI CRAPS", True, (255, 255, 255))
        win.blit(text, (500 - (int(text.get_width() / 2)), 100))
        text = fontAtariClassicSmooth25.render("Mini Craps v1.00", True, (255, 255, 255))
        win.blit(text, (500 - (int(text.get_width() / 2)), 250))
        text = fontAtariClassicSmooth25.render("Copyleft 2020 by Erich Kohl", True, (255, 255, 255))
        win.blit(text, (500 - (int(text.get_width() / 2)), 280))
        text = fontAtariClassicSmooth40.render("(2) RESET BALANCE", True, (255, 255, 255))
        x = 500 - int(text.get_width() / 2)
        win.blit(text, (x, 450))
        text = fontAtariClassicSmooth40.render("(1) PLAY GAME", True, (255, 255, 255))
        win.blit(text, (x, 400))
        text = fontAtariClassicSmooth40.render("(3) QUIT", True, (255, 255, 255))
        win.blit(text, (x, 500))
        if balance > 0:
            text = fontAtariClassicSmooth25.render("BALANCE = $" + str(balance), True, (0, 255, 0))
        elif balance < 0:
            text = fontAtariClassicSmooth25.render("BALANCE = $<" + str(abs(balance)), True, (255, 0, 0))
        else:
            text = fontAtariClassicSmooth25.render("BALANCE = $" + str(balance), True, (255, 255, 255))
        win.blit(text, (500 - (int(text.get_width() / 2)), 700))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return
                if event.key == pygame.K_2:
                    if balance != 1000:
                        balance_reset()
                elif event.key == pygame.K_3:
                    run = False
                    return
                elif event.key == pygame.K_ESCAPE:
                    run = False
                    return
            elif event.type == pygame.QUIT:
                run = False
                return
            
            
def screen_game_post():
    # Variables_begin
    global run
    global fontAtariClassicSmooth25
    global balance
    global balanceStart
    waitingForEscape = None
    text = None
    # Variables_end
    waitingForEscape = True
    while waitingForEscape:
        win.fill((0, 0, 255))
        pygame.draw.rect(win, (0, 255, 255), (0, 0, 1000, 25))
        pygame.draw.rect(win, (0, 255, 255), (0, 775, 1000, 25))
        pygame.draw.rect(win, (0, 255, 255), (0, 0, 25, 800))
        pygame.draw.rect(win, (0, 255, 255), (975, 0, 25, 800))
        if balance > balanceStart:
            text = fontAtariClassicSmooth25.render("YOU WON A TOTAL OF $" + str(balance - balanceStart), True, (0, 255, 0))
        elif balance < balanceStart:
            text = fontAtariClassicSmooth25.render("YOU LOST A TOTAL OF $" + str(balanceStart - balance), True, (255, 0, 0))
        else:
            text = fontAtariClassicSmooth25.render("YOU BROKE EVEN TODAY", True, (255, 255, 255))
        win.blit(text, (500 - (int(text.get_width() / 2)), 330))
        text = fontAtariClassicSmooth25.render("PRESS ESC FOR MAIN MENU", True, (255, 255, 255))
        win.blit(text, (500 - (int(text.get_width() / 2)), 430))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waitingForEscape = False
            elif event.type == pygame.QUIT:
                run = False
                return


def screen_game():
    # Variables_begin
    global win
    global run
    global balance
    global balanceStart
    global fontAtariClassicSmooth25
    global fontAtariClassicSmooth40
    global diceGame
    bet = None
    betOld = None
    betting = None
    event = None
    text = None
    waitingForEnter = None
    die1 = None
    die2 = None
    x = None
    point = None
    won = None
    lost = None
    clock = None
    timePassesd = None
    playedOnce = None
    quitGame = None
    # Variables_end
    betOld = 5
    playedOnce = False
    balanceStart = balance
    while True:
        win.fill((0, 0, 255))
        pygame.draw.rect(win, (0, 255, 255), (0, 0, 350, 25))
        pygame.draw.rect(win, (0, 255, 255), (650, 0, 350, 25))
        pygame.draw.rect(win, (0, 255, 255), (0, 775, 350, 25))
        pygame.draw.rect(win, (0, 255, 255), (650, 775, 350, 25))
        pygame.draw.rect(win, (0, 255, 255), (0, 0, 25, 800))
        pygame.draw.rect(win, (0, 255, 255), (975, 0, 25, 800))
        pygame.draw.rect(win, (0, 255, 255), (100, 600, 150, 100), 3)
        pygame.draw.rect(win, (0, 255, 255), (700, 600, 200, 100), 3)
        text = fontAtariClassicSmooth25.render("MINI CRAPS", True, (255, 255, 255))
        win.blit(text, (500 - int(text.get_width() / 2), 0))
        text = fontAtariClassicSmooth25.render("ESC QUITS", True, (255, 255, 255))
        win.blit(text, (500 - int(text.get_width() / 2), 773))
        text = fontAtariClassicSmooth25.render("POINT", True, (255, 255, 255))
        win.blit(text, (175 - int(text.get_width() / 2), 560))
        text = fontAtariClassicSmooth25.render("BALANCE", True, (255, 255, 255))
        win.blit(text, (800 - int(text.get_width() / 2), 560))
        if balance > 0:
            text = fontAtariClassicSmooth25.render("$" + str(balance), True, (0, 255, 0))
        elif balance < 0:
            text = fontAtariClassicSmooth25.render("$<" + str(abs(balance)), True, (255, 0, 0))
        else:
            text = fontAtariClassicSmooth25.render("$" + str(balance), True, (255, 255, 255))
        win.blit(text, (800 - int(text.get_width() / 2), 635))
        text = fontAtariClassicSmooth40.render("PLACE YOUR BET", True, (255, 255, 255))
        win.blit(text, (500 - int(text.get_width() / 2), 240))
        text = fontAtariClassicSmooth25.render("USE ARROW KEYS TO ADJUST BET", True, (255, 255, 255))
        win.blit(text, (500 - int(text.get_width() / 2), 415))
        text = fontAtariClassicSmooth25.render("PRESS ENTER WHEN DONE", True, (255, 255, 255))
        win.blit(text, (500 - int(text.get_width() / 2), 445))
        bet = betOld
        betting = True
        while betting:
            pygame.draw.rect(win, (0, 0, 255), (425, 300, 150, 100))
            pygame.draw.rect(win, (0, 255, 255), (425, 300, 150, 100), 3)
            text = fontAtariClassicSmooth40.render(str(bet), True, (255, 255, 0))
            win.blit(text, (500 - int(text.get_width() / 2), 330))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        bet += 5
                        if bet > 500:
                            bet = 500
                    elif event.key == pygame.K_LEFT:
                        bet -= 5
                        if bet < 5:
                            bet = 5
                    elif event.key == pygame.K_UP:
                        bet += 25
                        if bet > 500:
                            bet = 500
                    elif event.key == pygame.K_DOWN:
                        bet -= 25
                        if bet < 5:
                            bet = 5
                    elif event.key == pygame.K_RETURN:
                        betting = False
                    elif event.key == pygame.K_ESCAPE:
                        if playedOnce == True:
                            screen_game_post()
                        return
                elif event.type == pygame.QUIT:
                    run = False
                    return
        betOld = bet
        pygame.draw.rect(win, (0, 0, 255), (100, 100, 800, 450))
        pygame.draw.rect(win, (0, 255, 255), (100, 300, 800, 100), 3)
        text = fontAtariClassicSmooth40.render("ENTER TO ROLL DICE", True, (255, 255, 255))
        win.blit(text, (500 - int(text.get_width() / 2), 330))
        pygame.display.update()
        waitingForEnter = True
        while waitingForEnter:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        waitingForEnter = False
                    elif event.key == pygame.K_ESCAPE:
                        if playedOnce == True:
                            screen_game_post()
                        return
                elif event.type == pygame.QUIT:
                    run = False
                    return
        point = None
        won = False
        lost = False
        while won == False and lost == False:
            x = 105
            while x < 455:
                pygame.draw.rect(win, (0, 0, 255), (100, 100, 800, 450))
                pygame.draw.rect(win, (0, 255, 255), (100, 300, 800, 100), 3)
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                win.blit(pygame.transform.scale(diceGame[die1 - 1], (50, 50)), (x, 325))
                win.blit(pygame.transform.scale(diceGame[die2 - 1], (50, 50)), (945 - x, 325))
                x += 25
                pygame.display.update()
                pygame.time.wait(int(1000 / 30))
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            if playedOnce == True:
                                screen_game_post()
                            return
                    elif event.type == pygame.QUIT:
                        run = False
                        return
            if point == None:
                if (die1 + die2) == 7 or (die1 + die2) == 11:
                    won = True
                elif (die1 + die2) == 2 or (die1 + die2) == 3 or (die1 + die2) == 12:
                    lost = True
                else:
                    point = die1 + die2
                    text = fontAtariClassicSmooth40.render(str(point), True, (255, 0, 255))
                    win.blit(text, (175 - int(text.get_width() / 2), 630))
                    pygame.display.update()
            else:
                if (die1 + die2) == point:
                    won = True
                elif (die1 + die2) == 7:
                    lost = True
            if won == False and lost == False:
                text = fontAtariClassicSmooth40.render("YOUR ROLL: " + str(die1 + die2), True, (255, 255, 255))
                win.blit(text, (500 - int(text.get_width() / 2), 450))
                pygame.display.update()
                clock = pygame.time.Clock()
                timePassed = 0
                while timePassed < 2500:
                    clock.tick()
                    timePassed += clock.get_time()
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            return
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RETURN:
                                timePassed = 2500
                            if event.key == pygame.K_ESCAPE:
                                if playedOnce == True:
                                    screen_game_post()
                                return
                clock = None
        if won == True:
            balance += bet
            text = fontAtariClassicSmooth40.render("CONGRATS, YOU WON!", True, (0, 255, 0))
        else:
            balance -= bet
            text = fontAtariClassicSmooth40.render("SORRY, YOU LOST", True, (255, 0, 0))
        win.blit(text, (500 - int(text.get_width() / 2), 450))
        pygame.display.update()
        balance_write()
        playedOnce = True
        clock = pygame.time.Clock()
        timePassed = 0
        while timePassed < 5000:
            clock.tick()
            timePassed += clock.get_time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        timePassed = 5000
                    if event.key == pygame.K_ESCAPE:
                        if playedOnce == True:
                            screen_game_post()
                        return
        clock = None


def init():
    # Variables_begin
    global win
    global diceTitle
    global diceGame
    global fontCasino125
    global fontAtariClassicSmooth25
    global fontAtariClassicSmooth40
    global balance
    global appdataFolder
    fn = None
    a = None
    # Variables_end
    try:
        pygame.init()
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        win = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Mini Craps")
        fontCasino125 = pygame.font.Font("Assets\\CasinoShadow.ttf", 125)
        fontAtariClassicSmooth25 = pygame.font.Font("Assets\\AtariClassicSmooth.ttf", 25)
        fontAtariClassicSmooth40 = pygame.font.Font("Assets\\AtariClassicSmooth.ttf", 40)
        for a in range(1, 37):
            if a < 10:
                fn = "0" + str(a)
            else:
                fn = str(a)
            fn = fn + ".png"
            diceTitle.append(pygame.image.load("Assets\\Dice\\" + fn))
            if a >= 31:
                diceGame.append(pygame.image.load("Assets\\Dice\\" + fn))
    except:
        sys.exit()
    get_appdata_folder()
    balance_read()
        
    
def main():
    # Variables_begin
    global run
    # Variables_end
    run = True
    while run:
        screen_title()
        if run == True:
            screen_game()


def wrap_up():
    pygame.quit()


# Start of program

init()
main()
wrap_up()

sys.exit()