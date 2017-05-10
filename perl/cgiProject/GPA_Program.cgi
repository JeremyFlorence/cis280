#!/usr/bin/perl
# Names: Jeremy Florence, Christopher Tang
# Course: CIS 280 - Perl
# Assignment: CGI Project
# Due: 5/10/17
# 
# This program allows a user to enter their courses for a semester, the credits for those courses,
# and the grades they expect to earn for those courses (on the 4.0 scale), and will calculate the
# cumulative gpa they will have with those grades.

use warnings;
use strict;
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use CGI qw( :standard );

print( header() );
#This is what the title of tab is called
print( start_html( "GPA Calculator" ) );

#Parameters for the list of courses, credit hours, and gpa's'
my @courses = param('Courses');
my @creditHours = param('Credit Hours');
my @gpa = param('GPA');

print( h1( "GPA Calculator" ) );
print( h2( "A simple GPA calculator") );
if(param){
    if(validateCreditHours(@creditHours)){
        print('Error, you entered a non-numerical value into credit hours. Please fill out the table again.');
        gpaForm();
    }
    if(validateGPA(@gpa)){
        print('Error, you entered a non-numerical value into GPA. Please fill out the table again.');
        gpaForm();
    }
    calculateGPA(\@courses, \@creditHours, \@gpa);
}else{
    gpaForm();
    calculateGPA(\@courses, \@creditHours, \@gpa);    
}
print( end_html() );

#Form for filling out courses, credit hours, and GPA for each course to calculate overall GPA
sub gpaForm {
	print( start_form(), '<table width="50%" border="10">', 
            Tr( th( "Courses" ), th( "Credit Hours" ), th("GPA") ), 
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ),  
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ), 
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ), 
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ), 
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ), 
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ), 
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ), 
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ), 
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ), 
            Tr( td( textfield('Courses','-Enter Course Here-', 50, 80) ),
                td( textfield('Credit Hours', '-Enter Credit Hours Here-', 20, 20) ), 
                td( textfield('GPA', '-Enter GPA Here-', 20, 20) ) ),                                 
            '</table>', br(), submit( "Calculate GPA" ),
			end_form() );
}

#Loop through list of Credit Hours and check to see if what the user entered
#is not valid
sub validateCreditHours {
    my @creditHours = @_;
    foreach my $value (@creditHours){
        if($value =~ /^\D*$/){
            return 1;
        }else{
            return 0;
        }
    }
}

#Loop through list of GPA's and check to see if a GPA is not valid
sub validateGPA {
    my @gpa = @_;
    foreach my $value (@gpa){
        if($value !~ /^[0-3]\.\d|4\.0$/){
            return 1;
        }else{
            return 0;
        }
    }
}

#Calculate the GPA by looping through the list of GPA's assuming both the list of GPA's
#and Credit Hours are the same, totalling the quality points, totalling the credit hours, 
#then calculating the GPA by dividing quality points by total credit hours.
sub calculateGPA {
    #List of credit hours and gpa
    my ($courses, $creditHours, $gpa) = @_;
    
    #Total quality points earned
    my $totalQualityPoints;

    #Total credit hours
    my $totalCreditHours;

    #GPA
    my $grade;

    #Loop to calculate total quality points earned
    for(my $i = 0; $i < scalar @$gpa; $i++){
        $totalQualityPoints += @$creditHours[$i] * @$gpa[$i];
    }
    
    #Loop to calculate total credit hours
    for(my $i = 0; $i < scalar @$creditHours; $i++){
        $totalCreditHours += @$creditHours[$i];
    }

    #Check for division by 0
    if($totalCreditHours != 0){
        print('<table width="50%" border="10">', 
            Tr( th( "Courses" ), th( "Credit Hours" ), th("GPA") ), 
            Tr( td( @$courses[0] ),
                td( @$creditHours[0] ), 
                td( @$gpa[0] )),  
            Tr( td( @$courses[1] ),
                td( @$creditHours[1] ), 
                td( @$gpa[1] )), 
            Tr( td( @$courses[2] ),
                td( @$creditHours[2] ), 
                td( @$gpa[2] )), 
            Tr( td( @$courses[3] ),
                td( @$creditHours[3] ), 
                td( @$gpa[3] )), 
            Tr( td( @$courses[4] ),
                td( @$creditHours[4] ), 
                td( @$gpa[4] )), 
            Tr( td( @$courses[5] ),
                td( @$creditHours[5] ), 
                td( @$gpa[5] )), 
            Tr( td( @$courses[6] ),
                td( @$creditHours[6] ), 
                td( @$gpa[6] )), 
            Tr( td( @$courses[7] ),
                td( @$creditHours[7] ), 
                td( @$gpa[7] )), 
            Tr( td( @$courses[8] ),
                td( @$creditHours[8] ), 
                td( @$gpa[8] )), 
            Tr( td( @$courses[9] ),
                td( @$creditHours[9] ), 
                td( @$gpa[9] )),                                 
            '</table>');
        print(br());
        print('Your GPA is ');
        #Display GPA only up to 2 decimal point digits 
        printf("%.2f", $totalQualityPoints / $totalCreditHours);
    }
}