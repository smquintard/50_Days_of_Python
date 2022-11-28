##################
# Write a function called longest_value that takes a dictionary as an argument
# and returns the first longest value of the dictionary. 
# For example, the dictionary should return apple as the longest value
# fruits = {'fruit':'apple','color':'green'}
#################

# Define funtion
capitals = {
        "Maine":"Augusta",
        "New Hampshire":"Concord",
        "Vermont":"Montpelier",
        "Massachusetts":"Boston"
        }

longest_value = max(capitals.values())

print(longest_value)
