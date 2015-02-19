package com.harimm.sudokusolver.grid;

public class ProblemGrid extends BaseGrid {

	private GridSet gridSet;

	public ProblemGrid(int order, int rows, GridSet gridSet) {
		super(order, rows);
		this.gridSet = gridSet;
	}

	public void setValueAt(int row, int column, int value) {
		grid[row][column] = value;
		if(value == 0)
			return;
		CalcGrid gridOfValue = gridSet.getCalcGrids()[value - 1];
		gridOfValue.markCellAt(row, column, true);
		for (CalcGrid cGrid : gridSet.getCalcGrids()) {
			cGrid.markCellAt(row, column, false);
		}
	}
}
