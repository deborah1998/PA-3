
# Programmer:Deborah Onyuka
# Course:CS201.01T, Dr. Olsen
# Date:[10/20/2016)
# Programming Assignment:PA3
# Problem Statement:Create a program that will calculate various sports statistics for the user, based on the user’s choice of statistic.
# Data In:A series of inputs to questions that will then be used in order to  calculate certain sports statistics.
# Data Out: The results of those specific calculations made by the users choice of statistic
# Credits:Class Notes  on functions and while loops




#Purpose:checks to see if the answer inputs a numeric value
#Parameters:prompt
#Return:the user's valid input converted to an int
def read_int(prompt):
    number = input("Please enter a number value:")
    if number.isdigit():
        return int(number)
    elif number!= number.isdigit():
        print("This is not a valid input!")
        return 0

#Purpose:Calculate the quarterback rating
#Parameters:none
#Return:the result of the quarterback calculations given the user's input
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

#Purpose:Calculate the strength factor for the fencing team
#Parameters:none
#Return:The result of the fencing calculation given the user's input
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
    while result > 2:
        print("The strength factor can not be higher than 2!")
        strength_factor()
    return result

#Purpose:To determine the highest gymnastics execution score
#Parameters:a,b,c,d,e(each score)
#Return:the maximum score

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

#Purpose:To determine the lowest gymnastics execution score
#Parameters:a,b,c,d,e(each score)
#Return:the minimum score

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

#Purpose:To calculate the final gymnastics score by adding all of the execution scores
# after dropping the highest and lowest scores and adding the difficulty  scores
#Parameters:[none]
#Return:The result of the final gymnastics score given the user's input


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


#Purpose:menu
#Parameters:none
#Return:The user's sports stat choice and the given calculation based on that choice
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

#Purpose:main
#Parameters:none
#Return:none
def main():
    menu()


main()



