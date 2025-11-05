### Nos variables initiales
store_name: str = "ChossettZ"
product: str = "Chaussettes"
price: float = 5.99
quantity: int = 20
tva_rate: float = 0.20
client_account_balance: float = 100.0
store_account_balance: float = 0.0

### La phrase de bienvenue et d'information concernant la boutique (Hello btw ^^)
print(f"""Bienvenue chez {store_name}!
      Nous vendons des {product} à {price}€ HT
      en quantité de {quantity} unités. 
      La TVA est de {tva_rate*100}%. 
      Votre solde actuel est de {client_account_balance}€. 
      En espérant vous voir bientôt! Le solde de la boutique est de {store_account_balance}€.""")

### Demande d'achat
buy_socks: str = input("Combien de chaussettes souhaitez-vous acheter ? ")

### Conversion de la réponse en entier et vérifications du stock et des fonds diponibles
buy_socks_int: int = int(buy_socks)
if buy_socks_int > quantity:
    print("Stock insuffisant!")
    exit()
else:
    montant_ht: float = price * buy_socks_int
    price_ttc: float = price * (1 + tva_rate)
    montant_ttc: float = price_ttc * buy_socks_int
    print(f"Le montant total TTC est de {montant_ttc}€.")

    if montant_ttc > client_account_balance:
        print("Fonds insuffisants!")
    else:
        client_account_balance -= montant_ttc
        store_account_balance += montant_ttc
        quantity -= buy_socks_int
        print(f"""Achat réussi! 
              Nouveau solde client: {client_account_balance}€. 
              Nouveau solde boutique: {store_account_balance}€. 
              Stock restant: {quantity} unités.""") 

### Gestion du stock avec alertes en cas de faible quantité  
if quantity < 10:
    print("Stock bientôt épuisé!")
if quantity < 15 and quantity > 10 and price > 5:
    print("Produit bientôt en rupture!")

### Affichage de la facture    
montant_ttc_str: str = f"{montant_ttc:.2f}€" # avec formatage : montant_ttc_str: str = str(montant_ttc) + "€"
print("""---------------------------------------------------------------
ChossetZ
---------------------------------------------------------------""")
print(f"""Produit:                        qte           ht
{product}-------------------   {buy_socks_int}        {montant_ht:.2f}€

                                            Total HT: {price_ttc:.2f}€
                                            TVA:{montant_ttc - montant_ht:.2f}€
                                            Total TTC: {montant_ttc_str}
---------------------------------------------------------------""")

### Merci d'avoir acheté chez ChossettZ ^^
print("Merci pour votre achat et à bientôt chez ChossettZ!")


### Affichage des types de variables dans la console
print(f"Type de store_name: {type(store_name)}")
print(f"Type de product: {type(product)}")
print(f"Type de price: {type(price)}")
print(f"Type de quantity: {type(quantity)}")
print(f"Type de tva_rate: {type(tva_rate)}")
print(f"Type de client_account_balance: {type(client_account_balance)}")
print(f"Type de store_account_balance: {type(store_account_balance)}")