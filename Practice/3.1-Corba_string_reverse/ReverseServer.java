import ReverseApp.*;
import org.omg.CosNaming.*;
import org.omg.CosNaming.NamingContextPackage.*;
import org.omg.CORBA.*;
import org.omg.PortableServer.*;
import org.omg.PortableServer.POA;
import java.util.Properties;

class ReverseImpl extends ReverseIntfPOA {
    private ORB orb;

    public void setORB(ORB orb_val) {
        orb = orb_val;
    }

    public String getReverseString(String str) {
        String reversedStr = "";

        for (int i = str.length() - 1; i >= 0; i--) {
            reversedStr += str.charAt(i);
        }
        return reversedStr;
    }

    public int getReverseNumber(int num) {
        int reversedNum = 0;

        while (num > 0) {
            reversedNum = reversedNum * 10 + num % 10;
            num /= 10;
        }
        return reversedNum;
    }

    public void shutdown() {
        orb.shutdown(false);
    }
}

public class ReverseServer {
    public static void main(String args[]) {
        try {
            // Create and initialize the ORB
            ORB orb = ORB.init(args, null);

            // Get reference to rootpoa & activate the POAManager
            POA rootpoa = POAHelper.narrow(orb.resolve_initial_references("RootPOA"));
            rootpoa.the_POAManager().activate();

            // Create servant and register it with the ORB
            ReverseImpl reverseImpl = new ReverseImpl();
            reverseImpl.setORB(orb);

            // Get the object reference for the servant
            org.omg.CORBA.Object ref = rootpoa.servant_to_reference(reverseImpl);
            ReverseIntf reverseRef = ReverseIntfHelper.narrow(ref);

            // Get the root naming context
            org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");
            NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

            // Bind the Object Reference in Naming
            String name = "Reverse";
            NameComponent path[] = ncRef.to_name(name);
            ncRef.rebind(path, reverseRef);

            System.out.println("ReverseServer ready and waiting...");

            // Wait for invocations from clients
            orb.run();
        } catch (Exception e) {
            System.err.println("ERROR: " + e);
            e.printStackTrace(System.out);
        }

        System.out.println("ReverseServer Exiting...");
    }
}
