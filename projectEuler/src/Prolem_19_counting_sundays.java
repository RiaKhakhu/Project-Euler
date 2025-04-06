/**
 * Problem statement: count the number of Sundays that fell on the 1st of any month in the 20th century
 * 
 * @author : Khakhu Ria
 * @version: 07/02/2025
 */

public class Prolem_19_counting_sundays {
    /**
     * Given a starting and ending year, returns an array of the dates of all 1st of each month between the given years
     * @param start The starting year
     * @param end The ending year
     * @return All the dates of the 1st of each month in the form [day, month, year]
     */
    public static int[][] firstOfEachMonth(int start,int end)
    {
        int[][] dates = new int[(end-start+1)*12][];
        int i =0; // keep track of where to place the next date
        
        for (int year = start; year <= end; year++) 
        {
            for (int month = 3; month <= 14; month++)  // Jan and Feb are month 13 and 14 respectively
            {
                dates[i] = (new int[]{1, month, year});
                i++;
            }
        }
        return dates;
    }

    /**
     * Given an array of dates, determines how many sundays there are using Zeller's congruence
     * @param dates The dates to be considered, are of the form [day, month, year]; where jan and feb are month 13 and 14 respectively
     * @return The number of sundays
     */
    public static int countSundays(int[][] dates)
    {
        int count = 0;
        int dayOfWeek; //  (0=saturday,1=sunday,...,6=friday)
        int day,month,year;

        for (int[] date : dates)
        {
            day = date[0];
            month = date[1];
            year = date[2];
            
            dayOfWeek = (int)(day + Math.floor(13*(month+1)/5) + year + Math.floor(year/4) - Math.floor(year/100) + Math.floor(year/400)) % 7;

            if (dayOfWeek==1) { count++;}
        }
        return count;
    }

    public static void main(String args[])
    {
        int[][] dates = firstOfEachMonth(1901,2000);
        System.out.println(countSundays(dates));
    }
}
