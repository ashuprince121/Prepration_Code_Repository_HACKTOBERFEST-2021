import java.awt.Color;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingConstants;

public class BasicCalculatorGUI implements ActionListener {

    JFrame jf;
    JLabel displayLabel;
    JButton sevenButton, eightButton, nineButton;
    JButton fourButton, fiveButton, sixButton;
    JButton oneButton, twoButton, threeButton;
    JButton dotButton, zeroButton, equalButton;
    JButton divButton, mulButton, minusButton, plusButton;
    JButton clearButton;
    boolean isOperatorClicked = false;
    String oldValue, clickedOperator;

    public BasicCalculatorGUI() {
        jf = new JFrame("Calculator");
        jf.setLayout(null);
        jf.setSize(600, 600);
        jf.setLocation(400, 150);

        /*
         * === Calculator Screen ===
         */

        displayLabel = new JLabel();
        displayLabel.setBounds(30, 50, 540, 40);
        displayLabel.setBackground(Color.gray);
        displayLabel.setOpaque(true);
        displayLabel.setHorizontalAlignment(SwingConstants.RIGHT);
        displayLabel.setForeground(Color.white);
        displayLabel.setFont(new Font("Arial", Font.PLAIN, 20));
        jf.add(displayLabel);

        /*
         * === Calculator Buttons ===
         */

        // 7 Button
        sevenButton = new JButton("7");
        sevenButton.setBounds(30, 130, 80, 80);
        sevenButton.setFont(new Font("Arial", Font.PLAIN, 40));
        sevenButton.addActionListener(this);
        jf.add(sevenButton);

        // 8 Button
        eightButton = new JButton("8");
        eightButton.setBounds(130, 130, 80, 80);
        eightButton.setFont(new Font("Arial", Font.PLAIN, 40));
        eightButton.addActionListener(this);
        jf.add(eightButton);

        // 9 Button
        nineButton = new JButton("9");
        nineButton.setBounds(230, 130, 80, 80);
        nineButton.setFont(new Font("Arial", Font.PLAIN, 40));
        nineButton.addActionListener(this);
        jf.add(nineButton);

        // 4 Button
        fourButton = new JButton("4");
        fourButton.setBounds(30, 230, 80, 80);
        fourButton.setFont(new Font("Arial", Font.PLAIN, 40));
        fourButton.addActionListener(this);
        jf.add(fourButton);

        // 5 Button
        fiveButton = new JButton("5");
        fiveButton.setBounds(130, 230, 80, 80);
        fiveButton.setFont(new Font("Arial", Font.PLAIN, 40));
        fiveButton.addActionListener(this);
        jf.add(fiveButton);

        // 6 Button
        sixButton = new JButton("6");
        sixButton.setBounds(230, 230, 80, 80);
        sixButton.setFont(new Font("Arial", Font.PLAIN, 40));
        sixButton.addActionListener(this);
        jf.add(sixButton);

        // 1 Button
        oneButton = new JButton("1");
        oneButton.setBounds(30, 330, 80, 80);
        oneButton.setFont(new Font("Arial", Font.PLAIN, 40));
        oneButton.addActionListener(this);
        jf.add(oneButton);

        // 2 Button
        twoButton = new JButton("2");
        twoButton.setBounds(130, 330, 80, 80);
        twoButton.setFont(new Font("Arial", Font.PLAIN, 40));
        twoButton.addActionListener(this);
        jf.add(twoButton);

        // 3 Button
        threeButton = new JButton("3");
        threeButton.setBounds(230, 330, 80, 80);
        threeButton.setFont(new Font("Arial", Font.PLAIN, 40));
        threeButton.addActionListener(this);
        jf.add(threeButton);

        // [.] Button
        dotButton = new JButton(".");
        dotButton.setBounds(30, 430, 80, 80);
        dotButton.setFont(new Font("Arial", Font.PLAIN, 40));
        dotButton.addActionListener(this);
        jf.add(dotButton);

        // 0 Button
        zeroButton = new JButton("0");
        zeroButton.setBounds(130, 430, 80, 80);
        zeroButton.setFont(new Font("Arial", Font.PLAIN, 40));
        zeroButton.addActionListener(this);
        jf.add(zeroButton);

        // [=] Button
        equalButton = new JButton("=");
        equalButton.setBounds(230, 430, 80, 80);
        equalButton.setFont(new Font("Arial", Font.PLAIN, 40));
        equalButton.addActionListener(this);
        jf.add(equalButton);

        /*
         * === Calculator Operations ===
         */

        // [/] Button
        divButton = new JButton("/");
        divButton.setBounds(330, 130, 80, 80);
        divButton.setFont(new Font("Arial", Font.PLAIN, 40));
        divButton.addActionListener(this);
        jf.add(divButton);

        // [x] Button
        mulButton = new JButton("x");
        mulButton.setBounds(330, 230, 80, 80);
        mulButton.setFont(new Font("Arial", Font.PLAIN, 40));
        mulButton.addActionListener(this);
        jf.add(mulButton);

        // [-] Button
        minusButton = new JButton("-");
        minusButton.setBounds(330, 330, 80, 80);
        minusButton.setFont(new Font("Arial", Font.PLAIN, 40));
        minusButton.addActionListener(this);
        jf.add(minusButton);

        // [+] Button
        plusButton = new JButton("+");
        plusButton.setBounds(330, 430, 80, 80);
        plusButton.setFont(new Font("Arial", Font.PLAIN, 40));
        plusButton.addActionListener(this);
        jf.add(plusButton);

        // clear Button
        clearButton = new JButton("Clear");
        clearButton.setBounds(430, 430, 80, 80);
        clearButton.setFont(new Font("Arial", Font.PLAIN, 19));
        clearButton.addActionListener(this);
        jf.add(clearButton);

        jf.setVisible(true);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }

    public static void main(String[] args) throws Exception {
        new BasicCalculatorGUI();
    }

    // Function to add action to buttons
    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == sevenButton) {
            if (isOperatorClicked) {
                displayLabel.setText("7");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "7");
            }
        } else if (e.getSource() == eightButton) {
            if (isOperatorClicked) {
                displayLabel.setText("8");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "8");
            }
        } else if (e.getSource() == nineButton) {
            if (isOperatorClicked) {
                displayLabel.setText("9");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "9");
            }
        } else if (e.getSource() == fourButton) {
            if (isOperatorClicked) {
                displayLabel.setText("4");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "4");
            }
        } else if (e.getSource() == fiveButton) {
            if (isOperatorClicked) {
                displayLabel.setText("5");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "5");
            }
        } else if (e.getSource() == sixButton) {
            if (isOperatorClicked) {
                displayLabel.setText("6");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "6");
            }
        } else if (e.getSource() == oneButton) {
            if (isOperatorClicked) {
                displayLabel.setText("1");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "1");
            }
        } else if (e.getSource() == twoButton) {
            if (isOperatorClicked) {
                displayLabel.setText("2");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "2");
            }
        } else if (e.getSource() == threeButton) {
            if (isOperatorClicked) {
                displayLabel.setText("3");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "3");
            }
        } else if (e.getSource() == zeroButton) {
            if (isOperatorClicked) {
                displayLabel.setText("0");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + "0");
            }
        } else if (e.getSource() == dotButton) {
            if (isOperatorClicked) {
                displayLabel.setText(".");
                isOperatorClicked = false;
            } else {
                displayLabel.setText(displayLabel.getText() + ".");
            }
        } else if (e.getSource() == equalButton) {
            String newValue = displayLabel.getText();

            float oldValueF = Float.parseFloat(oldValue);
            float newValueF = Float.parseFloat(newValue);
            float result;

            if (clickedOperator == "+") {
                result = oldValueF + newValueF;
                displayLabel.setText(result + "");
            } else if (clickedOperator == "-") {
                result = oldValueF - newValueF;
                displayLabel.setText(result + "");
            } else if (clickedOperator == "x") {
                result = oldValueF * newValueF;
                displayLabel.setText(result + "");
            } else if (clickedOperator == "/") {
                result = oldValueF / newValueF;
                displayLabel.setText(result + "");
            }
        } else if (e.getSource() == plusButton) {
            isOperatorClicked = true;
            oldValue = displayLabel.getText();
            clickedOperator = "+";

        } else if (e.getSource() == minusButton) {
            isOperatorClicked = true;
            oldValue = displayLabel.getText();
            clickedOperator = "-";
        } else if (e.getSource() == mulButton) {
            isOperatorClicked = true;
            oldValue = displayLabel.getText();
            clickedOperator = "x";
        } else if (e.getSource() == divButton) {
            isOperatorClicked = true;
            oldValue = displayLabel.getText();
            clickedOperator = "/";
        } else if (e.getSource() == clearButton) {
            displayLabel.setText("");
        }

    }
}
