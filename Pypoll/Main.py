candylist =["snockers","kit kat","sour patch","juicy fruit","Swedish Fish", "skitles","hershey bar", "Starbust","M&M"]
allowance = 5
candycart = []

for x in candylist:
    print ("[" + str(candylist.index(x))+"]"+ x)

for i in range(allowance):
    kid_choice= int(input("which candy would you like to bring home?"))
    candycart.append(candylist[kid_choice])

for candy in candycart:
    print(candy)



