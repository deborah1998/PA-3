
def read_int(prompt):
    number = input("Please enter a number value:")
    if number.isdigit():
        return int(number)


def quarterback_rating():
    completions=(input("Please enter the number of completions:"))
    completions=read_int(completions)

    attempts=(input("Please enter the number of attempts:"))
    attempts=read_int(attempts)

    #error checking if user inputs zero for attempts  because you can't divide by zero
    while attempts <= 0:
        print("This is an invalid input.You cant have zero or less attempts!")
        attempts = (input("Please enter the number of attempts:"))
        attempts = read_int(attempts)

    passingyards=(input("Please enter the number of passing yards:"))
    passingyards=read_int(passingyards)

    touchdownpasses=(input("Please enter the number of touchdown passes:"))
    touchdownpasses=read_int(touchdownpasses)

    interceptions=(input("Please enter the number of interceptions:"))
    interceptions=read_int(interceptions
                           )
    result=(100 * ((5*(completions / attempts - 0.3 )+ 0.25*(passingyards / attempts - 3) + 20*(touchdownpasses / attempts)+ 2.375-(25 * interceptions / attempts))) / 6)

    if result >= 158.3:
        print("The quarterback rating of this player is", result, "They are a perfect passer!")

    elif result < 158.3 and result >=0:
        print("The quarterback rating of this player is", result, "They are not a perfect passer!")

    else:
        print("The quarterback rating of this player is", result,"that is an invalid answer you gave bad input!")
        return result

def strength_factor():
    N=(input("Please enter the number of fencing participants:"))
    N=read_int(N)
    Sr8=(input("Please enter the number of fencers ranked 1-8 in the World Cup Standings."))
    Sr8=read_int(Sr8)
    Sr16=(input("Please enter the number of fencers ranked 9-16 in the World Cup Standings."))
    Sr16=read_int(Sr16)
    Sr32=(input("Please enter the number of fencers ranked 17-32 in the World Cup Standings."))
    Sr32=read_int(Sr32)
    Sr64=(input("Please enter the number of fencers ranked 33-64 in the World Cup Standings."))
    Sr64=read_int(Sr64)
    Sr100=(input("Please enter the number of fencers ranked 65-100 in the World Cup Standings."))
    Sr100=read_int(Sr100)
    Jr16=(input("Please enter the number of fencers ranked 1-16 in the Junior World Cup Standings."))
    Jr16=read_int(Jr16)
    result=(((N / 10 )+ (7* Sr8) + (6*Sr16) + (5*Sr32) + (4 *Sr64) + (3*Jr16) + (2*Sr100)) /(100))
    print("The strength factor for the U.S Fencing team is",result)
    return result


def gymnastics_max(a,b,c,d,e):

    if a >= b and a >= c and a >= d and a >= e:
        return a
    elif b >= a and b >= c and b >= e and b >=d:
        return b
    elif c >= a and c >= b  and c >=d and c >= e:
        return c
    elif d >= a and d >= b and d>=c and d>=e:
        return d
    elif e >= a and e >= b and e >=c and e>=d:
        return e

    return gymnastics_max(a,b,c,d,e)

def gymnastics_min(a,b,c,d,e):
    if a <= b and a <= c and a <= d and a <= e:
        return a
    elif b <= a and b <= c and b <= e and b <=d:
        return b
    elif c <= a and c <= b  and c <= d and c <= e:
        return c
    elif d <= a and d <= b and d <= c and d <= e:
        return d
    elif e <= a and e <= b and e <= c and e <= d:
       return e


def gymnastics_calculation():
    a=float(input("Please enter the first score for execution:"))
    b=float(input("Please enter the second score for execution:"))
    c=float(input("Please enter the third score for execution:"))
    d=float(input("Please enter the fourth score for execution:"))
    e=float(input("Please enter the fifth score for execution:"))
    f=float(input("Please enter the sixth score for difficulty:"))
    min = gymnastics_min(a, b, c, d, e)
    max = gymnastics_max(a, b, c, d, e)
    result = float(a+b+c+d+e - (max+min))/3+(f)
    print("The final gymnastics score is", result )
    return result





def menu():
    print("Please choose the sport you would like to get stats for your choices are football,fencing and gymnastics")
    choice=input("Enter your choice of sport:")
    if choice.lower() =="football":
        quarterback_rating()
    elif choice.lower() == "fencing":
        strength_factor()
    elif choice.lower()=="gymnastics":
        gymnastics_calculation()

    return choice

def main():
    menu()


main()

