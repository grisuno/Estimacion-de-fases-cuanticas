# Estimacion-de-fases-cuanticas
![Sin título](https://github.com/grisuno/Estimacion-de-fases-cuanticas/assets/1097185/fe340e09-06d7-43f3-8f36-4576fcc76ad6)

from qiskit import QuantumCircuit, transpile, assemble, Aer, execute
from qiskit.visualization import plot_histogram
import numpy as np

# Define la fase real que deseamos estimar (por ejemplo, pi/4)
target_phase = np.pi / 4

# Número de qubits para la estimación (debe ser mayor o igual a 2)
num_qubits = 3

# Crea el circuito cuántico
qc = QuantumCircuit(num_qubits, num_qubits - 1)

# Aplica compuertas Hadamard a los qubits
for qubit in range(num_qubits - 1):
    qc.h(qubit)

# Aplica una puerta controlada con la fase que queremos estimar
qc.cp(target_phase, 0, num_qubits - 1)

# Aplica compuertas de Hadamard nuevamente
for qubit in range(num_qubits - 1):
    qc.h(qubit)

# Mide todos los qubits excepto el último
for qubit in range(num_qubits - 1):
    qc.measure(qubit, qubit)

# Dibuja el circuito
qc.draw(output='mpl')
