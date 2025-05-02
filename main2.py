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
        price_of_single_bag = st.number_input("Enter price of single Bag", placeholder="Purchasing price of single bag", value=1)
        purchasing_cost_per_kg = price_of_single_bag / weight_of_single_bag
        st.write(f'Total weight of items is :green[{total_weight_of_bags} kg] and price for one kg is :green[{purchasing_cost_per_kg} rupees]')
        return total_weight_of_bags, purchasing_cost_per_kg, purchasing_cost_per_kg * total_weight_of_bags
    elif(saved_user_input == "KG"):
        items_weight = st.number_input("Enter the quantity of the items in kg.", value=1)
        st.write(f'Total weight of items is :green[{items_weight}] kg')
        price_per_kg = st.number_input("Enter price of a kg item", placeholder="Purchasing price og one kg item", value=1)
        total_purchasing_cost = price_per_kg * items_weight
        st.text(f'Total purchasing cost of items is {total_purchasing_cost}')
        return items_weight, price_per_kg,total_purchasing_cost

    else:
        st.text("Enter valid input 'Bag' or 'KG'")

items_weight_and_cost = (calculate_weight_and_cost())
# st.write(items_weight_and_cost)
total_weight_of_items = (items_weight_and_cost[0])
# st.write(total_weight_of_items)
price_per_kg = items_weight_and_cost[1]
# st.write(price_per_kg)
total_purchasing_cost = items_weight_and_cost[2]
# st.write(total_purchasing_cost)

#Item grading
st.subheader("Grade wise Quantities ")
grade_b_percentage = st.number_input("Quantity of Grade B in percent (%) ", placeholder="Enter the percentage of grade B items in Kg", value=1)

grade_b_quantity = round((total_weight_of_items * grade_b_percentage) / 100, 2)
st.write(f'Grade B items is :green[{grade_b_quantity} kg]')

grade_c_percentage = st.number_input("Quantity of Grade C in percent (%) ", placeholder="Enter the percentage of grade C items in Kg", value=1)

grade_c_quantity = round(((total_weight_of_items - grade_b_quantity) * (grade_c_percentage) / 100),2)
st.write(f'Grade C items is :green[{grade_c_quantity} kg]')

grade_d_percentage = st.number_input("Quantity of Grade D in percent (%) ", placeholder="Enter the percentage of grade D items in Kg", value=1)

grade_d_quantity = round(((total_weight_of_items - grade_b_quantity - grade_c_quantity) * (grade_d_percentage) / 100), 2)
st.write(f'Grade d items is :green[{grade_d_quantity} kg]')

grade_a_quantity_in_percentage = (100 - grade_b_percentage - grade_c_percentage - grade_d_percentage)
grade_a_quantity_in_kg = round((total_weight_of_items - grade_b_quantity - grade_c_quantity - grade_d_quantity),2)
if grade_a_quantity_in_percentage < 0:
    st.write(f":red[Plese recheck your inputs percentage of grades B,C,D shouldn't more than 100 %]")
else:
    st.write(f'Quantity of grade A items is :green[{grade_a_quantity_in_percentage} %]')
    st.write(f'Quantity of grade A items is :green[{grade_a_quantity_in_kg} Kg]')
    
# purchasing costs in kg

    st.subheader(f'Grade wise purchasing cost of items before selling grade b, c, d items')

    grade_a_cost = grade_a_quantity_in_kg * price_per_kg
    st.write(f'Grade A purchasing cost is :green[₹ {grade_a_cost}]')

    grade_b_cost = grade_b_quantity * price_per_kg
    st.write(f'Grade B purchasing cost is :green[₹ {grade_b_cost}]')

    grade_c_cost = grade_c_quantity * price_per_kg
    st.write(f'Grade C purchasing cost is :green[₹ {grade_c_cost}]')

    grade_d_cost = grade_d_quantity * price_per_kg
    st.write(f'Grade D purchasing cost is :green[₹ {grade_d_cost}]')

# Additional cost


    logestic_cost = float(1)
    loading_cost = float(0.70)
    sorting_cost = float(0.50)
    additional_cost = round(loading_cost + loading_cost + sorting_cost)

    #Selling prices for all Items

    # b = st.number_input("Enter the selling price per kg for Grade B", value=0)
    # c =st.number_input("Enter the selling price per kg for Grade c", value=0)
    # d = st.number_input("Enter the selling price per kg for Grade d", value=0)
    # if b or c or d < 0:
    #     st.write(":red[Check your input and enter a positive input]")
    # else:
    #     grade_b_total_selling = round(b * grade_b_quantity,2)
    # st.write(f"Total amount collection from grade B is : :green[ ₹ {grade_b_total_selling}]")



    st.subheader("Grade Wise selling price per kg")

    grade_b_price = st.number_input("Enter the selling price per kg for Grade B", value=0)
    if grade_b_price < 0:
        st.write(":red[Check your input and enter a positive input]")

    # st.write(f'Final selling cost for garde B after adding additional cost: :green[{grade_b_price}]')
    grade_c_price = st.number_input("Enter the selling price for Grade C", value=0)
    if grade_c_price < 0:
        st.write(":red[Check your input and enter a positive input]")
    grade_d_price = st.number_input("Enter the selling price for Grade D", value=0)
    if grade_d_price < 0:
        st.write(":red[Check your input and enter a positive input]")

    grade_b_total_selling = round(grade_b_price * grade_b_quantity,2)
    st.write(f"Total amount collection from grade B is : :green[ ₹ {grade_b_total_selling}]")

    grade_c_total_selling = round(grade_c_price * grade_c_quantity,2)
    st.write(f"Total amount collection from grade C is : :green[ ₹ {grade_c_total_selling}]")

    grade_d_total_selling = round(grade_d_price * grade_d_quantity,2)
    st.write(f"Total amount collection from grade D is : :green[ ₹ {grade_d_total_selling}]")

    total_amount_collection_b_c_d = grade_b_total_selling + grade_c_total_selling + grade_d_total_selling
    # st.write(total_amount_collection_b_c_d)

    grade_a_amount = round(total_purchasing_cost - total_amount_collection_b_c_d,2)
    st.write(f' Purchasing cost for grade "A" is: :green[ ₹ {grade_a_amount}]')
    purchasing_cost_grade_a_kg = round(grade_a_amount / grade_a_quantity_in_kg,2)
    st.write(f'Purchasing cost per kg of grade "A" is: :green[ ₹  {purchasing_cost_grade_a_kg}]')
    if grade_a_amount < 0:
        st.write("Note: If purchasing price of grade A is negative it means that the purchasing cost of grade A recovered from grade B,C,D selling, and now negative value is your profit")
    else:
        pass



    st.subheader("Per kg selling price for Grades A, B, C and D")

    grade_a_selling_price = round((purchasing_cost_grade_a_kg + additional_cost),2)
    st.write(f'Grade "A": {grade_a_selling_price}')

    grade_b_selling_price = round(grade_b_price + additional_cost,2)
    st.write(f'Grade "B": {grade_b_selling_price}')

    grade_c_selling_price = round(grade_c_price + additional_cost,2)
    st.write(f'Grade "C": {grade_c_selling_price}')

    grade_d_selling_price = round(grade_d_price + additional_cost,2)
    st.write(f'Grade "D": {grade_d_selling_price}')








