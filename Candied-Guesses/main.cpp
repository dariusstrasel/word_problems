// Example program
// Author: Christian Marks
#include <iostream>
#include <string>
#include <list>

using std::list;

int main()
{
    int* guess = new int[5];
    guess[0] = 55;
    guess[1] = 59;
    guess[2] = 61;
    guess[3] = 65;
    guess[4] = 66;

    int answer = 0;
    bool answer_found = false;

    for(int i = 0; i < 5; i++)
    {
        int three_off = 0;
        int four_off = 0;
        for(int j = 50; j < 70; j++)
        {
            if(guess[i] == j + 3 || guess[i] == j - 3)
            {
                three_off++;
            }
            else if(guess[i] == j + 4 || guess[i] == j - 4)
            {
                four_off++;
            }
        }
        if(three_off == 2 && four_off == 1)
        {
            printf("Answer found!\n");
            answer_found = true;
            answer = guess[i];
            break;
        }
    }
    if(answer_found)
        printf("Answer is %i!", answer);
    else
        printf("No answer found");
}