
		ZipRecovery 1.6 
		
		This version of ZipRecovery 1.6 demonstrates the possibility
		to recover files from a particular corrupted file.
		
		During the demo recovery the original directory/file structure is restored,
		but the contents of recovered files are replaced by this text. 
		To recover the contents of files you need to purchase the commercial version of
		ZipRecovery 1.6 at:

		http://ref.officerecovery.com/zip/?5316zr/
// Area of Tringle in C
#include <stdio.h>
#include <math.h>
int main()
{
  double a, b, c, s, area;

  printf("Enter sides of a triangle\n");
  scanf("%lf%lf%lf", &a, &b, &c);

  s = (a+b+c)/2; // Semiperimeter

  area = sqrt(s*(s-a)*(s-b)*(s-c));

  printf("Area of the triangle = %.2lf\n", area);

  return 0;
}
