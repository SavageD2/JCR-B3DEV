"""
Module d'affichage - Gère tous les affichages sur la console
"""

def show_welcome(store_name: str, product: str, price: float, quantity: int, 
                 tva_rate: float, client_balance: float, store_balance: float) -> None:
    """Affiche le message de bienvenue avec les informations de la boutique"""
    print(f"""Bienvenue chez {store_name}!
      Nous vendons des {product} à {price}€ HT
      en quantité de {quantity} unités. 
      La TVA est de {tva_rate*100}%. 
      Votre solde actuel est de {client_balance}€. 
      En espérant vous voir bientôt! Le solde de la boutique est de {store_balance}€.""")


def show_invoice(product: str, quantity_bought: int, montant_ht: float, 
                 price_ttc: float, montant_ttc: float) -> None:
    """Affiche la facture formatée"""
    montant_ttc_str: str = f"{montant_ttc:.2f}€"
    print("""---------------------------------------------------------------
ChossetZ
---------------------------------------------------------------""")
    print(f"""Produit:                        qte           ht
{product}-------------------   {quantity_bought}        {montant_ht:.2f}€

                                            Total HT: {price_ttc:.2f}€
                                            TVA:{montant_ttc - montant_ht:.2f}€
                                            Total TTC: {montant_ttc_str}
---------------------------------------------------------------""")
    print("Merci pour votre achat et à bientôt chez ChossettZ!")


def show_transaction_success(client_balance: float, store_balance: float, 
                            remaining_stock: int) -> None:
    """Affiche le résultat de la transaction réussie"""
    print(f"""Achat réussi! 
              Nouveau solde client: {client_balance}€. 
              Nouveau solde boutique: {store_balance}€. 
              Stock restant: {remaining_stock} unités.""")


def show_variable_types(store_name: str, product: str, price: float, quantity: int,
                       tva_rate: float, client_balance: float, store_balance: float) -> None:
    """Affiche les types de toutes les variables"""
    print("\n=== Types de variables ===")
    print(f"Type de store_name: {type(store_name)}")
    print(f"Type de product: {type(product)}")
    print(f"Type de price: {type(price)}")
    print(f"Type de quantity: {type(quantity)}")
    print(f"Type de tva_rate: {type(tva_rate)}")
    print(f"Type de client_account_balance: {type(client_balance)}")
    print(f"Type de store_account_balance: {type(store_balance)}")
