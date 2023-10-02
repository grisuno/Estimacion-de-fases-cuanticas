# Simulador Aer para ejecutar el circuito
simulator = Aer.get_backend('main')

# Ejecuta el circuito 1024 veces para obtener estadísticas
shots = 1024
compiled_circuit = transpile(qc, simulator)
job = execute(compiled_circuit, simulator, shots=shots)
result = job.result()

# Obtiene el histograma de resultados
counts = result.get_counts(qc)

# Dibuja el histograma
plot_histogram(counts)
