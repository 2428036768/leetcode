"""
柠檬水找零
简单
"""

def lemonadeChange(bills):
    five=0
    ten=0
    for i in bills:
        if i==5: five+=1
        elif i==10: five-=1; ten+=1
        else: 
            if ten>0:
               ten-=1
               five-=1
            else:
                five-=3

        if ten<0 or five<0:
            return False
    return True

bills = [5,5,10,20]
print(lemonadeChange(bills))
            