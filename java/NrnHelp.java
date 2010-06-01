
//import java.io.* ;
import javax.swing.* ;
//import javax.swing.text.* ;

//import java.awt.* ;
//import javax.swing.event.* ;
//import java.awt.event.*;
//import java.net.URL ;

public class NrnHelp {

	HtmlBrowser hb;
	JFrame frame;

	public NrnHelp() {
		hb = new HtmlBrowser();
		frame = new JFrame();
		frame.getContentPane().add(hb);
		frame.addWindowListener(hb);

		frame.pack();
		frame.show();

		hb.reload();
	}

	public void setPage(String su) {
		hb.setPage(su);
	}
}
