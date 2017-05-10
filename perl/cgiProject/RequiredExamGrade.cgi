#!/usr/bin/perl

use warnings;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI qw( :standard );
use Scalar::Util qw(looks_like_number);

print( header() );
print( start_html( "Required Exam Grade" ) );

my @categories = param( "categories[]" );
my @weights = param( "weights[]" );
my @points = param( "points[]" );
my $exam_weight = param( "exam_weight" );
my $desired_grade = param( "desired_grade" );

if (param) {
    print "Categories: @categories", br(), " Weights: @weights", br(),  "Points: @points";
    my $valid_form = validateForm(\@categories, \@weights, \@points, $exam_weight, $desired_grade);
    if ($valid_form) {
        print br(), "The form is valid!";
    } else {
        print br(), "Invalid input";
        CategoryScoreForm();
    }

} else {
    CategoryScoreForm();
}

print( end_html() );

sub CategoryScoreForm {
    print( start_form(),
            "Category 1: ", textfield( -name => "categories[]" ),
            "Category 1 weight: ", textfield( -name => "weights[]" ),
            "Category 1 points: ", textfield( -name => "points[]" ), br(),

            "Category 2: ", textfield( -name => "categories[]" ),
            "Category 2 weight: ", textfield( -name => "weights[]" ),
            "Category 2 points: ", textfield( -name => "points[]" ), br(),


            "Category 3: ", textfield( -name => "categories[]" ),
            "Category 3 weight: ", textfield( -name => "weights[]" ),
            "Category 3 points: ", textfield( -name => "points[]" ), br(),

            "Category 4: ", textfield( -name => "categories[]" ),
            "Category 4 weight: ", textfield( -name => "weights[]" ),
            "Category 4 points: ", textfield( -name => "points[]" ), br(),

            "Category 5: ", textfield( -name => "categories[]" ),
            "Category 5 weight: ", textfield( -name => "weights[]" ),
            "Category 5 points: ", textfield( -name => "points[]" ), br(),

            "Category 6: ", textfield( -name => "categories[]" ),
            "Category 6 weight: ", textfield( -name => "weights[]" ),
            "Category 6 points: ", textfield( -name => "points[]" ), br(),

            "Category 7: ", textfield( -name => "categories[]" ),
            "Category 7 weight: ", textfield( -name => "weights[]" ),
            "Category 7 points: ", textfield( -name => "points[]" ), br(),

            "Category 8: ", textfield( -name => "categories[]" ),           
            "Category 8 weight: ", textfield( -name => "weights[]" ),      
            "Category 8 points: ", textfield( -name => "points[]" ), br(),

            "Final exam weight: ", textfield( -name => "exam_weight" ),
            "Desired Grade: ", textfield( -name => "desired_grade" ),
            

			br(), submit( "Calculate" ),
			end_form() );
}

sub validateForm {
    my ($categories, $weights, $points, $exam_weight, $desired_grade) = @_;
    if (scalar @$categories != scalar @$weights || scalar @$categories != scalar @$points || scalar @$weights != scalar @$points) {
        return 0;
    }

    my $weight_sum = 0;
    foreach my $weight (@$weights) {
        if(looks_like_number($weight)) {
            $weight_sum += $weight;
        } else {
            return 0;
        }
    }

    if ($weight_sum != 100) {
        return 0;
    }

    return 1;



    
}