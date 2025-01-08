is_game_over = False
print(is_game_over)

is_game_over = True
print(is_game_over)

is_game_over = 5 > 6
print(is_game_over)

num_lives = 5
print(num_lives)

percent_health = 0.5
print(percent_health)

player_name = 'Tacos'
print(player_name)

player_name = "Spoon"
print(player_name)

print(type(is_game_over))
print(type(num_lives))
print(type(percent_health))
print(type(player_name))

num_lives = 5
str_num_lives = str(num_lives)
print(type(num_lives))
print(type(str_num_lives))

print(bool(0))
print(bool(0.1))
print(bool("asdf"))
print(bool("False"))

# print(int("asdfasdf"))
print(int("1"))
print(int(0.5))
print(int(False))
print(int(True))

print(float("1"))
print(float(5))
print(float(False))
print(float(True))

# Operators
health = 50
new_health = health + 20
print(health)
health += 20
print(health)

xPos = 5
print(xPos % 2)
print(xPos // 2)
print(xPos ** 2)
print(xPos)

first_name = "first"
last_name = "last"
print(first_name + " " + last_name)

name = "first"
name += " last"
print(name)

print("a" == False)
print("aa" > "b")

# not
is_game_over = False
is_game_over = not is_game_over
print(is_game_over)

# and
health = 0
lives = 1
print(health <= 0 and lives <= 0)

# or
print(health <= 0 or lives <= 0)