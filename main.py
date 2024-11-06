from tabulate import tabulate
from math import sqrt


class Membership:
    user_data = {"Sumbul": "Platinum", "Ana": "Gold", "Cahya": "Platinum"}

    membership = {
        "Membership": ["Platinum", "Gold", "Silver"],
        "Discount": ["15%", "10%", "8%"],
        "Another Benefit": [
            "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%",
            "Benefit Silver + Voucher Ojek Online",
            "Voucher Makanan",
        ],
    }

    requirements = {
        "Membership": ["Platinum", "Gold", "Silver"],
        "Monthly Expense (juta)": [8, 6, 5],
        "Monthly Income (juta)": [15, 10, 7],
    }

    def __init__(self, username):
        self.username = username

    def show_benefit(self):
        print("Benefit Membership PacCommerce")
        print("")
        print(
            tabulate(
                self.membership, headers="keys", tablefmt="github", stralign="center"
            )
        )

    def show_requirements(self):
        print("Requirements Membership PacCommerce\n")
        print(
            tabulate(
                self.requirements, headers="keys", tablefmt="github", stralign="center"
            )
        )

    def predict_membership(self, monthly_expense, monthly_income):
        r_list = []
        for i in range(len(self.requirements["Membership"])):
            r_user = sqrt(
                (monthly_expense - self.requirements["Monthly Expense (juta)"][i]) ** 2
                + (monthly_income - self.requirements["Monthly Income (juta)"][i]) ** 2
            )
            r_list.append(r_user)

        membership_list = self.requirements["Membership"]

        r_dict = dict(zip(membership_list, r_list))

        index_r_user = r_list.index(min(r_list))

        membership_type = self.requirements["Membership"][index_r_user]
        print(
            f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {r_dict}"
        )
        print(membership_type)

        # Check if username in self.data, if not add
        if self.username not in self.user_data:
            self.user_data[self.username] = membership_type

    def show_membership(self):
        if self.username in self.user_data:
            return self.user_data[self.username]

    def calculate_price(self, list_harga_barang):
        user_membership = self.show_membership()

        index_membership = self.membership["Membership"].index(user_membership)

        discount_str = self.membership["Discount"][index_membership]

        discount = int(discount_str.rstrip("%")) / 100

        sum_list_harga_barang = sum(list_harga_barang)

        final_price = sum_list_harga_barang - (sum_list_harga_barang * discount)

        print(f"Final price: {final_price}")
