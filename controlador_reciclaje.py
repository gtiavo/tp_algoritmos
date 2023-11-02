import csv
from datetime import date

class Control_actividad:

    def eliminar_papelera_presentismo(self,archivo, alumnos):
        try:
            with open(archivo, mode='r+', newline='') as arch:
                reader = csv.reader(arch,delimiter=";")
                next(reader)
                writer = csv.writer(arch,delimiter=";")
                for fecha, alumno, estado in alumnos:
                    writer.writerow([fecha, alumno, estado])
        except:
            with open(archivo, mode='w', newline='') as arch:
                writer = csv.writer(arch,delimiter=";")
                writer.writerow(['Eliminados:'])
                for fecha, alumno, estado in alumnos:
                    writer.writerow([fecha, alumno, estado])

    def eliminar_papelera_alumno(self,archivo, alumno):
        self.control_carga_escritura_simple(archivo, ['Eliminados:'], [alumno.nombre, alumno.apellido])

    def logger(self, archivo, accion, alumno):
        self.control_carga_escritura_simple(archivo, ['Fecha', 'Accion','Alumno'], [date.today(), accion, alumno])

    def control_carga_escritura_simple(self, archivo, columna_nombre, filas):
        try:
            with open(archivo, mode='r+', newline='') as arch:
                reader = csv.reader(arch,delimiter=";")
                next(reader)
                writer = csv.writer(arch,delimiter=";")
                writer.writerow(filas)
        except:
            with open(archivo, mode='w', newline='') as arch:
                writer = csv.writer(arch,delimiter=";")
                writer.writerow(columna_nombre)
                writer.writerow(filas)
        

            

            
