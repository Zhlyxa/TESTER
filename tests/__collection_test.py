from tester import test_case

def tests() -> None:
    @test_case([(1,2),(3,4)],[3,7])
    def test1(number1,number2):
        return number1 + number2

    @test_case([('name','Anton'),('name','Nikita')],[{'name':'Anton'},{'name':'Nikita'}])
    def test2(key,value):
        return {key:value}

    @test_case([('Anton',),('Nikita',)],["Person(self.name='Anton')","Person(self.name='Nikita')"])
    def test3(name):
        class Person:
            def __init__(self,name) -> None:
                self.name = name
            
            def __str__(self) -> str:
                return f'Person({self.name=})'

        return str(Person(name))

    @test_case([({'name':'Anton','hobby':['sport','programming','chilling']},)],["Person(self.name='Anton',self.hobby=['sport', 'programming', 'chilling'])"])
    def test4(data):
        class Person:
            def __init__(self,name,hobby) -> None:
                self.name = name
                self.hobby = hobby
            
            def __str__(self) -> str:
                return f'Person({self.name=},{self.hobby=})'

        return str(Person(data['name'],data['hobby']))

    test1(number1=..., number2=...)
    test2(key=..., value=...)
    test3(name=...)
    test4(name=...,hobby=...)


if __name__ == "__main__":
    tests()

