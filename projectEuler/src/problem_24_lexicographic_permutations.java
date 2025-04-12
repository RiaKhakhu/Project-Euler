import java.util.Scanner;
/**
 * find the millionth permutation of the digits 0 -> 9.
 * I utilise a greedy algorithm to achieve this. Starting at index 0. Place the digit 0.
 * If the permutations with 0 in that index exceed 1 000 000, then proceed to select the next smallest number (1) at the following index. Else
 * skip 0 and select 1 at this index. Continue until the 1 000 000th permutation is found.
 * 
 * @author Khakhu Ria
 * @version 12/04/2025
 */

 public class problem_24_lexicographic_permutations{
    /**
     * Main method
     * @param args 
     */
    public static void main(String[] args) 
    {
        Scanner input = new Scanner(System.in);
        int totalPermutations = 0;
        try 
        {
            System.out.println("Enter the nth permutation you seek:");
            totalPermutations = input.nextInt();
        } 
        catch (Exception e) 
        {
            System.err.println(e);
            System.exit(1);
        }
        input.close();

        if (totalPermutations > factorial(10))
        {
            System.err.println("The nth permutation you entered exceeds the total number of possible permutations.");
            System.exit(1);
        }

        int permutationCount = 0, currentPermutations;
        int[] digits = new int[10]; // digits[i] = 0 if unpicked, 1 otherwise.
        int[] permutation = new int[10];
        
        for (int i = 0; i < 10; i++)
        {
            currentPermutations = factorial(10-i-1);
            for (int j = 0; j < 10; j++)
            {
                if (digits[j] == 0)
                {
                    permutation[i] =  j;
                    digits[j] = 1;
                }
                else continue; // digit already picked

                if (permutationCount + currentPermutations < totalPermutations)
                {
                    permutationCount += currentPermutations;
                    digits[j] = 0; // unpick this j
                }
                else break;
            }
        }
        System.out.println(totalPermutations);
        // show the permutation on the terminal
        for (int digit : permutation) { System.out.print(digit);}
    }


    /**
     * Find n!
     * @param n the factorial to compute
     * @return n!
     */
    private static int factorial(int n)
    {
        if (n < 0)
        {
            System.err.println("Enter a non-negative integer");
            System.exit(1);
        }
        if ( n == 0 ) return 1;
        else return n * factorial(n-1);
    }
 }