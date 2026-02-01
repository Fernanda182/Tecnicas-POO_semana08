# === SISTEMA DE GESTIÓN ACADÉMICA ===
# Incluye: tareas, notas y horarios
# Autor: Fernanda Vaca
# Fecha: 2026
# Este archivo es para organizar tareas, registrar notas y visualizar horarios académicos


# ---------------------------
# Sección 1: GESTIÓN DE TAREAS
# ---------------------------


tareas = []


def agregar_tarea():
    nombre = input("Nombre de la tarea: ")
    materia: str = input("Materia: ")
    fecha = input("Fecha de entrega (dd/mm/aaaa): ")
    tareas.append({"nombre": nombre, "materia": materia, "fecha": fecha})
    print("✅ Tarea añadida.\n")


def mostrar_tareas():
  
    if not tareas:
        print("📋 No hay tareas registradas.\n")
        return
    print("📋 Lista de tareas:")
    for i, t in enumerate(tareas, 1):
        estado = "✅" if t.get("completada", False) else "❌"
        
        print(f"{i}. {t['nombre']} - {t['materia']} - Entrega: {t['fecha']} - Estado: {estado}")
    print()


def completar_tarea():
    mostrar_tareas()
i = int(input("Número de la tarea completada: ")) - 1
def completar_tarea():
    mostrar_tareas()
    i = int(input("Número de la tarea completada: ")) - 1
    if 0 <= i < len(tareas):
        tareas[i]["completada"] = True
        print("✅ Tarea marcada como completada.\n")


# ---------------------------
# Sección 2: REGISTRO DE NOTAS
# ---------------------------


notas = {}


def agregar_nota():
    materia = input("Nombre de la materia: ")
    nota = float(input("Nota obtenida (0-10): "))
    notas[materia] = nota
    print("✅ Nota registrada.\n")


def mostrar_notas():
    if not notas:
        print("📘 No hay notas registradas.\n")
        return
    total = 0
    print("📈 Notas por materia:")
    for materia, nota in notas.items():
        estado = "APROBADA" if nota >= 7 else "REPROBADA"
        print(f"{materia}: {nota} ({estado})")
        total += nota
    promedio = total / len(notas)
    print(f"\n📊 Promedio general: {promedio:.2f}\n")


# ---------------------------
# Sección 3: HORARIO ACADÉMICO
# ---------------------------


horario = []


def agregar_horario():
    materia = input("Nombre de la asignatura: ")
    dia = input("Día de la semana: ")
    hora = input("Hora (HH:MM): ")
    horario.append({"materia": materia, "dia": dia, "hora": hora})
    print("✅ Asignatura añadida al horario.\n")


def mostrar_horario():
    if not horario:
        print("📅 No hay asignaturas en el horario.\n")
        return
    print("📚 Horario Académico:")
    for clase in horario:
        print(f"{clase['dia']} - {clase['hora']} - {clase['materia']}")
    print()


# ---------------------------
# Menú Principal
# ---------------------------
def menu():
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Añadir tarea")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Añadir nota")
        print("5. Ver notas")
        print("6. Añadir clase al horario")
        print("7. Ver horario")
        print("0. Salir")
        opcion = input("Elige una opción: ")
        print()
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            completar_tarea()
        elif opcion == "4":
            agregar_nota()
        elif opcion == "5":
            mostrar_notas()
        elif opcion == "6":
            agregar_horario()
        elif opcion == "7":
            mostrar_horario()
        elif opcion == "0":
            print("👋 Hasta luego.")
            break
        else:
            print("⚠️ Opción no válida.\n")
# Ejecutar el menú
menu()
