import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMaximize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Estandar", cat='Integer')
x2 = pulp.LpVariable("Pro",lowBound=2 , cat='Integer')

# 3. Función Objetivo
model += 10000 * x1 + 25000 * x2, "Capacidad de procesamiento"

# 4. Restricciones
model += 1500 * x1 + 4000 * x2 <= 30000 , "Capital_Demand"
model += 1 * x1 + 3 * x2  <=24 , "Rack_Demand"
model +=  2 * x1 + 5 * x2 <= 45, "Watage_Demand"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Usar  {x1.varValue} Estandar")
print(f"Usar {x2.varValue} Pro")
print(f"Capacidad de procesamiento maxima: {pulp.value(model.objective)}")

#source .venv/bin/activate