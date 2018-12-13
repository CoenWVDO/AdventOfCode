#include "pch.h"
#include "Day10.h"
#include <iostream>
#include <fstream>
#include <array>


Day10::Day10(std::string datalocation)
{
	std::fstream fileread(datalocation);
	std::string line;

	if (fileread.is_open())
	{
		while (getline(fileread, line))
		{
			coordinates.push_back(line);
		}
	}

}


Day10::~Day10()
{
}


struct Point
{
	int xPos;
	int yPos;
	int xSpeed;
	int ySpeed;

	void passTime(int time)
	{
		this->xPos = xPos + time * xSpeed;
		this->yPos = yPos + time * ySpeed;
	}
};


void Day10::findMessage(int startSec, int endSec)
{
	std::vector<Point> points;

	for (std::string line : coordinates)
	{
		Point point;
		point.xPos = stoi(line.substr(10,6));
	    point.yPos = stoi(line.substr(18,6));
		point.xSpeed = stoi(line.substr(36, 2));
		point.ySpeed = stoi(line.substr(40, 2));
		points.push_back(point);
	}

	//Command window width on current monitor
	for (int i = 0; i < 237; i++)
	{
		std::cout << "X";
	}

	for (Point& p : points)
	{
		p.passTime(startSec);
	}


	int maxX = 0;
	int minX = 0;
	int maxY = 0;
	int minY = 0;
	for (int i = 0; i < (endSec - startSec); ++i)
	{
		for (Point& p : points)
		{
			p.passTime(1);
		}

		for (const Point& p : points)
		{
			if (p.xPos > maxX)
			{
				maxX = p.xPos;
			}
			if (p.yPos > maxY)
			{
				maxY = p.yPos;
			}
			if (p.xPos < minX)
			{
				minX = p.xPos;
			}
			if (p.yPos < minY)
			{
				minY = p.yPos;
			}
		}

		std::cout << "For " << startSec + i << " seconds, minX - maxX (diff), minY - maxY (diff)  --- SUM: " << minX << " - " << maxX
			<< " (" << maxX - minX << ")" << ", " << minY << " - " << maxY << " (" << maxY - minY << ")" <<  
			" --- " << maxX - minX + maxY - minY << std::endl;

		if (startSec + i == 10406)
		{
			break;
		}
	}

	//10406 is minimum distance between all points:

	minX = 10000;
	minY = 10000;

	for (const Point& p : points)
	{
		if (p.xPos > maxX)
		{
			maxX = p.xPos;
		}
		if (p.yPos > maxY)
		{
			maxY = p.yPos;
		}
		if (p.xPos < minX)
		{
			minX = p.xPos;
		}
		if (p.yPos < minY)
		{
			minY = p.yPos;
		}
	}

	for (Point& p : points)
	{
		p.xPos = p.xPos - minX;
		p.yPos = p.yPos - minY;
	}

	std::array<std::array<bool, 237>, 237> output;
	for (int i = 0; i < output.size(); ++i)
	{
		output[i].fill(false);
	}

	for (const Point& p : points)
	{
		output[p.xPos][p.yPos] = true;
	}

	for (int i = 0; i < output.size(); ++i)
	{
		for (int j = 0; j < output[i].size(); ++j)
		{
			if (output[j][i])
			{
				std::cout << "X";
			}
			else
			{
				std::cout << " ";
			}
		}
	}



}


