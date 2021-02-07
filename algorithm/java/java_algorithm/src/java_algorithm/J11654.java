package java_algorithm;
import java.util.Scanner;

public class J11654{
	public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        String ab = "ab";
        //abacdabacdbabcbacababab > "ab"Á¦°Å
        int cnt = 0;
        
        
        System.out.println();
        for(int i=0; i<str.length()-1; i++) {
        	if(str.substring(i, i+2).equals("ab")) {
        		cnt++;
        	}
        }
       System.out.println(cnt);
    }
}