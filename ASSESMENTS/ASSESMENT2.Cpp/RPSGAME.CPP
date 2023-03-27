/***************************************
    	alphabetacoder.com
C++ program for simple rock paper scissor
game by playing completely random move
****************************************/
#include<iostream>
#include<cstdlib>
#include<ctime>

using namespace std;

int main() {
    // feed time as random seed
    srand(time(0));

    // declare variables
    int computer, user;
    string move[] = {"Rock", "Paper", "Scissor"};

    // keep repeating until user wants to exit
    while (1) {
        // take input from user
        cout << "Enter 1 for Rock." << endl;
        cout << "Enter 2 for Paper." << endl;
        cout << "Enter 3 for Scissor." << endl;
        cout << "Enter 0 to exit." << endl;
        cout << "Choice >> ";
        cin >> user;

        // check if player wants to exit
        if (user == 0)
            break;

        // input validation
        if (!(user >= 1 && user <= 3)) {
            cout << "\nEnter a valid choice!\n" << endl;
            continue;
        }

        // computer chooses random move
        // Genearte a random number from 1 to 3
        // Number 1, 2, 3 indicates rock, 
        // paper, scissor resepectively
        computer = rand() % 3 + 1;

        // display the move of each player
        // fetch move name from string array
        cout << "\nYou played     : " << move[user - 1];
        cout << "\nComputer played: " << move[computer - 1];

        //check for the winner
        // rock vs paper => paper wins
        // rock vs scissor => rock wins
        // paper vs scissor => scissor wins
        if (computer == user)
            cout << "\nIt is a tie!" << endl;
        else if (computer == 1 && user == 3)
            cout << "\nComputer wins!" << endl;
        else if (computer == 2 && user == 1)
            cout << "\nComputer wins!" << endl;
        else if (computer == 3 && user == 2)
            cout << "\nComputer wins!" << endl;
        else
            cout << "\nYou win!" << endl;

        // new line
        cout << "\n";
    }

    return 0;
}
