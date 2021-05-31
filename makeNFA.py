def make_nfa():
    inputs = input("Enter possibe inputs separated by spaces : ").split()
    n = int(input("Enter no. of states : "))
    nfa = [{} for i in range(n)]
    print("Enter transitions in order of inputs separated by spaces ('_' for null) : ")
    for i in range(n):
        print(f"For q{i} : ",end="")
        lst = input().split()
        for j in range(len(lst)):
            if(lst[j]=="_"):
                nfa[i][inputs[j]] = {}
            else:
                nfa[i][inputs[j]] = set([int(i) for i in lst[j]])
    print()
    return(nfa)
    