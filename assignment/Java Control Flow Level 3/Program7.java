import java.util.Scanner;
public class Program7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double weight = sc.nextDouble();
        double heightCm = sc.nextDouble();
        double heightM = heightCm / 100.0;
        double bmi = weight / (heightM * heightM);
        if (bmi < 18.5) System.out.println("BMI: " + bmi + " Underweight");
        else if (bmi < 24.9) System.out.println("BMI: " + bmi + " Normal");
        else if (bmi < 29.9) System.out.println("BMI: " + bmi + " Overweight");
        else System.out.println("BMI: " + bmi + " Obese");
    }
}