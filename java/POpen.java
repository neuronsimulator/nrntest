// The analogy seed for implementing this was found with a google search.
// http://www.nerdlabs.com/paul/software/javasnippets.html
// I originally tried to do the whole thing in hoc but was defeated by
// the fact that most of the io methods require an exception handler.
// Also it is tedious to load_java every intermediate class used by the code.
// In the process of implementing this, I fixed a bug in the nrnjava interface
// having to do with returning a null object. i.e. returning returning null
// from String getline() below ended up in hoc as a String that could not
// be accessed instead of a NULLObject

import java.io.*;
import java.lang.Process;
import java.lang.Runtime;
import java.lang.String;

public class POpen {

Process p;
BufferedReader reader;
BufferedWriter writer;

public POpen(String command) {
    try {
        p = Runtime.getRuntime().exec(command);
        reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
        writer = new BufferedWriter(new OutputStreamWriter(p.getOutputStream()));
System.out.println("POpen " + command);
    } catch (IOException ioex) {
        ioex.printStackTrace();
    }
}

public void destroy() {
    try {	
        reader.close();
        writer.close();
        p.destroy();
        p = null;
        reader = null;
        writer = null;
    } catch (IOException ioex) {
        ioex.printStackTrace();
    }
}

public boolean ready2get() {
    try {
        return reader.ready();
    }catch (IOException ioex) {
        ioex.printStackTrace();
    }
    return false;
}

public String getLine() {
    try {
	String line = reader.readLine();
System.out.println("getLine " + line);
        return line;
    }catch (IOException ioex) {
        ioex.printStackTrace();
    }
    return null;
}

public int readChar() {
    try {
        return reader.read();
    }catch (IOException ioex) {
        ioex.printStackTrace();
        return -2;
    }
}

public void put(String s) {
    try {
        writer.write(s, 0, s.length());
        writer.newLine();
        writer.flush();
    }catch (IOException ioex) {
        ioex.printStackTrace();
    }
}

}

