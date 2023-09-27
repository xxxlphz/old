# africa_game
import time
countries = ['Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon', 'Central African Republic', 'Chad', 'Comoros', 'Ivory Coast', 'Djibouti', 'Democratic Republic of the Congo', 'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana', 'Guinea', 'Guinea-Bissau', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar', 'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria', 'Republic of the Congo', 'Rwanda', 'Sao Tome &Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa', 'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe' ]
named = []
print('---Countries of Africa---\n\n*Note: to check the countries you\'ve named, type \'named\'\n')
score = 0
while len(countries) >0:
    print('Number of countries to guess', len(countries))
    print('Score:',score)
    time.sleep(0.75)
    country = input('name a country in Africa ')
    if country in countries:
        print('Good guess')
        score += 1
        named.append(country)
        countries.remove(country)
        time.sleep(0.7)
    elif country == 'named':
        named.sort()
        print(*named)
    else:
        print('Invalid guess')
        print('Try again')
        time.sleep(0.7)
if len(countries) == 0:
    print('WOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\nGood game')
