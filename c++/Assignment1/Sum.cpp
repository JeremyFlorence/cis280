/*
	Name: Jeremy Florence
	Course: CIS 280 - Selected Languages
	Assignment: 1
	Due: 2/2/2017
*/

/*
	This program prompts the user to enter 10 integers upon which the following
	calculations are performed and displayed as output in the terminal:
		- The sum and average of the positive numbers
		- The sum and average of the non-positve numbers
		- The sum and average of all  of the numbers
*/

#include <iostream>
using namespace std;

int main() {
	int counter = 0;
	int pos_count = 0;	// Counts the number of positive numbers
	int neg_count = 0;	// Counts the number of non-positive numbers
	int pos_sum = 0;	// The sum of the positive numbers
	int neg_sum = 0;	// The sum of the non-positive numbers
	int total_sum = 0; // The sum of all the numbers

	while (counter < 10) {
		int input;
		cout << "Please enter a number: " << endl;
		cin >> input;
		if (cin.fail()) {
			cout << "ERROR: That was not a number." << endl;
			cin.clear();
			cin.ignore(1000, '\n');
			continue;
		}

		if (input > 0) {
			pos_sum += input;
			pos_count++;
		} else {
			neg_sum += input;
			neg_count++;
		}

		total_sum += input;
		counter++;
	}

	cout << "The sum of the positive numbers is: " << pos_sum << endl;
	cout << "The average of the positive numbers is: ";
	cout <<	(double)pos_sum / pos_count << endl;
	cout << "The sum of the non-positive numbers is: " << neg_sum << endl;
	cout << "The average of the non-positive numbers is: ";
	cout << (double)neg_sum / neg_count << endl;
	cout << "The sum of all the numbers is: " << total_sum << endl;
	cout << "The average of all the numbers is: ";
	cout << (double)total_sum / 10 << endl;



	return 0;
}
