#1
def rev(s, i):
  if i == 0:
    return ""
  else:
    rev_s = s[::-1] #this reverse it 
    new_s = rev_s * i #this is times of how many to save reversed of s
  return new_s

print(rev("hello",2))
###########################################################################################################################
#2
def arranging(s):
  u = ""
  l = ""
  for char in s:
    if char.isupper(): # I remembered in Java the isUpperCase so I googled the python version of it
      u += char
    else:
      l += char
  return u + l

print(arranging("HelloWorld"))
#####################################################################################################

#3
def test(s1, s2):
  return sorted(s1) == sorted(s2)  #just the simplist way

print(test("hello","ohlel"))
##################################################################################

#4
def h_l(list):

    hv = list[0]
    hi = 0
    lv = list[0]
    li = 0
    i = 1
    while i < len(list): 
      if list[i] > hv:
          hv = list[i]
          hi = i
      elif list[i] < lv:
          lv = list[i]
          li = i
      i += 1

    print("The highest value in the list is ",str(hv)," at index",str(hi) ,".")
    print("The lowest value in the list is ",str(lv)," at index ",str(li),".")


l = [5, 6, 3, 2, 7, 2, 0, 1, 6]
h_l(l)
#####################################################################

#5
def count (a):   # It can use some loop to keep running until break, but what I didn't know is
  c = str(a)     # why when I input 000 it gives me 1 or any other set of 0s always 1 unless it is 10 or 100 or more
  return print(len(c))

num = input("Enter a number: ")
s = int(num)
count(s)
#################################################################################

#6

def list_jumps(jumps): # Chat Gpt wrote this one cause I had no logic for it and how to jump and till now 
  n = len(jumps)       # I can't understand how it works 
  index = 0

  for i in range(n):
    if index < 0 or index >= n:
      return "out-of-bounds"
    index += jumps[index]

  return "cycle"

jumps = [2,1,0,-1,-2]
print(list_jumps(jumps))  #cycle

jumps = [1,2,3,4,-5]
print(list_jumps(jumps))  #out of bounds

#7

def add_item(items, barcode, quantity):
    if barcode in items:
        item_name, item_price = items[barcode]  # it gets the name and price inside dictionary items by using the key
        # barcode
        total_cost = item_price * quantity
        return item_name, quantity, total_cost  # the same thing as getters and setters in Java


def print_receipt(receipt):
    total_amount = 0
    print("\nReceipt:")  # I had to google the new line \n
    for item in receipt:
        name, quantity, total_cost = item
        receipt_line = "Name: " + name + "\n" + \
                       " - Quantity: " + str(quantity) + "\n" + \
                       " - Total Cost: " + str(total_cost)
        print(receipt_line)
        total_amount += total_cost

    print("Total:", total_amount)


def pos_system():
    items = {
        12345: ("Coca-Cola", 2.5),
        67890: ("Chips", 1.8)
    }

    while True:
        new_receipt = input("Start a new receipt? (yes to start / no to exit): ").lower()
        # If the user decided to input them upper I can add it inside the if statement,
        # but what if the user decided to input "Yes" , "YEs" or any other way to input yes or no,
        # so the safe side is to make it always lower
        if new_receipt == "no":
            break
        elif new_receipt == "yes":
            current_receipt = []
            # I used list to help me manage the data I didn't know how to use a normal string, so
            # I checked your menu example and I did it
            while True:
                barcode = input("Enter the item barcode (0 to see receipt or restart): ")
                if not barcode.isdigit():
                    # I had to google it because I tried using if barcode != "12345" ... and it made problems when I
                    # wanted to input 0 to show the receipt or restart
                    print("Invalid input. Please enter a valid number.")
                    continue
                barcode = int(barcode)
                if barcode == 0:
                    break
                if barcode not in items:
                    print("Invalid barcode. Item not found!")  # Provide immediate feedback
                    continue
                quantity = input("Enter the quantity purchased: ")
                if not quantity.isdigit():
                    print("Invalid input. Please enter a valid number.")
                    continue
                quantity = int(quantity)
                item = add_item(items, barcode, quantity)  # Here it will calculate
                if item:
                    current_receipt.append(item)  # This will add the new data to the list

            print_receipt(current_receipt)  # this will return a string with the formatted receipt


# It works by running the pos_system function first
pos_system()

# It can be modified so that the user can add items to the system too, 
# but I didn't do it because it took me 3 hours to do these (which is more than the time took me 
# to do my Female Automated Voice Assistant FAVA)
# hope no user can ruin this one :)
