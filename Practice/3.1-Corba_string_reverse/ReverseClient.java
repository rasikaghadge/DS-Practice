import ReverseApp.*;
import org.omg.CosNaming.*;
import org.omg.CosNaming.NamingContextPackage.*;
import org.omg.CORBA.*;
import java.io.*;
public class ReverseClient{

  public static void main(String args[]){
 
    try{
 // create and initialize the ORB
      ORB orb = ORB.init(args, null);

      // get the root naming context
      org.omg.CORBA.Object objRef =
      orb.resolve_initial_references("NameService");
     
      // Use NamingContextExt instead of NamingContext. This is
      // part of the Interoperable naming Service. 
      NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

      // resolve the Object Reference in Naming
      String name = "Reverse";
      ReverseIntf helloImpl = ReverseIntfHelper.narrow(ncRef.resolve_str(name));

      System.out.println("Obtained a handle on server object: "+ helloImpl);
      System.out.println("Enter the String to reverse");
      String  strn=(new BufferedReader(new InputStreamReader(System.in)).readLine());

     System.out.println("Enter the number");
     int num=Integer.parseInt(new BufferedReader(new                                InputStreamReader(System.in)).readLine());
    System.out.println("Reverse of the string is");
    System.out.println(helloImpl.getReverseString(strn));
    System.out.println("Reverse of the number is "+helloImpl.getReverseNumber(num));
      helloImpl.shutdown();
      }
     
    catch (Exception e) {
      System.out.println("ERROR : " + e) ;
      e.printStackTrace(System.out);
    }
  }
}