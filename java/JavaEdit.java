//compile with
/*
javac -classpath \
 .:$N/share/nrn/classes/neuron.jar:/usr/j2sdk1_3_1/demo/jfc/Notepad/Notepad.jar\
 JavaEdit.java

To use in NEURON one needs a
 /usr/j2sdk1_3_1/demo/jfc/Notepad/Notepad.jar
*/

import neuron.*;

import java.awt.*;
import java.awt.event.*;
import java.beans.*;
import java.io.*;
import java.net.URL;
import java.util.*;

import javax.swing.text.*;
import javax.swing.undo.*;
import javax.swing.event.*;
import javax.swing.*;

/** Test class 
 * objref tmp
 * tmp = new JavaEdit()
 */
public class JavaEdit { 
    public JavaEdit() {
	try {
	    np = new Notepad();
	}catch (Throwable t) {
            System.out.println("uncaught exception: " + t);
            t.printStackTrace();
	}
	start();
    }

public Object notepad() {
	return np;
}

    public String text() {
	return np.getEditor().getText();
    }
    public boolean exec() {
	return Neuron.execute(np.getEditor().getText());
    }
    public void map() {
	start();
    }
    Notepad np;
    void start() {
	try {
        JFrame frame = new JFrame();
        frame.setTitle("JavaEdit for NEURON");
        frame.setBackground(Color.lightGray);
        frame.getContentPane().setLayout(new BorderLayout());
        frame.getContentPane().add("Center", np);
        frame.addWindowListener(new Closer());
        frame.pack();
        frame.setSize(500, 600);
        frame.show();
	Neuron.windowListen(frame, this);
        } catch (Throwable t) {
            System.out.println("uncaught exception: " + t);
            t.printStackTrace();
        }
 
    }
    protected static final class Closer extends WindowAdapter {
        public void windowClosing(WindowEvent e) {
		System.out.println("Notepad window closed.");
        }
    }   
}
