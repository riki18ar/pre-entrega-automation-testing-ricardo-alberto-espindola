from faker import Faker


fake = Faker() # Faker genera datos aleatorios para pruebas.

def get_login_faker(num_casos=5):
    casos = []
    # usuarios_valido = "standard_user"
    # password_valido = "secret_sauce"
    for _ in range(num_casos):
        #if fake.boolean(chance_of_getting_true=30):
        username = fake.user_name()
        password = fake.password(length=12)
            # username = fake.random_choices(usuarios_valido)
            # password = password_valido
        login_example = fake.boolean(chance_of_getting_true=50)
            #login_example = True
        # else:
        #     username = fake.user_name()
        #     password = fake.password(length=12)
        #     login_example = False
        casos.append((username, password, login_example))
    return casos