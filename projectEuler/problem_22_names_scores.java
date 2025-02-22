import java.io.FileReader;
import java.io.IOException;
import java.util.Scanner;


// author: Khakhu Ria
// version: 12/02/2025

// problem statement: Given a list of names, calculate the total score of the names in the list, where a name's score is its alphabetical value * position in sorted list
// eg. the list {"acc"} has a total value of 7, and the list {"aaa","bbb"} has a total of 9

public class problem_22_names_scores {
    
    /**
     * Given a list of strings ,sort in alphabetical order and calculate the total score of the list
     * @param names The array in focus
     * @return The total score of the list
     */
    private static int getScore(String[] names)
    {
        int score = 0;
        names = mergeSort(names);

        for (int i = 0; i < names.length; i++)
        {
            score += (i+1)*getAlphabeticalValue(names[i]);
        }
        return score;
    }
    /**
     * Given a string, calculate its alphabetical value by adding the alphabetical position of each character
     * @param str The string in focus
     * @return The alphabetical value of str
     */
    private static int getAlphabeticalValue(String str)
    {
        int value = 0 ;
        str = str.toUpperCase();
        
        for (int i = 0; i < str.length(); i++)
        {
            value += (int) str.charAt(i) - 64;
        }
        return value;
    }
    /**
     * Use merge sort to sort a list of strings
     * @param arr Array to be sorted
     * @return The sorted array
     */
    private static String[] mergeSort(String[] arr)
    {
        if (arr.length==0 || arr.length==1) { return arr;}

        String[] sortedArr = new String[arr.length];
        String[] leftHalf = new String[(int)arr.length/2];
        String[] rightHalf = new String[arr.length-leftHalf.length];
        

        for (int i = 0; i< arr.length; i ++)
        {
            if ( i < leftHalf.length) { leftHalf[i] = arr[i];}
            else { rightHalf[i-leftHalf.length] = arr[i];}
        }
        
        sortedArr = merge(mergeSort(leftHalf),mergeSort(rightHalf));

        return sortedArr;
    }
    // helper function for merge-sort
    private static String[] merge(String[] arr1, String[] arr2)
    {
        String[] mergedArr = new String[arr1.length+arr2.length];
        int k = 0; // next index of mergedArr to be occupied
        int i = 0; // index of arr1 to be compared with index j of arr2
        int j = 0; 
        while (true)
        {
            if (i==arr1.length && j == arr2.length) { break;} // elements from both arrays merged
            if (i==arr1.length) // elements from arr1 all merged 
            {
                mergedArr[k] = arr2[j];
                j++;
                k++;
            }
            else if (j==arr2.length) // elements from arr2 all merged
            {
                mergedArr[k] = arr1[i];
                i++;
                k++;
            }
            else if (arr1[i].compareTo(arr2[j])<0) // arr1[i] comes before arr2[j] alphabetically
            {
                mergedArr[k] = arr1[i];
                i++;
                k++;
            }
            else  // arr1[i] comes after arr2[j] alphabetically, or they're the same word
            {
                mergedArr[k] = arr2[j];
                j++;
                k++;
            }   
        }
        return mergedArr;

    }

    public static void main (String args[])
    {
        Scanner file = null;
        
        try
        {
            String[] names = new String[5163]; // there are 5163 names in the problem file 
            int i = 0; // keep track of how many names have been added to names array;
           
            file = new Scanner( new FileReader("projectEuler\\problem_22_names.txt"));
            file.useDelimiter(",");
            
            while (file.hasNext())
            {    
                names[i] = file.next();
                i++;
            }

            System.out.println(getScore(names)); // get the total score   
        }
        catch (IOException e)
        {
            System.err.println(e);
        }
        finally
        {
            if (file != null){ file.close();}
        }
    
    }
}
