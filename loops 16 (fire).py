rain = input("is it raining? ")
rain = rain.lower()

if rain == "yes":
    wind = input("Is it also windy? ")
    wind = wind.lower()
    if wind == "yes":
        print("\nits too windy for an umbrella just stay inside.")
    else:
        print ("\ntake an umbrellla with you.")
        
else:
    sunny = input("is it sunny then? ")
    sunny = sunny.lower()
    if sunny == "yes":
        v_sunny = input("is it REALLY sunny?? ")
        v_sunny = v_sunny.lower()
        if v_sunny == "yes":
            print("\nstay inside or you'll melt.")
        else:
            print("\n all good go out and chill lil bro")
        
    else:
        print("\nhave a nice day.")