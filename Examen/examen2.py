import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Examen1", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Ilustraciones", lowBound=2, cat='Integer')
x2 = pulp.LpVariable("Iconos", upBound=8, cat='Integer')

# 3. Función Objetivo
model +=  40* x1 +  20* x2, "Costo_Total"

# 4. Restricciones

model +=  2* x1 +  1* x2 <= 12, "Work_cost"
model +=  1* x1 +  1* x2 <= 9, "Render_cost"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f" {x1.varValue} Ilustraciones ")
print(f" {x2.varValue} Iconos")
print(f" ${pulp.value(model.objective)}")

#source .venv/bin/activate