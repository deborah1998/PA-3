def inputfootball_numbers():
    float(input("Please enter the number of completions:"))
    float(input("Please enter the number of attempts:"))
    float(input("Please enter the number of passing yards:"))
    float(input("Please enter the number of touchdown passes"))
    return inputfootball_numbers()
def inputfencing_numbers():
    float(input("Please enter the number of fencing participants:"))
    float(input("Please enter the number of fencers ranked 1-8 in the World Cup Standings."))
    float(input("Please enter the number of fencers ranked 9-16 in the World Cup Standings."))
    float(input("Please enter the number of fencers ranked 17-32 in the World Cup Standings."))
    float(input("Please enter the number of fencers ranked 33-64 in the World Cup Standings."))
    float(input("Please enter the number of fencers ranked 65-100 in the World Cup Standings."))
    float(input("Please enter the number of fencers ranked 1-16 in the Junior World Cup Standings."))
    return inputfencing_numbers()
def inputgymnastics_numbers():
    float(input("Please enter the highest score for execution."))
    float(input("Please enter the lowest score for execution."))
    float(input("Please enter the third score for execution."))
    float(input("Please enter the fourth score for execution."))
    float(input("Please enter the fifth score for execution"))
    float(input("Please enter the sixth score for difficulty"))
    return inputgymnastics_numbers()
def quarterback_rating(completions,attempts,passingyards,touchdownpasses,interceptions):
    100 * [(5(completions / attempts - 0.3 )+ 0.25(passingyards / attempts - 3) + 20(touchdownpasses / attempts)+ 2.375-(25 * interceptions / attempts))] / 6
    return quarterback_rating()
def strength_factor(N,Sr8,Sr16,Sr32,Sr64,Sr100,Jr16):
    [ N / 10 + 7(Sr8) + 6(Sr16) + 5(Sr32) + 4(Sr64) + 3(Jr16) + 2(Sr100)] / 100
    return strength_factor()

