import streamlit as st

st.title("VillaMart Price Calculator")
st.subheader("Calculte the price of Potato")

user_choice = st.text_input("Type Here", placeholder = "Enter Your Purchasing Type: 'Bag or Kg'")
user_choice_lower = user_choice.lower()

if(user_choice_lower == "bag"):
    bag_price = st.number_input("Enter Bag Price", placeholder ="Enter the price of a Bag: ", value = 1)
    bag_weight = st.number_input("Enter Bag weight", placeholder = "Enter the weight of Bag in Kg: ", value=1)
    price_per_kg = (bag_price / bag_weight)
    st.write(price_per_kg)

    st.write(f'Purchasing cost per kg in ruppes before grading: {price_per_kg}')
elif(user_choice == "kg"):
    item_price_kg = st.number_input("Enter the price of items in Kilogram", value = 1)
    item_weight_kg = st.number_input("Enter the weight of total items in Kilogram", value = 1)
    items_total_price = (item_price_kg * item_weight_kg)
    st.write(f'Item total price in ruppes: {items_total_price}')
else:
    st.text("Enter a valid Value 'Bag or Kg'")

    
        
logestic_cost = float(1)
loading_cost = float(0.70)
sorting_cost = float(0.50)
additional_cost = float(loading_cost + loading_cost + sorting_cost)

# Item Grading


st.subheader("Grade wise Quantities ")
# grade_b_quantity = st.number_input("Quantity of Grade B", placeholder="Enter the quantity of grade B items in Kg")
grade_b_quantity = st.number_input("Quantity of Grade B", placeholder="Enter the quantity of grade B items in Kg")
grade_c_quantity = st.number_input("Quantity of Grade C", placeholder="Enter the quantity of grade C items in Kg")
grade_d_quantity = st.number_input("Quantity of Grade D", placeholder="Enter the quantity of grade D items in Kg")
total_weight_grade_b_c_d = (grade_d_quantity + grade_b_quantity + grade_c_quantity)
if (user_choice == "bag"):
    grade_a_quantity = bag_weight - total_weight_grade_b_c_d

    # grade_b_percentage = st.number_input("Enter the percentage of Grade B")
    # grade_b_quantity_percentage = (bag_weight * grade_b_percentage) / 100
    # st.write(grade_b_quantity_percentage)
elif(user_choice == 'kg'):
    grade_a_quantity = item_weight_kg - total_weight_grade_b_c_d
    st.write(f'Quantity of grade A is: {grade_a_quantity}')

    # grade_b_percentage = st.number_input("Enter the percentage of Grade B")
    # grade_b_quantity_percentage = (item_weight_kg * grade_b_percentage) / 100
    # st.write(grade_b_quantity_percentage)

else:
    st.write("Provide a valid input")



def item_grading():
    
    if (user_choice_lower == "bag"):
        if (total_weight_grade_b_c_d > bag_weight):
             st.write("Quantity of items can't be more than the quantity of bag")
        elif(total_weight_grade_b_c_d <= bag_weight):
             grade_a_quantity = (bag_weight - total_weight_grade_b_c_d)
             st.write(f'Quantity of grade A is: {grade_a_quantity}')
                 
    elif(user_choice_lower == "kg"):
        if (total_weight_grade_b_c_d > item_weight_kg):
             st.write("Quantity of items can't be more than the quantity of bag")
        elif(total_weight_grade_b_c_d <= item_weight_kg):
             grade_a_quantity = (item_weight_kg - total_weight_grade_b_c_d)
             st.write(f'Quantity of grade A is: {grade_a_quantity} kg')
item_grading()




#purchasing cost of grade A

st.subheader("Grade Wise selling price per kg")
grade_b_price = st.number_input("Enter the selling price per kg for Grade B")
st.write(f'Final selling cost for garde B after adding additional cost: :green[{grade_b_price}]')
grade_c_price = st.number_input("Enter the selling price for Grade C")
grade_d_price = st.number_input("Enter the selling price for Grade D")



#Total purchasing cast as per grade
Total_cost_grade_b = grade_b_quantity * grade_b_price
st.write(Total_cost_grade_b)
Total_cost_grade_c = grade_c_quantity * grade_c_price
st.write(Total_cost_grade_c)
Total_cost_grade_d = grade_d_quantity * grade_d_price
st.write(Total_cost_grade_d)
def grade_a_total_cost():

    if user_choice == "bag":
        garde_a_total_cost = bag_price - (Total_cost_grade_b + Total_cost_grade_c + Total_cost_grade_d)
        return garde_a_total_cost
    elif(user_choice == "kg"):
        garde_a_total_cost = items_total_price - (Total_cost_grade_b + Total_cost_grade_c + Total_cost_grade_d)
        return garde_a_total_cost
grade_a_total_cost()
st.write(f'Total cost for Grade A is {grade_a_total_cost()}')

grade_a_cost_per_kg = (grade_a_total_cost() / grade_a_quantity)
# cost_with_margin = (grade_a_cost_per_kg * 10) / 100
# st.write(cost_with_margin)
st.write(f"Purchasing Cost for grade A is ruppes {grade_a_cost_per_kg} per kg")



required_margin = st.number_input("How much margin you required", value = 1)
margin = (grade_a_cost_per_kg * required_margin) / 100
st.write(f'Margin will be {required_margin}')

grade_a_selling_price_all_costs = grade_a_cost_per_kg + additional_cost + margin
# st.write(f'Grade A selling price perkg with all additionalcosts and margin should be {grade_a_selling_price_all_costs}')










        
     
          
#     # total_quantity_of_bags = int(input("Enter the Quantity of Total Bags"))
#     Choose_type = st.number_input("Enter the price of a Bag: ")
#     quantity_of_item_per_bag= int(input("Enter the quantity of items in kg per bag: "))
    
#     # total_purchasing_cost_of_items = total_quantity_of_bags * purchasing_price_of_bag
#     # print(f'Total cost of purchasing items in ruppes is {total_purchasing_cost_of_items}')
#     price_per_kg = purchasing_price_of_bag / quantity_of_item_per_bag

#     print(f'purchasing price per kg is {price_per_kg} rupees')
# elif(lower_purchasing_type == "kg"):
#     int(input("Enter the price of item in kg: "))

# else:
#     print("Enter a valid Value 'Bag or Kg'")




# # purchasing_type = input("Type of purchasing: Enter Bag or Kg: " )
# # lower_purchasing_type = purchasing_type.lower()
# # print(lower_purchasing_type)



# if(lower_purchasing_type == "bag"):
#     # total_quantity_of_bags = int(input("Enter the Quantity of Total Bags"))
#     purchasing_price_of_bag = int(input("Enter the price of a Bag: "))
#     quantity_of_item_per_bag= int(input("Enter the quantity of items in kg per bag: "))
    
#     # total_purchasing_cost_of_items = total_quantity_of_bags * purchasing_price_of_bag
#     # print(f'Total cost of purchasing items in ruppes is {total_purchasing_cost_of_items}')
#     price_per_kg = purchasing_price_of_bag / quantity_of_item_per_bag

#     print(f'purchasing price per kg is {price_per_kg} rupees')
# elif(lower_purchasing_type == "kg"):
#     int(input("Enter the price of item in kg: "))

# else:
#     print("Enter a valid Value 'Bag or Kg'")


# #Additional Costs
# # labour_cost = 
# # packaging_cost =
# # transportation_cost = 


# grade_b_quantity= int(input("What is Quantity of grade B: "))
# grade_c_quantity= float(input("What is Quantity of grade C: "))
# grade_d_quantity = int(input("What is Quantity of grade D: "))
# grade_a_quantity = (quantity_of_item_per_bag - (grade_b_quantity + grade_c_quantity + grade_d_quantity ))

# print(f'Quantity of grade A is: {grade_a_quantity}')
# print(f'Quantity of grade B is: {grade_b_quantity}')
# print(f'Quantity of grade C is: {grade_c_quantity}')
# print(f'Quantity of grade D is: {grade_d_quantity}')





# #Selling price for per kg

# price_of_grade_b = int(input("Enter the price per kg of grade B in ruppes: "))
# price_of_grade_c = int(input("Enter the price per kg of grade C in ruppes: "))
# price_of_grade_d = int(input("Enter the price per kg of grade D in ruppes: "))
# # price_of_grade_a = (purchasing_price_of_bag - (price_of_grade_b + price_of_grade_c + price_of_grade_d))

# #Total cost of items as per grades
# # total_cost_grade_a = price_of_grade_a * grade_a_quantity
# total_cost_grade_b = price_of_grade_b * grade_b_quantity
# total_cost_grade_c = price_of_grade_c * grade_c_quantity
# total_cost_grade_d = price_of_grade_d * grade_d_quantity
# total_cost_of_b_c_d = (total_cost_grade_b + total_cost_grade_c + total_cost_grade_d)

# total_purchasing_cost_for_grade_a = (purchasing_price_of_bag - total_cost_of_b_c_d)
# print(f'Total purchasing cost for grade a is {total_purchasing_cost_for_grade_a} befor additional cost')
# total_purchasing_cost_for_grade_a_in_kg = total_purchasing_cost_for_grade_a / grade_a_quantity

# print(f'Selling price per kg for Grade A items is {total_purchasing_cost_for_grade_a_in_kg} befor anyadditional cost')


# # per_kg_price_for_grade_a = 

# # print(f'Quantity of grade A is {grade_a_quantity} total price of Grade A items is {price_of_grade_a * grade_a_quantity}')
# print(f'Total price of Grade B items is {price_of_grade_b * grade_b_quantity}')
# print(f'Total price of Grade C items is {price_of_grade_c  * grade_c_quantity}')
# print(f'Total price of Grade D items is  {price_of_grade_d * grade_d_quantity}')




