import re

full_name = str(input("Enter First Name, Middle Name, Last Name (separated by comma): "))
name_parts = re.split(r"[, ]", full_name)

if len(full_name) >= 3:
    first_name = name_parts[0]
    mid_name = name_parts[1]
    last_name1 = name_parts[2]
    last_name2 = name_parts[3]
    
    capitalized_first = first_name.capitalize()
    capitalized_last1 = last_name1.capitalize()
    capitalized_last2 = last_name2.capitalize()
    
    if mid_name:
        mid_initial = mid_name[0].upper() + "."
    else:
        mid_initial = ''
    
    if full_name:
        last_name1 + "" + last_name2
    
    else:
        last_name1 - "" - last_name2
    formatted_name = f"{capitalized_last1} {capitalized_last2}, {capitalized_first} {mid_initial}"
    print(f"Formatted name: {formatted_name}")
    
   
else:
    print("Invalid input. Please enter your name in the format: First, Middle, Last.")