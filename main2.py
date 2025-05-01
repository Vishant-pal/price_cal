import streamlit as st
from decimal import Decimal, getcontext


st.header('Price Calculator')

user_input = st.text_input("Type here" , placeholder = "Enter tha purchasing type: Bags or Kgs", value="BAG")
saved_user_input = user_input.upper()
st.write(saved_user_input)


#calculate the weight of items and price per kg
def calculate_weight_and_cost():
    if saved_user_input == 'BAG':
        total_bags = st.number_input("Total numbers of bags", placeholder= "Enter the total quantity of Bags", value=1)
        weight_of_single_bag = st.number_input("Enter a Bag Weight",placeholder = "Enter the weight of a single bag", value=1)
        total_weight_of_bags = total_bags * weight_of_single_bag
        price_of_single_bag = st.number_input("Enter price of single Bag", placeholder="Purchasing price of single bag")
        purchasing_cost_per_kg = price_of_single_bag / weight_of_single_bag
        st.write(f'Total weight of items is {total_weight_of_bags} kg and price per kg is {purchasing_cost_per_kg}')
        return total_weight_of_bags, purchasing_cost_per_kg, purchasing_cost_per_kg * total_weight_of_bags
    elif(saved_user_input == "KG"):
        items_weight = st.number_input("Enter the quantity of the items in kg.", value=1)
        st.write(f'Total weight of items is {items_weight} kg')
        price_per_kg = st.number_input("Enter price of a kg item", placeholder="Purchasing price og one kg item", value=1)
        total_purchasing_cost = price_per_kg * items_weight
        st.text(f'Total purchasing cost of items is {total_purchasing_cost}')
        return items_weight, price_per_kg,total_purchasing_cost

    else:
        st.text("Enter valid input 'Bag' or 'KG'")

items_weight_and_cost = (calculate_weight_and_cost())
st.write(items_weight_and_cost)
total_weight_of_items = (items_weight_and_cost[0])
st.write(total_weight_of_items)
price_per_kg = items_weight_and_cost[1]
st.write(price_per_kg)
total_purchasing_cost = items_weight_and_cost[2]
st.write(total_purchasing_cost)

#Item grading
st.subheader("Grade wise Quantities ")
grade_b_percentage = st.number_input("Quantity of Grade B in% ", placeholder="Enter the percentage of grade B items in Kg")

grade_b_quantity = (total_weight_of_items * grade_b_percentage) / 100
st.write(f'Grade B items is {grade_b_quantity} kg')

grade_c_percentage = st.number_input("Quantity of Grade C in% ", placeholder="Enter the percentage of grade C items in Kg")

grade_c_quantity = ((total_weight_of_items - grade_b_quantity) * (grade_c_percentage) / 100)
st.write(f'Grade C items is {grade_c_quantity} kg')

grade_d_percentage = st.number_input("Quantity of Grade D in% ", placeholder="Enter the percentage of grade D items in Kg")

grade_d_quantity = ((total_weight_of_items - grade_b_quantity - grade_c_quantity) * (grade_d_percentage) / 100)
st.write(f'Grade d items is {grade_d_quantity} kg')

grade_a_quantity_in_percentage = (total_weight_of_items - grade_b_percentage - grade_c_percentage - grade_d_percentage)
grade_a_quantity_in_kg = (total_weight_of_items - grade_b_quantity - grade_c_quantity - grade_d_quantity)
st.write(f'Quantity of grade A items in percentage {grade_a_quantity_in_percentage}')
st.write(f'Quantity of grade A items in Kilogram {grade_a_quantity_in_kg}')

# purchasing costs in kg

st.subheader(f'Grade wise purchasing cost of items before selling grade b, c, d items')

grade_a_cost = grade_a_quantity_in_kg * price_per_kg
st.write(f'Grade A purchasing cost is {grade_a_cost}')

grade_b_cost = grade_b_quantity * price_per_kg
st.write(f'Grade B purchasing cost is {grade_b_cost}')

grade_c_cost = grade_c_quantity * price_per_kg
st.write(f'Grade C purchasing cost is {grade_c_cost}')

grade_d_cost = grade_d_quantity * price_per_kg
st.write(f'Grade D purchasing cost is {grade_d_cost}')

# Additional cost


logestic_cost = float(0.99)
loading_cost = float(0.70)
sorting_cost = float(0.50)
additional_cost = round(loading_cost + loading_cost + sorting_cost)
st.write(additional_cost)

#Selling prices for all Items

st.subheader("Grade Wise selling price per kg")

grade_b_price = st.number_input("Enter the selling price per kg for Grade B")
# st.write(f'Final selling cost for garde B after adding additional cost: :green[{grade_b_price}]')
grade_c_price = st.number_input("Enter the selling price for Grade C")
grade_d_price = st.number_input("Enter the selling price for Grade D")

grade_b_total_selling = grade_b_price * grade_b_quantity
st.write(f"Total amount collection from grade B is : {grade_b_total_selling}")

grade_c_total_selling = grade_c_price * grade_c_quantity
st.write(f"Total amount collection from grade C is : {grade_c_total_selling}")

grade_d_total_selling = grade_d_price * grade_d_quantity
st.write(f"Total amount collection from grade D is : {grade_d_total_selling}")

total_amount_collection_b_c_d = grade_b_total_selling + grade_c_total_selling + grade_d_total_selling
st.write(total_amount_collection_b_c_d)

grade_a_amount = total_purchasing_cost - total_amount_collection_b_c_d
st.write(f' Purchasing cost for grade A is {grade_a_amount}')
purchasing_cost_grade_a_kg = (grade_a_amount / grade_a_quantity_in_kg)
st.write(f'Purchasing cost per kg of grade A is {purchasing_cost_grade_a_kg} ruppes')

st.subheader("Per kg selling price for Grades A, B, C and D")

grade_a_selling_price = (purchasing_cost_grade_a_kg + additional_cost)
st.write(f'Grade "A": {grade_a_selling_price}')

grade_b_selling_price = grade_b_price + additional_cost
st.write(f'Grade "B": {grade_b_selling_price}')

grade_c_selling_price = grade_c_price + additional_cost
st.write(f'Grade "C": {grade_c_selling_price}')

grade_d_selling_price = grade_d_price + additional_cost
st.write(f'Grade "D": {grade_d_selling_price}')









