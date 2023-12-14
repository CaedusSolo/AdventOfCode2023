from collections import Counter, defaultdict
puzzle = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

data = puzzle.strip().split("\n")
cardsArr = []  # list containing tuples (hand,bid)
answer = 0

def getHandStrength(hand):

    hand = hand.replace("T",chr(ord('9')+1))
    hand = hand.replace("J",chr(ord('9')+2))
    hand = hand.replace("Q",chr(ord('9')+3))
    hand = hand.replace("K",chr(ord('9')+4))
    hand = hand.replace("A",chr(ord('9')+5))

    counter = Counter(hand)

    if list(counter.values()) == [5]:
        return (10, hand)

    elif sorted(counter.values()) == [1, 4]:
        return (9, hand)

    elif sorted(counter.values()) == [2, 3]:
        return (8,hand)

    elif sorted(counter.values()) == [1, 1, 3]:
        return (7,hand)

    elif sorted(counter.values()) == [1, 2, 2]:
        return (6,hand)
    
    elif sorted(counter.values()) == [1,1,1,2]:
        return (5,hand)

    elif sorted(counter.values()) == [1, 1, 1, 1, 1]:
        return (4,hand)
    

for hand in data:
    cards, bid = hand.split(" ")
    cardsArr.append((cards, bid))

cardsArr = sorted(cardsArr, key=lambda item:getHandStrength(item[0]))     

for index, (cards, bid) in enumerate(cardsArr):
    answer += (index+1) * int(bid)    # rank * bid

print(answer)