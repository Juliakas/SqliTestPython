import cx_Oracle

user_id = input("Įveskite vartotojo ID: ")

conn_str = 'JR/JR@localhost:01521/dba.sqli_test'
conn = cx_Oracle.connect(conn_str)
c = conn.cursor()

prompt = "select all users where user id is {0}".format(user_id)
# Klaidingai teigiamas
unused = "SELECT * FROM users WHERE user_id = {0}".format(user_id)

# Aptinka
query = "SELECT * FROM users WHERE user_id = {0}".format(user_id)
# query = "SELECT * FROM users WHERE user_id = " + user_id
row = c.execute(query)
for row in c:
    print ([col for col in row])

# Neaptinka
query = "SELECT * FROM users WHERE user_id = {0}"
query = query.format(user_id)
# query = "SELECT * FROM users WHERE user_id = " + user_id
row = c.execute(query)
for row in c:
    print ([col for col in row])

# Aptinka
query = 'SELECT * FROM users WHERE user_id = %s' % user_id
row = c.execute(query)
for row in c:
    print ([col for col in row])

# Neaptinka
query = "SELECT * FROM users WHERE user_id = " + user_id
row = c.execute(query)
for row in c:
    print ([col for col in row])

# Aptikta (Tik su Python Security PyCharm plugin)
query = f'SELECT * FROM users WHERE user_id = {user_id}'
row = c.execute(query)
for row in c:
    print ([col for col in row])

# Aptinka (nors innerVal reikšmė priskiriama kode)
innerVal = '1'
query = f'SELECT * FROM users WHERE user_id = {innerVal}'
row = c.execute(query)
for row in c:
    print ([col for col in row])

table = "users"
query = "SELECT * FROM users WHERE user_id = :user_id"
row = c.execute(query, {"user_id": user_id})
for row in c:
    print ([col for col in row])

conn.close()
