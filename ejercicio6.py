import pulp

# 1. Definir el problema (Minimización)
model = pulp.LpProblem("Cloud_Optimization", pulp.LpMinimize)

# 2. Definir Variables (Enteras, ya que no puedes rentar media instancia)
x1 = pulp.LpVariable("Almacenamineto_Estandar",  cat='Integer')
x2 = pulp.LpVariable("Alamacenamiento_Pro",  cat='Integer')

# 3. Función Objetivo
model += 20 * x1 + 60 * x2, "Costo_Total"

# 4. Restricciones

model += 1 * x1 + 3 * x2 >= 15, "VEL_Units"
model += 2 * x1 + 2 * x2 >=14, "RET_Days"

# 5. Resolver y mostrar
model.solve()

print(f"Estado: {pulp.LpStatus[model.status]}")
print(f"Contratar : {x1.varValue} Terabytes Estandar")
print(f"Contratar : {x2.varValue} Terabytes Pro")
print(f"Costo Mínimo Mensual: ${pulp.value(model.objective)}")

#source .venv/bin/activate