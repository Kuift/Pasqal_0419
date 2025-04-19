import pulser

reg2 = pulser.Register.from_coordinates(
    [[0, 0], [5, 0], [0, 5], [5, 5]],  # Takes just the coordinates
    prefix="q",  # All qubit IDs will start with 'q'
    center=True,
)
print("(Centered) qubits:", reg2.qubits)
