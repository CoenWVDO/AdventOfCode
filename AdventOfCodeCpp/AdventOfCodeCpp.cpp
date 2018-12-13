// AdventOfCodeCpp.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include "Day5.h"
#include "Day6.h"
#include "Day7.h"
#include "Day8.h"
#include "Day9.h"
#include "Day9Performance.h"
#include "Day10.h"

int main(int argc, char* argv[])
{
	//Day5 day5("day5coen.txt");
	//day5.perform();
	//day5.performPart2();
	
	//Day6 day6("day6data.txt");
	//day6.perform();
	//day6.performPart2();

	Day7 day7("input.txt");
	//day7.perform();
	day7.performPart2();

	//Day8 day8("day8data.txt");
	//day8.calcSum();
	//day8.part2();

	// Day9 day9;
	// day9.winnerPoints();
	// day9.part2(404, 7185200);

	 //Day9Performance day9improved;
	 //long long answer2 = day9improved.calculateWinnerPoints(404, 7185200);
	 //std::cout << answer2 << std::endl;

	//Day10 day10("day10data.txt");
	//day10.findMessage(10390, 10440);

}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
