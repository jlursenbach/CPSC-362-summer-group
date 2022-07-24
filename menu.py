#!/usr/bin/env python3
# Jacob Ursenbach
# CPSC 386-01
# 2022-07-21
# jlursenbach@csu.fullerton.edu
# @jlursenbach
#
# Lab 02-00
#
# Blackjack game
#

"""
header
"""


class Menu(dict):
    """
    menu
    """

    def __init__(self, name=None, header=None, body=None, footer=None):
        super().__init__()
        self.name = name
        self.border = "- " * 30
        self.header = header
        self.body = body
        self.footer = footer

    @staticmethod
    def quit_program() -> None:
        """
        used to quit the program, (selecting q in menu calls this and breaks the menu loop) prints "goodbye"
        :return: None
        """
        print("< Exiting Menu")

    # this isn't really NEEDED? < (I never call this function,but it can help another coder understand/use the menu)
    # this CAN be used in loops, and to add items to menu. Needed?
    @staticmethod
    def create_menu_tuple(function, parameters, menu_text: str, display_item: bool) -> tuple:
        """
        this is not currently being used int the program.
        used to provide a structured way to create new menus that reminds coders how they're built.
        :param function: name of the function to be called
        :param parameters: parameters for any function what needs them.
        :param menu_text: The text the user sees when printing the menu
        :param display_item: Bool - choose whether the item is printed or not
                allows additional user controls without needing a bloated menu
        :return: a tuple containing all of the above info
        """
        return function, parameters, menu_text, display_item

    # same as above
    @staticmethod
    def new_menu_item(menu_key: str, menu_tuple: tuple) -> dict:
        """
        adds a new menu item with the correct parameters to a menu.
        can call create_menu_tuple, or just put a tuple directly into the menu_tuple parameter
        :param menu_key: a string holding the text used to select a menu item
        :param menu_tuple: a tuple containing all the information in a menu
                (the tuple is better described in create_menu_tuple() function)
        :return: a dictionary object with a single key, and corresponding menu tuple
        """

        # a dict containing a single key, with a tuple containing
        # (function, parameters, "menu_text", display_item: bool)
        menu_item = {menu_key: menu_tuple}
        return menu_item

    def print_menu(self) -> None:
        """
        prints the menu_text part of the tuple in the provided menu
        :param menu: the menu is a dictionary of keys and tuples
                menu item format: {key: (function, parameters, "display text", bool(print item?)
        :return: None
        """
        # border = "- " * 30
        print(f"{self.border}")

        if self.header:
            if type(self.header) == str:
                print(self.header)
            elif type(self.header) == list:
                for item in self.header:
                    print(item)
        if self.body:
            if type(self.body) == str:
                print(self.body)
            elif type(self.body) == list:
                for item in self.body:
                    print(item)

        print(f"\nPlease select a menu key from below: ")
        print(self.border)

        # value[3] is a boolean value called 'display_item' stating whether to print menu item,
        # value[2] is the menu text the user will see printed
        # key is the dictionary key the user uses to select the menu item.
        for key, value in self.items():
            if value[3]:
                print(f"{key}: {value[2]}")
        print(self.border)

        if self.footer:
            if type(self.footer) == str:
                print(self.footer)
            elif type(self.footer) == list:
                for item in self.footer:
                    print(item)

    def run_menu(self) -> False:
        """
        Takes user input to choose a menu object, than runs the correlated menu function
        If an invalid entry is given, prints a warning to user, with reminders of how to quit or print the menu
        :param menu: a dictionary holding menu keys and tuples
        :return: BOOL value: False (once q is presses escapes menu, tells program menu is not running)
        """

        #  sentinel, priming loop
        choice = ''
        self.print_menu()
        # Q escapes menu and quits.
        while choice.upper() != 'Q':
            try:
                print(f"__{self.name}__")
                print("M to print menu")
                choice = input("Please select a menu item:  ").upper().strip()
                # menu_choice[0] is a function call,
                # menu_choice[1] holds the function parameters
                if self[choice][1] == ():
                    self[choice][0]()
                else:
                    self[choice][0](self[choice][1])

            # invalid entry provides user with a reminder.
            except LookupError:
                print('\nInvalid Entry. \n'
                      '                 M to print menu\n'
                      '                 Q to quit menu\n')
        return False

    # def run_program(profiles: dict, menu: dict, is_running: bool) -> bool:
    #    return is_running

    def print_a_page(self):
        pass


if __name__ == '__main__':

    last_program_update = 20210810

    TITLE_PAGE = [
        f"xxxxxxxxxxxxxxxxxxxx -------- Welcome to -------- xxxxxxxxxxxxxxxxxxxx",
        f"    ____    _                  _           _                  _       ",
        fr"   |  _ \  | |                | |         | |                | |      ",
        f"   | |_) | | |   __ _    ___  | | __      | |   __ _    ___  | | __   ",
        f"   |  _ <  | |  / _` |  / __| | |/ /  _   | |  / _` |  / __| | |/ /   ",
        f"   | |_) | | | | (_| | | (__  |   <  | |__| | | (_| | | (__  |   <    ",
        fr"   |____/  |_|  \__,_|  \___| |_|\_\  \____/   \__,_|  \___| |_|\_\   ",
        f"xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        f"Last System Update: {last_program_update}                         -Jacob Ursenbach-",
    ]

    for item in TITLE_PAGE:
        print(item)

    input("\n       -------------- PRESS ENTER TO CONTINUE --------------\n")

    # Player Menu ---------------------------------------------------------------------------

    player_header = [
        fr" __                      __                       ",
        fr"|__) |     /\  \ / |__  |__)     |\/| |__  |\ | |  | ",
        fr"|    |___ /~~\  |  |___ |  \     |  | |___ | \| \__/ ",
    ]

    player_menu = Menu(name="Player Menu", header=player_header)

    def print_hello():
        print("hello")

    player_menu.update(
        {
            'M': (player_menu.print_menu, (), "Print Menu", False),
            'H': (print_hello, (), "Print Hello", True),
            'Q': (player_menu.quit_program, (), "Quit Menu", True)
        }
    )

    # Main Menu ---------------------------------------------------------------------------

    title = [

    ]

    body = [
        fr"select 'M' to print the menu if needed",
        fr"                                          ",
        fr" |\/|  /\  | |\ |     |\/| |__  |\ | |  | ",
        fr" |  | /~~\ | | \|     |  | |___ | \| \__/ ",
    ]
    foot = [

    ]

    # declaring the menu here so it can be used as a parameter, and print its self
    # main_menu = {}
    main_menu = Menu(name="Main Menu", header=title, body=body, footer=foot)

    def game_loop():
        print("this will be the game loop\n"
              "|````````````````````````````````````\n"
              "| --------------------------------\n"
              "|    THIS IS THE BLACKJACK GAME\n"
              "| --------------------------------\n"
              "_____________________________________")

    def loaded_players():
        print("-------ACTIVE PLAYERS-------\n"
              "Players Currently Loaded \n(limit 4):\n"
              "============================\n"
              "Jacob: Bank: $10,000\n"
              "Rosa: Bank: $100,000\n"
              "Dealer: Bank: WOAH\n"
              "============================\n")

    # menu format = (function, parameters, "Menu Text", Show_Item?)
    main_menu.update(
        {
            'M': (main_menu.print_menu, (), "Print Menu", False),
            'B': (game_loop, (), "Play BlackJack!!!", True),
            'P': (player_menu.run_menu, (), "PLayer Load Menu", True),
            'A': (loaded_players,(),"Print Active Players",True),
            'Q': (main_menu.quit_program, (), "Quit", True)
        }
    )

    # ------------------------------------------------------------------------------

    program_is_running = True

    while program_is_running:
        # run_menu returns false once loop is broken
        program_is_running = main_menu.run_menu()

        user_continue = input("do you want to quit the program? (Y/N)")
        if user_continue.upper() == 'N':
            program_is_running = True

        print("Goodbye")
