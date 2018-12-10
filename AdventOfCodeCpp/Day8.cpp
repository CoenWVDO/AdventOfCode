#include "pch.h"
#include "Day8.h"
#include <iostream>
#include <fstream>
#include <array>
#include <algorithm>
#include <memory>
#include <numeric>
#include <stdexcept>
#include <vector>

Day8::Day8(std::string datalocation)
{
	std::ifstream fileread(datalocation);
	std::string line;

	if (fileread.is_open())
	{
		while (getline(fileread, line, ' '))
		{
			data.push_back(stoi(line));
		}
	}
}




Day8::~Day8()
{
}

void Day8::calcSum()
{
	int metaDataSum = 0;
	std::deque<int> childrenPerNode;
	std::deque<int> metaData;
	bool done = false;
	int counter = 0;
	int currentNode = 0;
	std::array<int, 10000> nodeValues;
	nodeValues.fill(0);
	std::vector<std::vector<int> > nodeChildren;

	for (int pointer = 0; pointer < data.size(); ++pointer)
	{
		if (childrenPerNode.size() > 0 && metaData.size() > 0)
		{
			while (childrenPerNode[0] == 0 && metaData[0] == 0)
			{
				childrenPerNode.pop_front();
				metaData.pop_front();
			}
		}
		if (pointer != 0 && childrenPerNode.size() == 0 && metaData.size() == 0)
		{
			counter == 0;
		}

		int currentData = int(data[pointer]);

		if (counter == 0)
		{
			int children = currentData;
			childrenPerNode.push_front(children);
			counter++;
		}
		else if (counter == 1)
		{
			int nrMetaData = currentData;
			metaData.push_front(nrMetaData);
			counter++;
		}
		else if (counter == 2)
		{
			if (childrenPerNode.size() > 0 && childrenPerNode[0] != 0)
			{
				counter = 1;
				childrenPerNode[0]--;
				childrenPerNode.push_front(currentData);
			}

			//If current node has no children:
			else if (metaData.size() > 0 && metaData[0] > 0)
			{
				metaDataSum += currentData;
				if (--metaData[0] == 0)
				{
					//MetaData of current node done
					metaData.pop_front();
					childrenPerNode.pop_front();

					if (childrenPerNode.size() != 0 && childrenPerNode[0] == 0)
					{
						counter = 2;
					}
					else if (childrenPerNode.size() != 0)
					{
						childrenPerNode[0]--;
						counter = 0;
					}

					if (childrenPerNode.size() == 0)
					{
						continue;
					}					
				}
			}
		}
	}
	std::cout << metaDataSum;	
}


struct node
{
	std::vector<int> metadata;
	std::vector<std::unique_ptr<node> > children;
	node(int nmeta, int nchildren)
	{
		metadata.reserve(nmeta);
		children.reserve(nchildren);
	}
};



void Day8::part2()
{
	std::deque<int> childrenPerNode;
	std::deque<int> metaData;
	int counter = 0;
	int currentNode = 1;
	int nr_nodes = 1;
	std::array<int, 10000> nodeValues;
	nodeValues.fill(0);
	std::vector<std::vector<int> > nodeChildren;
	std::vector<int> parentNodes;
	parentNodes.resize(10000);
	nodeChildren.resize(10000);

	for (int pointer = 0; pointer < data.size(); ++pointer)
	{
		if (childrenPerNode.size() > 0 && metaData.size() > 0)
		{
			while (childrenPerNode[0] == 0 && metaData[0] == 0)
			{
				childrenPerNode.pop_front();
				metaData.pop_front();
				currentNode = parentNodes[currentNode];
			}
		}
		if (pointer != 0 && childrenPerNode.size() == 0 && metaData.size() == 0)
		{
			counter == 0;
		}

		int currentData = int(data[pointer]);

		if (counter == 0)
		{
 			int children = currentData;
			int temp = nr_nodes;
			for (int i = nr_nodes; i < temp + children; ++i)
			{
				nodeChildren[currentNode].push_back(i+1);
				parentNodes[i + 1] = currentNode;
				nr_nodes++;
			}
			childrenPerNode.push_front(children);
			counter++;
		}
		else if (counter == 1)
		{
			int nrMetaData = currentData;
			metaData.push_front(nrMetaData);
			counter++;
		}
		else if (counter == 2)
		{
 			if (childrenPerNode.size() > 0 && childrenPerNode[0] != 0)
			{
				int size = nodeChildren[currentNode].size();
				currentNode = nodeChildren[currentNode][size - childrenPerNode[0]];
				counter = 0;
				pointer--;
				childrenPerNode[0]--;
				//childrenPerNode.push_front(currentData);
			}

			//If current node has no children:
			else if (metaData.size() > 0 && metaData[0] > 0)
			{
				if (nodeChildren[currentNode].size() > 0)
				{
					if (currentData <= nodeChildren[currentNode].size())
					{
						nodeValues[currentNode] += nodeValues[nodeChildren[currentNode][currentData-1]];
					}
				}
				else
				{
					nodeValues[currentNode] += currentData;
				}

				if (--metaData[0] == 0)
				{
					//MetaData of current node done
					currentNode = parentNodes[currentNode];
					metaData.pop_front();
					childrenPerNode.pop_front();

					if (childrenPerNode.size() != 0 && childrenPerNode[0] == 0)
					{
						counter = 2;
					}
					else if (childrenPerNode.size() != 0)
					{
						int size = nodeChildren[currentNode].size();
						currentNode = nodeChildren[currentNode][size - childrenPerNode[0]];
						childrenPerNode[0]--;
						counter = 0;
					}

					if (childrenPerNode.size() == 0)
					{
						continue;
					}
				}
			}
		}
	}
	std::cout << nodeValues[1];
}
