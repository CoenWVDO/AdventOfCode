#pragma once
#include <string>
#include <map>
#include <vector>

class Day7
{
public:
	Day7(std::string data);
	~Day7();
	void perform();
	void performPart2();

private:
	std::map<char, std::vector<char> > map;
};

