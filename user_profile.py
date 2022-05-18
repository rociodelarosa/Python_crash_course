from distutils.command.build import build


def build_profile(first, last, **user_info): # **user_infoel doble asterisco crea un diccionario vacío de nombre user_info y guarda cualquier combinación nombre-valor
    """Build a dictionary containing everything we know abost a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)