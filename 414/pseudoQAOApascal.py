from pulser import Register, Sequence, Pulse
from pulser.devices import MockDevice, AnalogDevice
from pulser.waveforms import RampWaveform
import pulser
import matplotlib.pyplot as plt
import math

def get_registers(initial_d,distance2): 
    print(math.sqrt((initial_d/2)**6 - distance2**2))
    return Register({
    "q0": (-initial_d/2, 0),
    "q1": (initial_d/2, 0),
    "q2": (0, math.sqrt((initial_d/2)**6 - distance2**2)),
    })

def set_pulse_sequence(R_ij, C_6, device):
    delta_const = C_6 / (R_ij ** 6)
    #C_6 / (distance1 ** 6) = 0.5 * (C_6/ (distance2 ** 6))
    dist_2 = 0.89089871814*R_ij
    #dist_2 = 1.12246204830*R_ij

    reg = get_registers(R_ij,dist_2)
    reg.draw()
    seq = Sequence(reg, MockDevice)
    seq.declare_channel("ch3", "rydberg_global")

    amp1 = RampWaveform(252, 0, 12.566370614359172)
    pulse1 = Pulse.ConstantDetuning(amp1, -delta_const, 0)

    det2 = RampWaveform(800, -delta_const, -delta_const)
    pulse2 = Pulse.ConstantAmplitude(12.566370614359172, det2, 0)

    amp3 = RampWaveform(500, 12.566370614359172, 0)
    pulse3 = Pulse.ConstantDetuning(amp3, -delta_const, 0)

    seq.add(pulse1, "ch3")
    seq.add(pulse2, "ch3")
    seq.add(pulse3, "ch3")
    seq.measure("ground-rydberg")

    return seq

def run_experiment(backend):
    result = backend.run()
    counts = result.sample_final_state(1000)
    return counts


device = MockDevice
C_6 = device.interaction_coeff
R_ij = 6 # distance in micrometers

print(f"R_ij : {R_ij}")

seq = set_pulse_sequence(R_ij,C_6,device)
counts = run_experiment(pulser.backends.QutipBackend(seq))

# Let's plot the histogram associated to the measurements
# Let's select only the states that are measured more than 10 times
print(counts)
most_freq = {k: v for k, v in counts.items() if v > 10}
plt.bar(list(most_freq.keys()), list(most_freq.values()))
plt.xticks(rotation="vertical")
plt.show()

