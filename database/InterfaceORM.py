#!/usr/bin/python3.6

from database.ConnectionDb import ConnectionDb


class InterfaceORM(type):
    connection = ConnectionDb()

    def __new__(mcs, class_name, supers, class_dict):
        maped_name = InterfaceORM.__map_to_db_name(class_name)
        names = InterfaceORM.connection.get_column_names(maped_name)
        for name in names:
            func = lambda x: InterfaceORM.__get_column(name, class_name)
            class_dict.update({name: property(func)})
        return super(InterfaceORM, mcs).__new__(mcs, class_name, supers, class_dict)

    @staticmethod
    def __get_column(column, class_name):
        maped_name = InterfaceORM.__map_to_db_name(class_name)
        return InterfaceORM.connection.get_column(column, maped_name)

    @staticmethod
    def __map_to_db_name(name):
        return name.lower() + 's'


class Subject(metaclass=InterfaceORM):pass

a = Subject()

print(a.id)
