marks=45
maxmarks=90
#percentage=(marks/maxmarks)*100
#print(percentage)
def percentcalculate(marks,maxmarks):
    percentage = (marks / maxmarks) * 100
    return percentage

def displaypercent(percentage):
    print(f"percentage is : ",percentage)

def calculategrade(percentage):
    g=" "
    if percentage>=90:
        g="A"
    elif percentage<90 and percentage>=80 :
        g="B"
    elif percentage<80 and percentage>=70 :
        g="C"
    elif percentage<70 and percentage>=60 :
        g="D"
    else:
        g="F"

    return g

def displaygrade(g):
    print(f"grade is : ",g)


p=percentcalculate(marks,maxmarks)
displaypercent(p)
g=calculategrade(p)
displaygrade(g)