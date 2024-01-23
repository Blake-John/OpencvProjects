#include "transform.h"
#include <cmath>

std::string tool = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";

int To_ten (std::string num, int origin)
{
    // if ((int)(num[num.length () - 1] - '0') >= origin)
    // {
    //     std::cout << "Input Error !" << std::endl;
    //     return 0;
    // }

    if (num[num.length () - 1] > tool[origin - 1])
    {
        std::cout << "Input Error !" << std::endl;
        return 0;
    }
    
    
    std::string intermediates;
    // for (int i = 0; i < origin; i++)
    // {
    //     inter_tool[i] = tool[i];
    // }
    for (int i = (num.length () - 1); i >= 0; i--)
    {
        intermediates[num.length () - i - 1] = num[i];
    }
    int ten = 0;

    // for (int i = 0; i < num.length (); i++)
    // {
    //     ten += (int)(intermediates[i] - '0') * std::pow (origin, i);
    // }

    // std::cout << intermediates << std::endl;

    for (int i = 0; i < num.length (); i++)
    {
        ten += tool.find (intermediates[i]) * pow (origin, i);
    }
    
    return ten;
}

std::string To_other (int ten, int trans)
{
    int i = 0, j;
    std::string intermediates, target;

    do
    {
        j = ten % trans;
        intermediates.push_back (tool[j]);
        i++;
        ten /= trans;
    } while (ten);

    for (int k = (intermediates.length () - 1); k >= 0; k--)
    {
        target.push_back (intermediates[k]);
    }
    return target;

}


// int main ()
// {
//     // std::cout << To_ten ("C", 16) << std::endl;
//     std::cout << To_other (17, 17) << std::endl;
// }


