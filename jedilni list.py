print("Welcome to daily menu editor")

menu_txt = dict()

while True:
    answer = raw_input("Do you want to add menu(yes/no)? ")
    if answer == "no":
        break
    if answer == "yes":

        menu = raw_input("Enter your menu: ")
        
        price = raw_input("Enter a price: ")

        menu_txt[menu] = price 

        print("Your menu is " + menu + " and price of this menu is " + price)

print("Your menu: ")

for i in menu_txt:
    print("* " + i + ", price: " + menu_txt[i])
