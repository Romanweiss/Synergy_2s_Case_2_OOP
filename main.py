from __future__ import annotations


class Employee:
    """Базовый класс сотрудника."""

    def __init__(self, name: str, base_salary: float) -> None:
        self.name = name
        self.base_salary = float(base_salary)

    def get_role(self) -> str:
        """Метод базового класса."""
        return "Employee"

    def calc_salary(self) -> float:
        """Метод базового класса: базовая зарплата без надбавок."""
        return self.base_salary

    def info(self) -> str:
        """Общий метод, который использует другие методы (полиморфизм)."""
        return f"{self.name} | role={self.get_role()} | salary={self.calc_salary():.2f}"


class Developer(Employee):
    """Производный класс разработчика."""

    def __init__(self, name: str, base_salary: float, level: str, bonus: float = 0.0) -> None:
        super().__init__(name, base_salary)
        self.level = level
        self.bonus = float(bonus)

    # Переопределение (override) метода базового класса
    def get_role(self) -> str:
        return f"Developer({self.level})"

    # Переопределение (override) метода базового класса
    def calc_salary(self) -> float:
        # разработчик получает базу + бонус
        return self.base_salary + self.bonus

    def write_code(self) -> str:
        """Метод, которого нет в базовом классе."""
        return f"{self.name} writes code"


def print_staff(staff: list[Employee]) -> None:
    """Функция показывает полиморфизм: работает с базовым типом Employee."""
    for person in staff:
        print(person.info())


def main() -> None:
    e = Employee("Ivan", 50000)
    d = Developer("Roman", 70000, level="Middle", bonus=15000)

    # Демонстрация методов базового и производного классов
    print("=== Direct calls ===")
    print(e.get_role(), e.calc_salary())
    print(d.get_role(), d.calc_salary())
    print(d.write_code())

    # Демонстрация полиморфизма
    print("\n=== Polymorphism (same interface, different behavior) ===")
    staff: list[Employee] = [e, d]
    print_staff(staff)


if __name__ == "__main__":
    main()
