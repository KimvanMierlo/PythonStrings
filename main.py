# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
scorer1_name = 'Gullit'
scorer2_name = 'Van Basten'
goal_0 = 32
goal_1 = 54
scorers = scorer1_name + ' ' + str(goal_0) + ', ' + scorer2_name + ' ' + str(goal_1)
report = f'{scorer1_name} scored in the {goal_0}nd minute\n{scorer2_name} scored in the {goal_1}th minute'
player = 'Frank Rijkaard'
first_name = player[0:player.find(' ')]
last_name = player[player.find(' ') + 1:]
last_name_len = len(last_name)
name_short = first_name[:1] + '. ' + last_name
chant = (first_name + "! ") * (len(first_name) - 1) + ( first_name + "!")
good_chant = chant[len(chant) - 1:] != ' '