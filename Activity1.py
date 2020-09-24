# By submitting this assignment, I agree to the following:
#  "Aggies do not lie, cheat, or steal, or tolerate those who do"
#  "I have not given or received any unauthorized aid on this assignment"
#
# Name:         Nathaniel Michaud, Luca Maddaleni, Landon Matak, Anthony Matl
# Group:        8
# Section:      273
# Assignment:   Lab 5
# Date:         25 September 2020

user_dist = float(input('Enter the distance in feet: '))
fusion_time = float(input('What is the time before Mr. Fusion finishes updates in seconds: '))

dist = 0.0
TOL = 1.0**(-8)
time = 0.01
increment = 0.01
count = 0

while user_dist - dist > TOL:
    dist = time*1/2*(1936/15) #Uses a conversion factor from mph to ft/sec.
    time += increment
    count += 1
#Iterates until the distance is negative, meaning it has reached the input distance once done.
print('\nIt takes Marty', time, 'seconds to reach 88 mph.')
if time <= fusion_time:
    print('So he will make it in time.')
else:
    print('So he will not make it in time.')
print('And the process took', count//120, 'banana peels') #Per 120 iterations.


