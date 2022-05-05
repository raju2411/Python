class myClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name,age)


class calculate:
    def __init__(self,num1,num2):
        self.num11=num1
        self.num2=num2

    def addition(self,number):
        sum=number+self.num11
        print(sum)

    def subtract(self):
        sub=self.num1-self.num2
        print(sub)


s=calculate(2,3).addition(10)



