product_names = ["hamburger", "cheeseburger", "small fries"]
product_costs = [0.99, 1.29, 1.49]
product_stocks = [10, 8, 20]

n = str(input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit:"))
while n != "q":
    while n not in ["s", "l", "a", "r", "u", "q", "e"]:
        print("Invalid option, try again")
        n = str(input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit:"))
    if n == "s":
        product_name = str(input("Enter a product name: "))
        if product_name in product_names:
            print("We sell \"" + product_name + "\" at " + str(product_costs[product_names.index(product_name)]) + "per unit")
            print("We currently have " + str(product_stocks[product_names.index(product_name)]) + " in stock")
        else:
            print("Sorry, We don't sell \"" + product_name + "\"")
    elif n == "l":
        print('{:50}'.format("Product Name") + "|" + '{:10}'.format("Price") + "|" + '{:10}'.format("Quantity"))
        for i in range(len(product_names)):
            print('{:50}'.format(product_names[i]) + "|" + '{:10}'.format(product_costs[i]) + "|" + '{:10}'.format(product_stocks[i]))
    elif n == "a":
        product_name = str(input("Enter a new product name: "))
        while product_name in product_names:
            print("Sorry, We already sell that product. Try again.")
            product_name = str(input("Enter a new product name: "))
        product_cost = float(input("Enter the a product cost: "))
        while product_cost < 0:
            print("Invalid cose. Try again.")
            product_cost = float(input("Enter the a product cost: "))
        product_stock = int(input("How many of these products do we have? "))
        while product_stock < 0:
            print("Invalid quantity. Try again.")
            product_stock = int(input("How many of these products do we have? "))
        product_names.append(product_name)
        product_costs.append(product_cost)
        product_stocks.append(product_stock)
        print("Product added!")
    elif n == "r":
        product_name = str(input("Enter a product name: "))
        if product_name in product_names:
            product_costs.remove(product_costs[product_names.index(product_name)])
            product_stocks.remove(product_stocks[product_names.index(product_name)])
            product_names.remove(product_name)
            print("Product removed!")
        else:
            print("Product doesn't exist. Can't remove.")
    elif n == "u":
        product_name = str(input("Enter a product name: "))
        if product_name in product_names:
            un = str(input("(n)ame, (c)ost or (q)uantity: "))
            while un not in ["n", "c", "q"]:
                print("Invalid option, try again")
                un = str(input("(n)ame, (c)ost or (q)uantity: "))
            if un == "n":
                new_product_name = str(input("Enter a new product name: "))
                while new_product_name in product_names:
                    print("Duplicate name!")
                    new_product_name = str(input("Enter a new product name: "))
                product_names[product_names.index(product_name)] = new_product_name
            elif un == "c":
                product_cost = float(input("Enter a new cost: "))
                while product_cost <= 0:
                    print("Invalid cost!")
                    product_cost = float(input("Enter a new cost: "))
                product_costs[product_names.index(product_name)] = product_cost
            elif un == "q":
                product_stock = int(input("Enter a new quantity: "))
                while product_stock < 0:
                    print("Invalid quantity!")
                    product_stock = int(input("Enter a new quantity: "))
                product_stocks[product_names.index(product_name)] = product_stock
            print("Product quantity has been updated!")
        else:
            print("Product doesn't exist. Can't update.")
    elif n == "e":
        mostprice = 0.00
        leastprice = 0.00
        totalprice = 0.00
        for i in range(len(product_names)):
            totalprice += product_stocks[i] * product_costs[i]
            if product_costs[i] > mostprice:
                mostprice = product_costs[i]
            if product_costs[i] < leastprice or leastprice == 0.00:
                leastprice = product_costs[i]
        print("Most expensive product: " + str(mostprice) + " (small fries)")
        print("Least expensive product: " + str(leastprice) + " (hamburger)")
        print("Total value of all products: " + str(round(totalprice, 2)))
    n = str(input("(s)earch, (l)ist, (a)dd, (r)emove, (u)pdate, r(e)port or (q)uit:"))
print("See you soon!")