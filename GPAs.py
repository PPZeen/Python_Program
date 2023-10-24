ans = {}
n = int(input("Modules: "))
k = 0
while k < n :
    x = input("Gen Module Grade 6ex. (Phys 3 B+): ") # Phys 3 B+
    y = x.split()
    ans[y[0]] = [int(y[1]),y[2]]
    k += int(y[1])
    
def change(x) :
    if x == "A" : return float(4)
    elif x == "B+" : return float(3.5)
    elif x == "B" : return float(3)
    elif x == "C+" : return float(2.5)
    elif x == "C" : return float(2)
    elif x == "D+" : return float(1.5)
    elif x == "D" : return float(1)
    return float(0)

def point2Grade(x):
    x = float(x)
    if x >= 80 : print("A")
    elif x >= 75 : print("B+")
    elif x >= 70 : print("B")
    elif x >= 65 : print("C+")
    elif x >= 60 : print("C")
    elif x >= 55 : print("D+")
    elif x >= 50 : print("D")
    else : print("F")
    
for keys in ans :
    ans[keys][1] = change(ans[keys][1])
sum_credit = 0
multiple = 0
for key in ans :
    sum_credit += ans[key][0]
    multiple += ans[key][0]*ans[key][1]

print(round(multiple/sum_credit,2))