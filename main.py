from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary_per_hour, hours):
        self.__name = name
        self.__salary_per_hour = salary_per_hour
        self.__hours = hours

    @abstractmethod
    def calculate_salary(self):
        return self.__salary_per_hour * self.__hours

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name

    @property
    def salary_per_hour(self):
        return self.__salary_per_hour

    @salary_per_hour.setter
    def salary_per_hour(self, value):
        self.__salary_per_hour = value

    @salary_per_hour.deleter
    def salary_per_hour(self):
        del self.__salary_per_hour

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value):
        self.__hours = value

    @hours.deleter
    def hours(self):
        del self.__hours


class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return super().calculate_salary()


class PartTimeEmployee(Employee):
    def calculate_salary(self):
        return super().calculate_salary() - 10


ft1 = FullTimeEmployee("Toxir", 15, 8)
print(ft1.calculate_salary())


pt1 = PartTimeEmployee("Sobir", 14, 4)
print(pt1.calculate_salary())


# --------------------------------------------------------
