from rolepermissions.roles import AbstractUserRole

class Admin(AbstractUserRole):
    available_permissions = {
        'create_game' : True,
        'update_game' : True,
        'delete_game' : True,
    }


class Normal(AbstractUserRole):
    available_permissions = {
        'create_game' : False,
        'update_game' : False,
        'delete_game' : False,
        'read_game' : True,
    }
