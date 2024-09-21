class Calculator:

    def __init__(self ,  a ,j ,b):
        self.a = a
        self.b = b
        self.j = j

    def sum(self):
        s = self.a + self.b 
        print(f"{self.a}+{self.b}={s}") 

    def mul(self):
        z = self.a * self.b
        print(f"{self.a}*{self.b}={z}") 

    def sub(self):
       t = self.a - self.b
       print(f"{self.a}-{self.b}={t}")

    def taq(self):
        tt= self.a / self.b
        print(f"{self.a}/{self.b}={tt}") 


sss = Calculator(int(input("adadi 1 vorid ->" )),input("amal vorid bikun->"),int(input("adadi 2 vorid ->")) )        
sss.sum()
sss.sub()
sss.taq()
sss.mul()