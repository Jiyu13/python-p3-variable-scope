evil_monster = "Bowser"

# look for global scope inward to the local scope
def princess_peachs_castle():
    print(f"{evil_monster} is trying to kidnap Princess Peach!")

#  ==================================================================

# define function to include a local variable
def practicing_function_scope():
  im_trapped_in_the_function = "You can't access me outside this function!"

# print(im_trapped_in_the_function)
# NameError: name 'im_trapped_in_the_function' is not defined


#  =========================The Global Keyword==================================
change_the_world = "change yourself"

def change_yourself():
    change_the_world = "world changed"

change_yourself()
print(change_the_world)  # change yourself

#  Change global variable from a lcal scope using global keyword


change_the_world2 = "change yourself"

def change_yourself2():
    global change_the_world2
    change_the_world2 = "world changed"

change_yourself2()
print(change_the_world2)  # world changed