
import java.io.* ;
import javax.swing.* ;
import javax.swing.text.* ;

import java.awt.* ;
import javax.swing.event.* ;
import java.awt.event.*;
import java.net.URL ;




public class HtmlBrowser extends JPanel 
implements HyperlinkListener, ActionListener, WindowListener {

   JEditorPane jep;

   String[] history;
   int hpos;

   JTextField addressField;
   JTextField hyperField;

   // defaultText is for sending dynamically generated text to the browser,
   // such as error messages or instructions to the user
   String defaultText;



   public HtmlBrowser() {
      setLayout (new BorderLayout(2, 2));


      // make a non editable JEditorPane: if it iseditable, clicking
      // links causes them to be edited. Otherwise they are treated as 
      // hyperlink events
      
      jep = new JEditorPane();
      jep.setEditable (false); 
      jep.addHyperlinkListener(this);
      
      
      // wrap it in a scroll pane to get the scrollbars
      JScrollPane jsp = new JScrollPane(jep);
      add("Center", jsp);

      // the history list contains strings converted to URLs
      history = new String[20];
      hpos = -1;


      // now a panel at the top with some buttons and the address;
      JPanel topPanel = new JPanel();
      topPanel.setLayout(new GridLayout(2, 1, 2, 2));
      
      JPanel buttons = new JPanel();
      buttons.setLayout(new GridLayout(1, 3));

      JButton back = new JButton("back");
      buttons.add(back);
      back.addActionListener(this);

      JButton forward = new JButton("forward");
      buttons.add(forward);
      forward.addActionListener(this);

      JButton reload = new JButton("reload");
      buttons.add(reload);
      reload.addActionListener(this);


      topPanel.add(buttons);

      
      // the address bar has a label, the text field and a "go" button
      JPanel address = new JPanel();
      address.setLayout(new BorderLayout(2, 2));
      address.add("West", new JLabel("address"));
      
      JButton goButton = new JButton("go");
      address.add("East", goButton);
      goButton.addActionListener(this);

      addressField = new JTextField("http://www.neuron.yale.edu/");
      address.add("Center", addressField);
      addressField.addActionListener(this);

      topPanel.add(address);
      add("North", topPanel);

      // if the mouse is over a hyperlink, here is where it is shown
	JPanel hypershow = new JPanel();
	hypershow.setLayout(new GridLayout(1,1,1,1));
	hyperField = new JTextField("");
	hypershow.add("East", hyperField);
	add("South", hypershow);
   }



   
   // this class listens to all buttons and for pressing return on the 
   // text field
   public void actionPerformed(ActionEvent evt) {
      if (evt.getSource() instanceof JButton) {
	 String stxt = ((JButton)evt.getSource()).getText();
	 if (stxt.equals("reload")) {
	    reload();

	 } else if (stxt.equals("back")) {
	    back();


	 } else if (stxt.equals("forward")) {
	    forward();

	 } else if (stxt.equals("go")) {
	    reload();
	    
	 } else {
	    System.out.println("ERROR - unknown action event " + stxt);
	 }
      } else if (evt.getSource() instanceof JTextField) {
	// must be the address field;
	 reload();

      }
   }




   public void hyperlinkUpdate (HyperlinkEvent e) {
      Object etyp = e.getEventType();
      String surl = e.getDescription();
      URL url = e.getURL();
      if (url != null) surl = url.toString();


      if (etyp == HyperlinkEvent.EventType.ENTERED) {
	 // hand cursor to hover over links;
	 setCursor(new Cursor(Cursor.HAND_CURSOR));
	hyperField.setText(e.getURL().toString());

      } else if (etyp ==  HyperlinkEvent.EventType.EXITED) {
	 // revert to normal if the mouse moves away
	 setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
	hyperField.setText("");
	 
	 
	 
      } else if (etyp == HyperlinkEvent.EventType.ACTIVATED) {
	 // here one could catch special types of links for 
	 // internal comsumption by matching tags in the string surl

	 setPage(surl);
      }
   }

  

   public void setPage(String su) {
      if (su.equals("internally generated")) {
	 showDefaultText();
	 
      } else {
	 
	 try {
	    jep.setPage(new URL(su));
	 } catch (Exception e) {
	    setDefaultText("ERROR - cant load page \n page:   " +
			   su + "\n error:  " + e + "\n");
	 }	    
	 
	 if (hpos >= history.length-1) {
	    for (int i = 1; i < history.length; i++) {
	       history[i-1]=history[i];
	    }
	    hpos = history.length - 2;
	 }
	 history[++hpos] = su;
	 addressField.setText(su);
      }
   }


   // set the page text directly, and assign the address "internally generated"
   // to it. This could be used, for example, to send error messages or 
   // instructions to the user. 
   public void setDefaultText(String s) {
      defaultText = s;
      addressField.setText("internally generated");
      reload();
   }



   void showDefaultText() {
      jep.setContentType("text/html;");
      jep.setText(defaultText);
      jep.setEditable(false);
   }




   public void reload() {
      //      if (history != null && hpos >= 0) showPage(history[hpos]);
      showPage(addressField.getText());
   }




   public void showPage (String address) {
      if (address == null || address.trim().length() <= 0) return;

      if (address.startsWith("http:") ||
	  address.startsWith("file:") ||
	  address.startsWith("zip:")) {
	 setPage(address);

      } else if (address.equals("internally generated")) {
	 setPage(address);

      } else {
	 File f = new File(address);
	 if (f.exists() && f.isFile()) {
	    setPage("file:" + f.getAbsolutePath());
	 }
      }
   }

      

   public void forward() {
     if (hpos < history.length-1 && history[hpos+1] != null) {
	showPage(history[hpos+1]);
     }
   }

   
   public void back() {
      if (hpos > 0) {
	 hpos -= 2;
	 showPage(history[hpos+1]);
      }
   }



   public Dimension getPreferredSize() {
      return new Dimension(400, 500);
   }

   

   // listen the the frame if necessary and quit if the frame is closed
   
   public void windowClosing(WindowEvent wev) { System.exit(0); }
   public void windowClosed(WindowEvent wev) { System.exit(0); }
   public void windowOpened(WindowEvent wev) { }
   public void windowActivated(WindowEvent wev) { }
   public void windowDeactivated(WindowEvent wev) { }
   public void windowIconified(WindowEvent wev) { }
   public void windowDeiconified(WindowEvent wev) { }






   // simple main method - make a browser, put it in a frame, and 
   // show the frame
   public static void main(String[] argv) {
      HtmlBrowser hp = new HtmlBrowser();
      JFrame frame = new JFrame();
      frame.getContentPane().add(hp);
      frame.addWindowListener(hp);

      frame.pack();
      frame.show();

      hp.reload();
   }
   


} 





