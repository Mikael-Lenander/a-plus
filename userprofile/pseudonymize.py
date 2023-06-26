from faker import Faker
import hashlib

fake = Faker()
num_fakes = 500

fakes = {
    'first_name': [fake.unique.first_name() for _ in range(num_fakes)],
    'last_name': [fake.unique.last_name() for _ in range(num_fakes)],
    'email': [fake.unique.email() for _ in range(num_fakes)],
    'username': [fake.unique.user_name() for _ in range(num_fakes)],
    'student_id': [fake.unique.iana_id() for _ in range(num_fakes)],
}

def pseudonymize(key, data):
    # hashkey = int(hashlib.md5(data.encode('utf-8')).hexdigest(), 16) % num_fakes
    # if key in fakes:
    #     return fakes[key][hashkey]
    return key

