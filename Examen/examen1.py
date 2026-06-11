import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Examen1", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Server basico",  cat='Integer')
x2 = pulp.LpVariable("Server avanzado",  cat='Integer')

# 3. Función Objetivo
model +=  30* x1 +  50* x2, "Costo_Total"

# 4. Restricciones

model +=  1* x1 +  2* x2 <= 16, "ram_cost"
model +=  3* x1 +  2* x2 <= 24, "vCpu_cost"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f" {x1.varValue} Servers basicos ")
print(f" {x2.varValue} Servers avanzados")
print(f" ${pulp.value(model.objective)}")

#source .venv/bin/activate