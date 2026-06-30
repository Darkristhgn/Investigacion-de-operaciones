import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Inspeccion Basica", cat='Integer')
x2 = pulp.LpVariable("Inspeccion Profunda",  cat='Integer')

# 3. Función Objetivo
model += 2 * x1 + 5 * x2, "Puntos de mitigacion"

# 4. Restricciones
model +=  1 * x1 + 3 * x2 <= 18, "CPU_Demand"
model += 1 * x1 + 1 * x2 <= 8 , "RAM_Demand"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Usar  {x1.varValue} Gb de inspeccion basica")
print(f"Usar {x2.varValue} Gb de inspeccion profunda")
print(f"Puntos de mitgacion de riesgo totales: {pulp.value(model.objective)}")

#source .venv/bin/activate