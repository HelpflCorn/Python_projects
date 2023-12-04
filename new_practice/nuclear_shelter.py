# Write a function that accepts battlefield string and returns letters that survived
# the nuclear strike.

# The battlefield string consists of only small letters, #,[ and ].
# The nuclear shelter is represented by square brackets []. 
# The letters inside the square brackets represent letters inside the shelter.
# The # means a place where nuclear strike hit the battlefield. 
# If there is at least one # on the battlefield, all letters outside of shelter die.
# When there is no any # on the battlefield, all letters survive 
# (but do not expect such scenario too often ;-P ).
# The shelters have some durability. When 2 or more # hit close to the shelter, 
# the shelter is destroyed and all letters inside evaporate. 
# The 'close to the shelter' means on the ground between the shelter and the next shelter (or beginning/end of battlefield). 
# The below samples make it clear for you.

def alphabet_war(battlefield):
    for i in battlefield:
        if i.isdigit() or i.isupper():
            return "Should consist of only small letters, #,[ and ]"
        
    
    
    
print(alphabet_war("he#llo[there]"))   
    
         