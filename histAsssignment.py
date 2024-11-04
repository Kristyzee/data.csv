import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

# Assignment
# 1. Write a code that generates a histogram with the 
# blood sugar levels of men and women plotted side-by-side 
# for comparison.
# . Each bar represents the total number of patients falling 
# within the specified blood sugar range 
# . The bars should have colors 'Green' and 'Red', for the male 
# and female respectively
# . Each of the men and women diistributions shoud have 15 
# random entries each, generated using python
# . Label and format the X-label, Y-label and Title
# . The plot should change each time the code is ran
# . Each of the green-orange pair of bars is to be 
# separated from each other by a space of 0.98

# 2. Write a code to show the distribution of blood 
# sugar levels across three ranges(bins) (80–100, 100–125, 125–150)
# . Each bin will be colored differently: the first bin in red, the 
# second in yellow, and the third in blue.
# . The bars will have a relative width of 0.98, leaving a small 
# gap between each bar.
# . Also add a legend to the plot
# . Add X-labe, Y-label and Title

# 3. Create an animated histogram that updates in real-time. 
# The animation simulates new data coming in, and the 
# histogram dynamically updates to show changes in the 
# data distribution

# 4. Write a code to create and customize a histogram. 
# It should include color customization for the histogram 
# bars, vectorization for timestamp conversion, and 
# formatting of the plot. The plot should display a histogram 
# with 10 bins, each colored using a list of ten different colors 
# except red. The edge of each bar should be red, and the title 
# will read "My Histogram" with "Check it out" on the next line(create a line break for multi line text).

# 5. Write a code to visualize expenses with labels and 
# percentages using pie chart.
# . Using exp_vals = [1400, 600, 300, 410, 250]
# exp_labels = ['House rent', 'food', 'internet', 'car', 'others'],

# exp_vals: A list containing the monetary values of different expenses.
# exp_labels: A list of strings that label each corresponding expense in exp_vals.
# Each slice of the pie is to be separated from the center in the order 0, 0.1, 0.1, 0.2, 0.1
# respectively


        #  111111111111111111111111111111111111111111111
women_blood_sugar=np.random.randint(75, 100,15)
#print(f'random values for women are :{women} ')
men_blood_sugar = np.random.randint(75,100,15)
#print(f'random values for men are: {men} ')
plt.hist([women_blood_sugar,men_blood_sugar], label=["women", "men"],color=["red","green"] )
bar_width=0.98
plt.title("BLOOD SUGAR LEVELS OF WOMEN $ MEN",fontsize=20,color="purple")
plt.xlabel("women_blood_sugar", fontsize=30,color="hotpink")
plt.ylabel("men_blood_sugar", fontsize=25, color="maroon")
plt.show()




#########22222#################

# Generate random blood sugar levels
np.random.seed()
blood_sugar_levels = np.random.randint(80, 150, 100)

# Create bins for blood sugar ranges
bins = [0, 80, 100, 125]
labels = ['80-100', '100-125', '125-150']
colors = ['red', 'yellow', 'blue']

# Initialize counts for each bin
counts = [0] * len(labels)

# Count patients in each range
for sugar in blood_sugar_levels:
    if 80 <= sugar < 100: counts[0] += 1
    elif 100 <= sugar < 125: counts[1] += 1
    elif 125 <= sugar <= 150: counts[2] += 1

# Create figure and axis
fig, ax = plt.subplots()

# Set bar width
bar_width = 0.98

# Set bar positions
x = np.arange(len(labels))

# Create bars for each bin
ax.bar(x, counts, width=bar_width, color=colors)

# Set title and labels
ax.set_title('Distribution of Blood Sugar Levels')
ax.set_xlabel('Blood Sugar Range')
ax.set_ylabel('Number of Patients')

# Set xticks
ax.set_xticks(x)
ax.set_xticklabels(labels)

# Legend
ax.legend(labels, loc='upper right', title='Blood Sugar Ranges')

# Display plot
plt.show()






   #3333333333333333333333333333s

# Create figure and axis
fig, ax = plt.subplots()

# Function to update histogram
def update(frame):
    ax.clear()
    x= np.random.rand(100)

    n, bins, patches = ax.hist(x, bins=10)
    
    # Color each bin differently
    for i, patch in enumerate(patches):
        patch.set_facecolor(plt.cm.rainbow(i/len(patches)))
    
    ax.set_title("Dynamic Histogram", fontsize=14)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_xlim(-5, 5)  # Set x-axis limits
    ax.set_ylim(0, 20)  # Set y-axis limits

# Create animation
ani = animation.FuncAnimation(fig, update, interval=1000)

# Display animation
plt.show()







      #44444444444444444444444444444444444444444444

# Generate random data
np.random.seed()
data= np.random.randn(2000)

# Create list of colors (excluding red)
colors = ['orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'pink', 'brown', 'gray', 'cyan']

# Create figure and axis
fig, ax = plt.subplots()

# Create histogram with customized colors
n, bins, patches= ax.hist(data, bins=10, edgecolor='red')

#color each bin differently
for i, patch in enumerate(patches):
    patch.set_facecolor(colors[i % len(colors)])
    
# Set title with line break
ax.set_title("My Histogram\nCheck it out", fontsize=16)

# Set labels
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")

# Display plot
plt.show()












     #5555555555555555555555555555555
y=np.array([1400,600,300,410,250])
mylabels=['House rent', 'food','internet','car','others']
myexplode=[0,0.1,0.1,0.2,0.1]
plt.pie(y, labels = mylabels , explode=myexplode)

plt.show()


      


