def login(username, password):
    if username == "admin" and password == "123":
        return "Đăng nhập thành công"
    else:
        return "Đăng nhập thất bại"

username = input("Nhập tên đăng nhập: ")
password = input("Nhập mật khẩu: ")

print(login(username, password))