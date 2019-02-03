#include "stdafx.h"
#include <iostream>
#include <random>
#include <array>
#include <vector>
#include <algorithm>
#include <chrono>

using namespace std;

constexpr size_t NumOfPoints = 100; // amount of points in data
constexpr size_t rangeOfNumbers = 100;//range of the random numbers

class Point
{
public:
	explicit Point() = default;//default constructor and default values are inserted in the variables
	explicit Point(int x, int y) : _x(x), _y(y) {}//constructor
	//basic getter and setters
	int getX() const 
	{
		return _x;
	}
	int getY() const 
	{
		return _y;
	}
	void setX(int x) 
	{
		_x = x;
	}
	void setY(int y) 
	{
		_y = y;
	}
	//Assigment opperator
	Point& operator=(const Point& other)
	{
		_x = other._x;
		_y = other._y;

		return *this;
	}
	//equality opperator
	bool operator==(const Point& other) const
	{
		return _x == other._x && _y == other._y;
	}
	//inequality opperator
	bool operator!=(const Point& other) const
	{
		return !(*this == other);
	}
	//calculate distance via euclidian distance
	int operator-(const Point& other) const
	{
		int dx = _x - other._x;
		dx *= dx;

		int dy = _y - other._y;
		dy *= dy;

		return static_cast<int>(sqrt(dx + dy));
	}

private:
	int _x;
	int _y;
};

using Cluster = vector<Point>;
using ConstCluster = array<Point, NumOfPoints>;

ostream& operator<<(ostream& out, const Point& point)
{
	out << "X " << point.getX() << " Y " << point.getY() << "\t";

	return out;
}

Point getAveragePoint(const Cluster& cluster)
{
	if (cluster.size() == 0) return Point(0, 0);

	int sumOfX = 0;
	int sumOfY = 0;

	for (const auto& point : cluster)
	{
		sumOfX += point.getX();//sum all of x coordinates
		sumOfY += point.getY();//sum all of y coordinates
	}

	// Calculate the center average coordinates
	return Point(sumOfX / cluster.size(), sumOfY / cluster.size());
}

void printData(const Cluster& k1, const Point& m1, const Cluster& k2, const Point& m2,const Cluster& k3, const Point& m3)
{
	cout << "\nCluster 1:\n";
	for (const auto& point : k1)
	{
		cout << point;
	}
	cout << "\n\nCenter 1 = " << m1;
	cout << "\n\nCluster 2:\n";
	for (const auto& point : k2)
	{
		cout << point;
	}
	cout << "\n\nCenter 2 = " << m2;
	cout << "\nCluster 3:\n";
	for (const auto& point : k3)
	{
		cout << point;
	}
	cout << "\n\nCenter 3 = " << m3;
	cout << "\n ----";
}

int main()
{
	const auto tStart = chrono::high_resolution_clock::now();//to calculate the time of the execution - start timer
	size_t numberOfIterations = 0;

	ConstCluster k0;
	Cluster k1;
	Cluster k2;
	Cluster k3;

	random_device rd;
	mt19937 gen(rd());
	std::uniform_int_distribution<> rnd(1ul, rangeOfNumbers);

	cout << "\nNumber of points is " << NumOfPoints << ":\n";

	generate(begin(k0), end(k0), [&rnd, &gen]() { return Point(rnd(gen), rnd(gen)); });

	//initial centers
	Point m1(rnd(gen), rnd(gen));
	Point m2(rnd(gen), rnd(gen));
	Point m3(rnd(gen), rnd(gen));
	//old centers
	Point om1;
	Point om2;
	Point om3;
	do
	{
		k1.clear();
		k2.clear();
		k3.clear();
		//saving old centers
		om1 = m1;
		om2 = m2;
		om3 = m3;
		//creating clusters
		for (int i = 0; i < k0.size(); i++) {
			int d1 = k0[i] - m1;
			int d2 = k0[i] - m2;
			int d3 = k0[i] - m3;
			int minimunDistance = std::min(std::min(d1, d2),d3);
			if (minimunDistance == d1) {
				k1.push_back(k0[i]);
			}
			else if (minimunDistance == d2) {
				k2.push_back(k0[i]);
			}
			else {
				k3.push_back(k0[i]);
			}
		}
		
		

		//calculating new center
		m1 = getAveragePoint(k1);
		m2 = getAveragePoint(k2);
		m3 = getAveragePoint(k3);
		//printing clusters
		printData(k1, m1, k2, m2,k3,m3);
		++numberOfIterations;
	} while ((m1 != om1 && m2 != om2&& m3 != om3)||(numberOfIterations==40));

	chrono::duration<double, ratio<1>> elapsed_time = chrono::high_resolution_clock::now() - tStart;
	cout << "\n\nTime taken: " << elapsed_time.count() << " sec\n";
	cout << "Number of iterations was : " << numberOfIterations << "\n";

	return 0;
	//ending
}
