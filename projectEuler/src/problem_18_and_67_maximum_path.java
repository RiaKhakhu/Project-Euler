import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.Scanner;

/**
 * Generalized solution for problems 18 and 67.
 * For the solution, the triangle is treated as a di-graph with a height of r-1,where r is the number of rows of the triangle,
 * with the top row as the root node.
 * Notice that for each node in the jth index of the ith row, the left and right child of this node are in the (i+1)th row, in the 
 * jth and (j+1)th index respectively.
 * It is sufficient to use an array to store this graph, as the computations are relatively easy. Each node is stored as an 
 * array of the form [node_value, cost_to_node]. Initially all nodes have a cost of 0, and a value as specified in the triangle description.
 * The task now is to find the highest cost to get to any node, where cost_to_node = cost_to_parent + node_value. This graph has no
 * cycles so it is a DAG, it is now trivial to find the highest cost to any node starting from the root node by traversing the graph in
 * Topological order. The nodes in each level are independent of each other so doing a level-order traversal is sufficient.
 * Finally we will return the maximum cost to get to a node at the last row.
 * 
 * @author Khakhu Ria
 * @version 03/04/2025
 */
public class problem_18_and_67_maximum_path
{
    /**
     * Read in the triangle data. The 1st index of the array is ignored to simplify computations
     * @param filename The file with the triangle data
     * @param rows The number of rows in the file
     * @return graph in the form of an array
     */
    private static int[][] graph(String filename, int rows)
    {
        int[][] graph = new int[(int)(rows*(rows+1)/2)+1][]; // use arithmetic sum formula to determine the total number of nodes ( row i has i nodes)
        int i = 1; // next index of graph to be filled
        Scanner file = null;
        try
        {
            file = new Scanner(new FileReader(filename));
            while (file.hasNextLine())
            {
                Scanner line = new Scanner(file.nextLine());
                while (line.hasNext()) { graph[i++] = new int[]{line.nextInt(), 0};}
                line.close();
            } 
        }
        catch(FileNotFoundException e)
        {
            System.err.println("File not found.");
        }
        finally { if (file!=null) file.close();}

        return graph;
    }
    private static int maximum_sum(String filename, int rows)
    {
        int[][] graph = graph(filename,rows);

        // level order traversal
        int visited = 0; // total number of nodes visited in the previous rows
        graph[1][1] = graph[1][0]; // set cost of root node to equal its value

        for (int i = 1; i < rows; i++) // avoid traversing last row as those are leaf nodes
        {
            int k = 1; // row index of the node to be visited
            for (int j = visited+1; j < visited + 1 + i; j++) // visit the nodes in the ith level
            {
               int[] parent = graph[j], child_1 = graph[visited+i+k], child_2 = graph[visited+i+k+1]; // visited+i+k is the index of the left child of this node
               // update costs to childen
               if (parent[1]+ child_1[0] > child_1[1]) { child_1[1] = parent[1]+ child_1[0];}
               if (parent[1]+ child_2[0] > child_2[1]) { child_2[1] = parent[1]+ child_2[0];}
               k++;
            }
            visited +=i; 
        }
        int max = 0;
        for (int l = visited+1; l < (int)(rows*(rows+1)/2)+1; l++)
        {
            max = graph[l][1] > max ? graph[l][1]: max;
        }
        return max;
    }
    /**
     * Main method. Prints out maximum sum.
     * @param args "18" for problem 18 and "67" for problem 67
     */
    public static void main (String[] args)
    {
        switch (args[0])
        {
            case "18":
            System.out.println(maximum_sum("data/problem_18_triangle.txt", 15));
            break;

            case "67":
            System.out.println(maximum_sum("data/problem_67_triangle.txt", 100));
            break;

            default:
            System.err.println("Enter 18 or 67 only.");
        }
    }
}