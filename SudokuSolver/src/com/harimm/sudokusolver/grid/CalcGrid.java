package com.harimm.sudokusolver.grid;

public class CalcGrid extends BaseGrid {

	public CalcGrid(int order, int rows) {
		super(order, rows);
		for (int i = 0; i < order; i++)
			for (int j = 0; j < order; j++)
				grid[i][j] = 0;
	}

	public boolean markCellAt(int row, int column, boolean fill) {
		if (grid[row][column] != 0) {
			return false;
		}
		grid[row][column] = -1;

		if (fill) {
			fillRow(row);
			fillColumn(column);
			fillBox(row,column);
		}
		return true;
	}

	private void fillRow(int row) {
		for (int i = 0; i < order; i++) {
			grid[row][i] = -1;
		}
	}

	private void fillColumn(int column) {
		for (int i = 0; i < order; i++) {
			grid[i][column] = -1;
		}
	}

	private void fillBox(int row, int column) {
		int rowStart = super.getSubGridRowStart(row);
		int colStart = super.getSubGridColumnStart(column);
		int rowEnd = rowStart + rows;
		int colEnd = colStart + cols;

		for (int i = rowStart; i < rowEnd; i++)
			for (int j = colStart; j < colEnd; j++)
				grid[i][j] = -1;
	}
}
