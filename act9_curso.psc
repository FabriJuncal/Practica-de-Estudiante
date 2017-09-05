
funcion ingresar_alumnos()
	
	Definir alumnos Como Entero;

	Escribir " ";
	escribir "Ingrese la cantidad de alumnos: ";
	leer alumnos;
	
	si alumnos <= 0 entonces
		
		Escribir "** Ingrese un valor mayor a cero para la cantidad de alumnos. **";
		ingresar_alumnos();
		
	sino
		ingresar_cantIntegrantes(alumnos);
	finsi	
finfuncion	


Funcion  ingresar_cantIntegrantes(alumnos)
	Definir Nintegrantes,alumnoss, sobran Como Entero;
	Definir grupos como real;
	
	alumnoss = alumnos;
	Escribir  "Ingrese el numero de intengrantes que tendra cada grupo: ";
	leer Nintegrantes;
	
	si Nintegrantes >= 0 entonces
		si Nintegrantes > alumnoss entonces
			Escribir "** Ingrese un valor mayor o igual al numero de alumnos. **";
			ingresar_cantIntegrantes(alumnoss);
		sino
			
			grupos = trunc(alumnoss/Nintegrantes);
			sobran = alumnos - (grupos * Nintegrantes);
			
			si sobran <>0 Entonces
				si grupos = 1 entonces
					Escribir "Se formo un grupo de ", Nintegrantes, " y un grupo de ", (alumnoss - Nintegrantes) ".";
				
				sino
					Escribir "Se formaron ", grupos, " grupos de ", Nintegrantes, " y un grupo de ", sobran ".";
				
			
				FinSi
				
			SiNo
				si grupos = 1 entonces
					Escribir "Se formo un grupos de ", Nintegrantes, ".";
					
				sino
					
					
					Escribir "Se formaron ", grupos, " grupos de ", Nintegrantes, ".";
					
				FinSi
				
				
			finsi
		finsi
		
	sino
		
		Escribir  "** Ingrese valor mayor a cero. **";
		ingresar_cantIntegrantes(alumnoss);
		
	
	FinSi
	

	
FinFuncion



Proceso tarea
	
	ingresar_alumnos();
		
FinProceso


