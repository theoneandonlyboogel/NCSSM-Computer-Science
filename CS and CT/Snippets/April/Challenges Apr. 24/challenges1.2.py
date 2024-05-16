"""
Expanded Weather Advisor Program with Temperature Advice
Objective:
Enhance your Weather Advisor program to provide clothing and activity suggestions based on the weather condition and temperature input by the user.
Tools Needed:
Basic knowledge of Python 2.
Understanding of if statements and handling user inputs.
Steps to Follow:
Ask for User Input:
Modify your program to also ask for the current temperature after getting the weather condition.
You'll need to ensure that the temperature input is a valid number.
Modify the Weather Dictionary:
Update your weather dictionary to include nested dictionaries for each weather condition, with keys for different temperature ranges.
Implement Temperature-Based Advice:
Based on the weather and temperature input, your program should decide what advice to give about clothing or activities.
"""
#clothing is an outdated term I used, it should be "recommendation", but I don't feel like changing like 40 strs.
#Weather conditions sourced from https://www.wunderground.com/history/monthly/us/nc/asheville/KAVL/date/2023-8
def clothing_recommendation(weather, temperature):
    recommendations = {
        "sunny": {
            "min_temp": {
                "range": "65°F - 75°F",
                "clothing": "A cooler sunny day. Thicker clothes would help a little during cold breezes. Great day for outdoor activities."
            },
            "avg_temp": {
                "range": "75°F - 90°F",
                "clothing": "An average sunny day. Typical summer clothing will do here, but please wear sunscreen. Amazing day for sports or other outdoor acitivites."
            },
            "max_temp": {
                "range": "90°F - 102°F",
                "clothing": "A hot summer day. Thin clothes and sunscreen will help a lot. Could be too hot for some more intensive sports."
            }
        },
        "foggy": {
            "min_temp": {
                "range": "40°F - 57°F",
                "clothing": "Temperature will feel a lot colder than it actually is. Thicker clothes like a down jacket are good here. Use fog lights."
            },
            "avg_temp": {
                "range": "57°F - 68°F",
                "clothing": "Temp will feel sharp and cold. Thicker clothes than ususal would be helpful. Please use fog lights when driving."
            },
            "max_temp": {
                "range": "68°F - 82°F",
                "clothing": "It will feel muggy and hot outside. Visibility will be poor, and thin clothes will go a long way. USE FOG LIGHTS!"
            }
        },
        "rainy": {
            "min_temp": {
                "range": "41°F - 62°F",
                "clothing": "Cold and wet outside, the perfect miserable combo! Rain jacket and extra layers will help a bunch. Be cautious on the road due to reduced traction."
            },
            "avg_temp": {
                "range": "62°F - 82°F",
                "clothing": "A normal rainy day. Normal clothing with a rain jacket should keep you dry. Be careful on the road."
            },
            "max_temp": {
                "range": "82°F - 91°F",
                "clothing": "A rare hot and rainy day. The outdoors will feel moist and hot, and that makes it feel hotter than it is. Go with thin clothing, or try to not go outside, because it's kind of miserable."
            }
        },
        "snowy": {
            "min_temp": {
                "range": "12°F - 24°F",
                "clothing": "Super cold winter day. Make sure to wear extra insulation and consider snow boots. Playing in the snow is the #1 activity for this."
            },
            "avg_temp": {
                "range": "24°F - 30°F",
                "clothing": "Pretty average snowy day. Wear extra layers and snow boots would help if the snow is deep. What else can you do other than play in the snow?"
            },
            "max_temp": {
                "range": "30°F - 38°F",
                "clothing": "How is the snow sticking? Anyway, wear more layers than normal, but normal shoes should suffice. Go play in the snow!"
            }
        }
    }

    if weather in recommendations:
        print("For {} weather and temperature {}°F:".format(weather.capitalize(), temperature))
        if temperature < 45:
            print("Recommendation: {}".format(recommendations[weather]["avg_temp"]["clothing"]))
        elif 15 <= temperature < 65:
            print("Recommendation: {}".format(recommendations[weather]["avg_temp"]["clothing"]))
        else:
            print("Recommendation: {}".format(recommendations[weather]["max_temp"]["clothing"]))
    else:
        print("Weather type not recognized.")

def main():
    weather = input("Enter the weather type. (Can be Sunny, Foggy, Rainy or Snowy): ").lower().strip()
    temperature = float(input("Enter the current temperature (in Fahrenheit): "))

    clothing_recommendation(weather, temperature)

main()