import random
            print(f"{product.name} added to your cart.")
    
    def view_cart(self):
        if not self.cart:
            print("\nYour cart is empty.")
        else:
            print("\nItems in your cart:")
            total = 0
            for product in self.cart:
                print(f"- {product.name}, Price: ${product.price}")
                total += product.price
            print(f"Total: ${total:.2f}")
    
    def checkout(self):
        if not self.cart:
            print("\nYour cart is empty. Add some products before checking out.")
        else:
            print("\nChecking out...")
            total = sum(product.price for product in self.cart)
            print(f"Total amount to be paid: ${total:.2f}")
            print("Thank you for shopping with us!")
            self.cart.clear()
    
    def run(self):
        while True:
            print("\nWelcome to the Virtual Shopping Mall!")
            self.display_products()
            choice = input("\nEnter the product number to try it on, view cart (c), or checkout (x): ")
            if choice.isdigit():
                product_index = int(choice) - 1
                if 0 <= product_index < len(self.products):
                    user_size = int(input("Enter your size for simulation (e.g., 40 for a shirt): "))
                    self.try_on_product(product_index, user_size)
                else:
                    print("Invalid product number.")
            elif choice.lower() == 'c':
                self.view_cart()
            elif choice.lower() == 'x':
                self.checkout()
                break
            else:
                print("Invalid input. Please try again.")


if __name__ == "__main__":
    mall = ShoppingMallAR()
    mall.run()
