from bd import *

class Musico():
    def __init__(self,id_musico,nombre_musico,instrumento,banda=None):
        self.id_musico = id_musico
        self.nombre_musico = nombre_musico
        self.instrumento = instrumento
        self.banda = banda
    def __repr__(self):
        return(f"""
#################################
ID: {self.id_musico}
Nombre Banda: {self.nombre_musico}
Instrumento: {self.instrumento}
Banda: {self.banda}
#################################
""")
    
    def add_banda(self,banda):
        self.banda = banda
        query = "UPDATE MUSICO SET id_banda = :id_banda WHERE id_musico = :id_musico"
        variables = [self.banda.id_banda , self.id_musico]
        hacer_consulta(query,'update',variables)
        

    def guardar_musico(self):
        query = "INSERT INTO MUSICO VALUES(:id_musico, :nombre_musico, :instrumento, :banda)"
        variables = [self.id_musico, self.nombre_musico, self.instrumento, self.banda if self.banda != None else "NULL"]
        hacer_consulta(query,'insert',variables)

    def eliminar_musico(self):
        query = "DELETE FROM MUSICO WHERE id_musico = :id_musico "
        variables = [self.id_musico]
        hacer_consulta(query,'delete',variables)



class Banda():
    def __init__(self,id_banda,nombre_banda):
        self.id_banda = id_banda
        self.nombre_banda = nombre_banda

    def __repr__(self):
        return(f"""
#################################
ID: {self.id_banda}
Nombre Banda: {self.nombre_banda}
#################################
""")
    
    def __str__(self):
        return self.nombre_banda
    
    def guardar_banda(self):
        query = "INSERT INTO BANDA VALUES(:id_banda,:nombre_banda)"
        variables = [self.id_banda,self.nombre_banda]
        hacer_consulta(query,'insert',variables)


