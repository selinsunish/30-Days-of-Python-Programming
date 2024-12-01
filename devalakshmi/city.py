city = input("Enter the city name (Delhi, Agra, Jaipur): ").strip().lower()

if city == "delhi":
    print("Monument in Delhi: Red Fort")
elif city == "agra":
    print("Monument in Agra: Taj Mahal")
elif city == "jaipur":
    print("Monument in Jaipur: Jai Mahal")
else:
    print("Sorry, monument information is not available for this city.")
