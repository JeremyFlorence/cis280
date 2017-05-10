#!/usr/bin/perl
# Names: Jeremy Florence, Christopher Tang
# Course: CIS 280 - Perl
# Assignment: CGI Project
# Due: 5/10/17
# 
# This program allows the user to calculate what they must score on their final exam in order
# to achieve a grade that they specify. There are 8 text fields for entering points earned in specific grade
# categories, but it is not required to fill out all of these if there are less than 8 grading categories
# in a class.

use warnings;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI qw( :standard );
use Scalar::Util qw(looks_like_number);

print( header() );
print( start_html( "Required Exam Grade" ) );

print (h1 ("Required Final Exam Grade calculator"));
print (h2 ("A tool to calculate what you need to score on your final in order to get a certain grade"));
print "Please enter the points you have earned in each category according to your syllabus, the weight of the final exam, and your desired grade.";

my @points = param( "points[]" );
my $exam_weight = param( "exam_weight" );
my $desired_grade = param( "desired_grade" );

if (param) {

    # We want to make sure that use input is valid
    my $valid_form = validateForm(\@points, $exam_weight, $desired_grade);
    if ($valid_form) {
        my $required_grade = calculateRequiredExamGrade(\@points, $exam_weight, $desired_grade);
        print "You need a final exam grade of $required_grade in order to get a final grade of $desired_grade";
    } else {
        # If it's not valid, reprompt them
        print br(), "Invalid input";
        CategoryScoreForm();
    }

} else {
    CategoryScoreForm();
}

print( end_html() );

# Form for entering earned points, exam weight, and desired grade
sub CategoryScoreForm {
    print( start_form(),
            "Category 1 points: ", textfield( -name => "points[]" ), br(),
            "Category 2 points: ", textfield( -name => "points[]" ), br(),
            "Category 3 points: ", textfield( -name => "points[]" ), br(),
            "Category 4 points: ", textfield( -name => "points[]" ), br(),
            "Category 5 points: ", textfield( -name => "points[]" ), br(),
            "Category 6 points: ", textfield( -name => "points[]" ), br(),
            "Category 7 points: ", textfield( -name => "points[]" ), br(),     
            "Category 8 points: ", textfield( -name => "points[]" ), br(),
            "Final exam weight: ", textfield( -name => "exam_weight" ),
            "Desired Grade: ", textfield( -name => "desired_grade" ),
            

			br(), submit( "Calculate" ),
			end_form() );
}

# Calculates the required final exam grade
sub calculateRequiredExamGrade {
    my ($points, $exam_weight, $desired_grade) = @_;

    my $point_sum = 0;
    foreach my $score (@$points) {
        $point_sum += $score;
    }

    my $required_grade = (($desired_grade - $point_sum) / $exam_weight)*100;
    return $required_grade;
}

# Checks to see if the user input is valid
sub validateForm {
    my ($points, $exam_weight, $desired_grade) = @_;

    if (looks_like_number($desired_grade)) {
        if ($desired_grade > 100) {
            return 0;
        }
    } else {
        return 0;
    }

    return 1;    
}