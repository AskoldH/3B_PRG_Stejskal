import random


class Deck():
    def create_mixed_deck(self):
        pass

    def __init__(self):
        card_values = ["ESO", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JUNÁK", "DÁMA", "KRÁL"]
        self.generated_deck = []
        self.top_card = False

        not_used_card_values_hearts = card_values.copy()
        not_used_card_values_spades = card_values.copy()
        not_used_card_values_leaves = card_values.copy()
        not_used_card_values_diamonds = card_values.copy()

        while True:
            if not_used_card_values_hearts and not random.randint(0, 3):
                random_int = random.randint(0, len(not_used_card_values_hearts) - 1)
                self.generated_deck.append("♥" + not_used_card_values_hearts[random_int])
                del not_used_card_values_hearts[random_int]

            elif not_used_card_values_spades and not random.randint(0, 3):
                random_int = random.randint(0, len(not_used_card_values_spades) - 1)
                self.generated_deck.append("♠" + not_used_card_values_spades[random_int])
                del not_used_card_values_spades[random_int]

            elif not_used_card_values_diamonds and not random.randint(0, 3):
                random_int = random.randint(0, len(not_used_card_values_diamonds) - 1)
                self.generated_deck.append("♦" + not_used_card_values_diamonds[random_int])
                del not_used_card_values_diamonds[random_int]

            elif not_used_card_values_leaves and not random.randint(0, 3):
                random_int = random.randint(0, len(not_used_card_values_leaves) - 1)
                self.generated_deck.append("♣" + not_used_card_values_leaves[random_int])
                del not_used_card_values_leaves[random_int]

            elif not (len(not_used_card_values_spades) or len(not_used_card_values_diamonds) or len(
                    not_used_card_values_leaves) or len(not_used_card_values_hearts)):
                break

    def show_deck(self):
        print(self.generated_deck)

    def show_len(self):
        print(len(self.generated_deck))


class CardPile():
    def __init__(self, deck):
        self.top_card = deck.pop(0)

    def put_card_on_top(self, deck, card):
        # check validity
        if self.top_card[0] == card[0] or self.top_card[1] == card[1]:
            # put into deck
            deck.append(self.top_card)
            self.top_card = card
            # check for special cards
            if card[1] == 7:
                return 2
            elif card[0] == '♠' and card[1] == 'K':
                return 4
            elif card[1] == 'E':
                return "pass cycle"
            return False

        # casted off wrong card
        input(
            '\n' + f"No takhle to nepůjde!! {card} rozhodně nemůžeš dát na {self.top_card}! (Pro pokračování zmáčkni ENTER)")
        return card

    def show_top_card(self):
        print("\n" + f"Na vrcholu hromádky je karta {self.top_card}")


class HumanPlayer():
    def __init__(self):

        self.name = input(
            "Zdravím, vítej u snad všem známe hry prší, tentokrát ale v Pythonu!! Prosím zadej své jméno: ")
        self.card_deck = []

    def get_cards(self, deck, quantity=1):
        for i in range(0, quantity):
            self.card_deck.append(deck.pop(0))

    def show_cards(self):
        print("V ruce máš: ", end="")
        for card in self.card_deck:
            print(f"|{card}", end="")
        print("|")

    def put_card_into_pile(self, index):
        return self.card_deck.pop(index)


class PCPlayer():
    def __init__(self):
        self.card_deck = []

    def get_cards(self, deck, quantity=1):
        for i in range(0, quantity):
            self.card_deck.append(deck.pop(0))

    def show_cards(self):
        for card in self.card_deck:
            print(f"|{card}", end="")
        print("|")


def main():
    # init
    deck = Deck()
    human = HumanPlayer()
    pc = PCPlayer()
    pile = CardPile(deck.generated_deck)

    # get first 4 cards
    human.get_cards(deck.generated_deck, 4)
    pc.get_cards(deck.generated_deck, 4)

    deck.show_len()

    player_move = True
    pc_move = True

    while True:
        # win human
        if not len(human.card_deck):
            print(f"\nMusím prohlásit, že {human.name} je velice dobrým hráčem prší, gratuluji vyhrál jsi!!")
            break

        # win pc
        elif not len(pc.card_deck):
            print(
                f"Obávám se, že jsi prohrál, počítač má prázdnou ruku ale ty v ní máš ještě {' '.join(str(x) for x in human.card_deck)}!!")
            break

        # human player move
        while player_move:
            pc_move = True
            pile.show_top_card()
            human.show_cards()
            print(f"Počet karet tvého protivníka je {len(pc.card_deck)}!")
            user_input = input("Zadejte pořadí karty, kterou chcete odhodit nebo \"vzít\" pro kartu z hromádky: ")

            # user wanna get card
            if user_input == "vzít":
                human.get_cards(deck.generated_deck, 1)
                break

            # check if input is number
            try:
                int(user_input)
            except:
                print("!!Zadejte správně pořadí karty nebo \"vzít\"(př. \"2\" pro kartu druhou z leva)!!")
                continue

            # check user input index validity
            if int(user_input) - 1 > len(human.card_deck) or int(user_input) - 1 < 0:
                print("!!Zadal jsi špatné pořadí mimo možnosti!!")
                continue

            # cast off card
            returned_value = pile.put_card_on_top(deck.generated_deck, human.put_card_into_pile(int(user_input) - 1))

            # player put on top "attack" card
            if returned_value == 2 or returned_value == 4:
                pc.get_cards(deck.generated_deck, returned_value)

            # player casted off top ace
            elif returned_value == "pass cycle":
                pc_move = False

            # player casted off not valid card
            elif returned_value:
                human.card_deck.insert(int(user_input) - 1, returned_value)
            break

        # pc move
        while pc_move:
            player_move = True
            valid_card_found = False
            for card in pc.card_deck:
                if card[0] == pile.top_card[0] or card[1] == pile.top_card[1]:
                    returned_value = pile.put_card_on_top(deck.generated_deck, card)
                    pc.card_deck.remove(card)
                    # pc put on top "attack" card
                    if returned_value == 2 or returned_value == 4:
                        human.get_cards(deck.generated_deck, returned_value)

                    # pc casted off top ace
                    elif returned_value == "pass cycle":
                        player_move = False
                    valid_card_found = True
                    break
            if not valid_card_found:
                pc.get_cards(deck.generated_deck)
            #print(f"Počet karet v decku protivníka: { len(pc.card_deck) }")
            break



if __name__ == '__main__':
    main()
