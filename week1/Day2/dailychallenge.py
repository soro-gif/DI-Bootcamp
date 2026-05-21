# Daily Challenge - 1
mot = input("Entrez un mot : ")
index_dict = {}

for i, lettre in enumerate(mot):
    if lettre in index_dict:
        index_dict[lettre].append(i)
    else:
        index_dict[lettre] = [i]

print(index_dict)

# Daily Challenge - 2


items_purchase = {
    "Water": "$1", "Bread": "$3",
    "TV": "$1,000", "Fertilizer": "$20"
}
wallet = "$300"

# Nettoyage du portefeuille
budget = int(wallet.replace("$", "").replace(",", ""))
basket = []

for article, prix_str in items_purchase.items():
    prix = int(prix_str.replace("$", "").replace(",", ""))
    if prix <= budget:
        basket.append(article)
        budget -= prix

if not basket:
    print("Nothing")
else:
    print(sorted(basket))