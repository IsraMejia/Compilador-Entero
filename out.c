#include <stdio.h>
int main(void){
float s;
float a;
printf("Compilador pro\n");
printf("cuantas veces quiere ser saludado?\n");
if(0 == scanf("%f", &s)) {
s = 0;
scanf("%*s");
}
a = 0;
while(a<s){
printf("Hola\n");
a = a+1;
}
printf("Fin del programa\n");
return 0;
}
