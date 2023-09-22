

def play_madlibs():
    while True:
        set_choice = input("Which mad libs would you like to do? Press A, B or C \n").upper()
        if set_choice == "A":
            place_len = 1
            adj_len = 4
            pr_verb_len = 1
            pst_verb_len = 1
            noun_len = 2
            pl_noun_len = 1
            excl_len = 1
            person_len = 1
            num_len = 1
            break
        elif set_choice == "B":
            place_len = 1
            adj_len = 4
            pr_verb_len = 1
            pst_verb_len = 2
            noun_len = 1
            pl_noun_len = 1
            excl_len = 1
            person_len = 1
            num_len = 1
            break
        else:
            place_len = 1
            adj_len = 3
            pr_verb_len = 0
            pst_verb_len = 2
            noun_len = 2
            pl_noun_len = 1
            excl_len = 1
            person_len = 1
            num_len = 1
            break
    
    place = []
    adjective = []
    present_verb = []
    past_verb = []
    noun = []
    plural_noun = []
    exclaimation = []
    person = []
    number = []
    while True:
        for i in range(place_len):
            place_input = input("Please enter a place: \n")
            place.append(place_input)
        for i in range(adj_len):
            adjective_input = input("Please enter an adjective: \n")
            adjective.append(adjective_input)
        for i in range(pr_verb_len):
            pr_verb_input = input("Please enter a present tense verb: \n")
            present_verb.append(pr_verb_input)
        for i in range(pst_verb_len):
            pst_verb_input = input("Please enter a past tense verb: \n")
            past_verb.append(pst_verb_input)
        for i in range(noun_len):
            noun_input = input("Please enter a noun: \n")
            noun.append(noun_input)
        for i in range(pl_noun_len):
            pl_noun_input = input("Please enter a plural noun: \n")
            plural_noun.append(pl_noun_input)
        for i in range(excl_len):
            excl_input = input("Please enter an exclaimation: \n")
            exclaimation.append(excl_input)
        for i in range(person_len):
            person_input = input("Please enter a person: \n")
            person.append(person_input)
        for i in range(num_len):
            num_input = input("Please enter a number: \n")
            number.append(num_input)
        break
    def print_madlibs():
        if set_choice == "A":
        
            print(f"""
            One {adjective[0]} morning, I packed my {noun[0]} and decided to {present_verb[0]} at the beach. 
            I walked through the {adjective[1]} sand and found a perfect {place[0]} to lay down my {adjective[2]} towel. 
            The waves were crashing, and the seagulls were flying overhead. 
            I even saw a group of {plural_noun[0]} building a sandcastle.
            I couldn't resist the temptation to go for a swim. 
            I {past_verb[0]} into the water and felt the {adjective[3]} waves splashing all around me. 
            It was so refreshing! Afterwards, I enjoyed a delicious picnic, and I couldn't help but shout, "{exclaimation[0]}!" 
            The whole beach seemed to join in the celebration, and even {person[0]} showed up to join the fun.
            I spent {number[0]} hours at the beach and when it was time to leave, I felt as happy as a {noun[1]}.
            """)
        elif set_choice =="B":
            print(f"""
            One {adjective[0]} day, my friends planned a surprise birthday party for me. 
            They told me to {present_verb[0]} them at the {place[0]} and act completely surprised when I arrived. 
            I {past_verb[0]} to the venue, and when I walked in, everyone yelled, "{exclaimation[0]}!"
            The room was decorated with {adjective[1]} balloons and had a {adjective[2]} {noun[0]} on the table.
            My friends had even brought some {plural_noun[0]} to play games. We laughed, danced, and {past_verb[0]} until late in the night. 
            It was the most {adjective[3]} birthday ever!
            It was a day I'll cherish forever, thanks to my wonderful friends, especially {person[0]} who organized everything. 
            I can't believe I'm now {number[0]} years old!
            """)

        else:
            print(f"""
            One {adjective[0]} night, I decided to explore a haunted house with {person[0]}. 
            We entered the house, {past_verb[0]} and looked all around us. 
            The first room we entered was the {adjective[1]} room, and it was filled with {plural_noun[0]}.
            I could swear I saw a {noun[0]} moving in the shadows. 
            Suddenly, we heard a noise and {past_verb[1]} out of the house as fast as our {adjective[2]} legs could carry us, shouting, "{exclaimation[0]}!"
            Later I found out that the house was not just haunted; it was just home to a {noun[1]}! 
            I'll never forget that {number[0]} minute adventure in the spooky old house. 
            I was so relieved when I finally made it back to my own {place[0]}.
            """)
    print_madlibs()
    

play_madlibs() 