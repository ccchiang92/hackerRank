import java.util.*;
import java.io.*;
import java.lang.Math; 

class Solution{
    public static void main(String []argh){
        
        Scanner in = new Scanner(System.in);
        int t=in.nextInt();
        for(int i=0;i<t;i++){
            int a = in.nextInt();
            int b = in.nextInt();
            int n = in.nextInt();
            int last = a+b;
            String out =Integer.toString(last);
            for(int j=1;j<n;j++){
                int now = (int)Math.pow(2,j)*b +last;
                out = out + " "+ now;
                last = now;                
            }
            System.out.println(out);
        }
        in.close();
    }
}