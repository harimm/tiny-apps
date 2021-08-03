package dev.harimohan.app.tiny.sudokusolver.grid;

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

	@Override
	public String toString() {
		StringBuilder gridString = new StringBuilder();

		for (int i = 0; i < order; i++) {
			for (int j = 0; j < order; j++) {
				gridString.append(grid[i][j]).append(" ");
			}
			gridString.append("\n");
		}

		return gridString.toString();
	}
}
