class Product:
    def __init__(self, name, cost, discreption, rate):
        self.name = name
        self.cost = cost
        self.discreption = discreption
        self.rate = rate


def main():
    product_info = get_product()
    print(f"product name: {product_info.name} and its cost: {product_info.cost}")
    print(f'its discreption "{product_info.discreption}" rate: {product_info.rate}')


def get_product():
    name = input('Product name: ')
    cost = input("Product cost: ")
    info = input("discreption: ")
    rate = input("Product rate: ")
    product = Product(name, cost, info, rate)

    return product


if __name__=="__main__":
    main()