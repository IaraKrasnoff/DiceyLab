import random #We need real numbers to mimic real dice

class Bins: #This class keeps a count for each possible sum on the dice
    def __init__(self, min_bin: int, max_bin: int):
        self.min_bin=min_bin # The smallest total possible (like 2 with 2 dice)
        self.max_bin=max_bin # The largest total possible (like 12 with 2 dice)
    

        #if using dictionaries
        '''
        self.bins={}
        for i in range(self.min_bin, self.max_bin+1):
            self.bins[i]=0
        '''
        self.bins=[]  # Create empty bins, one for each possible sum
   
        for i in range(self.min_bin, self.max_bin+1):
            self.bins.append(0) # Start each bin count at zero


    def get_bin(self, bin_num: int):
       # Returns how many times we've hit 'bin_num' as the sum
        return self.bins[bin_num-self.min_bin]
    
    def get_index(self, value: int):
        # Not really used—finds which bin has a certain value
        return self.bins.index(value)+self.min_bin
      
    def increment_bin(self, bin_num: int):
       # Adds 1 to the bin that matches the rolled sum 
        self.bins[bin_num-self.min_bin]+=1
    


class Dice:
    # This class handles rolling a group of dice and getting their total
    def __init__(self, sides: int, rolls: int):
        self.sides=sides # How many sides does each die have? (6 for normal dice)
        self.rolls=rolls # How many dice are we rolling together?


    def __str__(self):
    # Words to describe what dice we're rolling
       
            if self.rolls==1:
                return f"Rolled a {self.sides}-sided die 1 time\n"
            return f"Rolled a {self.sides}-sided die {self.rolls} times\n"

    def roll(self): # Roll one die and get a number between 1 and 'sides'
    
        return random.randrange(1, self.sides+1)

    def toss_and_sum(self):
        # Roll all the dice, add their faces together, and return the total
        sum=0
        for i in range(self.rolls):
            sum+=self.roll()
        return sum


class Simulation:
    # This class runs the whole experiment many times and keeps the results

    def __init__(self, Sides: int, Dies: int, Tosses: int):
        self.Sides=Sides # Number of sides on a die
        self.Dies=Dies  # Number of dice thrown at once
        self.Tosses=Tosses # How many times do we throw all of them

        self.sim_bins=Bins(self.Dies, self.Dies*self.Sides) # Make bins for all possible totals
        self.die_roll=Dice(self.Sides, self.Dies)  # Make a dice object to roll

    def calculateMinMax(self):
         # Print how many different possible results we have
        print(f"There are {self.Dies*self.Sides-self.Dies+1} bins total")

    def run_simulation(self):
        # Do lots of dice throws, record each total in the right bin
        for i in range(self.Tosses):
            score=self.die_roll.toss_and_sum() # Roll all dice & get sum
            self.sim_bins.increment_bin(score)  # Add one to the right bin
        return self.sim_bins # Return all the bins (with counts)


    def print_results(self):
        # Print the results—showing the sum, how many times, % chance, and a star bar
        results= ""
        for index, bin in enumerate(self.sim_bins.bins):
            sum_value = index + self.Dies                    # The actual sum you rolled (like 2, 3,... for 2 dice)
            count = bin                                      # How many times did this sum happen?
            prob = round(count / self.Tosses, 2)             # Probability (rounded to 2 digits)
            stars = "*" * ((count * 100) // self.Tosses)     # Make 1 star per 1% chance, sort of
            results += f"{sum_value:>2} : {count:>8}: {prob:<4} {stars}\n"
        return results                                       # Return the whole fancy chart


def main():
# Try out the Dice class
    print("\nDice() Testing\n")
    craps=Dice(6, 2) # 2 dice, 6 sides
    for i in range(10):
        print(f"Roll {i+1} for craps is {craps.toss_and_sum()}")
       # Let's check if it's within range
        latest_roll = craps.toss_and_sum()
    if latest_roll in range(craps.rolls, craps.sides * craps.rolls + 1):
           print(f"Roll {i+1} is within range\n")
    print(craps)
    print("\n")



   # Try out the dice with 5 rolls (yahtzee style)
    yatzee = Dice(6, 5)
  # Just do 10 examples to save space
    for i in range(10):
        print(f"Roll {i+1} for yatzee is {yatzee.toss_and_sum()}")
        if craps.toss_and_sum() in range(craps.rolls, craps.sides*craps.rolls+1):
            print(f"Roll {i+1} is within range\n")
    print(yatzee)



    # Test Bins class
    print("\nBins() Testing \n")
    results = Bins(2, 12)  # for bins from 2..12
    print(f"Bins at start: {results.bins}")
    for i in range(100):
        roll=craps.toss_and_sum() # Roll dice
        results.increment_bin(roll) # Add to bin
    for i in range(len(results.bins)):
        print(f"Bin {i+results.min_bin}'s total is {results.get_bin(i)}")
    print(f"Bins at end: {results.bins}")



    # Now let's try a real simulation!
    print("\nSimulation() Testing \n")

    print("Test 1")
    sim1 = Simulation(6, 2, 20) # 2 dice, 6 sides, 20 times
    sim1.calculateMinMax()
    finals1=sim1.run_simulation()
    print(finals1.bins)
    printings1=sim1.print_results()
    print(printings1)

    print("Test 2")
    sim2 = Simulation(8, 3, 100) # 3 dice, 8 sides, 100 times 
    sim2.calculateMinMax()
    finals2=sim2.run_simulation()
    print(finals2.bins)
    printings2=sim2.print_results()
    print(printings2)


# If we run this file, start at main()!
if __name__ == "__main__":
    main()