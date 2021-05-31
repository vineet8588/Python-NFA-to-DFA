# Python-NFA-to-DFA
A simple python program for converting a give NFA transition table into DFA


To take NFA as user input , uncomment line 3-5 in `NFA to DFA.py` and comment or remove the given NFA list.


NFA Transition table is represented by a list of dictionaries, where array index represents state number and the dictionaries represents the possible transitions from that state.


DFA Transition table is represented by a dictionary, with key : State No. as string,<br/>
and values : Again a dictionary representing the possible transitions from that state.
