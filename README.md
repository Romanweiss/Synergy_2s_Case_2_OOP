# Кейс-задача №2 — Демонстрация работы базового и производного классов (Python OOP)

## Описание
Программа демонстрирует работу методов базового и производного классов.
Реализованы и наглядно показаны:
- наследование;
- переопределение методов;
- полиморфизм.

## Условие задачи
Написать тестовую программу, которая демонстрирует работу методов базового и производного классов.

## Что сделано для наглядности проверки
- Вывод разделён на 3 логических блока:
  1. Методы базового класса.
  2. Методы производного класса.
  3. Полиморфизм через общий интерфейс.
- Добавлено разнообразие данных: используется несколько объектов `Developer` с разными уровнями и бонусами.
- Для каждого вызова явно показано, какой метод вызван и какой результат получен.

## Реализованные классы
- `Employee` — базовый класс.
- `Developer(Employee)` — производный класс.

## Запуск
```bash
python main.py
```

## Пример вывода
```text
========================================================================
DEMO: BASE AND DERIVED CLASS METHODS
========================================================================

[1] Base class object (Employee)
Object data: name=Ivan, base_salary=50000.00
get_role() -> Employee
calc_salary() -> 50000.00
info() -> Ivan | role=Employee | salary=50000.00

[2] Derived class objects (Developer)
Developer #1: name=Roman, level=Middle
  get_role() -> Developer(Middle)
  calc_salary() -> 85000.00 (base=70000.00 + bonus=15000.00)
  write_code() -> Roman writes code
  info() -> Roman | role=Developer(Middle) | salary=85000.00
Developer #2: name=Anna, level=Junior
  get_role() -> Developer(Junior)
  calc_salary() -> 60000.00 (base=55000.00 + bonus=5000.00)
  write_code() -> Anna writes code
  info() -> Anna | role=Developer(Junior) | salary=60000.00

[3] Polymorphism demo
Calling one interface info() for mixed list[Employee]:
1. [Employee] Ivan | role=Employee | salary=50000.00
2. [Developer] Roman | role=Developer(Middle) | salary=85000.00
3. [Developer] Anna | role=Developer(Junior) | salary=60000.00
```
