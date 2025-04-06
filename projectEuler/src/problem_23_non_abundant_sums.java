/**
 * Find all positive integers that cannot be expressed as a sum of 2 abundant numbers ( sum of proper divisors > number)
 * It can be shown that all integers > 28123 can be written as the sum of 2 abundant numbers.
 * @author Khakhu Ria
 * @version 06/04/2025
 */

 public class problem_23_non_abundant_sums
 {
    public static void main(String[] args)
    {
        // find all abundant numbers <= 28123
        String abundant_nums_str = "";
        for (int i = 1; i <= 28123; i++)
        {
            if (Problem_21_amicable_numbers.sumOfProperDivisors(i) > i) { abundant_nums_str += i+" ";}
        }
        //  store abundant numbers in an array
        String[] abundant_nums = abundant_nums_str.split(" ");
        
        int[] arr = new int[28124]; // arr[i] = 0 if i cannot be expressed as a sum of 2 amicable numbers. i = 0 is ignored
        
        // search for numbers which can be expressed as a sum of 2 amicable numbers
        for (int j = 0; j<abundant_nums.length; j++)
        {
            int a = Integer.parseInt(abundant_nums[j]);

            for (int k = j; k<abundant_nums.length; k++)
            {
                int b = Integer.parseInt(abundant_nums[k]);
                 if (a+b < arr.length) arr[a+b] = 1;
            }
        }
        // sum all i where arr[i]=0
        int sum = 0;
        for (int i = 1; i < 28124; i++) { sum = (arr[i] == 0) ? sum+i : sum;}

        System.out.println(sum);
    }
 }
