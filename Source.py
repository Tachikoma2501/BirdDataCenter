#defines answers as True
answer = True

import numpy as np
import matplotlib.pyplot as plt

hawks = 1000
eagles = 1000
vultures = 1000
ravens = 1000

print("Welcome to the bird database")
print("This program will show the average wingspan of four birds")
print("and their respective graphs showing the data")

while answer:
    print("""
    1. View Bird Wingspans
    2. View Graph
    3. Exit
    """)
    #if statement for if the user inputs 1 to list current birds and their wingspans
    answer=input('Enter Option: ')
    if answer == '1':
        print("The average wingspan of a Red-Tailed hawk is 3.4-4.8 feet or 40.8-57.6 inches")
        print("The average wingspan of a Bald Eagle is 5.9-7.5 feet or 70.8-90 inches")
        print("The average wingspan of a Black Vulture is 4.4-5.5 feet or 52.8-66 inches")
        print("The average wingspan of a Common Raven is 3.3-4.9 feet or 39.6-58.8 inches")

    # if statement for if the user inputs 2 to view the graph
    elif answer == '2':

        print("Hawk = Blue, Eagle = Red, Vulture = Green, Raven = Yellow")

        # The average wingspan of a Red-Tailed hawk is 3.4-4.8 feet or 40.8"-57.6" inches
        # The average wingspan of a Bald Eagle is 5.9-7.5 feet or 70.8"-90" inches
        # The average wingspan of a Black Vulture is 4.4-5.5 feet or 52.8"-66" inches
        # The average wingspan of a Common Raven is 3.3-4.9 feet or 39.6"-58.8" inches
        # Add plus/minus inches (depending on the bird)
        # for the different sizes for a type of bird
        hawk_wingspan = 40 + 14 * np.random.randn(hawks)
        eagle_wingspan = 71 + 19 * np.random.randn(eagles)
        vulture_wingspan = 53 + 13 * np.random.randn(vultures)
        raven_wingspan = 40 + 10 * np.random.randn(ravens)

        # Visualize our data in a histogram
        # Bombers in blue and fighters in red

        plt.hist([hawk_wingspan, eagle_wingspan, vulture_wingspan, raven_wingspan], stacked=True,
                 color=['b', 'r', 'g', 'y'])
        plt.show()

    #elif statement to end the program
    elif answer == '3':
        break





