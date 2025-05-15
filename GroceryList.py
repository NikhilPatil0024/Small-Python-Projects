
GroceryList = ["Apples", "Mango", "IceCream", "Vegetables", "Ingredients"]
a = GroceryList[0] = int(input("\nEnter the price of an Apple: ")) # type: ignore
b = GroceryList[1] = int(input("\nEnter the price of a Mango: ")) # type: ignore
c = GroceryList[2] = int(input("\nEnter the price of an IceCream: ")) # type: ignore
d = GroceryList[3] = int(input("\nEnter the price of the Vegetables: ")) # type: ignore
e = GroceryList[4] = int(input("\nEnter the price of an Ingredients: ")) # type: ignore

TotalSum = a + b + c + d + e
print("\nThe total sum of the items is ", TotalSum)
budget = 500
# UseOnly = 450


if  TotalSum <= 450:
    print("\n-----Kashi, Quickly add all items to Grocery list.----")
elif TotalSum == 500:
    print("\n----Kashi, bargen for the vegetables and fruits.----\n")
else:
    print("----Kashi, don't add the items to Grocery list.----")
