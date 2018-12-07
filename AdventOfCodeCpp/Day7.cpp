#include "pch.h"
#include "Day7.h"
#include <fstream>
#include <iostream>
#include <algorithm>
#include "Worker.h"


Day7::Day7(std::string dataloc)
{
	std::ifstream inputstream(dataloc);
	std::string line;
	std::vector<char> chars = { 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
		'S','T','U','V','W','X','Y', 'Z' };
	for (char c : chars)
	{
		map.insert(std::make_pair(c, std::vector<char>{}));
	}

	if (inputstream.is_open())
	{
		while (getline(inputstream, line))
		{
			char before = line[5];
			char after = line[36];
			if (map.find(after) == map.end())
			{
				std::cout << "Can't find entry in map, error?? Lost key: " << after << std::endl;
			}
			else
			{
				map.at(after).push_back(before);
			}
		}
	}
}


Day7::~Day7()
{
}

void Day7::perform()
{
	std::string stepOrder = "";
	while (map.size() > 0)
	{
		char nextStep;
		for (std::pair<char, std::vector<char> > i : map)
		{
			if (i.second.size() == 0)
			{
				nextStep = i.first;
				break;
			}
		}
		for (std::pair<char, std::vector<char> > i : map)
		{
			auto it = std::find(map[i.first].begin(), map[i.first].end(), nextStep);
			if (it != map[i.first].end())
			{
				map[i.first].erase(it);
			}
		}
		stepOrder += nextStep;
		map.erase(nextStep);
	}

	std::ofstream outputday7("outputDay7.txt");
	if (outputday7.is_open())
	{
		outputday7 << stepOrder;
		outputday7.close();
	}
}


void Day7::performPart2()
{
	Worker worker0;
	Worker worker1;
	Worker worker2;
	Worker worker3; 
	Worker worker4;
	std::vector<Worker*> workers = {&worker0, &worker1, &worker2, &worker3, &worker4};

	int totalseconds = 0;
	bool allfinished = false;

	while (!(map.size() == 0 && allfinished))
	{
		std::vector<int> availableWorkers;
		for (int i = 0; i < workers.size() ; ++i)
		{
			if (!(workers[i]->isBusy()))
			{
				availableWorkers.push_back(i);
			}
		}

		std::vector<char> jobsStarted = {};
		for (std::pair<char, std::vector<char> > i : map)
		{
			if (availableWorkers.size() == 0)
			{
				break;
			}

			if (i.second.size() == 0)
			{
				int worker = availableWorkers.back();
				availableWorkers.pop_back();
				workers[worker]->startJob(i.first);
				jobsStarted.push_back(i.first);
			}		
		}

		for (char c : jobsStarted)
		{
			map.erase(c);
		}

		for (Worker* w : workers)
		{
			bool finishedJob = w->doCycle();
			if (finishedJob)
			{
				char job = w->getJob();
				for (std::pair<char, std::vector<char> > i : map)
				{
					auto it = std::find(map[i.first].begin(), map[i.first].end(), job);
					if (it != map[i.first].end())
					{
						map[i.first].erase(it);
					}
				}
			}
		}
		allfinished = true;
		for (Worker* w : workers)
		{
			if (w->isBusy())
			{
				allfinished = false;
			}
		}

		totalseconds++;
	}
	std::cout << "Total seconds: " << totalseconds << std::endl;
}