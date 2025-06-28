# dictionary comprehension: create dictionaries using an expression
# can replace for loops and certain lambda functions
# dictionary = {key:expression for (key,value) in iterable}
# dictionary = {key:expression for (key,value) in iterable if conditional}
# dictionary = {key: (if/else) for (key,value) in iterable }
# dictionary = {key: function(value) for (key,value) in iterable }


# cities_in_F = {"new york": 32,"boston":75,
#                "los angeles":100,"chicago":50,"india":40}
# cities_in_C = {key: round((value-32)*(5/9)) for (key,value) in cities_in_F.items() }
# print(cities_in_C)

# weather ={'new york': "snowing",'boston':'sunny','los angeles':'sunny',
#           'chicago':"cloudy",'india':'snowing'}
# sunny_weather= {key: value for (key,value) in weather.items() if value=="sunny" }
# print(sunny_weather)
#
# cities = {"new york": 32,"boston":75,
#                "los angeles":100,"chicago":50,"india":40}
# desc_cities = {key: "sunny" if value >=50 else "cold" for (key,value) in cities.items() }
# print(desc_cities)


def check_temp(value):
    if value >=70:
        return "HOT"
    elif 69>= value >=40:
        return "WARM"
    else:
        return "COLD"
cities = {"new york": 32,"boston":75,
               "los angeles":100,"chicago":50,"india":40}
temp_cities = {key: check_temp(value) for (key,value) in cities.items()}
print(temp_cities)