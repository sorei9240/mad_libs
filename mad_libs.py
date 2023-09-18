#import random


def play_madlibs():
    place = []
    adjective = []
    verb = []
    adverb = []
    noun = []
    ing_verb = []
    while True:
        for i in range(1):
            place_input = input("Please enter a place: \n")
            place.append(place_input)
        for i in range(4):
            adjective_input = input("Please enter an adjective: \n")
            adjective.append(adjective_input)
        for i in range(0):
            verb_input = input("Please enter a verb: \n")
            verb.append(verb_input)
        for i in range(0):
            adverb_input = input("Please enter an adverb: \n")
            adverb.append(adverb_input)
        for i in range(5):
            noun_input = input("Please enter a noun: \n")
            noun.append(noun_input)
        for i in range(1):
            ing_verb_input = input("Please enter a verb ending in -ing: \n")
            ing_verb.append(ing_verb_input)

        print(f"One {adjective[0]} morning, I woke up and decided to spend the day at the {place[0]}.")
        print(f"I packed my {noun[0]}, {adjective[1]} {noun[2]}, and a delicious {noun[3]}.") 
        print(f"As soon as I arrived, I was amazed by the {adjective[2]} scenery.") 
        print(f"I spent the day {ing_verb[0]} and even saw a {noun[4]}! It was the most {adjective[3]} day ever.")
        break
play_madlibs()