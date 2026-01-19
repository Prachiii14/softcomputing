import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


attendance = ctrl.Antecedent(np.arange(0, 101, 1), 'attendance')
assignments = ctrl.Antecedent(np.arange(0, 101, 1), 'assignments')
final_grade = ctrl.Consequent(np.arange(0, 101, 1), 'final_grade')

attendance['poor'] = fuzz.trapmf(attendance.universe, [0, 0, 40, 60])
attendance['average'] = fuzz.trimf(attendance.universe, [40, 60, 80])
attendance['excellent'] = fuzz.trapmf(attendance.universe, [60, 80, 100, 100])

assignments['poor'] = fuzz.trapmf(assignments.universe, [0, 0, 40, 60])
assignments['average'] = fuzz.trimf(assignments.universe, [40, 60, 80])
assignments['excellent'] = fuzz.trapmf(assignments.universe, [60, 80, 100, 100])

final_grade['fail'] = fuzz.trimf(final_grade.universe, [0, 0, 50])
final_grade['pass'] = fuzz.trimf(final_grade.universe, [40, 60, 80])
final_grade['distinction'] = fuzz.trimf(final_grade.universe, [70, 100, 100])

rule1 = ctrl.Rule(attendance['poor'] | assignments['poor'], final_grade['fail'])
rule2 = ctrl.Rule(attendance['average'] & assignments['average'], final_grade['pass'])
rule3 = ctrl.Rule(assignments['excellent'], final_grade['distinction'])
rule4 = ctrl.Rule(attendance['excellent'] & assignments['average'], final_grade['distinction'])

evaluation_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4])
evaluation_sim = ctrl.ControlSystemSimulation(evaluation_ctrl)

try:
    att_in = float(input("Enter Attendance % (0-100): "))
    ass_in = float(input("Enter Assignment Score (0-100): "))
    
    evaluation_sim.input['attendance'] = att_in
    evaluation_sim.input['assignments'] = ass_in

    evaluation_sim.compute()

    result = evaluation_sim.output['final_grade']
    print(f"--- Evaluation Result ---")
    print(f"Predicted Final Grade Score: {result:.2f}%")

    
    final_grade.view(sim=evaluation_sim)
    plt.show()

except ValueError:
    print("Invalid input. Please enter numbers between 0 and 100.")