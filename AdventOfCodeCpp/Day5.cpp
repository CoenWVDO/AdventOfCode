#include "pch.h"
#include "Day5.h"
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

Day5::Day5(std::string filename)
{
	std::ifstream inputstream(filename);
	std::string line;
	if (inputstream.is_open())
	{
		while (getline(inputstream, line))
		{
			m_data += line;
			std::cout << "Adding line to data";
		}
		std::cout << "Done";
		inputstream.close();
	}
	else
	{
		std::cout << "Unable to open filename..";
	}
}


Day5::~Day5()
{
}

int Day5::perform(std::string dat)
{ 
	std::string data;
	if (dat == "")
	{
		data = m_data;
	}
	else
	{
		data = dat;
	}

	int i = 0;
	while(i < data.length())
	{
		char first = data[i];
		char second = data[i + 1];
		if (char(first + 32) == second || char(second + char(32)) == first)
		{
			data.erase(data.begin()+i, data.begin()+i + 2);
			i = i - 2;
			if (i < 0)
			{
				i = -1;
			}
		}
		i++;
	}
	std::cout << data.length();
	std::cout << std::endl;
	std::ofstream outputday5("outputDay5.txt");

	if (outputday5.is_open())
	{
		outputday5 << data;
		outputday5.close();
	}
	return data.length();
}

void Day5::performPart2()
{
	int i = 0;
	std::vector<int> countPerCharFromAtoZ;
	for (int j = 0; j < 26; j++)
	{
		std::string dataNew = m_data;
		int k = 0;
		while (k < dataNew.length())
		{
			if (dataNew[k] == char('A' + j) or dataNew[k] == char('A' + j + 32))
			{
				dataNew.erase(dataNew.begin() + k);
			}
			else
			{
				k++;
			}
		}
		int count = perform(dataNew);
		countPerCharFromAtoZ.push_back(count);
	}
	std::cout << "Max Element Index: " << std::distance(countPerCharFromAtoZ.begin(), std::min_element(countPerCharFromAtoZ.begin(), countPerCharFromAtoZ.end()));
}