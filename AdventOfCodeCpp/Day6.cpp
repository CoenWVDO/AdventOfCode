#include "pch.h"
#include "Day6.h"
#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <unordered_map>

Day6::Day6(std::string datalocation)
{
	std::ifstream inputstream(datalocation);
	std::string line;
	if (inputstream.is_open())
	{
		while (getline(inputstream, line))
		{
			std::string tempstring = "";
			int point = 0;
			while (line[point] != ',')
			{
				tempstring += line[point];
				point++;
			}
			int x = std::stoi(tempstring);
			x_values.push_back(x);

			point += 2;
			tempstring = "";
			while (point < line.size() && line[point] != ' ' && line[point] != '\n')
			{
				tempstring += line[point];
				point++;
			}
			int y = std::stoi(tempstring);
			y_values.push_back(y);
			
			coordinates.push_back(std::make_pair(x, y));
			std::cout << "Adding coordinate to data" << std::endl;
		}
		std::cout << "Done";
		inputstream.close();
	}
	else
	{
		std::cout << "Unable to open filename..";
	}
}


Day6::~Day6()
{
}

void Day6::perform()
{
	int maxX = x_values[std::distance(x_values.begin(), std::max_element(x_values.begin(), x_values.end()))] -1;
	int maxY = y_values[std::distance(y_values.begin(), std::max_element(y_values.begin(), y_values.end()))] -1;
	int minX = x_values[std::distance(x_values.begin(), std::min_element(x_values.begin(), x_values.end()))] +1;
	int minY = y_values[std::distance(y_values.begin(), std::min_element(y_values.begin(), y_values.end()))] +1;
	std::unordered_map<int, int> coordinateCounts;
	std::unordered_map<int, int> coordinateCounts2;

	for (int p = 0; p < coordinates.size(); ++p)
	{
		int key = makeKey(coordinates[p]);
		coordinateCounts.insert({ key, 0 });
	}
	
	for (int p = 0; p < coordinates.size(); ++p)
	{
		int key = makeKey(coordinates[p]);
		coordinateCounts2.insert({ key, 0 });
	}

	//Loop over x and y grid
	for (int i = minX; i < maxX; ++i)
	{
		for (int j = minY; j < maxY; ++j)
		{
			int mindistance = 5000;
			std::pair<int, int> closestcoordinate = std::make_pair(-1, -1);
			//Loop over the special coordinates and check distance:
			for (int k = 0; k < coordinates.size(); ++k)
			{
				int distance = abs(coordinates[k].first - i) + abs(coordinates[k].second - j);
				if (distance < mindistance)
				{
					mindistance = distance;
					closestcoordinate = coordinates[k];
				}
				else if (distance == mindistance)
				{
					closestcoordinate = std::make_pair(-1, -1);
				}
			}
			//After evaluating the point, add one point to the winning coordinate
			int key = makeKey(closestcoordinate);
			coordinateCounts[key] += 1;
		}
	}

	//Do the same but for a larger grid, to determine which coordinates go infinite
	for (int i = minX-50; i < maxX+50; ++i)
	{
		for (int j = minY-50; j < maxY+50; ++j)
		{
			int mindistance = 5000;
			std::pair<int, int> closestcoordinate = std::make_pair(-1, -1);
			//Loop over the special coordinates and check distance:
			for (int k = 0; k < coordinates.size(); ++k)
			{
				int distance = abs(coordinates[k].first - i) + abs(coordinates[k].second - j);
				if (distance < mindistance)
				{
					mindistance = distance;
					closestcoordinate = coordinates[k];
				}
				else if (distance == mindistance)
				{
					closestcoordinate = std::make_pair(-1, -1);
				}
			}
			//After evaluating the point, add one point to the winning coordinate
			int key = makeKey(closestcoordinate);
			coordinateCounts2[key] += 1;
		}
	}

	//Remove coordinates that go infinite
	for (auto key : coordinateCounts)
	{
		if (coordinateCounts[key.first] != coordinateCounts2[key.first])
		{
			coordinateCounts[key.first] = 0;
		}
	}

	//Find the remaining maximum area around a coordinate:
	int max = 0;
	int winningKey = 0;
	std::pair<int, int> winningcoordinate;
	for (auto a : coordinateCounts)
	{
		if (a.second > max)
		{
			max = a.second;
			winningKey = a.first;
		}	
	}

	//Determine coordinate:
	std::cout << max << std::endl;
	for (int i = 0; i < coordinates.size(); ++i)
	{
		if (makeKey(coordinates[i]) == winningKey)
		{
			winningcoordinate = coordinates[i];
			std::cout << coordinates[i].first << ", " << coordinates[i].second;
		}
	}

}

int Day6::makeKey(std::pair<int, int> paar)
{
	int x = paar.first;
	int y = paar.second;
	return x * 100 + y;
}


void Day6::performPart2()
{
	int maxX = x_values[std::distance(x_values.begin(), std::max_element(x_values.begin(), x_values.end()))]+50;
	int maxY = y_values[std::distance(y_values.begin(), std::max_element(y_values.begin(), y_values.end()))]+50;
	int minX = x_values[std::distance(x_values.begin(), std::min_element(x_values.begin(), x_values.end()))]-50;
	int minY = y_values[std::distance(y_values.begin(), std::min_element(y_values.begin(), y_values.end()))]-50;
	std::vector<std::vector<int> > gridcoords;
	
	gridcoords.resize(maxX - minX, std::vector<int>{});
	for (int i = 0; i < gridcoords.size(); ++i)
	{
		gridcoords[i].resize(maxY - minY, 0);
	}
	
	for (int i = 0; i < gridcoords.size(); ++i)
	{
		for (int j = 0; j < gridcoords[i].size(); ++j)
		{
			for (int k = 0; k < coordinates.size(); ++k)
			{
				int distance = abs(coordinates[k].first - i) + abs(coordinates[k].second - j);
				gridcoords[i][j] += distance;
			}
		}
	}

	int count = 0;

	for (int i = 0; i < gridcoords.size(); ++i)
	{
		for (int j = 0; j < gridcoords[i].size(); ++j)
		{
			if (gridcoords[i][j] < 10000)
			{
				count++;
			}
		}
	}

	std::cout << std::endl << count;

}


