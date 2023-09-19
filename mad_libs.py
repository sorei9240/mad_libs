
def choose_madlib():
     """
    set_choice = input("Which madlibs would you like to do? /n)
    if set_choice == 1:
        place_range = 1
        adjective_range = 4
        verb_range = 0
        adverb_range = 0
        noun_range = 5
        ing_verb_range = 1
    elif set_choice == 2:
    """

def play_madlibs():
    place = []
    adjective = []
    present_verb = []
    past_verb = []
    adverb = []
    noun = []
    plural_noun = []
    exclaimation = []
    person = []
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

        print(f"""
        One {adjective[0]} morning, I woke up and decided to spend the day at the {place[0]}.
        I packed my {noun[0]}, {adjective[1]} {noun[2]}, and a delicious {noun[3]}. 
        As soon as I arrived, I was amazed by the {adjective[2]} scenery. 
        I spent the day {ing_verb[0]} and even saw a {noun[4]}! It was the most {adjective[3]} day ever.
        """)
        break

"""
One [adj] morning, I packed my [noun] and decided to [prsnt verb] at the beach. 
I walked [adv] through the sand and found a perfect [place] to lay down my [adj] towel. 
The waves were crashing, and the seagulls were flying overhead. 
I even saw a group of [pl noun] building a sandcastle.
I couldn't resist the temptation to go for a swim. 
I [pst verb] into the water and felt the [adj] waves splashing all around me. 
It was so refreshing! Afterward, I enjoyed a delicious picnic, and I couldn't help but shout, "[excl]!" 
The whole beach seemed to join in the celebration, and even [person] showed up to join the fun.
I spent [num] hours at the beach, and when it was time to leave, I felt like a happy [noun].

One [adj] day, my friends planned a surprise birthday party for me. 
They told me to meet them at the [place] and act completely surprised when I arrived. 
I [pst verb] to the venue, and when I walked in, everyone yelled, "[excl]!"
The room was decorated with [place] balloons and had a [adj] cake on the table.
My friends had even brought some [pl noun] to play games. We laughed, danced, and [pst verb] until late in the night. 
It was the most [adj] birthday ever!
It was a day I'll cherish forever, thanks to my wonderful friends, especially [person] who organized everything. 
I can't believe I'm now [num] years old!

One [adj] night, I decided to explore a [adj] haunted haunted. I entered the house, [prsnt verb] and looked [adv] around me. 
The first room I entered was the [adj] room, and it was filled with [pl noun].
As I walked through the house, I heard strange noises and felt a chill in the air. 
I could swear I saw a [noun] moving in the shadows. Suddenly, I [pst verb] and ran out of the house as fast as my [adj] legs could carry me, shouting, "[excl]!"
It turns out, the house was not just haunted; it was home to a [noun]! 
I'll never forget that 12-minute adventure in the spooky old house. I was so relieved when I finally made it back to my own [place].

"""

#play_madlibs() 