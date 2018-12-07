#pragma once
#include <string>
#include <vector>
#include <utility>

class Day6
{
public:
	Day6(std::string dataloc);
	~Day6();

	void perform();
	int makeKey(std::pair<int, int> paar);
	void performPart2();


private:
	std::vector<std::pair<int, int> > coordinates;
	std::vector<int> x_values;
	std::vector<int> y_values;
};

