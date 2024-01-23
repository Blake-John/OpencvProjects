#include "transform.h"


int main ()
{
    std::string num;
    int record;
    int origin;
    int trans;

    while (true)
    {
        std::cout << "1. Transform the number." << std::endl;
        std::cout << "0. Exit ." << std::endl;
        std::cout << "Please choose the number : "; std::cin >> record;
        if (record == 0)
        {
            break;
        }
        else if (record == 1)
        {
            std::cout << "Please input the origin form : "; std::cin >> origin;
            std::cout << "Please input the origin number : "; std::cin >> num;
            std::cout << "Please input the transform target : "; std::cin >> trans;
            int intermidiate = To_ten (num, origin);
            std::cout << "The Transformed number is : " << To_other (intermidiate, trans) << std::endl;
        }
        else
        {
            std::cout << "Input Error ! " << std::endl;
        }
        
        
    }
    

    std::cout << "Please press any key to exit .";
    std::cin.get ();
    return 0;
}