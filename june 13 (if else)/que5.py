# Nested if--

website=input("Enter website name: ").lower()

if website=="amazon" :
    print("Welcome to Amazon")
    website=input("enter product or service: ").lower()

    if website=="product" :
        website=input("Enter Clothes or Shoes: ").lower()

        if website=="clothes" :
            print("2000")

        elif website=="shoes" :
            print("1000")

        else :
            print("Invalid")

    elif website=="service" :
        print("Not Available")

    else :
        print("Invalid")

else :
    print("Invalid")