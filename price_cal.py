
#purchasing Details
purchasing_type = input("Type of purchasing: Enter Bag or Kg: " )
lower_purchasing_type = purchasing_type.lower()
print(lower_purchasing_type)



if(lower_purchasing_type == "bag"):
    # total_quantity_of_bags = int(input("Enter the Quantity of Total Bags"))
    purchasing_price_of_bag = int(input("Enter the price of a Bag: "))
    quantity_of_item_per_bag= int(input("Enter the quantity of items in kg per bag: "))
    
    # total_purchasing_cost_of_items = total_quantity_of_bags * purchasing_price_of_bag
    # print(f'Total cost of purchasing items in ruppes is {total_purchasing_cost_of_items}')
    price_per_kg = purchasing_price_of_bag / quantity_of_item_per_bag

    print(f'purchasing price per kg is {price_per_kg} rupees')
elif(lower_purchasing_type == "kg"):
    int(input("Enter the price of item in kg: "))

else:
    print("Enter a valid Value 'Bag or Kg'")


#Additional Costs
# labour_cost = 
# packaging_cost =
# transportation_cost = 


grade_b_quantity= int(input("What is Quantity of grade B: "))
grade_c_quantity= float(input("What is Quantity of grade C: "))
grade_d_quantity = int(input("What is Quantity of grade D: "))
grade_a_quantity = (quantity_of_item_per_bag - (grade_b_quantity + grade_c_quantity + grade_d_quantity ))

print(f'Quantity of grade A is: {grade_a_quantity}')
print(f'Quantity of grade B is: {grade_b_quantity}')
print(f'Quantity of grade C is: {grade_c_quantity}')
print(f'Quantity of grade D is: {grade_d_quantity}')





#Selling price for per kg

price_of_grade_b = int(input("Enter the price per kg of grade B in ruppes: "))
price_of_grade_c = int(input("Enter the price per kg of grade C in ruppes: "))
price_of_grade_d = int(input("Enter the price per kg of grade D in ruppes: "))
# price_of_grade_a = (purchasing_price_of_bag - (price_of_grade_b + price_of_grade_c + price_of_grade_d))

#Total cost of items as per grades
# total_cost_grade_a = price_of_grade_a * grade_a_quantity
total_cost_grade_b = price_of_grade_b * grade_b_quantity
total_cost_grade_c = price_of_grade_c * grade_c_quantity
total_cost_grade_d = price_of_grade_d * grade_d_quantity
total_cost_of_b_c_d = (total_cost_grade_b + total_cost_grade_c + total_cost_grade_d)

total_purchasing_cost_for_grade_a = (purchasing_price_of_bag - total_cost_of_b_c_d)
print(f'Total purchasing cost for grade a is {total_purchasing_cost_for_grade_a} befor additional cost')
total_purchasing_cost_for_grade_a_in_kg = total_purchasing_cost_for_grade_a / grade_a_quantity

print(f'Selling price per kg for Grade A items is {total_purchasing_cost_for_grade_a_in_kg} befor anyadditional cost')


# per_kg_price_for_grade_a = 

# print(f'Quantity of grade A is {grade_a_quantity} total price of Grade A items is {price_of_grade_a * grade_a_quantity}')
print(f'Total price of Grade B items is {price_of_grade_b * grade_b_quantity}')
print(f'Total price of Grade C items is {price_of_grade_c  * grade_c_quantity}')
print(f'Total price of Grade D items is  {price_of_grade_d * grade_d_quantity}')
