class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file1 = open(self.__file_name, 'r')
        product = file1.read()
        file1.close()
        return product

    def add(self, *products):
        file = open(self.__file_name, 'r+')
        for el in products:
            if str(el) in self.get_products():
                print(f"Продукт {str(el)} уже есть в магазине")
            else:
                file.write(str(el) + '\n')
        file.close()


class Product(Shop):
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())