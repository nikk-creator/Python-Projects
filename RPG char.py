def create_character(char_name,strength,intelligence,charisma):
    if not(isinstance(char_name,str)):
        return "The character name should be a string"
    if char_name == "":
        return "The character should have a name"
    if len(char_name)>10:
        return "The character name is too long"
    if " " in char_name:
        return "The character name should not contain spaces"
    if not(isinstance(strength, int)) or not(isinstance(intelligence, int)) or not(isinstance(charisma, int)):
        return "All stats should be integers"
    if strength<1 or intelligence<1 or charisma<1:
        return "All stats should be no less than 1"
    if strength>4 or intelligence>4 or charisma>4:
        return "All stats should be no more than 4"
    if strength+intelligence+charisma!=7:
        return "The character should start with 7 points"
    return( char_name + "\n"
    + "STR " + "●" * strength + "○" * (10 - strength) + "\n"
    + "INT " + "●" * intelligence + "○" * (10 - intelligence) + "\n"
    + "CHA " + "●" * charisma + "○" * (10 - charisma))
print(create_character("ren",4,2,1)) #you can change the values to test the function 