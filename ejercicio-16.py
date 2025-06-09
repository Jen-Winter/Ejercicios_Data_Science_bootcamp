# Phone number: +34-913724710-56
telefono_completo = input("Add the complete phone number: ")
telefono_split = telefono_completo.split("-")
print(f"Phone number without prefix and extension is: {telefono_split[1]}")