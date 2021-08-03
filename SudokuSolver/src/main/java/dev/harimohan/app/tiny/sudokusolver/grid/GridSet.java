package dev.harimohan.app.tiny.sudokusolver.grid;

import java.util.Scanner;

public class GridSet {
	private final ProblemGrid problemGrid;
	private final CalcGrid[] calcGrids;
	int order;
	int remainingCellCount;

	public GridSet(int order, int rows) {
		this.order = order;
		this.remainingCellCount = order * order;
		problemGrid = new ProblemGrid(order, rows, this);
		calcGrids = new CalcGrid[order];

		for (int i = 0; i < order; i++) {
			calcGrids[i] = new CalcGrid(order, rows, problemGrid, i + 1);
		}
	}

	public void insertNumbersFromCommandLine() {
		try (Scanner scn = new Scanner(System.in)) {
			boolean isValid = true;
			for (int i = 0; i < order && isValid; i++) {
				for (int j = 0; j < order; j++) {
					int value = scn.nextInt();
					if (value < 0 || value > order) {
						isValid = false;
						break;
					}
					problemGrid.setValueAt(i, j, value);
					if (value == 0)
						continue;
					remainingCellCount--;
					calcGrids[value - 1].markCellAt(i, j, true);
					for (int k = 0; k < order; k++) {
						calcGrids[k].markCellAt(i, j, false);
					}
				}
			}
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public boolean solvePuzzle() {
		boolean solved = true;

		while (remainingCellCount > 0) {
			int countBeforeParse = remainingCellCount;
			for (int i = 0; i < order; i++) {
				remainingCellCount -= calcGrids[i].checkForSolution();
			}
			if (remainingCellCount == countBeforeParse) {
				solved = false;
				break;
			}
		}

		return solved;
	}

	public CalcGrid[] getCalcGrids() {
		return calcGrids;
	}

	public ProblemGrid getProblemGrid() {
		return problemGrid;
	}
}
