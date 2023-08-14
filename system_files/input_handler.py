import pygame
from system_files.save.save import SAVE
import sys
from pygame.locals import *

def input(SCREEN):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # deactivates the pygame library
            SAVE("SCREEN",SCREEN,"config.txt")
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEWHEEL:
               print(event)
               print(event.x, event.y)
               print(event.flipped)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE: 
                return "backspace"
            if event.key == pygame.K_TAB: 
                return "tab"
            if event.key == pygame.K_CLEAR: 
                return "clear"
            if event.key == pygame.K_RETURN: 
                return "return"
            if event.key == pygame.K_PAUSE: 
                return "pause"
            if event.key == pygame.K_ESCAPE:
                print ("escape") 
                SAVE("SCREEN",SCREEN,"config.txt")
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE: 
                return "space"
            if event.key == pygame.K_EXCLAIM: 
                return "exclaim"
            if event.key == pygame.K_HASH: 
                return "hash"
            if event.key == pygame.K_QUOTEDBL: 
                return "quotedbl"
            if event.key == pygame.K_DOLLAR: 
                return "dollar"
            if event.key == pygame.K_AMPERSAND: 
                return "ampersand"
            if event.key == pygame.K_QUOTE: 
                return "quote"
            if event.key == pygame.K_LEFTPAREN: 
                return "left parenthesis"
            if event.key == pygame.K_RIGHTPAREN: 
                return "right parenthesis"
            if event.key == pygame.K_ASTERISK: 
                return "asterisk"
            if event.key == pygame.K_PLUS: 
                return "plus sign"
            if event.key == pygame.K_COMMA: 
                return "comma"
            if event.key == pygame.K_MINUS: 
                return "minus sign"
            if event.key == pygame.K_PERIOD : 
                return "period"
            if event.key == pygame.K_SLASH: 
                return "forward slash"
            if event.key == pygame.K_0 : 
                return "0"
            if event.key == pygame.K_1: 
                return "1"
            if event.key == pygame.K_2: 
                return "2"
            if event.key == pygame.K_3: 
                return "3"
            if event.key == pygame.K_4: 
                return "4"
            if event.key == pygame.K_5: 
                return "5"
            if event.key == pygame.K_6: 
                return "6"
            if event.key == pygame.K_7: 
                return "7"
            if event.key == pygame.K_8: 
                return "8"
            if event.key == pygame.K_9: 
                return "9"
            if event.key == pygame.K_COLON: 
                return "colon"
            if event.key == pygame.K_SEMICOLON: 
                return "semicolon"
            if event.key == pygame.K_LESS: 
                return "less"
            if event.key == pygame.K_EQUALS: 
                return "equals"
            if event.key == pygame.K_GREATER: 
                return "greater"
            if event.key == pygame.K_QUESTION : 
                return "question"
            if event.key == pygame.K_AT: 
                return "at"
            if event.key == pygame.K_LEFTBRACKET: 
                return "left bracket"
            if event.key == pygame.K_BACKSLASH : 
                return "backslash"
            if event.key == pygame.K_RIGHTBRACKET: 
                return "right bracket"
            if event.key == pygame.K_CARET: 
                return "caret"
            if event.key == pygame.K_UNDERSCORE: 
                return "underscore"
            if event.key == pygame.K_BACKQUOTE: 
                return "grave"
            if event.key == pygame.K_DELETE: 
                return "delete"
            if event.key == pygame.K_KP0: 
                return "0"
            if event.key == pygame.K_KP1: 
                return "1"
            if event.key == pygame.K_KP2: 
                return "2"
            if event.key == pygame.K_KP3: 
                return "3"
            if event.key == pygame.K_KP4: 
                return "4"
            if event.key == pygame.K_KP5: 
                return "5"
            if event.key == pygame.K_KP6: 
                return "6"
            if event.key == pygame.K_KP7: 
                return "7"
            if event.key == pygame.K_KP8: 
                return "8"
            if event.key == pygame.K_KP9: 
                return "9"
            if event.key == pygame.K_KP_PERIOD: 
                return "period"
            if event.key == pygame.K_KP_DIVIDE: 
                return "divide"
            if event.key == pygame.K_KP_MULTIPLY: 
                return "multiply"
            if event.key == pygame.K_KP_MINUS: 
                return "minus"
            if event.key == pygame.K_KP_PLUS: 
                return "plus"
            if event.key == pygame.K_KP_ENTER: 
                return "enter"
            if event.key == pygame.K_KP_EQUALS: 
                return "equals"
            if event.key == pygame.K_UP: 
                return "up"
            if event.key == pygame.K_DOWN: 
                return "down"
            if event.key == pygame.K_RIGHT: 
                return "right"
            if event.key == pygame.K_LEFT: 
                return "Left"
            if event.key == pygame.K_INSERT: 
                return "Insert"
            if event.key == pygame.K_HOME: 
                return "Home"
            if event.key == pygame.K_END: 
                return "End"
            if event.key == pygame.K_PAGEUP: 
                return "Page Up"
            if event.key == pygame.K_PAGEDOWN: 
                return "Page Down"
            if event.key == pygame.K_F1: 
                return "F1"
            if event.key == pygame.K_F2: 
                return "F2"
            if event.key == pygame.K_F3: 
                return "F3"
            if event.key == pygame.K_F4: 
                return "F4"
            if event.key == pygame.K_F5: 
                return "F5"
            if event.key == pygame.K_F6: 
                return "F6"
            if event.key == pygame.K_F7: 
                return "F7"
            if event.key == pygame.K_F8: 
                return "F8"
            if event.key == pygame.K_F9: 
                return "F9"
            if event.key == pygame.K_F10: 
                return "F10"
            if event.key == pygame.K_F11: 
                return "F11"
            if event.key == pygame.K_F12: 
                return "F12"
            if event.key == pygame.K_F13: 
                return "F13"
            if event.key == pygame.K_F14: 
                return "F14"
            if event.key == pygame.K_F15: 
                return "F15"
            if event.key == pygame.K_NUMLOCK: 
                return "Numlock"
            if event.key == pygame.K_CAPSLOCK: 
                return "Capsloack"
            if event.key == pygame.K_SCROLLOCK: 
                return "Scrollock"
            if event.key == pygame.K_RSHIFT: 
                return "shift"
            if event.key == pygame.K_LSHIFT: 
                return "shift"
            if event.key == pygame.K_RCTRL: 
                return "control"
            if event.key == pygame.K_LCTRL: 
                return "control"
            if event.key == pygame.K_RALT : 
                return "alt"
            if event.key == pygame.K_LALT : 
                return "alt"
            if event.key == pygame.K_RMETA: 
                return "right meta"
            if event.key == pygame.K_LMETA : 
                return "left meta"
            if event.key == pygame.K_LSUPER: 
                return "Windows key"
            if event.key == pygame.K_RSUPER : 
                return "Windows key"
            if event.key == pygame.K_MODE: 
                return "mode shift"
            if event.key == pygame.K_HELP: 
                return "Help"
            if event.key == pygame.K_PRINT: 
                return "Print Screen"
            if event.key == pygame.K_SYSREQ: 
                return "sysrq"
            if event.key == pygame.K_BREAK: 
                return "Break"
            if event.key == pygame.K_MENU: 
                return "Menu"
            if event.key == pygame.K_POWER: 
                return "Power"
            if event.key == pygame.K_EURO: 
                return "Euro"
            return pygame.key.name(event.key)

    return "null"

def mouse_position():
    return pygame.mouse.get_pos()
