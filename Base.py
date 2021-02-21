import psycopg2 

class consulta:
    def __init__(self):
        self.conexion1 = psycopg2.connect(database="Cursos_vacacionales", user="postgres", password="20181020072")
        
    def Agregar(self):
        pass

    def Borrar(self):         
        pass

    def Consultar(self,username=None,password=None):
        try:
            print("esta entrad")
            cursor=self.conexion1.cursor()
            cursor.execute("select * from usuario where k_nombreu =%s and k_contraseÑa=%s",(username,password))
            lista=cursor.fetchall()
            self.conexion1.commit()  
            self.conexion1.close() 
            if len(lista)!=0:
                return True 
            else:
                return False
        except :
            print("ta mal")
               


if __name__ == "__main__":
    consulta().Consultar(username='Johan Aguirre',password='12345')
        
