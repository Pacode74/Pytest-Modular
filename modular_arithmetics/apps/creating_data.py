

def data(modulus: int, remainder: int, value_property=True, start_num: int = 1, end_num: int = 100):
    congruent_list = [num for num in range(start_num, end_num + 1) if num % modulus == remainder]
    remainder_list = [(value % modulus) for value in congruent_list]
    if value_property:
        mod_list_value_property = [f'Mod(value={value%modulus}, modulus={modulus})' for value in congruent_list]
        params = [(value, modulus, mod) for value, mod in zip(congruent_list, mod_list_value_property)]
        return params
    else:
        mod_list_value_property = [f'Mod(value={value}, modulus={modulus})' for value in congruent_list]
        params = [(value, modulus, mod) for value, mod in zip(congruent_list, mod_list_value_property)]
        return params