"""
Programme principal - Gestion de boutique ChossettZ
Point d'entrée du programme qui orchestre les différents modules
"""

# Imports des modules
import config
from display import show_welcome, show_invoice, show_transaction_success, show_variable_types
from transaction import calculate_price_ttc, calculate_total_ht, calculate_total_ttc, process_purchase
from utils import check_stock_alerts, get_user_quantity


def main():
    """Fonction principale du programme"""
    
    # Afficher le message de bienvenue
    show_welcome(
        config.store_name, 
        config.product, 
        config.price, 
        config.quantity,
        config.tva_rate, 
        config.client_account_balance, 
        config.store_account_balance
    )
    
    # Demander à l'utilisateur combien il souhaite acheter
    buy_quantity: int = get_user_quantity()
    
    # Calculer les montants
    price_ttc: float = calculate_price_ttc(config.price, config.tva_rate)
    montant_ht: float = calculate_total_ht(config.price, buy_quantity)
    montant_ttc: float = calculate_total_ttc(price_ttc, buy_quantity)
    
    print(f"Le montant total TTC est de {montant_ttc}€.")
    
    # Traiter l'achat
    new_client_balance, new_store_balance, new_stock, success = process_purchase(
        buy_quantity,
        config.quantity,
        montant_ttc,
        config.client_account_balance,
        config.store_account_balance
    )
    
    # Si l'achat a réussi
    if success:
        # Mettre à jour les variables de config
        config.client_account_balance = new_client_balance
        config.store_account_balance = new_store_balance
        config.quantity = new_stock
        
        # Afficher le succès de la transaction
        show_transaction_success(
            config.client_account_balance,
            config.store_account_balance,
            config.quantity
        )
        
        # Vérifier les alertes de stock
        check_stock_alerts(config.quantity, config.price)
        
        # Afficher la facture
        show_invoice(config.product, buy_quantity, montant_ht, price_ttc, montant_ttc)
        
        # Afficher les types de variables
        show_variable_types(
            config.store_name,
            config.product,
            config.price,
            config.quantity,
            config.tva_rate,
            config.client_account_balance,
            config.store_account_balance
        )
    else:
        # L'achat a échoué (stock ou fonds insuffisants)
        exit()


if __name__ == "__main__":
    main()