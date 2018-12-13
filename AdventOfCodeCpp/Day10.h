#pragma once
#include <string>
#include <vector>

class Day10
{
public:
	Day10(std::string datalocation);
	~Day10();

	void findMessage(int startSec, int endSec);

	std::vector<std::string> coordinates;
};

