# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total_sales = sum(d[product_key]for d in data)
    return total_sales


def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    total_sales = sum(d[product_key] for d in data)
    num_days = len(data)
    return total_sales / num_days if num_days > 0 else 0



def best_selling_day(data):
    """Finds the day with the highest total sales."""
    max_day = max(data,key=lambda d: d["product_a"] + d["product_b"] + d["product_c"])
    total = max_day["product_a"] + max_day["product_b"] + max_day["product_c"]
    return max_day["day"], total


def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    return sum(1 for d in data if d[product_key] > threshold)



def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    # Calculamos las ventas totales de cada producto

    total_sales_a = sum(d["product_a"] for d in data)
    total_sales_b = sum(d["product_b"] for d in data)
    total_sales_c = sum(d["product_c"] for d in data)

    # Comparamos precios de con condicionales
    if total_sales_a >= total_sales_b and total_sales_a >= total_sales_c:
        return "product_a", total_sales_a
    elif total_sales_b >= total_sales_a and total_sales_b >= total_sales_c:
        return "product_b", total_sales_b
    else:
        return "product_c", total_sales_c
    
def worst_selling_day(data):
    """Finds the day with the lowest total sales"""
    min_day = data[0]
    min_total = min_day["product_a"] + min_day["product_b"] + min_day["product_c"]

    for d in data[1:]:
        total = d["product_a"] + d["product_b"] + d["product_c"]
        if total < min_total:
            min_day = d
            min_total = total

    return min_day["day"], min_total

def top_3_selling_days(data):
    """Returns the top 3 days with the highest total sales"""
    #Agregamos total de ventas por dia
    sorted_days = sorted(data, key=lambda d: d["product_a"] + d["product_b"] + d["product_c"], reverse=True)

    #Tomamos los 3 primeros
    top_3 = sorted_days[:3]

    #Extraemos dia y total de ventas
    return [(d["day"], d["product_a"] + d["product_b"] + d["product_c"]) for d in top_3]

def sales_range(data, product_key):
    """Calculates the range (max - min) of sales for a given product."""
    sales = [d[product_key] for d in data]
    return max(sales) - min(sales)

#Ejemplos de uso
# El producto con las ventas totales mas altas es
producto, ventas_totales = top_product(sales_data)
print(f"El producto con las ventas totales más altas es {producto} con {ventas_totales} ventas.")
# Calculando las ventas totales de 'product_a'
ventas_totales_product_a = total_sales_by_product(sales_data, "product_a")
print("Ventas totales de product_a en 20 días:", ventas_totales_product_a)
#Calculamos el promedio
promedio_product_a = average_daily_sales(sales_data, "product_a")
print("Promedio diario de ventas de product_a:", promedio_product_a)
#Calculamos eldia con mas ventas totales
dia, total = best_selling_day(sales_data)
print(f"El día con más ventas totales fue el día {dia} con un total de {total} ventas.")
# Dado dichos dias que un producto supera el umbral
umbral = 200
dias_superaron_umbral_product_a = days_above_threshold(sales_data, "product_a", umbral)
print(f"Días en los que las ventas de product_a superaron {umbral}:", dias_superaron_umbral_product_a)
#Calculamos las peores ventas
dia_peor, ventas_peor = worst_selling_day(sales_data)
print(f"El dia con las peores ventas fue el dia {dia_peor} con un total de {ventas_peor} ventas")
#Ponemos por pantalla el resultado de los 3 primeros
mejores_dias = top_3_selling_days(sales_data)
print("Top 3 días con mayores ventas totales:")
for dia, total in mejores_dias:
    print(f"Día {dia} con {total} ventas.")
#Calculamos el maximo y minimo de las ventas
rango_product_a = sales_range(sales_data, "product_a")
print(f"Rango de ventan para product_a:{rango_product_a}")




# Function tests
print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))
