'''
Product management With Python
Teamwork
'''


class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.product_id}, Name: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_id):
        self.products = [
            p for p in self.products if p.product_id != product_id]

    def search_product(self, product_id):
        # Sử dụng tìm kiếm nhị phân để tìm kiếm sản phẩm
        left, right = 0, len(self.products) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.products[mid].product_id == product_id:
                return self.products[mid]
            elif self.products[mid].product_id < product_id:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def bubble_sort(self):
        n = len(self.products)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if self.products[j].product_id > self.products[j + 1].product_id:
                    self.products[j], self.products[j +
                                                    1] = self.products[j + 1], self.products[j]

    def display_products(self):
        for product in self.products:
            print(product)


def main():
    product_manager = ProductManager()

    while True:
        print("Chọn hành động:")
        print("1. Thêm sản phẩm")
        print("2. Xóa sản phẩm")
        print("3. Tìm kiếm sản phẩm")
        print("4. Sắp xếp sản phẩm")
        print("5. Hiển thị danh sách sản phẩm")
        print("6. Thoát")
        choice = input("Nhập số tương ứng: ")

        if choice == "1":
            product_id = int(input("Nhập ID sản phẩm: "))
            name = input("Nhập tên sản phẩm: ")
            price = float(input("Nhập giá sản phẩm: "))
            quantity = int(input("Nhập số lượng sản phẩm: "))
            product = Product(product_id, name, price, quantity)
            product_manager.add_product(product)
            print("Sản phẩm đã được thêm.")

        elif choice == "2":
            product_id = int(input("Nhập ID sản phẩm để xóa: "))
            product_manager.remove_product(product_id)
            print("Sản phẩm đã được xóa.")

        elif choice == "3":
            product_id = int(input("Nhập ID sản phẩm để tìm kiếm: "))
            product = product_manager.search_product(product_id)
            if product:
                print("Kết quả tìm kiếm:")
                print(product)
            else:
                print("Không tìm thấy sản phẩm.")

        elif choice == "4":
            # Sắp xếp sản phẩm bằng thuật toán sắp xếp nổi bọt
            product_manager.bubble_sort()
            print("Sản phẩm đã được sắp xếp.")

        elif choice == "5":
            print("Danh sách sản phẩm:")
            product_manager.display_products()

        elif choice == "6":
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
