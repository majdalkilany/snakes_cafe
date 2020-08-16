from textwrap import dedent


intro_message = """**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
"""
print(dedent(intro_message))

menu  = {
  'wings': 0,
  'cookies': 0,
  'spring Rolls': 0,
  'salmon': 0,
  'steak': 0,
  'meat Tornado': 0,
  'a Literal Garden': 0,
  'ice Cream': 0,
  'cake': 0,
  'pie': 0,
  'coffee': 0,
  'tea': 0,
  'unicorn Tears': 0,
}





menu_p= """
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

"""
print(dedent(menu_p))
# print(menu['Coffee'])

def order() :
     inp_user = input().lower() 
     if inp_user == "quit" :
       print('thanks for your visit')
       exit()
     elif inp_user in menu.keys() :
          menu[inp_user] +=1
          print(f"** {menu[inp_user] } order of {inp_user.capitalize()} have been added to your meal **")
    
          while inp_user !='quit':
            
            inp_user = input()
            if inp_user == "quit" :
                print('thanks for your visit')
                exit()
            else :
              
                np_user=  input('your order is not exisit please order from the menu or print quit to exit /n')
              
            # menu[inp_user] +=1
            print(f"** {menu[inp_user] } order of {inp_user.capitalize()} have been added to your meal **")

     else:
        print('your order is not exisit please order from the menu')
order()