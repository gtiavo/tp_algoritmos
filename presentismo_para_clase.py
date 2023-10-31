import csv
from datetime import date

class Presentismo:
    def __init__(self, fecha, alumno, estado):
        '''fecha = fecha actual,
           (apellido + nombre) del arch alumnos.cvs,
           estado = S, N'''       
        self.fecha = fecha
        self.alumno = alumno
        self.estado = estado
 
class Presentismo_dia:
    def __init__(self):
        self.pres_dia = []
        self.alumnos = []

    def agregar_presentismo(self, pres_alumno):
        self.pres_dia.append(pres_alumno)
    
    def guardar_presentismo(self, archivo):
        with open(archivo, mode='w', newline='') as arch:
            writer = csv.writer(arch,delimiter=";")
            writer.writerow(['Fecha', 'Alumno','Presentismo'])
            for pres in self.pres_dia:
                writer.writerow([pres.fecha, pres.alumno,pres.estado])

    def cargar_presentismo(self, archivo):
        try :
            with open(archivo) as arch:
                reader = csv.reader(arch,delimiter=";")
                next(reader)
                for fecha, alumno, estado in reader:
                    #nombre, apellido= row
                    self.agregar_presentismo(Presentismo(fecha, alumno, estado))
            return True
        except FileNotFoundError:
            opcion = input(f"El archivo {archivo} no existe, Desea crearlo ? Si o No :").upper()
            if opcion == 'S':
                with open(archivo, mode='w', newline='') as arch:
                    writer = csv.writer(arch, delimiter=";")
                    writer.writerow(['Fecha', 'Alumno','Presentismo'])
                return True
            else:
                return False
    
    def cargar_alumnos(self, archivo):
        try :
            with open(archivo) as arch:
                reader = csv.reader(arch,delimiter=";")
                next(reader)
                for nombre, apellido in reader:                   
                    self.alumnos.append(apellido +" "+  nombre)
            return True
        except FileNotFoundError:
            print(f"El archivo {archivo} no existe, ingrese a la opcion 1 del menú para crearlo")
            return False

# Nueva metodo devolver, devuelve en una lista con todos los registros de presentismo para luego poder manipularlo, en los listados            
    def devolver(self):
        lista= []
        for pres in self.pres_dia:
            lista.append([pres.fecha, pres.alumno,pres.estado])
        return lista 

    def eliminar_presentismo(self,archivo, alumnos):
        
        with open(archivo, mode='w', newline='') as arch:
            writer = csv.writer(arch,delimiter=";")
            writer.writerow(['Fecha', 'Alumno','Presentismo'])
            for fecha, alumno, estado in alumnos:
                writer.writerow([fecha, alumno, estado])



