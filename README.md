# Mini-Electronic-Drumset---DE-Final
The goal was to create a drumset that would be less expensive, easy to move around, and have a place to connect headphones to, in order to not disturb other people.
<img width="1816" height="1358" alt="Screenshot 2026-01-11 185201" src="https://github.com/user-attachments/assets/43be39ec-66f4-4b97-8c63-8b58a1b856f9" />
# Sensors
I chose to use a piezo sensor to act as the drum since the voltage it generates is proportional to the force it is hit with, so the drumset can make sounds according to the voltage level
<img width="520" height="461" alt="piezo" src="https://github.com/user-attachments/assets/9059543c-80d0-4dd2-814f-882f8d02d4cb" />
I also used an analog to digital converter since the Raspberry Pi 4 that I used doesn't have analog pins, so I selected the ADS1015 12-bit ADC because of its faster sampling rates
<img width="1362" height="1060" alt="ADC" src="https://github.com/user-attachments/assets/1de1086a-d877-433c-b4a3-9f3687f1685d" />
# CAD
I started in Onshape and first made a model of one of the drums to put the piezo in, which was a disk with walls around the perimeter and a tiny slit in the walls for the wires to go through
<img width="1106" height="769" alt="drum" src="https://github.com/user-attachments/assets/64e1e3ce-0357-42e1-85b4-7a0571182b66" />
<img width="462" height="300" alt="real piezo drum" src="https://github.com/user-attachments/assets/2d5e31e8-61f8-4732-81ba-5a54235ab498" />
After that, I created the frame of the drumset based off of the size of a single drum, and added the other drums and cymbals to the frame to create the first version of the drumset
<img width="1816" height="1358" alt="drumset" src="https://github.com/user-attachments/assets/4d0d45c0-7862-437f-ba1b-178b402618c4" />
I'm also still working on adding a table clamp to the design so it doesn't slide around when being hit
# Challenges
One issue that took a really long time to resolve was getting the ADC to read the piezo values, since when I initially connected them, the ADC would only read zeroes and small negative voltages. I eventually decided to rebuild the circuit and slowly add parts back, which got the ADC to read values that made more sense. Another issue that I'm still working on is how to sense the start and end of a voltage spike, since the ADC reads multiple spikes in each hit.
