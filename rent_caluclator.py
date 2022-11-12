rent= int(input("Enter your monthly rent: "))
grocery= int(input("Enter your grocery total: "))
utilities= int(input("Enter your utilities: "))
persons= int(input("Enter the numbers of person living: "))

total_bill=(rent+grocery+utilities)//persons

print("Each person will pay: ",total_bill)