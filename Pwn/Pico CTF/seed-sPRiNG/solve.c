#include <stdlib.h> 
#include <stdio.h> 
#include <time.h> 
#include <stdbool.h>

int main() { 

  srand(time(NULL)); 

  for(int i = 1;i <= 30; i++){
    int random_number = rand() & 0xf;
    printf("%d : %d\n", i, random_number); 
  }

  return 0; 
}
