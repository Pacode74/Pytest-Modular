from modular_arithmetics.apps.modular import Mod

congruent_list = []

# Define the modulus for the congruence
modulus = 5

# Set the range of numbers to check
start_num = 1
end_num = 100

# Loop through the range of numbers and check for congruence
for num in range(start_num, end_num + 1):
    if num % modulus == 2:
        congruent_list.append(num)

# Print the list of congruent numbers
print(
    "Congruent numbers with modulus",
    modulus,
    "between",
    start_num,
    "and",
    end_num,
    "are:",
    congruent_list,
)

remainders_list = []
for value in congruent_list:
    remainders_list.append(value % modulus)

print(f"{remainders_list=}")

mod_list_value_private = []
for value in congruent_list:
    mod_list_value_private.append(Mod(value, modulus))

print(f"{mod_list_value_private}")


mod_list_value_property = []
for value in congruent_list:
    mod_list_value_property.append(f"Mod(value={value}, modulus={modulus})")

print(f"{mod_list_value_property=}")

params_values_are_property = []
for value, mod in zip(congruent_list, mod_list_value_property):
    params_values_are_property.append((value, modulus, mod))

print(f"{params_values_are_property=}")


params_values_are_private = []
for value, mod in zip(congruent_list, mod_list_value_private):
    params_values_are_private.append((value, modulus, mod))

print(f"{params_values_are_private=}")
