from faker import Faker
fake = Faker()


fakes = {
    'first_name': [fake.unique.first_name() for _ in range(500)],
    'last_name': [fake.unique.last_name() for _ in range(500)]
}

def pseudonymize(key, data):
    if key in fakes:
        return fakes[key][len(data)]
    return key
