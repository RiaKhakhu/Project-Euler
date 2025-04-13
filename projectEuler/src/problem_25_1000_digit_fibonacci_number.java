import java.util.Scanner;

/**
 * Find the 1st fibonacci number with 1000 digits
 * 
 * @author Khakhu Ria (KHKRIA001)
 * @version 13/04/2025
 */

 public class problem_25_1000_digit_fibonacci_number
 {
    /**
     * Given an integer, determine the number of digits it has
    * @param n the integer to compute number of digits
    * @return the number of digits
    */
    public static int numDigits(int n)
    {
        int count = 0;
        n = n < 0 ? -n : n;
        if (n == 0) return 1;
        while ( n > 0)
        {
            count++;
            n = n/10;
        }
        return count;
    }

    /**
     * Determine the 1st fibonacci number with n digits
     * @param n the number of digits
     * @return the fibonacci number
     */
    public static int firstFibonacci(int n)
    {
        int f1 = 1, f2 = 1, f;

        if (n <= 0)
        {
            System.err.println("Enter a positive integer");
            System.exit(1);
        }
        else if ( n == 1) return 1;
    
        while (true)
        {
            f = f1 + f2;
            if (numDigits(f) == n) return f;
            f1 = f2; f2 = f;
        }
    }

    /**
     * Main method
     * @param args
     */
    public static void main(String[] args) 
    {
        Scanner input  = new Scanner(System.in);
        int n; String str;
        while (true) 
        { 
            System.out.print("Enter the number of digits (x to exit): ");
            str = input.nextLine().toLowerCase();
            if (str.equals("x")) { break;}
            else { n = Integer.parseInt(str);}
            System.out.printf("The 1st fibonacci number with %d digits is : %d\n", n, firstFibonacci(n));
        }
        input.close();  
    }
}