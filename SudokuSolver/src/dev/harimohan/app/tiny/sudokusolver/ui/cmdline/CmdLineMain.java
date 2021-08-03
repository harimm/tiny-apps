package dev.harimohan.app.tiny.sudokusolver.ui.cmdline;

import java.util.Scanner;

import dev.harimohan.app.tiny.sudokusolver.grid.GridSet;

/*
 * As a initial test, the app is run through command line. It accepts 2 inputs
 * 1. Order of the whole grid
 * 2. No. of rows of sub-grid 
 */
public class CmdLineMain {

	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);
		int order = 0;
		int rows = 0;
		boolean flag;
		do {
			System.out.println("How many numbers?(1-10)");
			flag = true;

			try {
				order = scn.nextInt();
				if (order > 10 || order < 1) {
					flag = false;
					System.out.println("Invalid number. Try again!");
					continue;
				}
				flag = true;
			} catch (Exception e) {
				System.out.println("Exception has occurred. Try again!");
				flag = false;
			}
		} while (!flag);

		do {
			System.out.println("How many rows in each subgrid?");
			flag = true;
			try {
				rows = scn.nextInt();
				if (rows < 1 || rows > order || (order % rows != 0)) {
					flag = false;
					System.out.println("Invalid number. Try again!");
					continue;
				}
				flag = true;
			} catch (Exception e) {
				System.out.println("Exception has occurred. Try again!");
			}
		} while (!flag);

		GridSet gridSet = new GridSet(order, rows);
		System.out
				.println("Enter the grid of numbers. Enter zero for blank cell.");
		gridSet.insertNumbersFromCommandLine();
		if (gridSet.solvePuzzle()) {
			System.out.println("\n\nSOLUTION\n");
			System.out.println(gridSet.getProblemGrid().toString());
		} else
			System.out.println("Failed to solve puzzle!");
		scn.close();
	}
}
