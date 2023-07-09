#include<stdlib.h>
#include<conio.h>
#include<stdio.h>

int y;

double llenarMatriz(double matriz){
	for(int i=0; i<y; i++){
		for(int j=0;j<4;j++){
			printf("\n\nIngrese el valor \n[%d][%d]: ",i,j);
			scanf("%f",&matriz[i][j]);
			switch(j):
				case 0:
					if(adfjkasdfklasdfjkasdfkasd)
		}
	}
	return matriz;
}

int main(){
	printf("\t\tCALCULADORA DE PROMEDIOS\n");
	
	//Inicio Anderson
	while(true){
		do{
			printf("digite el numero de alumnos\n");
			scanf("%d",&y);
			if(y<0 || y>=100){
				printf("Cantidad erronea. Ingresar numero de dos cifras\n");
			}
			if(y == 0){
				break;
			}
			system("pause");
			system("cls");
		}while(y<0 || y>=100);
		
		//Construccion de la matriz
		double b[y][4];
		printf("El primer numero del vector, representa el numero de estudiante, mientras que el segundo representa el dato a ingresar tal que\n\n0. codigo del estudiante\t1. genero del estudiante\t2. Nota de algebra\t3. Nota de fundamentos");
		printf("ingrese los datos\n\n");
		
		//Ciclo
		llenarMatriz(b);
		
		break;
	}
		
	//Fin Anderson
	
	//Inicio de la etiqueta
/*	start:
		printf("digite el numero de alumnos\n");
		scanf("%d",&y);
		if(y>=99){
			error:
			printf("error, solo se aceptan valores de dos cifras\n");
			system("pause");
			system("cls");
			goto start;
		}
		if(y<=0){
			goto error;
		}
		double b[y][4];
		int i,j;
			printf("El primer numero del vector, representa el numero de estudiante, mientras que el segundo representa el dato a ingresar tal que\n\n0. codigo del estudiante\t1. genero del estudiante\t2. Nota de algebra\t3. Nota de fundamentos");
		printf("ingrese los datos\n\n");
		//ciclo
		
		for(i=0; i<y; i++){
			
			for(j=0;j<4;j++){

			printf("\n\nIngrese el valor \n[%d][%d]: ",i,j);
			scanf("%f",&b[i][j]);
		}
		}*/
		
}