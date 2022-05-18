unconfirmed_users = ['alice', 'brian', 'candance']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop() #pop() remueve los ususarios no verificados uno a la vez desde el final de unconfirmed_users

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())