"""
Module utilitaire - Fonctions de vérification et alertes liées au stock et aux fonds
"""

def check_stock_alerts(quantity: int, price: float) -> None:
    """Vérifie le stock et affiche des alertes si nécessaire"""
    if quantity < 10:
        print("Stock bientôt épuisé!")
    
    if quantity < 15 and quantity > 10 and price > 5:
        print("Produit bientôt en rupture!")


def get_user_quantity() -> int:
    """Demande à l'utilisateur combien il souhaite acheter et retourne la quantité"""
    buy_input: str = input("Combien de chaussettes souhaitez-vous acheter ? ")
    return int(buy_input)
