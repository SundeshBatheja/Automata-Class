class Automata:
    # kleenPlus Combinations
    def kleenComb(self, letter, inlang):
        # Language on which the elements are going to be made
        lang = inlang
        # array to store the combinations
        lis = []
        # iterating over langauge's characters and the passed character like ("")a = a
        for i in lang:
            lis.append(letter + i)
        return lis

    # Kleen function to send existing character to make new combinations like (a+b)(a+b) = aa ab ba bb
    def Kleen(self, emp, lim, inlang, lang=[" "], count=1):
        # list to store the combinations of the above functions
        lis = []
        for i in lang:
            # Calling kleen combination function to make new combination
            k = self.kleenComb(i, inlang)
            # once an iteration is over, the combinations which are made being added to the list of all combinations
            lis.extend(k)
        # limit of iteration like 1 to 10
        if count <= lim:
            # converting the list to a string
            emp.append(" ".join(lis))
            self.Kleen(emp, lim, inlang, lis, count + 1)
            # spliting the string from space=> " " and returning it in a list of elements
            return (" ".join(emp)).split()

    def ExtendedKleenPrint(self, lang):
        print("\n".join(lang))

    def KleenPrint(self, lang):
        lang.insert(0, "Lamda")
        print("\n".join(lang))
        lang.remove("Lamda")

    # Factorial
    def factorial(self, num):
        # Return the number if its equal to 0 or 1 as its factorial = 1 in both cases
        if num == 1 or num == 0:
            return num
        # Return the number * number-1 ....*1
        else:
            return num * self.factorial(num - 1)

    def power(self, num, exp):
        # if power = 0 then return 1
        if exp == 0:
            return 1
        # else return Number^power
        else:
            return num * self.power(num, exp - 1)

    def recfibon(self, numb):
        # if number is less than or equal to 1 return the number itself
        # base Case
        if numb <= 1:
            return numb
        else:
            # returning the recursive function
            return self.recfibon(numb - 1) + self.recfibon(numb - 2)

    def reverse(self, string):
        # if there is only one character left
        if len(string) == 0:
            return string
        # else take last character of the string and pass the string in function without it
        else:
            return string[-1] + self.reverse(string[:-1])

    def permutations(self, elems, curInd=0):
        if curInd == len(elems) - 1:
            # el.extend(elems)
            print("".join(elems))

        for i in range(curInd, len(elems)):
            # Swapping the elements
            temp = elems[curInd]
            elems[curInd] = elems[i]
            elems[i] = temp
            # recurrsive functions
            self.permutations(elems, curInd + 1)
            # Swapping the elements
            temp = elems[curInd]
            elems[curInd] = elems[i]
            elems[i] = temp

    def TransitionTable(self, initial, final, states):
        print("States Input(a) input(b)")

        for i in states:
            if i == initial:
                print(f"-{i} {states[i][0]} {states[i][1]}")

            elif i == final:
                print(f"+{i} {states[i][0]} {states[i][1]}")

            else:
                print(f" {i} {states[i][0]} {states[i][1]}")

        # Transition Function

    def delta(self, states, st):
        string = st

        # initial states
        initial = input("Enter initial State : ")
        final = input("Enter final State : ")

        # index to get input
        char = 0

        # loop will run on the length of string
        for i in range(len(string)):
            # first charcter of input if a then 0 or if b then 1
            if string[0] == "a" or string[0] == 0:
                initial = states[initial][0]
                # character by character removing after running of one input
                string = string[char + 1 : :]
            else:
                initial = states[initial][1]
                string = string[char + 1 : :]

        if initial == final:
            return f"{st} : Accepted at {initial} state"
        else:
            return f"{st} : rejected at {initial} state"

    def Palendrome(self, elem):
        return elem == elem[::-1]

    def NFAtoDFA(self):
        import pandas as pd

        nfa = {}
        states = int(input("number  of states : "))
        trans = int(input("number of transitions : "))
        for i in range(states):
            s_t = input("enter the state name : ")
            nfa[s_t] = {}
            for j in range(trans):
                path = input("path : ")
                print("Enter state from state {} at input {} : ".format(s_t, path))
                final_state = [x for x in input().split()]
                nfa[s_t][path] = final_state

        print("\nNFA :- \n")
        print(nfa)
        print("\nPrinting NFA table :- ")
        n_fa_t = pd.DataFrame(nfa)
        print(n_fa_t.transpose())

        n_fa_f_s = [x for x in input("Final state of NFA : ").split()]

        temp = []
        dfa = {}
        keys = list(list(nfa.keys())[0])
        keys2 = list(nfa[keys[0]].keys())

        dfa[keys[0]] = {}
        for i in range(trans):
            ele = "".join(nfa[keys[0]][keys2[i]])
            dfa[keys[0]][keys2[i]] = ele
            if ele not in keys:
                temp.append(ele)
                keys.append(ele)

        while len(temp) != 0:
            dfa[temp[0]] = {}
            for _ in range(len(temp[0])):
                for i in range(len(keys2)):
                    lst = []
                    for j in range(len(temp[0])):
                        lst += nfa[temp[0][j]][keys2[i]]
                    sub = ""
                    sub = sub.join(lst)
                    if sub not in keys:
                        temp.append(sub)
                        keys.append(sub)
                    dfa[temp[0]][keys2[i]] = sub
            temp.remove(temp[0])

        print("\n====DFA Transition ==== ")
        d_fa_t = pd.DataFrame(dfa)
        print(d_fa_t.transpose())

        d_fa_s_l = list(dfa.keys())
        d_fa_f_s = []
        for k in d_fa_s_l:
            for j in k:
                if j in n_fa_f_s:
                    d_fa_f_s.append(k)
                    break

        print("\nFinal states of the DFA : ", d_fa_f_s)


# Language on which the elements are going to be made
print("Welcome To Automata Class")
operation = int(
    input(
        """What Operation do you want to perform : \n1) Kleen \n2) Extended Kleen \n3) Factorial\n4) Exponent\n5) Fibonnaci Series\n6) reverse string
7) Permutations \n8) Transition Table of DFA \n9) Check Validation of string in you DFA.\n10) Palendrome\n11) NFAtoDFA \nEnter the number : """
    )
)
a = Automata()

if operation == 1 or operation == 2:
    language = input("Enter characters followed by a space : ").split()
    leng = int(input("Enter final length of the string : "))
    # List to store and return the elements of a language
    Elements = []
    # Function calling to make combinations of the language
    # kleen1=Kleen(Elements,leng,language)
    # calling function to print the language
    if operation == 1:
        a.KleenPrint(a.Kleen(Elements, leng, language))
    if operation == 2:
        a.ExtendedKleenPrint(a.Kleen(Elements, leng, language))

elif operation == 3:
    number = int(input("enter a number : "))
    print(f"Factorial of {number} is : {a.factorial(number)}")

elif operation == 4:
    # Calling function
    number = int(input("enter a number : "))
    exponent = int(input("enter a number to be exponent : "))
    print(f"{number} with the exponent of {exponent} is : {a.power(number,exponent)}")

elif operation == 5:
    numb = int(input("enter a number : "))
    print(f"Fibonnaci of {numb} Terms")
    for i in range(numb):
        print(a.recfibon(i), end=" ")

elif operation == 6:
    word = input("Enter a word to be reversed : ")
    print(f"the reverse of {word} is ", a.reverse(word))

elif operation == 7:
    num = input("Enter Number to be permutated : ")
    print(f"Permuatations of {num}")
    a.permutations(list(num))

elif operation == 8 or operation == 9:
    # States
    states = {}
    totalStates = int(input("Enter number of Total States : "))

    for i in range(totalStates):
        states[f"Q{i}"] = [
            input(f"States Q{i} at input 0 leads to: "),
            input(f"States Q{i} at input 1 leads to: "),
        ]

    if operation == 8:
        a.TransitionTable(
            input("Enter Initial State : "), input("Enter Final State : "), states
        )

    elif operation == 9:
        print(a.delta(states, input("enter string to be checked : ")))
        print(a.delta(states, input("enter string to be checked : ")))

elif operation == 10:
    st = input("enter string to be checked : ")
    print(f"Palendrome of {st} : ", a.Palendrome(st))

elif operation == 11:
    a.NFAtoDFA()
