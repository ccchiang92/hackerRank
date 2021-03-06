import java.util.*;

public class Solution {
    public static boolean helper(int i,int leap, int[] game,boolean [] checked){
            int n = game.length;
            if (i<0||(i>n-1)){
                return false;
            }else if (checked[i]){
                return false;
            }else if (game[i]!=0){
                return false;
            }else if ((i==(n-1))||((i+leap)>=n)){
                return true;
            }else{
                checked[i]=true;                
                return helper(i-1,leap,game,checked)||helper(i+1,leap,game,checked)||helper(i+leap,leap,game,checked);
            }
        }
    public static boolean canWin(int leap, int[] game) {
        // Return true if you can win the game; otherwise, return false.
        int n = game.length;
        boolean[] checked = new boolean[n];
        for (int j=0; j<n;j++){
            checked[j]=false;
        }
       
        return helper(0,leap,game,checked);
    }


    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int q = scan.nextInt();
        while (q-- > 0) {
            int n = scan.nextInt();
            int leap = scan.nextInt();
            
            int[] game = new int[n];
            for (int i = 0; i < n; i++) {
                game[i] = scan.nextInt();
            }

            System.out.println( (canWin(leap, game)) ? "YES" : "NO" );
        }
        scan.close();
    }
}