// File: main.cpp
// Testing program for Rational class
/*
 * Name: Jeremy Florence
 * Course: CIS 280
 * Assignment: 3
 * Date: 3/14/17
*/

#include <iostream>
#include "rational.h"

using namespace std;

int main() {
	
    cout << "Testing declarations" << endl;
	cout << "Rational x, y(2), z(-5,-6), w(1,-3);" << endl;
	Rational x, y(2), z(-5,-6), w(1,-3);
	cout << "x = " << x << ", y = " << y << ", z = " << z
				<< ", w = " << w << endl;
	cout << "Enter "
		<< "a fraction in the format "
		<< "integer_numerator/integer_denominator"
		<< endl;
	cin >> x;
	cout << "You entered the equivalent of: " << x << endl;
	cout << "Testing the constructor and normalization routines: " << endl;
	y =Rational(-128, -48);
	cout << "y =Rational(-128, -48) outputs as " << y << endl;
	y =Rational(-128, 48);
	cout << "y =Rational(-128, 48)outputs as " << y << endl;
	y = Rational(128,-48);
	cout << "y = Rational(128, -48) outputs as " << y << endl;
	Rational a(1,1);
	cout << "Rational a(1,1); a outputs as: " << a << endl;

	
	w = Rational(25,9);
	z = Rational(3,5);
	cout << "Testing arithmetic and relational "
		<< " operator overloading" << endl;
	
	cout << w << " * " << z << " = " << (w*z) << endl;
	cout << w << " + " << z << " = " << (w+z) << endl;
	cout << w << " - " << z << " = " << (w-z) << endl;
	cout << w << " / " << z << " = " << (w/z) << endl;
	cout << w << " < " << z << " = " << (w<z) << endl;
	cout << w << " < " << w << " = " << (w<w) << endl;
	cout << w << " == "	<< w << " = " << (w==w) << endl;

	w = Rational(-21,9);
	z = Rational(3,5);
	cout << w << " * " << z << " = " << (w*z) << endl;
	cout << w << " + " << z << " = " << (w+z) << endl;
	cout << w << " - " << z << " = " << (w-z) << endl;
	cout << w << " / " << z << " = " << (w/z) << endl;
	cout << w << " < " << z << " = " << (w<z) << endl;
	cout << w << " < " << w << " = " << (w<w) << endl;
	cout << w << " <= " << z << " = " << (w<=z) << endl;
	cout << w << " <= " << w << " = " << (w<=w) << endl;
	cout << z << " <= " << w << " = " << (z<=w) << endl;

	cout << neg(w) << " neg " << " = " << neg(neg(w)) << endl;
	cout << w << " neg " << " = " << neg(w) << endl;

	w = Rational(-5,4);
	z = Rational(1,2);
	cout << w << " < " << z << " = " << (w<z) << endl;
	cout << w << " < " << w << " = " << (w<w) << endl;
	cout << w << " <= " << z << " = " << (w<=z) << endl;
	cout << w << " <= " << w << " = " << (w<=w) << endl;
	cout << z << " <= " << w << " = " << (z<=w) << endl;
	cout << w << " > " << z << " = " << (w>z) << endl;
	cout << w << " >= " << z << " = " << (w>=z) << endl;
	cout << w << " >= " << w << " = " << (w>=w) << endl;
	cout << z << " >= " << w << " = " << (z>=w) << endl;
	

    return 0;
}