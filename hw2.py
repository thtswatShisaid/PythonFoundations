#!/usr/bin/env python
# Assignment 2

# Wrap all of the following in a single function definition, then invoke the function (no parameters are needed).
# Gather the following user inputs and store each item as a variable:
def dealership():
    name = input('Enter your name: firstname lastname')
    address = input('Enter your address: ')
    phone_number = input('Enter your phone number: XXX-XXX-XXXX')
    car_model = input('Enter your car make and model: ')
    price = input('Enter your purchase price: ')

    # After the user inputs the above information, your program should add the following values to the sale price:
    # Sales tax as a percent of sale price (10.1% combined rate for ZIP 98101)

    purchase_price = float(price)
    sales_tax = round(0.101 * purchase_price,2)
    licensing_fee = 50
    dealer_prep_fee = 50
    total_price = sales_tax + licensing_fee + dealer_prep_fee

    # Assign the transaction a unique ID composed of the last four letters of the purchaser's last name and their area code, separated by an underscore
    last_name = name.split(" ")[-1]
    last_name4 = last_name[-4:]
    area_code = phone_number.split("-")[0]
    unique_ID = last_name4 + "_" + area_code

    # Print out the information to the screen, with the same line breaks as shown in the example below
    sentence = "Hello {}! \n Thank you for your purchase of a {}. Following is a breakdown of your total price: " \
               "\n Sales Price: ${} \n Tax: ${} \n Licensing Fee: ${} \n Dealer Prep Fee: ${} \n Total Price: ${} " \
               "\n You have been assigned an ID number of {}. Please refer to this ID number if you have any questions :)".format(name,car_model,purchase_price,sales_tax,licensing_fee,dealer_prep_fee,total_price,unique_ID)
    print (sentence)

dealership()




