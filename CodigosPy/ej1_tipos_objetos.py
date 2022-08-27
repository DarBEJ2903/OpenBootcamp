Persona = {'Nombre':'Daniel',
            'Apellidos':'Ramirez Bejarano',
            'Edad': 24,
            'Email': 'daniel0327@outlook.es',
            'Telefono': 3214276138,
            'Casado': True,
            'Hijos': True,
            'Amigos': ['Julian','Juan Manuel','Felipe','Cristian'],
            'Peliculas': {1:'The Hobbit',2:'Harry Potter',3:'A Beautifull Mind'                             }    
            }
print("Nombre: "+ Persona['Nombre'])
print("Apellidos: " + Persona['Apellidos'])
print("Edad: " + str(Persona['Edad']))
print("Email: " + Persona['Email'])
print("Telefono: " + str(Persona['Telefono']))
print("Casado: " + str(Persona['Casado']))
peliculas = Persona['Peliculas'].values()
peliculas = ",".join(peliculas)
print("Lista De Peliculas: " + peliculas)
