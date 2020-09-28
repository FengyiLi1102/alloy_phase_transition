# Simulation 2D binary substitutional alloy phase transition with Monte Carlo method
The full instruction of the simulation can be found in the [project-v1](https://github.com/FengyiLi1102/alloy_phase_transition/blob/master/project-v1.pdf) from page 3.

Two types of atoms A and B are randomly distributed in a square metric with periodic boundary condition. The size of atom A and B is not considered, and the vacancies and dislocations are not included in the simulation as well. The bond energy between same type atom is zero while equaling to non-zero values between different type atoms. According to the Metropolis algorithm, the switch of atoms are achieved, and this contributes the entropy change of the system. As the energy osillates with a small enough value, the simulation can be stopped for collecting and processing the data. Bond energy, composition, and system size are changed in order to find the effect of these variables on the system. The transition temperature is also found by observing a sharp change of the heat capacity.

The [report]() will provide information of the experiment, codes of the simulation, and results under different system states. 
