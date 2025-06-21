# If a name is less than 3 characters long.
#     print name must be at least 3 characters long
# Otherwise if its more than 50 characters long
#     print name can be a maximum of 50 characters
# otherwise
#     name looks good

name = "Ja"
name_lenght = len(name)

if name_lenght < 3:
    print("name must be at least 3 characters long")
elif name_lenght >50:
    print("name can be a maximum of 50 characters ")
else:
    print("Everything looks good")