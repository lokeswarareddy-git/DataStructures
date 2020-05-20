"""
Use the Stack to check weather or not a string has balanced usage of paranthasis 
Examples :
(),()(),(({[]}))<-- Balanced 
((),{{)}},[][[]]]  <-- Not balanced 

Balanced Ex:  
"""

from stack import Stack
def is_match(p1,p2):
    if p1=="(" and p2 == ")":
        return True
    elif p1=="{" and  p2=="}":
        return True
    elif p1=="[" and p2 =="]":
        return True
    else:
        return False

def is_paran_balanced(paran_string):
    s=Stack()
    is_balanced = True
    index=0
    while index < len(paran_string) and is_balanced:
        paran=paran_string[index]
        if paran in "{[(":
            s.push(paran)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top=s.pop()
                if not is_match(top,paran):
                    is_balanced= False
        index +=1
    if s.is_empty() and is_balanced:
        return True
    else:
        return False





if __name__ == "__main__":
    print(is_paran_balanced("[()]"))
