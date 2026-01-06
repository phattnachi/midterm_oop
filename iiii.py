class BackAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount >0:
            self,__balance += amount
            print(f'ฝากสำเร็จ: {amount} บาท')
        else:
            print('ยอดเงินต้องมากกว่า 0')

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
                self.__balance -= amount
                print(f'ถอนเงินสำเร็จ: {amount} บาท')
        else:
                print(f'ถอนไม่สำเร็จ ! (ยอดเงินไม่เพียงพอ: {amount})')

    def check_balance(self):
        return self.__balance