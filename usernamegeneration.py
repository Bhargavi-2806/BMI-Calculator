import java.lang.*;
import java.util.*;
class Multiplication
{
    public static void main (String args[])
    {
        int i,j,mul,n;
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number to perform multiplication");
        i=sc.nextInt();
        System.out.println("enter  range for multiplication");
        n=sc.nextInt();
        for(j=1;j<=n;j++)
         { mul=i*j;
          System.out.println(i+"*"+j+"="+mul);
         }
    }
}
