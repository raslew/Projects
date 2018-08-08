class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)
        return item

    def stock_price(self):
        #itererar igenom self.items men tar endast 'price' och lägger in i total.
        return sum([intererar_igenom['price'] for intererar_igenom in self.items])

    @classmethod
    def franchise(cls, store):
        #två olika sätt att göra return på.
        return cls(store.name + " - franchise")
        #return Store(store.name + " - franchise")

    @staticmethod
    def store_details(store):
        return "{}, total stock price: {}".format(store.name, int(store.stock_price()))

store = Store('Amazon')
store.add_item('Book1', 12)
store.add_item('Book2', 20)
store.add_item('Book3', 150)
print(store.stock_price())
store2 = Store.franchise(store)
print(store2.name)
print(store.franchise(store))
print(Store.store_details(store))
