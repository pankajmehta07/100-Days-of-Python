import random


word_list = ['abruptly','absurd','abyss','affix','askew','avenue','awkward','axiom','azure','bagpipes','bandwagon','banjo','bayou','beekeeper','bikini','blitz','blizzard', 'boggle','bookworm','boxcar','boxful','buckaroo','buffalo','buffoon','buxom','buzzard',
'buzzing','buzzwords','cobweb','cockiness','caliph','croquet','crypt','curacao','cycle','daiquiri','dirndl','disavow','dizzying','duplex','dwarves','embezzle','equip','espionage','euouae','exodus', 
'faking','fishhook','fixable','fjord','flapjack','flopping','fluffiness','flyby','foxglove','frazzled','frizzled','fuchsia','funny','gabby','galaxy','galvanize','gazebo','giaour','gizmo', 
'glowworm','glyph','gnarly','gnostic','gossip','grogginess','haiku','haphazard','hyphen','iatrogenic','icebox','injury','ivory','ivy','jackpot','jaundice','jawbreaker', 
'jaywalk','jazziest','jazzy','jelly','jigsaw','jinx','jiujitsu','jockey','jogging','joking','jovial','joyful','juicy','jukebox','jumbo','kayak', 
'kazoo','keyhole','khaki','kilobyte','kiosk','kitsch','kiwifruit','klutz','knapsack','larynx','lengths','lucky','luxury', 
'lymph','marquis','matrix','megahertz','microwave','mnemonic','mystify','naphtha','nightclub','nowadays','numbskull','nymph','onyx','ovary','oxidize','oxygen','pajama','peekaboo','phlegm','pixel','pizazz','pneumonia','polka','pshaw', 
'psyche','puppy','puzzling','quartz','queue','quips','quixotic','quiz','quizzes','quorum','razzmatazz','rhubarb','rhythm','rickshaw','schnapps','scratch','shiv','snazzy','sphinx','spritz','squawk','staff','strength','strengths','stretch','stronghold','stymied', 
'subway','swivel','syndrome','thriftless','thumbscrew','topaz','transcript','transgress','transplant','triphthong','twelfth','twelfths','unknown','unworthy', 
'unzip','uptown','vaporize','vixen','vodka','voodoo','vortex','voyeurism','walkway','waltz','wave','wavy','waxy', 
'wellspring','wheezy','whiskey','whizzing','whomever','wimpy','witchcraft','wizard','woozy','wristwatch','wyvern', 
'xylophone','yachtsman','yippee','yoked','youthful','yummy','zephyr','zigzag','zigzagging','zilch','zipper','zodiac','zombie',]

stages = [
"""
 +--+
 |  |
    |
    |
    |
    |
=====            
          
""",
"""
 +--+
 |  |
 O  |
    |
    |
    |
=====            
          
""",
"""
 +--+
 |  |
 O  |
 |  |
    |
    |
=====            
          
""",
"""
 +--+
 |  |
 O  |
/|  |
    |
    |
=====            
          
""",
"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====              
          
""",
"""
 +--+
 |  |
 O  |
/|\ |
    |
        |
=====             
          
""",
"""
 +--+
 |  |
 O  |
/|\ |
    |
    |
=====             
          
""",
"""
 +--+
 |  |
 O  |
/|\ |
/ \ |
    |
=====             
          
"""
]

missed = []
word = list(random.choice(word_list).upper())
won = False
print("\n\n\t\t\tHangman\n\n")
print(stages[0])
guessed = list("_"*len(word))
counter = 1
while counter<len(stages):
    print("Missed Letters:\t"," ".join(missed))
    print("\n"," ".join(guessed))
    guess =input("\nGuess a letter:\t").strip()[0].upper()
    if guess in word:
        for letter in range(len(guessed)):
            if guess==word[letter]:
                guessed[letter]=guess

    else:
        missed.append(guess)
        print(stages[counter])
        counter +=1
    if "_" not in guessed:
        word = " ".join(word)
        print(f"Yes! The secrect word is: {word}\nYou have won!")
        won = True
        break
        

if not won:
    word = " ".join(word)
    print(f"\nYou Lost!!!\nThe secrect word was: {word}")