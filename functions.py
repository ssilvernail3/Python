# def greet(person):
#     return f'Hello There, {person}'

# def divide(a,b):
#     if type(a) is int and type(b) is int:
#          return a / b
#     return "a and b must be integers!"


def send_email(to_email, from_email, subject, body):
    email = f'''
        to: {to_email} 
        from: {from_email}
        subject: {subject}
        --------------------
        body: {body}
    '''
    print(email)


send_email(subject="meow", to_email='blue@gmail.com',
           from_email='colt@humans.com', body='hi blue you are my cat i love you!')


def power(num, power):
    '''Take a number and raise to a particular power'''
    return num ** power

# use dir() to see methods and properties
