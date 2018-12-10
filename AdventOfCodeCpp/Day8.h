#pragma once
#include <string>
#include <vector>
#include <deque>

class Day8
{
public:
	Day8(std::string dataloc);
	~Day8();

	void calcSum();
	void part2();

private:
	std::vector<int> data;
};

