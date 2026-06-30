import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Backend", upBound=6,cat='Integer')
x2 = pulp.LpVariable("DataWorker",upBound=7, cat='Integer')

# 3. Función Objetivo
model += 300 * x1 + 250 * x2, "Costo de cluster por hora"

# 4. Restricciones
model += 2 * x1 + 1 * x2 <= 16 , "Ram_Demand"
model += 1 * x1 + 2 * x2  <=17 , "Storage_Denand"


# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Usar  {x1.varValue} Backend")
print(f"Usar {x2.varValue} DataWorkers")
print(f"Costo de cluster por hora: {pulp.value(model.objective)}")

#source .venv/bin/activate