"""
Module de transaction - Gère les calculs et opérations
"""

def calculate_price_ttc(price_ht: float, tva_rate: float) -> float:
    """Calcule le prix TTC à partir du prix HT et du taux de TVA"""
    return price_ht * (1 + tva_rate)


def calculate_total_ht(price_ht: float, quantity: int) -> float:
    """Calcule le montant total HT"""
    return price_ht * quantity


def calculate_total_ttc(price_ttc: float, quantity: int) -> float:
    """Calcule le montant total TTC"""
    return price_ttc * quantity


def process_purchase(quantity_to_buy: int, stock: int, montant_ttc: float, 
                    client_balance: float, store_balance: float) -> tuple:
    """
    Traite l'achat et retourne les nouvelles valeurs
    Returns: (client_balance, store_balance, remaining_stock, success)
    """
    # Vérifier le stock
    if quantity_to_buy > stock:
        print("Stock insuffisant!")
        return client_balance, store_balance, stock, False
    
    # Vérifier les fonds
    if montant_ttc > client_balance:
        print("Fonds insuffisants!")
        return client_balance, store_balance, stock, False
    
    # Effectuer la transaction
    new_client_balance = client_balance - montant_ttc
    new_store_balance = store_balance + montant_ttc
    new_stock = stock - quantity_to_buy
    
    return new_client_balance, new_store_balance, new_stock, True
