print("Wlcome to the basketball Roster Program")
print()
players = []
player = input("Who is your point guard: ")
players.append(player.title())
player = input("Who is your shooting guard: ")
players.append(player.title())
player = input("Who is your small forward: ")
players.append(player.title())
player = input("Who is your power forward: ")
players.append(player.title())
player = input("Who is your center: ")
players.append(player.title())
print("Your starting 5 for the upcoming basketball")
print()
print("\t\tPoint guard:\t\t" + players[0])
print("\t\tshooting guard:\t\t" + players[1])
print("\t\tsmall forward:\t\t" + players[2])
print("\t\tpower forward:\t\t" + players[3])
print("\t\tcenter: \t\t" + players[4])
print()
print("oh no," + players[3] + " is injured")
print("your roaster has only four players now")
newplayer = input("who will take " + players[3] + "'s spot: ")
players[3] = newplayer.title()
print()
print("Your starting 5 for the upcoming basketball")
print()
print("\t\tPoint guard:\t\t" + players[0])
print("\t\tshooting guard:\t\t" + players[1])
print("\t\tsmall forward:\t\t" + players[2])
print("\t\tpower forward:\t\t" + players[3])
print("\t\tcenter: \t\t" + players[4])
print()

print("Good luck " + players[3]+ '..!')
