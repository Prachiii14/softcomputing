import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt # Standard alias is plt

# Universe variables
temp_range = np.arange(0, 41, 1)
fs_range = np.arange(0, 101, 1)

# Fuzzy variables
temperature = ctrl.Antecedent(temp_range, 'temperature')
fan_speed = ctrl.Consequent(fs_range, 'fan_speed')

# Membership functions
# automf(3) creates 'poor', 'average', and 'good'
temperature.automf(3)
fan_speed.automf(3)

# Rules
rule1 = ctrl.Rule(temperature['poor'], fan_speed['poor'])
rule2 = ctrl.Rule(temperature['average'], fan_speed['average'])
rule3 = ctrl.Rule(temperature['good'], fan_speed['good'])

# Control system
fan_speed_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_speed_simulation = ctrl.ControlSystemSimulation(fan_speed_ctrl)

# User input
try:
    temp_input = float(input("Enter temperature in C (0-40): "))
    fan_speed_simulation.input['temperature'] = temp_input

    # Compute
    fan_speed_simulation.compute()

    # Fixed the variable name from temp_temp to temp_input
    fanSpeed = fan_speed_simulation.output['fan_speed']
    print(f"For a temperature of {temp_input} C, the calculated fan speed is: {fanSpeed:.2f}%")
    
    # Visualize result
    fan_speed.view(sim=fan_speed_simulation)
    plt.show()

except ValueError:
    print("Please enter a valid numeric temperature.")
