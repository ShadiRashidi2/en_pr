class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Buyer(User):
    def __init__(self, username, password, address, national_code):
        super().__init__(username, password)
        self.address = address
        self.national_code = national_code

    def print_details(self):
        print("Username:", self.username)
        print("Password:", self.password)
        print("Address:", self.address)
        print("National Code:", self.national_code)
# ایجاد یک شیء از کلاس Buyer
buyer = Buyer("Fatemeh", "f12345", "pardisan", "1234567890")

# نمایش جزئیات
buyer.print_details()
        