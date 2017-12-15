from deck import StandardPlayingCardDeck
import poker_hands

def main():
    deck = StandardPlayingCardDeck()
    user_input = ''
    while user_input.lower() != 'q':
        deck.shuffle()
        hand = [deck.draw() for i in range(5)]
        hand = poker_hands.classify(hand)
        print(hand.__class__)
        print(hand)
        for card in hand:
            deck.insert_to_bottom(card)
        user_input = input('q to quit. Enter to continue')
        print()
        print('=' * 20)

if __name__ == '__main__':
    main()


