package com.harimm.sudokusolver.grid;

public abstract class BaseGrid {
	protected int order;
	protected int rows;
	protected int cols;
	protected int[][] grid;

	public BaseGrid(int order, int rows) {
		this.order = order;
		this.rows = rows;
		this.cols = order / rows;
		this.grid = new int[order][order];
	}

	protected int getSubGridColumnStart(int column) {
		return column - (column % cols);
	}
	
	protected int getSubGridRowStart(int row) {
		return row - (row % rows);
	}
}
