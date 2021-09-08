from django.contrib.auth.models import User

from transactions_api.models import Transact

usernames = ['one', 'two', 'three']
first_names = ['Lex', 'Oleg', 'Michail']
last_names = ['Ovcharov', 'Richardson', 'De Leville']
emails = ['acies@mail.com', 'test@example.com', 'jorj23@vc.ru']

for user in range(3):
    User(usernames[user],
         first_names[user],
         last_names[user],
         emails[user]).save()

# for transact in range(8):
