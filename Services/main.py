from datetime import date
from UsersService import User, UsersFilter
from UserServiceImpl import UsersServiceImpl

service = UsersServiceImpl()

u1 = User(name="Pepe", birth_date=date(1990, 1, 1))
id1 = service.create_user(u1)

u2 = User(name="Maria", birth_date=date(2005, 5, 20))
id2 = service.create_user(u2)

u3 = User(name="Pepa", birth_date=date(1990, 1, 1))
id3 = service.create_user(u3)

u4 = User(name="Mario", birth_date=date(2005, 5, 20))
id4 = service.create_user(u4)


print(service.read_user(id1))


nuevo_datos = User(name="Pepe Modificado", birth_date=date(1990, 1, 1))
print(service.update_user(id1, nuevo_datos))


filtro = UsersFilter(match_pattern="Maria", min_age=0)
print(service.list_users(filtro, 0, 10))

print(service.delete_user(id2))

print(service.list_users(UsersFilter(min_age=-1), 0, 100))
