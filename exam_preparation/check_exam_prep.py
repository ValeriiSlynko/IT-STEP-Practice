print("\n/ООП/ Dog-Собака")
class Product:
    def __init__(self, product_name:str, price:float, count:int):
        self.product_name = product_name
        self.price = price
        self.count = count

    def display(self):
        print(f":Product name: '{self.product_name}' | Price: '{self.price}' | Count: {self.count}")

    def set_price(self, new_price:float):
        if new_price >= 0:
            self.price = new_price
            print(f"Price for '{self.product_name}' update: {self.price} hrn")
        else:
            print("Error! Price cannot in negative")

    def restock(self, amount:int):
        if amount > 0:
            self.count += amount
            print(f"Added to stock {amount} pieces. Товар: '{self.product_name}'")
        else:
            print("Error! The quantity to add must be greater then '0'.")

# --- РОБОТА КЛАСУ ---
# 1. Створюємо об'єкт продукту
func_prod = Product("TP-Link Archer 17", "1800", 3)

# 2. Виводимо початкову інформацію
func_prod.display()

# 3. Тестуємо заміну ціни (помилкову)
func_prod.set_price(-10)

# 4. Тестуємо заміну ціни (ПРАВИЛЬНУ)
func_prod.set_price(2000.99)

# 5. Тестуємо заповнення складу
func_prod.restock(4)

# 5. Вивід результату
func_prod.display()
