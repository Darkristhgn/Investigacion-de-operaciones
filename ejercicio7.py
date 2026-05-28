import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("3DModels_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Personaje",  cat='Integer')
x2 = pulp.LpVariable("Escenario",  cat='Integer')

# 3. Función Objetivo
model += 80 * x1 + 60 * x2, "Costo_Total"

# 4. Restricciones

model += 2 * x1 + 1 * x2 <= 12, "Hours_Demand"
model += 1 * x1 + 2 * x2 <= 14, "VRAM_Demand"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Hacer : {x1.varValue} Modelos de personaje")
print(f"Hacer : {x2.varValue} Modelos de escenario")
print(f"Valor Maximo de proyecto: ${pulp.value(model.objective)}")

#source .venv/bin/activate