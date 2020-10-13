global sm_shirt
global sm_shoe
global s_shirt
global s_shoe
global total_cost
global shirt_cost
global shoe_cost


def total_bill():
  


if __name__ == '__main__':
  sm_shirt = 0
  sm_shoe = 0
  s_shirt = 0
  s_shoe = 0
  total_cost = 0
  shirt_cost = 0
  shoe_cost = 0
  for _ in range(int(input("Enter no. of commands:"))):
    cmd = input("Enter command:")
    if cmd == "END":
      break
    clst = cmd.split(" ")
    if clst[1] == "S":
      if clst[2] == 'GET_ORDER_AMOUNT':           # Getting Order Amount
        total_cost = (s_shirt*shirt_cost)+(s_shoe*shoe_cost)
        print("{:0.2f}".format(total_cost))
      elif clst[2] == "ADD":                      # Adding item to inventory
        if clst[3] == "SHIRT" and sm_shirt >= int(clst[4]):
          s_shirt = int(clst[4])
          sm_shirt -= int(clst[4])
        elif clst[3] == "SHOE" and sm_shoe >= int(clst[4]):
          s_shoe = int(clst[4])
          sm_shoe -= int(clst[4])
        else:
          print(-1)
      elif clst[2] == "REMOVE":                   # Removing Item From Cart
        if clst[3] == "SHIRT" and s_shirt:
          sm_shirt += s_shirt
          s_shirt = 0
          print(s_shirt)
        elif clst[3] == "SHOE" and s_shoe:
          sm_shoe -= s_shoe
          s_shoe = 0
          print(s_shoe)
        else:
          print(-1)
      elif clst[2] == "INCR":                   # Incrementing Quantity in Cart
        pass
      elif clst[2] == "DCR":                    # Decrementing Quantity in C
        pass
      else:
        print(-1)
    elif clst[1] == "SM":                          # SM Management
      if clst[2] == "ADD":                         # ADD Section
        if clst[3] == "SHIRT":
          sm_shirt += int(clst[4])
          print(sm_shirt)
        elif clst[3] == "SHOE":
          sm_shoe += int(clst[4])
          print(sm_shoe)
      elif clst[2] == "SET_COST":                 # Setting COST section
        if clst[3] == "SHIRT":
          shirt_cost = int(clst[4])
          print("{:0.1f}".format(shirt_cost))
        elif clst[3] == "SHOE":
          shoe_cost = int(clst[4])
          print("{:0.1f}".format(shoe_cost))
      elif clst[2] == "GET_QTY":                  # Quantity section
        if clst[3] == "SHIRT":
          print(sm_shirt)
        elif clst[3] == "SHOE":
          print(sm_shoe)
      elif clst[2] == "REMOVE":                   # Removal section
        if clst[3] == "SHIRT":
          sm_shirt = 0
          print(1)
        elif clst[3] == "SHOE":
          sm_shoe = 0
          print(1)
      elif clst[2] == "INCR":                    # Incremental Section
        if clst[3] == "SHIRT":
          sm_shirt += int(clst[4])
          print(sm_shirt)
        elif clst[3] == "SHOE":
          sm_shoe += int(clst[4])
          print(sm_shoe)
      elif clst[2] == "DCR":                    # Decremental Section
        if clst[3] == "SHIRT":
          rm_shirt = int(clst[4])
          if sm_shirt >= rm_shirt:
            sm_shirt -= int(clst[4])
            print(sm_shirt)
          else:
            sm_shirt = 0
            print("Current Quantity of shirts is less than your request",-1)
        elif clst[3] == "SHOE":
          rm_shoe = int(clst[4])
          if sm_shirt >= rm_shoe:
            sm_shoe -= rm_shoe
            print(sm_shoe)
          else:
            sm_shoe = 0
            print("Current Quantity of shoes is less than your request",-1)
      elif clst[2:4] == "SET COST":           # Setting Cost
        if clst[4] == "SHIRT":
          shirt_cost = int(clst[5])
          print("{:0.1f}".format(shirt_cost))
        elif clst[4] == "SHOE":
          shoe_cost = int(clst[5])
          print("{:0.1f}".format(shoe_cost))
    else:
      print(-1)



