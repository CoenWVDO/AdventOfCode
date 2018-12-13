#include "pch.h"
#include "Day9.h"
#include <vector>
#include <iostream>
#include <list>

Day9::Day9()
{
}


Day9::~Day9()
{
}

void Day9::winnerPoints()
{
	//Nr of players is 404
	scores.fill(0);
	//Last marble is worth 71852 polong longs, so then we stop.
	std::list<long long> circleList;
	std::vector<long long> circle;
	long long marbleCounter = 0;
	long long indexOfActiveMarble = 0;
	long long indexOfActiveMarble2 = 0;
	bool stop = false;

	long long counter = 0;
	while (!stop)
	{
		for (long long i = 0; i < scores.size(); ++i)
		{
			indexOfActiveMarble = placeMarble(marbleCounter, indexOfActiveMarble, circle, i);		//passing circle by reference;
			marbleCounter++;
			if (marbleCounter > 1000)
			{
				long long max = 0;
				for (long long i = 0; i < scores.size(); ++i)
				{
					if (scores[i] > max)
					{
						max = scores[i];
					}
				}
				stop = true;
				break;
			}

			long long max = 0;
			for (long long i = 0; i < scores.size(); ++i)
			{
				if (scores[i] > max)
				{
					max = scores[i];
				}
			}
			/*
			long long max2 = 0;
			for (long long i = 0; i < scores2.size(); ++i)
			{
				if (scores2[i] > max2)
				{
					max2 = scores2[i];
				}
			}
			winningscore2.push_back(max2);
			*/
 			winningscore.push_back(max);
			std::cout << "Score for " << counter + 1 << " marbles: " << winningscore[counter] << std::endl;
			counter++;
		}
	}
}


void Day9::part2(int players, long long lastmarble)
{
	//Nr of players is 404
	scores2.resize(players, 0);
	//Last marble is worth 7185200 polong longs, so then we stop.
	std::list<long long> circleList;
	std::list<long long>::iterator currentmarble;
	long long marbleCounter = 0;
	bool stop = false;

	long long counter = 0;
	while (!stop)
	{
		for (long long i = 0; i < scores2.size(); ++i)
		{
			currentmarble = placeMarble2(marbleCounter, currentmarble, circleList, i);		//passing circle by reference;
			marbleCounter++;
			if (marbleCounter > lastmarble)
			{
				long long max = 0;
				for (long long i = 0; i < scores2.size(); ++i)
				{
					if (scores2[i] > max)
					{
						max = scores2[i];
					}
				}
				std::cout << "Winning score for 7185200 marbles: " << max << std::endl;
				stop = true;
				break;
			}

			/*
			long long max = 0;
			for (long long i = 0; i < scores2.size(); ++i)
			{
				if (scores2[i] > max)
				{
					max = scores2[i];
				}
			}
			winningscore2.push_back(max);
			std::cout << "Score for " << counter + 1 << " marbles: " << winningscore2[counter] << std::endl;
			*/
			
			counter++;
		}
	}
}

long long Day9::placeMarble(long long marbleCounter, long long index, std::vector<long long>& circle, long long player)
{

	if (marbleCounter > 0 && marbleCounter % 23 == 0)
	{
		scores[player] += marbleCounter;
		long long removeMarbleIndex = index - 7;
		if (removeMarbleIndex < 0)
		{
			removeMarbleIndex = circle.size() + removeMarbleIndex;
		}
		scores[player] += circle[removeMarbleIndex];
		circle.erase(circle.begin() + removeMarbleIndex);
		return removeMarbleIndex;
	}
	if (marbleCounter == 0)
	{
		circle.push_back(marbleCounter);
		return 0;
	}
	else if (marbleCounter == 1)
	{
		circle.push_back(marbleCounter);
		return 1;
	}
	else
	{
		long long newindex = index + 2;
		if (newindex == circle.size())
		{
			circle.push_back(marbleCounter);
			return newindex;
		}
		else if (newindex == circle.size() + 1)
		{
			circle.insert(circle.begin() + 1, marbleCounter);
			return 1;
		}
		else
		{
			circle.insert(circle.begin() + newindex, marbleCounter);
			return newindex;
		}
	}
}


std::list<long long>::iterator Day9::placeMarble2(long long marbleCounter, std::list<long long>::iterator index, std::list<long long>& circle, long long player)
{

	if (marbleCounter > 0 && marbleCounter % 23 == 0)
	{
		scores2[player] += marbleCounter;
		for (long long i = 0; i < 7; ++i)
		{
			if (index == circle.begin())
			{
				index = circle.end();
				index--;
			}
			else
			{
				--index;
			}
		}
		scores2[player] += *index;

		std::list<long long>::iterator temp = index;
		if (index != circle.begin())
		{
			temp--;
			circle.erase(index);
			temp++;
			return temp;
		}
		else
		{
			circle.erase(index);
			return circle.begin();
		}
	}

	if (marbleCounter == 0)
	{
		circle.push_back(marbleCounter);
		return circle.begin();
	}

	else if (marbleCounter == 1)
	{
		circle.push_back(marbleCounter);
		return (++circle.begin());
	}

	else
	{
		for (long long i = 0; i < 2; ++i)
		{
			if (index == circle.end())
			{
				index = circle.begin();
				index++;
			}
			else
			{
				index++;
			}
		}
		circle.insert(index, marbleCounter);
		return --index;
	}
}