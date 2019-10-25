import java.util.Scanner;

public class Avion
{
  public static void main(String[] args)
  {
    String output = "";
    Scanner scan = new Scanner(System.in);
    for (int i=1; i<6; i++) {
      String thing = scan.next().toString();
      
      if(thing.contains("FBI")) {
        output += i + " ";
      }
    }
    if(output.length()==0) {
      output = "HE GOT AWAY!";
    }    
    System.out.print(output);
  }
}