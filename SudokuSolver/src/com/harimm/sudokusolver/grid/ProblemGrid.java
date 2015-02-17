package com.harimm.sudokusolver.grid;

public class ProblemGrid extends BaseGrid {

	public ProblemGrid(int order, int rows) {
		super(order, rows);
	}
	
	public void setValueAt(int row, int column, int value){
		grid[row][column] = value;
	}

}
