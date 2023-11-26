package hk.edu.polyu.comp.comp2021.tms.model.GUI.SearchAndPrintPage;

import hk.edu.polyu.comp.comp2021.tms.model.GUITMS;
import hk.edu.polyu.comp.comp2021.tms.model.Main.Controller;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ReportDuration extends JPanel{
	private GUITMS frame;
	private JPanel backgroundPanel;
	private JButton resetButton;
	private JButton backButton;
	private JButton enterButton;
	private JPanel upperPanel;
	private JTextField getTaskName;
	private JLabel NameLabel;
	private JPanel lowerPanel;

	public ReportDuration(GUITMS frame) {
		this.frame = frame;
		backgroundPanel.setPreferredSize(frame.getSize());
		add(backgroundPanel);

		enterButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent e) {
				if (getTaskName.getText().equals("")) {
					JOptionPane.showMessageDialog(frame, "You are required to fill in every elements",
							"Warning", JOptionPane.WARNING_MESSAGE);
				} else {
					String str = getTaskName.getText();
					Controller controller = new Controller();
					controller.reportDuration(getTaskName.getText());
				}
			}

		});

		resetButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed (ActionEvent e){
				getTaskName.setText("");
			}
		});

		backButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed (ActionEvent e){
				frame.switchToPanel(frame.getSearchAndPrintPanel());
			}
		});
	}
}
