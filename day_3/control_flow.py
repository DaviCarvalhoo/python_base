def unlock_adult_movies(name,age):
    name = name.title()
    if age >= 18:
        msg= f"{name} pode assistir"
    else:
        msg= f"{name} não pode assistir"
    return msg
print(unlock_adult_movies("davi",18))