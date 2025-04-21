from pulser import Register, Sequence, Pulse
from pulser.devices import MockDevice, AnalogDevice
from pulser.waveforms import RampWaveform
import pulser
import matplotlib.pyplot as plt

def get_registers(initial_d):
    return Register({
    "q0": (0, 0),
    "q1": (0, 0),
    "q2": (R_ij, 0),
    })

def set_pulse_sequence(R_ij, delta_const):
    reg = get_registers(R_ij)

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
    print("supge")
    result = backend.run()
    print("dopge")
    counts = result.sample_final_state(1000)
    return counts
device = AnalogDevice
print(device.specs)
for i in list(range(1,15)):
    device = AnalogDevice
    C_6 = device.interaction_coeff
    R_ij = i
    delta_const = C_6 / (R_ij ** 6)
    print(f"deltaconst : {delta_const}, R_ij : {R_ij}")
    seq = set_pulse_sequence(R_ij,delta_const)
    counts = run_experiment(pulser.backends.QutipBackend(seq))

    # Let's plot the histogram associated to the measurements
    # Let's select only the states that are measured more than 10 times
    print(counts)
    most_freq = {k: v for k, v in counts.items() if v > 10}
    plt.bar(list(most_freq.keys()), list(most_freq.values()))
    plt.xticks(rotation="vertical")
    plt.show()

