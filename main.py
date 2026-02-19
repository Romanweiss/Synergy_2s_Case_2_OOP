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
        """Общий метод с полиморфным поведением через get_role/calc_salary."""
        return f"{self.name} | role={self.get_role()} | salary={self.calc_salary():.2f}"


class Developer(Employee):
    """Производный класс разработчика."""

    def __init__(self, name: str, base_salary: float, level: str, bonus: float = 0.0) -> None:
        super().__init__(name, base_salary)
        self.level = level
        self.bonus = float(bonus)

    def get_role(self) -> str:
        """Переопределение метода базового класса."""
        return f"Developer({self.level})"

    def calc_salary(self) -> float:
        """Переопределение метода базового класса: база + бонус."""
        return self.base_salary + self.bonus

    def write_code(self) -> str:
        """Метод, которого нет в базовом классе."""
        return f"{self.name} writes code"


def print_staff(staff: list[Employee]) -> None:
    """Показывает полиморфизм: единый вызов info() для разных классов."""
    for index, person in enumerate(staff, start=1):
        print(f"{index}. [{person.__class__.__name__}] {person.info()}")


def print_header(title: str) -> None:
    separator = "=" * 72
    print(separator)
    print(title)
    print(separator)


def main() -> None:
    employee = Employee("Ivan", 50_000)
    developers = [
        Developer("Roman", 70_000, level="Middle", bonus=15_000),
        Developer("Anna", 55_000, level="Junior", bonus=5_000),
    ]

    print_header("DEMO: BASE AND DERIVED CLASS METHODS")

    print("\n[1] Base class object (Employee)")
    print(f"Object data: name={employee.name}, base_salary={employee.base_salary:.2f}")
    print(f"get_role() -> {employee.get_role()}")
    print(f"calc_salary() -> {employee.calc_salary():.2f}")
    print(f"info() -> {employee.info()}")

    print("\n[2] Derived class objects (Developer)")
    for index, developer in enumerate(developers, start=1):
        print(f"Developer #{index}: name={developer.name}, level={developer.level}")
        print(f"  get_role() -> {developer.get_role()}")
        print(
            f"  calc_salary() -> {developer.calc_salary():.2f} "
            f"(base={developer.base_salary:.2f} + bonus={developer.bonus:.2f})"
        )
        print(f"  write_code() -> {developer.write_code()}")
        print(f"  info() -> {developer.info()}")

    print("\n[3] Polymorphism demo")
    print("Calling one interface info() for mixed list[Employee]:")
    staff: list[Employee] = [employee, *developers]
    print_staff(staff)


if __name__ == "__main__":
    main()
