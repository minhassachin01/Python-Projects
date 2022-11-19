
stock = [['Id', 'Model', 'Make', 'Year','Miles', 'Insurance Claimed','Price', 'Discount', 'Price After Discount'],
            [125, 'Camry', 'Toyota',2008,125000,'No',25000, 10, 22500]]

def export_txt():
    count = 0;
    text_file = open("car.txt", "w")
    for record in stock:
        text_file.write(str(record)+'\n')
    print("file exported successfully \n")
def read_txt():
    text_file = open("car.txt", "r")
    print(text_file.read())
    text_file.close()
def add_car():
    car_id = int(input("Enter car id (integers only): "))
    car_name = input("Enter the name of car: ")
    manf = input("Enter Company info: ")
    make_year = input("Enter year of make: ")
    driven = input("Enter miles driven: ")
    claim = input("Is there any insurance claim (yes/no): ")
    price = float(input("Enter the price of car: "))
    discount = float(input("Enter discount on product in percent: "))
    total_price = price - price*(discount/100)
    stock.append([car_id, car_name, manf, make_year,driven,claim, price, discount, total_price])
    print("success. \n")
    choice=input("Do you want to add another car? (Y/N) :")
    if choice == 'Y' or choice == 'y' or choice == 'N' or choice == 'n':
        if choice == 'Y' or choice == 'y':
            add_car()
        if choice == 'N' or choice == 'n':
            return
def menu():
    while True:
        print('\n1.     View All Cars in Stock\n2.     Add new car\n3.     Export stock data\n4.     Read Text File\n5.     Exit\n')
        user_input =int(input("Enter your choice (1/2/3/4/5): "))
        while True:
            if user_input <=5 and user_input >0:
                break
            else:
                user_input = int(input("Please enter a option: "))
        if user_input == 1:
            count = 0
            for r in stock:
                if count == 0 :
                    print("\n","_" * 190)
                print(" %10s  %-20s %-25s %-25s %-25s %15s %15s %15s %25s " % (
                    r[0], r[1], r[2], r[3], r[4], r[5], r[6],r[7],r[8]))
                if count == 0 :
                    print( "_" * 190)
                count +=1
            print('\n')
        if user_input == 2:
            add_car()
        if user_input == 3:
            export_txt()
        if user_input == 4:
            read_txt()
        if user_input == 5:
            print("Thank You")
            break
def main():
    print('\n','_'*40,'\n')
    print("\t ******* Sachin ****** \n\t****** Car Bazar *******")
    print('_'*40)
    menu()
main()