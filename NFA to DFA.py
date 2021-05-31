# Transition table = list of transitions(dictionaries), where index represents state no.

# # For taking input
# from makeNFA import make_nfa
# nfa = make_nfa()

nfa = [
    {'0':{0} , '1':{0,1}},
    {'0':{2}, '1':{2}},
    {'0':{}, '1':{}}
    ]
   
# inputs = ['0','1']
inputs = list(nfa[0])

# Perform move operation on a set of states and return the resultant set
def move(states,inp):
    ans = ""
    for state in states:
        for i in nfa[int(state)][inp]:
            if(str(i) not in ans):
                ans += str(i)
    return ans

# Check if two states are equal
def equal(st1,st2):
    for i in st1:
        if(i not in st2):
            return False
    for i in st2:
        if(i not in st1):
            return False
    return True

# Check if state is present in dfa already
def ispresent(st,dfa):
    for i in list(dfa):
        if(equal(i,st)):
            return True
    return False


dfa = dict()

def make_dfa(stateId):
    # Ex => stateId '01'
    dfa[str(stateId)] = transitions = dict() # Transitions of stateId = '01'

    # for all ch in inputs
    for ch in inputs:
        if(ch not in transitions):
            transitions[ch] = "" #  now in transitions {'0' : ''}
        
        st = move(stateId,ch) # Ex= > move('01','0')
        
        if(not ispresent(st,dfa)):
            make_dfa(st)
        
        transitions[ch] += st
    
    # Finally all transitions are added to dfa
    dfa[str(stateId)] = transitions


start = 0 # Start state
make_dfa(str(start))

# Printing
print("Input NFA =>")
print("Sno.\t\t"+"\t\t".join(inputs))
print()
for i in range(len(nfa)):
    st = ""
    for ch in inputs:
        st += f"\t\t{nfa[i][ch]}"
    print(f"{i}{st}")
print()
print("Output DFA =>")
print("Sno.\t\t"+"\t\t".join(inputs))
print()
for i in dfa:
    st = ""
    for ch in inputs:
        st += f"\t\t{dfa[i][ch]}"
    print(f"{i}{st}")