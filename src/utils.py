import copy
import curses
from enum import Enum


moves = ['U', 'D', 'F', 'B', 'L', 'R', ]


color_codes = {
    'R': '\033[41m',
    'G': '\033[42m',
    'Y':  '\33[43m',
    'B': "\033[44m",
    'O': '\033[48;2;255;165;0m',
    'W': '\33[47m',
    "_": '\33[37m',
    'RESET': "\033[0m"

}


class Node:
    def __init__(self, value):
        self.value: any = value
        self.next: Node = None

    def __getitem_index__(self, key: int):
        iter_node = self
        if (key >= 0):
            for _ in range(key):
                iter_node = iter_node.next
            return iter_node
        else:
            for _ in range(4):
                if iter_node.__getitem_index__(-key) == self:
                    return iter_node
                iter_node = iter_node.next

    def __getitem__(self, key: str):
        if (type(key) == int):
            return self.__getitem_index__(key)
        iter_node = self
        while iter_node.next != self:
            if iter_node.value == key:
                break
            iter_node = iter_node.next
        return iter_node


class CircularChainedList:
    def __init__(self):
        self.head_node: Node = None

    def __init__(self, elem_lst: list):
        self.head_node: Node = None
        for elem in elem_lst:
            self.add_elem(elem)

    def add_elem(self, value):
        new_node = Node(value)
        if self.head_node is None:
            self.head_node = new_node
            new_node.next = self.head_node
        else:
            iter_node = self.head_node
            while iter_node.next != self.head_node:
                iter_node = iter_node.next
            new_node.next = self.head_node
            iter_node.next = new_node


def afficher_menu(win, title, options, choix_actuel):

    win.clear()
    height, width = win.getmaxyx()
    x = width // 2 - len(title) // 2
    y = height // 5
    win.addstr(y, x, title)
    for index, option in enumerate(options):
        x = width // 2 - len(option) // 2
        y = height // 2 - len(options) // 2 + index
        if index == choix_actuel:
            win.addstr(y, x, option, curses.color_pair(1))
        else:
            win.addstr(y, x, option)
    win.refresh()


def choisir_option(win, title, options):
    choix_actuel = 0
    afficher_menu(win, title, options, choix_actuel)

    while True:
        key = win.getch()
        if key == curses.KEY_DOWN and choix_actuel < len(options) - 1:
            choix_actuel += 1
        elif key == curses.KEY_UP and choix_actuel > 0:
            choix_actuel -= 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            return choix_actuel
        afficher_menu(win, title, options, choix_actuel)


def input_choice(win, prompt):
    win.clear()
    height, _ = win.getmaxyx()
    win.addstr(height // 2, 0, prompt)
    curses.echo()  # Activer l'écho pour afficher la saisie de l'utilisateur
    valeur = win.getstr(height // 2 + 1, 0).decode('utf-8')
    curses.noecho()  # Désactiver l'écho
    return valeur


def choice_option(stdscr, options: list[str], title: str, input=False):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    if not input:
        choice = choisir_option(stdscr, title, options)
        choice = options[choice]
    else:
        choice = input_choice(stdscr, title)
    curses.endwin()
    return choice


def get_options(argv: list[str]):
    lenght = len(argv)
    generate, generated_lenght, visualise, visualise_mix, visualise_speed, auto_visualise = None, None, None, None, None, None
    count = 0
    i = 1
    while (i < 4) and i < lenght:
        if argv[i][0:2] == '--':
            if argv[i] == '--visualise':
                visualise = True
                count += 1
            elif argv[i] == '--generate':
                generate = True
                count += 2
                try:
                    generated_lenght = int(argv[i + 1])
                    i += 1
                except:
                    raise Exception("The lenght of generated mouves must be an int --generate [lenght]")
            else:
                raise Exception('Invalid option')
        i += 1

    if not generate and lenght < 2 + count:
        raise Exception('Please provide mixing array or use the --generate option for a random mix.')

#    if generate:
#        generated_lenght = curses.wrapper(
#            lambda stdscr: choice_option(stdscr, ["Yes", "False"], "Enter the lenght of the mix", input=True))
#        try:
#            generated_lenght = int(generated_lenght)
#        except:
#            raise Exception("Lenght of mix must be an integer")

    if visualise:
        visualise_mix = curses.wrapper(
            lambda stdscr: choice_option(stdscr, ["Yes", "False"], "Visualise mix ?"))
        visualise_mix = visualise_mix == "Yes"
    # auto_visualise = curses.wrapper(
    #     lambda stdscr: choice_option(stdscr, ["Yes", "False"], "Run auto mouves ? "))
        auto_visualise = True

    return generate, generated_lenght, visualise, visualise_mix, auto_visualise, count
