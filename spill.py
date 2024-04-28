import pygame
import sys
from pygame.locals import *

# Starter pygame
pygame.init()

# her velge æ farga
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Her definere jeg hvor stort selve vinduet som spillet blir vist på er
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman-spill")

# Her definerer ejg hvor hangmannen skal være, så når vi skriver feil bokstav, så popper disse delen opp
HEAD_POS = (WIDTH // 2, 160)
BODY_POS = (WIDTH // 2, 240)
LEFT_ARM_POS = (WIDTH // 2 - 50, 220)
RIGHT_ARM_POS = (WIDTH // 2 + 50, 220)
LEFT_LEG_POS = (WIDTH // 2 - 30, 300)
RIGHT_LEG_POS = (WIDTH // 2 + 30, 300)

# Her velger jeg bare hvilken font jeg skal bruke
FONT = pygame.font.SysFont(None, 50)

# Funksjon for å tegne tekst på skjermen
def tegn_tekst(tekst, farge, x, y):
    tekstflate = FONT.render(tekst, True, farge)
    tekstrektangel = tekstflate.get_rect(center=(x, y))
    WIN.blit(tekstflate, tekstrektangel)

# Her tenker jeg hangmannen
def tegn_hangman(forsøk):
    if forsøk >= 1:  # Tegn hode
        pygame.draw.circle(WIN, BLACK, HEAD_POS, 20)
    if forsøk >= 2:  # Tegn kropp
        pygame.draw.line(WIN, BLACK, HEAD_POS, BODY_POS, 2)
    if forsøk >= 3:  # Tegn venstre arm
        pygame.draw.line(WIN, BLACK, BODY_POS, LEFT_ARM_POS, 2)
    if forsøk >= 4:  # Tegn høyre arm
        pygame.draw.line(WIN, BLACK, BODY_POS, RIGHT_ARM_POS, 2)
    if forsøk >= 5:  # Tegn venstre ben
        pygame.draw.line(WIN, BLACK, BODY_POS, LEFT_LEG_POS, 2)
    if forsøk >= 6:  # Tegn høyre ben
        pygame.draw.line(WIN, BLACK, BODY_POS, RIGHT_LEG_POS, 2)

# Dette er selve funksjonen av spillet
def hoved():
    forsøk = 0
    gjettede_bokstaver = set()
    ord_eller_setning = input("Skriv inn et ord eller en setning for den andre spilleren å gjette:").upper()
    ord_set = set(ord_eller_setning.replace(' ', ''))  # Fjern mellomrom fra ordet for sammenligning

    kjør = True
    while kjør:
        WIN.fill(WHITE)
        tegn_hangman(forsøk)
        vis_ord = ''
        for bokstav in ord_eller_setning:
            if bokstav == ' ':
                vis_ord += ' '
            elif bokstav in gjettede_bokstaver:
                vis_ord += bokstav
            else:
                vis_ord += '_'
        tegn_tekst(vis_ord, BLACK, WIDTH//2, HEIGHT//2 + 50)
        tegn_tekst(f"Gjettede bokstaver: {' '.join(gjettede_bokstaver)}", BLACK, WIDTH//2, HEIGHT//2 + 150)
        tegn_tekst(f"Forsøk igjen: {6 - forsøk}", BLACK, WIDTH//2, HEIGHT//2 + 250)
        pygame.display.update()

        for hendelse in pygame.event.get():
            if hendelse.type == pygame.QUIT:
                kjør = False
                sys.exit()

            if hendelse.type == KEYDOWN:
                if hendelse.key == K_ESCAPE:
                    kjør = False
                    sys.exit()
                if hendelse.key >= 97 and hendelse.key <= 122:  # Sjekke æ om tasten som ble trykket e en liten bokstav
                    bokstav = chr(hendelse.key).upper()
                    if bokstav in gjettede_bokstaver:
                        continue
                    gjettede_bokstaver.add(bokstav)
                    if bokstav not in ord_set:
                        forsøk += 1
                    if forsøk == 6:
                        tegn_hangman(6)
                        tegn_tekst("Spillet er over!", RED, WIDTH//2, HEIGHT//2 - 100)
                        pygame.display.update()
                        pygame.time.delay(3000)
                        kjør = False

        if all(letter in gjettede_bokstaver or letter == ' ' for letter in ord_eller_setning):
            tegn_tekst("Gratulerer! Du gjettet ordet!", RED, WIDTH//2, HEIGHT//2 - 100)
            pygame.display.update()
            pygame.time.delay(3000)
            kjør = False

# Her starte hovedfunksjonen
if __name__ == "__main__":
    hoved()
