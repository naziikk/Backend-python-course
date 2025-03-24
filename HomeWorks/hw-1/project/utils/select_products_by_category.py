def select_products_by_category(products, category):
    ans = []
    for product in products:
        if product.category == category:
            ans.append(product)
    return ans
