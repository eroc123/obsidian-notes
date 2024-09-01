**definition:** The process of converting alternating current and voltage into [[obsidian-notes/Physics/9 - Electricity/Electric Current|direct current]] and voltage
- Rectification for example is used in electronic appliances which require a direct current from the alternating current produced at power stations.
##### Rectification types:
- Half-wave rectification
- Full-wave rectification

##### Half-rectification:
- Graph of the output voltage $V_{out}$ against time is a sine curve with the positive cycles and a flat line ($V_{out} = 0$) on the negative cycle
- ![[Pasted image 20240828153934.png]]
- To half-rectify, use a single diode in a circuit and attach a a.c power source to it. Add a load resistor and take the voltage across the load resistor. The diode will only allow the current to conduct in one direction (when the voltage is positive). $V_{out}$ will fluctuate in the same way except it will output 0 during negative cycles.
- Avaliable power is reduced because voltage is 0 half the time.

##### Full-wave rectification:
- Requires **bridge rectifier circuit**
- consists of 4 diodes connected across an input alternating power supply
- output $V_{out}$ is taken across a load resistor
- ![[Pasted image 20240828160151.png]]
##### How it works:
- during positive phase of cycle, current flows through diodes 2 and 3, whilst 1 and 4 are in reverse bias and do not conduct current. (complete circuit so current can flow)
- during negative phase of cycle, current flows through diodes 4 and 1, whilst 2 and 3 are in reverse bias and do not conduct current. Either way, the current still ends up going in the same direction across the load resistor

##### Benefits of full-wave rectification
- more power avaliable as the negative phase of the cycle gets reflected and turned positive. This doubles the power output compared to half wave (where voltage is 0 during negative phase)

