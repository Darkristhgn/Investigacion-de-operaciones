import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Escritorio", cat='Integer')
x2 = pulp.LpVariable("Laptop",  cat='Integer')

# 3. Función Objetivo
model += 2000 * x1 + 4000 * x2, "Costo_Total"

# 4. Restricciones
model +=  x1 + x2 <= 60, "CPU_Demand"
model += 1 * x1 + 3 * x2 <= 100 , "Hour_Demand"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Hacer {x1.varValue} de escritorio")
print(f"Hacer {x2.varValue} laptops")
print(f"Ganancia maxima por 100horas: ${pulp.value(model.objective)}")

#source .venv/bin/activate