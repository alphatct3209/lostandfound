database = []


def start():
  print ("Select a function to begin. \n[1] Report a lost item \n[2] Find a lost item \n[3] Exit")
  lor = input("Function:")

  if lor == '1':
    print("You have chosen to report an item.")
    lname = input("Item name:").lower()
    database.append(lname)
    print("Item Saved.")
    start()

  if lor == '2':
    print("You have chosen to find an item.")
    fname = input("Item name:").lower()
    if fname in database:
      print("Item Found.")
      confirm = input("Collect item? Y/N").lower()
      if confirm == 'Y':
       database.remove(fname)
       start()
    else:
      print("Item not Found.")
      start()

  if lor == '3':
    return
start()
