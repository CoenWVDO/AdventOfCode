#pragma once
#include <string>

class Day5
{
public:
	Day5(std::string data);
	~Day5();
	int perform(std::string dat = "");
	void performPart2();

	std::string m_data;
};

