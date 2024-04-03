class Product():
    def __init__(self, product_name, description, color, brand, price, quantity):
        self.product_name = product_name
        self.description = description
        self.color = color
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.type = None
        
    def view_product(self):
        print(f"\nDetalles del producto {self.product_name}:")
        print(f"Descripción: {self.description}.")
        print(f"Colores disponibles: {self.color}.")
        print(f"Marca: {self.brand}.")
        print(f"Precio: ${self.price} COP")
        print(f"Cantidad: {self.quantity}")
    
    def view_especifics_product(self):
        pass

class Clothing(Product):
    def __init__(self, product_name, description, color, brand, price, quantity, size, clothing_type ):
        super().__init__(product_name, description, color, brand, price, quantity)
        self.size = size
        self.clothing_type = clothing_type
    
    def view_especifics_product(self):
        print(f"Tallas disponibles: {self.size}")
        print(f"Tipo de producto: {self.clothing_type}")


class Sneakers(Product):
    def __init__(self, product_name, description, color, brand, price, quantity, size, sneakers_type):
        super().__init__(product_name, description, color, brand, price, quantity)
        self.size = size
        self.sneakers_type = sneakers_type
    
    def view_especifics_product(self):
        print(f"Tallas disponibles: {self.size}")
        print(f"Tipo de producto: {self.sneakers_type}")

class Accessories(Product):
    def __init__(self,product_name, description, color, brand, price, quantity, accessories_type ):
        super().__init__(product_name, description, color, brand, price, quantity)
        self.accessories_type = accessories_type

    def view_especifics_product(self):
        print(f"Tipo de producto: {self.accessories_type}")
    

class Shopping_car():
    def __init__(self):
        self.items = []

    def add_product_car(self, product, quantity):
        if product.quantity >= quantity:
            self.items.append({"producto": product, "cantidad": quantity})
            product.quantity -= quantity
            print(f"{quantity} unidades de {product.product_name} agregadas al carrito.")
        else:
            print("No hay suficientes unidades disponibles en el inventario.")

    def shopping_car(self):
        total = 0
        if not self.items:
            print("\nEl carrito está vacío.")
            return None
        print("Contenido del carrito:\n")
        for item in self.items:
            product = item["producto"]
            quantity = item["cantidad"]
            subtotal = product.price * quantity
            total += subtotal
            print(f"Producto: {product.product_name}, Cantidad: {quantity}, Subtotal: ${subtotal:.2f} COP")
        print(f"Total del carrito: ${total:.2f} COP\n")

    def purshase(self):
        if not self.items:
            return None
        else:
            pay = input('\n¿Realizar la compra?: ')
            if pay == 'si':

                print("\nPor favor, complete la información de pago y envío:\n")
                nombre = input("Nombre: ")
                direccion = input("Dirección de envío: ")
                print("\nAhora unos datos sobre tu medio de pago\n")
                tarjeta_credito = input("Número de tarjeta de crédito: ")
                fecha_expiracion = input("Fecha de expiración de la tarjeta (MM/YY): ")
                codigo_seguridad = input("Código de seguridad de la tarjeta: ")

                print("\nProcesando el pago...")
                print("Pago completado con éxito.\n")

                print("Enviando los productos...\n")
                print("Productos enviados a la siguiente dirección:")
                print(f"Dirección: {direccion}")
                print(f"A nombre de: {nombre} \n")

                self.items = []
                print("Pedido completado. \n")  

            else:
                print("Compra cancelada. \n")


class Shopping(): 
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

def view_products():
    print("\nProductos disponibles en la tienda:\n")
    for product in tienda.products:
        product.view_product()
        product.view_especifics_product()

if __name__ == "__main__":
    tienda = Shopping()
    carrito = Shopping_car()

    ropa_1 = Clothing("Camisa Oversize", "Camisa Oversize con estampado", "Negro - Blanco - Rojo", "H&M", 60000, 20, "M - L - XL", "Camisa")
    ropa_2 = Clothing("Camisa", "Camisa normal sin estampado", "Blanco - Negro - Amarillo ","Calvin Klein", 30000, 20, "X - M - L - XL", "Camisa")
    ropa_3 = Clothing("Pantalon Vaquero", "Pantalon Vaquero con rotos", "Azul - Negro", "Levis", 80000, 25, "32 - 34 - 36", "Pantalon")
    ropa_4 = Clothing("Pantalon Skinny", "Pantalón Skinny", "Negro - Azul oscuro - Azul claro", "Sara", 85000, 30, "30 - 32 - 36", "Pantalon")

    zapatillas_1 = Sneakers("Zapato Nike", "Zapato Nike para correr", "Negro - Rojo ", "Nike", 750000, 10, "8.5 - 9 - 10", "Skin-Tight Fit")
    zapatillas_2 = Sneakers("Zapato Converse", "Zapato clásico y cómodo", "Verde - Blanco", "Converse", 450000, 24, "6.5 - 7.5 - 8", "Relajada Cushioning")
    zapatillas_3 = Sneakers("Zapato Adidas", "Zapato para caminar", "Blanco - Negro - Azul - Rojo", "Adidas", 500000, 40, "7 - 7.5 - 8 - 8.5", "Relaxed Fit")

    accesorios_1 = Accessories("Collar Dolar", "Collar con diseño de dólar en plata.", "Plata - Oro", "Pandora", 1000000, 12, "Joyeria" )
    accesorios_2 = Accessories("Anillo de diamante", "Anillo de diamante brillante y elegante.", "Diamante", "Pandora", 5000000, 5, "Joyeria")
    accesorios_3 = Accessories("Reloj de lujo", "Reloj con diamantes y esmeraldas", "Oro rosado - Plata - Oro", "Rolex", 20000000, 7, "Relojeria")

    tienda.add_product(ropa_1)
    tienda.add_product(ropa_2)
    tienda.add_product(ropa_3)
    tienda.add_product(ropa_4)

    tienda.add_product(zapatillas_1)
    tienda.add_product(zapatillas_2)
    tienda.add_product(zapatillas_3)

    tienda.add_product(accesorios_1)
    tienda.add_product(accesorios_2)
    tienda.add_product(accesorios_3)

    view_products()

    carrito.add_product_car(ropa_1, 20)
    carrito.add_product_car(ropa_2, 20)
    carrito.add_product_car(ropa_3, 25)
    carrito.add_product_car(ropa_4, 30)
    
    carrito.add_product_car(zapatillas_1, 10)
    carrito.add_product_car(zapatillas_2, 24)
    carrito.add_product_car(zapatillas_3, 40)
    
    carrito.add_product_car(accesorios_1, 12)
    carrito.add_product_car(accesorios_2, 5)
    carrito.add_product_car(accesorios_3, 7)

    carrito.shopping_car()
    carrito.purshase()


