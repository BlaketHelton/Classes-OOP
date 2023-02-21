import FoodClass as fc
# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

customer_dict = {    
    570: ["Danni Sellyar", "97 Mitchell Way Hewitt Texas 76712", "dsellyarft@gmpg.org", "254-555-9362", False],
    569: ["Aubree Himsworth", "1172 Moulton Hill Waco Texas 76710", "ahimsworthfs@list-manage.com", "254-555-2273", True]
    }

customer_orders = {}

for key, value in dict.items():
    customerid = value[3]

    if customerid in customer_orders:
        customer_orders[customerid].append(value)
    else:
        customer_orders[customerid] = [value]

for customerid, orders in customer_orders.items():
    order_total = 0
    discount = 0
    
    if customerid in customer_dict:
        customer = customer_dict[customerid]
        name = customer[0]
        address = customer[1]
        email = customer[2]
        phone = customer[3]
        member_status = customer[4]
        
        for order in orders:
            item_name = order[1]
            cost = order[2]
            order_total += cost
            print(f"Customer Name: {name}")
            print(f"Phone: {phone}")
            print(f"Order Item: {item_name} Price: ${cost}")
            print(f"Total cost: ${order_total}")
        
        if member_status == True: 
            discount = 0.2 * order_total
            final_total = order_total - discount
            print(f"Member Discount: ${discount:.2f}")
            print(f"Total cost after discount: ${final_total:.2f}")
        else:
            print()
       