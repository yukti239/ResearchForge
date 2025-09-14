import java.util.Scanner;
public class Program3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int phy = sc.nextInt(), chem = sc.nextInt(), math = sc.nextInt();
        int total = phy + chem + math;
        double avg = total / 3.0;
        if (avg >= 90) System.out.println("Average: " + avg + " Grade: A Excellent");
        else if (avg >= 75) System.out.println("Average: " + avg + " Grade: B Very Good");
        else if (avg >= 50) System.out.println("Average: " + avg + " Grade: C Good");
        else System.out.println("Average: " + avg + " Grade: F Fail");
    }
}