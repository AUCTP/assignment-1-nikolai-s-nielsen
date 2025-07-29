import random

items = ["Sandwich", "Salad", "Cake", "Coffee"]  #added one new item
prices = [35, 40, 20, 10]  # added new prices
inventories = [100, 50, 100, 200]  # added one new inventory amount

sales = []  # the new list with the sales of the day

randomNumber = random.randint(250, 750)  # chooses a number between 250 and 750 as the number of students (total, so those who buy and those who does not buy)
print(f'\nTotal number of students at the university today: {randomNumber}')

for i in range(randomNumber):  # simulates the students one by one
    if random.random() < 0.5:  # for every student, there is a 50% chance of purchase
        item = random.randint(0, len(items) - 1)  # chooses a random item from the items list
        if inventories[item] > 0:  # checks if the random item is in stock
            inventories[item] -= 1  # subtracts one item from the inventory at purchase
            sales.append(item)  # adds the id of the sold item to the sales list

## Alternative method ##
    #customers = int(randomNumber / 2)  # only difference is that buying students are calculated by taking the totalt number of students and divide by 2 to indicate the 50% chance for purchase
    #print(f'\nThe number of students, who buy an item in the cafeteria is: {customers}')

    #for i in range(customers):
    #item = random.randint(0, len(items) - 1)
    
    #if inventories[item] > 0:
    #    inventories[item] -= 1
    #    sales.append(item)

print(f'\nThe list of sale ids are as follows: {sales}') # prints out the ids of the sold items from the list "items"


def proces_sales(sales, prices):  # a new function which calculates the total revenue

    return sum(prices[i] for i in sales if 0 <= i < len(prices))  # returns a sum of the sold items by taking the the ids from the sales list and match it with the index number from the prices list (with i being an index between 0 and 3 from the prices list)

total_revenue = proces_sales(sales, prices)  # calls the new proces_sales function as the variable total_revenue
print(f'\nTotal revenue: {total_revenue} DKK')  # prints out total_revenue


def generate_report(sales, items, prices, inventories):  # a new function which gathers the information from the former functions into one report
    print("\nSales summary of the day:")
    total_revenue = proces_sales(sales, prices)  # this is used to call the total_revenue which was calculated in the previous function (see line 51)

    print("\nSold items:")  # summarises total sales per item
    for i in range(len(items)):  # gathers the i values (4 values) from the items list
        count = sales.count(i)  # counts the number of indexes in the sales list
        revenue = count * prices[i]  # calucultes the revenue by multiplying the previous count variable with the matching index from the prices list
        print(f'{items[i]}: {count} units sold, {revenue} in revenue')  # prints all the units sold per item and revenue per item 
        
    print(f'\nTotal revenue: {total_revenue} DKK')  # calls and prints the total_revenue from the proces_sales function

    print("\nRemaining inventory:")  # summarises remaining inventory
    for i in range(len(items)):  # # gathers the i values (4 values) from the items list
        print(f'{items[i]}: {inventories[i]} left')  # prints all the units left per item by referring back to the function, which subtracted and item from the inventory for every sale in the beginning of the code (see line 16)

generate_report(sales, items, prices, inventories)  # calls the generate_report function