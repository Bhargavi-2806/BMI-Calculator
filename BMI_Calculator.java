import java.lang.*;
import java.util.*;
class BmiCalculator
  {
    public static void main(String []args)
    {
      double weight,height,h,bmi;
      Scanner bc=new Scanner(System.in);
      System.out.println("enter weight in kg:");
      weight=bc.nextInt();
      System.out.println("enter your height in cm");
      height=bc.nextInt();
      h=height*height;
      bmi=weight/h;
      System.out.println("the BMI average : "+bmi);
    }
  }
