main(){

int plh; 
int X;
inisialisasi();

printf("PROGRAM LINKED LIST\n"); 
printf("1. MEMASUKKAN SIMPUL AWAL\n");
printf("2. INSERT DEPAN\n"); 
printf("3. INSERT SETELAH X\n"); 
printf("4. INSERT SEBELUM X\n"); 
printf("5. INSERT BELAKANG\n");
printf("6. DELETE DEPAN\n"); 
printf("7. DELETE SIMPUL X\n"); 
printf("8. DELETE BELAKANG\n");
printf("9. TAMPIL DATA\n");

do{
printf("MASUKKAN PILIHAN: ");
scanf("%i", &plh);

switch(plh){


case 1:
 

printf("\n");
printf("MASUKKAN ANGKA: ");
scanf("%i",&X);
printf("\n");
 

buatSimpul(X); awal(); break;

case 2:
printf("\n");
printf("MASUKKAN ANGKA: ");
scanf("%i",&X);
printf("\n");

buatSimpul(X); InsertBelakang(); break;

case 3:
printf("\n");
printf("MASUKKAN ANGKA: ");
scanf("%i",&X);
printf("\n");

buatSimpul(X); InsertDepan(); break;


 
case 4:
 

printf("\n"); printf("MASUKKAN ANGKA:");
scanf("%i",&X);
printf("\n");
buatSimpul(X); printf("\n");
printf("MASUKKAN ANGKA SETELAH:");
scanf("%i",&X);
printf("\n"); InsertSetelah(X); break;
 
case 5:
 

printf("\n");
printf("MASUKKAN ANGKA:");
scanf("%i",&X);
printf("\n");

buatSimpul(X);


printf("\n");
printf("MASUKKAN ANGKA SEBELUM:");
scanf("%i",&X);
printf("\n"); InsertSebelum(X); break;
case 6:
deleteDepan(); break;

case 7:
deleteBelakang(); break;

case 8:
printf("\n");
printf("\nSIMPUL YANG AKAN DIHAPUS: "); 
printf("\nMASUKKAN ANGKA: ");
scanf("%i",&X);
printf("\n");

deleteSimpul(X);
break;

case 9:
tampil(); break;

case 10:
printf("\n");
printf("\n"); break;

default :
printf("\n");
printf("MASUKKAN ANDA SALAH, SILAHKAN ULANGI LAGI"); break;
}
getch(); } while(plh!=10); return 0;
}
