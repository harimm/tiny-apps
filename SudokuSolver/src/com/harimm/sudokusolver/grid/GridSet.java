package com.harimm.sudokusolver.grid;

public class GridSet {
	private ProblemGrid problemGrid;
	private CalcGrid[] calcGrids;

	public GridSet(int order, int rows) {
		problemGrid = new ProblemGrid(order, rows);
		calcGrids = new CalcGrid[order];

		for (int i = 0; i < order; i++) {
			calcGrids[i] = new CalcGrid(order, rows);
		}
	}
}
