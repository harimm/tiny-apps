package dev.harimohan.app.tiny.sudokusolver.grid;

public class CalcGrid extends BaseGrid {

	private ProblemGrid problemGrid;
	private int calcValue;

	public CalcGrid(int order, int rows, ProblemGrid problemGrid, int calcValue) {
		super(order, rows);
		this.calcValue = calcValue;
		this.problemGrid = problemGrid;
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
			fillBox(row, column);
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

	public int checkForSolution() {
		int solvedCells = 0;
		solvedCells += checkRows();
		solvedCells += checkColumns();
		solvedCells += checkBoxes();
		return solvedCells;
	}

	private int checkRows() {
		int solvedCells = 0;

		for (int i = 0; i < order; i++) {
			int candidateCell = -1;
			for (int j = 0; j < order; j++) {
				if (this.grid[i][j] == 0) {
					if (candidateCell == -1) {
						candidateCell = j;
					} else {
						candidateCell = -1;
						break;
					}
				}
			}
			if (candidateCell != -1) {
				problemGrid.setValueAt(i, candidateCell, calcValue);
				solvedCells++;
			}
		}
		return solvedCells;
	}

	private int checkColumns() {
		int solvedCells = 0;

		for (int i = 0; i < order; i++) {
			int candidateCell = -1;
			for (int j = 0; j < order; j++) {
				if (this.grid[j][i] == 0) {
					if (candidateCell == -1) {
						candidateCell = j;
					} else {
						candidateCell = -1;
						break;
					}
				}
			}
			if (candidateCell != -1) {
				problemGrid.setValueAt(candidateCell, i, calcValue);
				solvedCells++;
			}
		}
		return solvedCells;
	}

	private int checkBoxes() {
		int solvedCells = 0;
		int boxRowStart = 0;
		int boxColStart = 0;
		int boxRowEnd = rows;
		int boxColEnd = cols;

		for (int i = 0; i < cols; i++) {
			boxColStart = 0;
			boxColEnd = cols;
			for (int j = 0; j < rows; j++) {
				boolean found = false;
				boolean possible = true;
				int candidateRow = -1;
				int candidateColumn = -1;
				for (int k = boxRowStart; k < boxRowEnd && possible; k++) {
					for (int l = boxColStart; l < boxColEnd; l++) {
						if (grid[k][l] == 0) {
							if (found) {
								found = false;
								possible = false;
								break;
							} else {
								candidateRow = k;
								candidateColumn = l;
								found = true;
							}
						}
					}
				}

				if (found) {
					problemGrid.setValueAt(candidateRow, candidateColumn,
							calcValue);
					solvedCells++;
				}

				boxColStart = boxColEnd;
				boxColEnd += cols;
			}
			boxRowStart = boxRowEnd;
			boxRowEnd += rows;
		}
		return solvedCells;
	}
}
