/**
 * Problem statement: find the sum of all amicable numbers < 10,000
 * 
 * @author : Khakhu Ria
 * @version: 10/02/2025
 */


public class Problem_21_amicable_numbers {
    
    /**
     * Given a positive integer n, compute the sum of its proper divisors
     * 
     * @param n The number to compute its divisors
     * @return The sum of its divisors
     */
    public static int sumOfDivisors(int n)
    {
        int sum = 0;
        for ( int i = 1; i <= (int)Math.sqrt(n); i++)
        { 
            if (n%i ==0) 
            {
                sum += i;
                if (i != (int)Math.sqrt(n) && i != 1) {sum += (int)n/i;}        
            }
        }
        return sum;
    }

    /**
     * Prints amicable numbers until terminated (work in progress)
     */
    public static void printAmicableNumbers()
    {
        int a = 2;
        int d_a = sumOfDivisors(a);
        int b = sumOfDivisors(d_a);
        while (true)
        {
            if (a == b && a!=d_a)
            {
                System.out.println(String.format("(%d,%d)",a,d_a));
            }
            a++;
            d_a = sumOfDivisors(a);
            b = sumOfDivisors(d_a);
        }
    }

    public static void main(String args[])
    {
        printAmicableNumbers(); // every pair is printed twice
    }
}
