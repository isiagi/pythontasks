picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}


def menu(picnicItems):
   print("---PICNIC ITEMS--")
   for key, value in picnicItems.items():
        print(f"{key}{'.' * (12-len(key))} {value}")

   print("------PICNIC ITEMS------")
   for key, value in picnicItems.items():
        print(f"{key}{'.' * (20-len(key))} {value}")

       
        

menu(picnicItems)