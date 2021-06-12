from covid import Covid
from win32com.client import Dispatch

def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)

# covid = Covid()
covid = Covid(source="worldometers")

# To get all the data

# data=covid.get_data()
# print(data)

# To get all countries list
# countries = covid.list_countries()
# print(countries)

def stat(status):
    country = status['country']
    print(f'Getting COVID info of {country}')
    speak(f'Getting COVID info of {country}')

    confirmed = status['confirmed']
    print(f"Total confirmed cases are {confirmed} ")
    speak(f"Total confirmed cases are {confirmed} ")

    new_cases = status['new_cases']
    print(f" {new_cases} new cases found ")
    speak(f"{new_cases} new cases found")

    deaths = status['deaths']
    print(f"Total death cases are {deaths} ")
    speak(f"Total death cases are {deaths} ")

    recover = status['recovered']
    print(f"Total recover cases are {recover} ")
    speak(f"Total recover cases are {recover} ")

    active = status['active']
    print(f"Total active cases are {active} ")
    speak(f"Total active cases are {active} ")

    critical = status['critical']
    print(f"Total critical cases are {critical} ")
    speak(f"Total critical cases are {critical} ")

    recover = status['recovered']
    print(f"Total recover cases are {recover} ")
    speak(f"Total recover cases are {recover} ")

    new_deaths = status['new_deaths']
    print(f"Total new death cases are {new_deaths} ")
    speak(f"Total new death cases are {new_deaths} ")

    total_tests = status['total_tests']
    print(f" {total_tests} Total tests are done")
    speak(f" {total_tests} Total tests are done")

    population = status['population']
    print(f"Total population of this country {population} ")
    speak(f"Total population of this country {population} ")

# Getting total covid info
def tota():

    active = covid.get_total_active_cases()
    print(active)
    speak(f"The total covid active cases over the world are {active}")

    confirmed = covid.get_total_confirmed_cases()
    print(confirmed)
    speak(f"The total covid confirmed cases over the world are {confirmed}")

    recovered = covid.get_total_recovered()
    print(recovered)
    speak(f"The total covid recovered cases over the world are {recovered}")

    deaths = covid.get_total_deaths()
    print(deaths)
    speak(f"The total covid death cases over the world are {deaths}")

# Getting country wise
def countries(country):
    if (country=='India'):

        status = covid.get_status_by_country_name("India")
        # print(status)
        stat(status)

    elif (country=='China'):
        status = covid.get_status_by_country_name("China")
        stat(status)

    elif (country=='africa'):
        status = covid.get_status_by_country_name("africa")
        stat(status)

    elif (country=='usa'):
        status = covid.get_status_by_country_name("usa")
        stat(status)

    elif (country=='germany'):
        status = covid.get_status_by_country_name("germany")
        stat(status)

    elif (country=='europe'):
        status = covid.get_status_by_country_name("europe")
        stat(status)

# country=input("which country status : ")
# countries(country)