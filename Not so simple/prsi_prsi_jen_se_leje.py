import random


class Deck():
    def create_mixed_deck(self):
        pass

    def __init__(self):
        card_values = ["ESO", "2", "3", "4", "5", "6", "7", "8", "9", "10", "KLUK", "DÁMA", "KRÁL"]
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
        deck.append(self.top_card)
        self.top_card = card

    def show_top_card(self):
        print(f"Na vrcholu hromádky je karta {self.top_card}")


class HumanPlayer():
    def __init__(self):

        self.name = input("Tvé jméno: ")
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
    deck = Deck()
    human = HumanPlayer()
    pc = PCPlayer()
    pile = CardPile(deck.generated_deck)

    human.get_cards(deck.generated_deck, 4)
    pc.get_cards(deck.generated_deck, 4)

    deck.show_len()

    while True:
        if not len(human.card_deck):
            print(f"\nMusím prohlásit, že {human.name} je velice dobrým hráčem prší, gratuluji vyhrál jsi!!")
            break
        elif len(pc.card_deck):
            print(f"Ovávám se, že jsi prohrál, počítač má prázdnou ruku ale ty v ní máš ještě {' '.join(str(x) for x in human.card_deck)}!!")
            break
        human.show_cards()
        user_input = input("Zadejte pořadí karty, kterou chcete odhodit nebo \"vzít\" pro kartu z hromádky: ")

        try:
            pile.put_card_on_top(deck.generated_deck, human.put_card_into_pile(int(user_input) - 1))
        except:
            if user_input == "vzít":
                human.get_cards(deck.generated_deck, 1)
            else:
                print("!!Zadejte to správně!!\n")


if __name__ == '__main__':
    main()
