import json
import time


class TrieNode:
    def __init__(self):
        self.children = {}  # Lưu các ký tự con
        self.products = []  # Lưu danh sách sản phẩm dưới nút này


def insert_product(root, product):
    node = root
    name = product.get("name", "")  # Giả sử "name" là khóa cho tên sản phẩm
    for char in name:
        if char not in node.children:
            node.children[char] = TrieNode()
        node = node.children[char]
    node.products.append(product)


def search_products(root, query):
    node = root
    for char in query:
        if char not in node.children:
            return []
        node = node.children[char]
    return node.products


# Tạo nút gốc cho Trie
root = TrieNode()

# Đọc dữ liệu sản phẩm từ tệp JSON
with open("đường dẫn tới file.json nhé", "r") as file:
    products = json.load(file)

# Thêm các sản phẩm vào Trie
for product in products:
    insert_product(root, product)

while True:
    print("Chọn hành động:")
    print("1. Thêm sản phẩm")
    print("2. Tìm kiếm sản phẩm")
    print("3. Thoát")
    choice = input("Nhập số tương ứng: ")

    if choice == "1":
        # Nhập thông tin sản phẩm từ người dùng
        new_product = {
            "id": int(input("ID: ")),
            "sku": int(input("SKU: ")),
            "name": input("Tên sản phẩm: "),
            "discount": int(input("Giảm giá: ")),
            "price": int(input("Giá tiền: ")),
            "original_price": int(input("Giá gốc: "))
        }

        # Đo thời gian thực hiện thêm sản phẩm
        start_time = time.time()

        # Thêm sản phẩm mới vào Trie
        insert_product(root, new_product)

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(
            f"Sản phẩm đã được thêm. Thời gian thực hiện: {elapsed_time} giây")

    elif choice == "2":
        search_query = input("Nhập tên sản phẩm để tìm kiếm: ")

        # Đo thời gian thực hiện tìm kiếm sản phẩm
        start_time = time.time()

        results = search_products(root, search_query)

        end_time = time.time()
        elapsed_time = end_time - start_time

        if results:
            print("Kết quả tìm kiếm:")
            for result in results:
                print(result)
        else:
            print("Không tìm thấy sản phẩm nào phù hợp.")

        print(f"Thời gian thực hiện tìm kiếm: {elapsed_time} giây")

    elif choice == "3":
        break

    else:
        print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
