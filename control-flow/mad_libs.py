# Prompt the User for Words
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")
adjective4 = input("Enter a final adjective: ")

# Story template
story = f"""On a beautiful {adjective1} day, I went to the zoo.
I saw a funny {adjective2} monkey swinging from the trees.
Then, I spotted a majestic {adjective3} lion lounging in the sun.
What a wild and {adjective4} experience!"""

if adjective1.lower() == "rainy":
    story += " Unfortunately, it stated to drizzle, making everything a little gloomy."
elif adjective1.lower() == "sunny":
    story += "The sun made the animals extra lively and playful."
if adjective2.lower() == "silly":
    story += " The monkey was especially goofy!"
elif adjective2.lower() == "scary":
    story += " The monkey gave me an eerie stare"

print("\nHere's your Mad Libs story:\n")
print(story)