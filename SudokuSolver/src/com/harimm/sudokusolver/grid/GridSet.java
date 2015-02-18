package com.harimm.sudokusolver.grid;

import java.util.Scanner;

public class GridSet {
	private ProblemGrid problemGrid;
	private CalcGrid[] calcGrids;
	int order;

	public GridSet(int order, int rows) {
		this.order = order;
		problemGrid = new ProblemGrid(order, rows);
		calcGrids = new CalcGrid[order];

		for (int i = 0; i < order; i++) {
			calcGrids[i] = new CalcGrid(order, rows);
		}
	}

	public void insertNumbersFromCommandLine() {
		Scanner scn = new Scanner(System.in);
		try {
			boolean isValid = true;
			for (int i = 0; i < order && isValid; i++) {
				for (int j = 0; j < order; j++) {
					int value = scn.nextInt();
					if (value < 0 || value > order) {
						isValid = false;
						break;
					}
					problemGrid.setValueAt(i, j, value);
					if(value == 0)
						continue;
					calcGrids[value - 1].markCellAt(i, j, true);
					for (int k = 0; k < order; k++) {
						calcGrids[k].markCellAt(i, j, false);
					}
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			scn.close();
		}
	}
}
