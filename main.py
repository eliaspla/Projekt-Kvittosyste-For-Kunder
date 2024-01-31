Spacing = "                                     "
lovely_loveseat_description = "Härlig Kärlekssoffa. Tuftad polyesterblandning på trä. 81 cm hög x 102 cm bred x 76 cm djup. Röd eller vit."
lovely_loveseat_price = 254.00
stylish_settee_description = "Stilfull Bänksoffa. Konstläder på björk. 75 cm hög x 139 cm bred x 71 cm djup. Svart."
stylish_settee_price = 180.50
luxurious_lamp_description = "Lyxig Lampa. Glas och järn. 91 cm hög. Brun med cremefärgad skärm."
luxurious_lamp_price = 52.15
sales_tax = 0.088
customer_one_total = 0
customer_one_itemization = ""
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description
customer_one_itemization += Spacing
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
customer_one_tax = customer_one_total * sales_tax
print("Kund Ett Föremål:")
print(customer_one_itemization)
print("Kund Ett Total:")
print(customer_one_total)