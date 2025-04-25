# Pasqal's Pulse 414 Challenge

Please refer to the `submission.ipynb` notebook for the main summary of the work completed.

![QAOA and QAA in action on the different registers created for this project](imgs/pasqalQAOA_QAA_flower_cat_fast_no_error-ezgif.com-video-to-gif-converter.gif)

**Interesting notes:**
- A function was created to generate a QUBO matrix from atom registers.
- Some preliminary work has been done to analyze the chaotic behavior (if any) of the Pasqal system.

## Structure of this Repository

The `Archived_notebooks` folder contains various notebooks used to rapidly test different features of Pasqal's Pulser technology.

The `export` folder contains various data generated during the Pulse 414 challenge.

The `.json` files can be imported into Pulser Studio:

- `QAOA_submission1.json` contains the optimized pulse sequence for finding the ground state using QAOA in Pulser. The atoms are arranged in the shape of a Pascal triangle.

- `QAA_submission1.json` contains the pulse sequence for finding the ground state using QAA with neutral atoms arranged in a Pascal triangle configuration.

![Diagram of the Pascal triangle registers in Pulser Studio](imgs/pascal_triangle_register.JPG)

![Diagram of the Pascal triangle](imgs/pascals4.jpg)  
*Pascal triangle image from [source](https://jwilson.coe.uga.edu/EMAT6680Su12/Berryman/6690/BerrymanK-Pascals/BerrymanK-Pascals.html)*

- `Cat_QAA.json` contains the pulse sequence for finding the ground state using QAA with neutral atoms arranged in the shape of a cat.

![Diagram of the cat register in Pulser Studio](imgs/cat_register.JPG)

- `flower_QAA.json` contains the pulse sequence for finding the ground state using QAA with neutral atoms arranged in the shape of a flower.

![Diagram of the flower register in Pulser Studio](imgs/flower_register.JPG)

Some preliminary work has been done to analyze the chaotic behavior (if any) of the Pasqal system:

![Graph of clustering and radius with ratio](imgs/plotly_graph.JPG)
