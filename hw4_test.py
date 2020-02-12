import unittest
import hw4_cards as cards

#########################################
##### Name: Daniel Vasquez       #####
##### Uniqname: Danvas           #####
#########################################

## You can write any additional debugging/trying stuff out code here...
## OK to add debugging print statements, but do NOT change functionality of existing code.
## Also OK to add comments!

class TestCard(unittest.TestCase):
    def test_0_create(self):
        card = cards.Card()
        self.assertEqual(card.suit_name, "Diamonds")
        self.assertEqual(card.rank, 2)

    # Add methods below to test main assignments. 
    def test_1_queen(self):
        # If a card with rank 12 is created, rank_name = "Queen"
        c1 = cards.Card(rank=12)
        self.assertEqual(c1.rank_name, "Queen")

    def test_2_Clubs(self):
        # Test that if you create a card instance with suit 1, its suit_name will be "Clubs"
        c2 = cards.Card(suit=1)
        self.assertEqual(c2.suit_name, "Clubs")

    def test_3_king_of_spade(self):
        # Test that if you invoke the __str__ method of a card instance that is created with suit=3, rank=13, it returns the string "King of Spades"
        c3 = cards.Card(suit=3, rank=13)
        self.assertEqual(c3.__str__(), "King of Spades")

    def test_4_deck(self):
        # Test that if you create a deck instance, it will have 52 cards in its cards instance variable
        d0 = cards.Deck()
        self.assertEqual(len(d0.cards), 52)

    def test_5_deckcard(self):
        # Test that if you invoke the deal_card method on a deck, it will return a card instance.
        d1 = cards.Deck().deal_card()
        self.assertIsInstance(d1, cards.Card)

    def test_6_decklen(self):
        # Test that if you invoke the deal_card method on a deck, the deck has one fewer cards in it afterwards.
        d2 = cards.Deck()
        primary_len = len(d2.cards)
        _ = d2.deal_card()
        updated_len = len(d2.cards)

        self.assertEqual(primary_len-1, updated_len)

    def test_7_replace(self):
        #Test that if you invoke the replace_card method, the deck has one more card in it afterwards.
        # #(Please note that you want to use deal_card function first to remove a card from the deck and then add the same card back in)
        d3 = cards.Deck()
        primary_len =  len(d3.cards) # 52 Total
        card = d3.deal_card()
        d3.replace_card(card)
        updated_len = len(d3.cards) # 51 -> 52 updated total

        self.assertEqual(primary_len, updated_len)

    def test_8_already(self):
        # Test that if you invoke the replace_card method with a card that is already in the deck, the deck size is not affected.
        # (The function must silently ignore it if you try to add a card that’s already in the deck)
        d4 = cards.Deck()
        primary_len = len(d4.cards) # 52 Total

        card = cards.Card(suit=3, rank=13)
        self.assertEqual(card.__str__(), d4.cards[-1].__str__()) # Check the card in the deck

        d4.replace_card(card)
        updated_len = len(d4.cards)

        self.assertEqual(primary_len, updated_len)


############
### The following is a line to run all of the tests you include:
if __name__ == "__main__":
    unittest.main()
