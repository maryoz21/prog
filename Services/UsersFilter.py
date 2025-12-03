from UsersService import *

def filter_user_with_name(pattern: str, users: list[User]) -> list[User]:
    result: list[User] = []
    for user in users:
        if pattern in user.name:
            result.append(user)
    return result

def calculate_age(birth_date: date) -> int:
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def filter_user_with_age(min_age: int, users: list[User]) -> list[User]:
    result = []
    for user in users:
        if user.birth_date is None:
            continue
        age = calculate_age(user.birth_date)
        if age >= min_age:
            result.append(user)
    return result
