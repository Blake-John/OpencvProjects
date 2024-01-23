#include <opencv2/imgproc.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <string>

void getColor (cv::Mat, cv::Scalar, cv::Scalar, int);

//todo a color tracebar
cv::Scalar black_low (0, 0, 0), black_up (0, 0, 0);
cv::Scalar blue2_low (74, 144, 131), blue2_up (110, 255, 255);
cv::Scalar white_low (0, 0, 221), white_up (180, 30, 255);
cv::Scalar red1_low (121, 90, 123), red1_up (179, 250, 229);
cv::Scalar red2_low (0, 154, 131), red2_up (0, 232, 255);
cv::Scalar orange_low (0, 111,200), orange_up (19, 255, 255);
cv::Scalar yellow_low (20, 93, 119), yellow_up (64, 255, 255);
cv::Scalar green_low (69, 33, 110), green_up (99, 148, 255);
cv::Scalar blue1_low (96, 75, 151), blue1_up (133, 255, 255);
cv::Scalar purple_low (118, 139, 117), purple_up (179, 255, 117);

std::vector <std::vector<cv::Scalar>> mycolors = {{black_low,black_up}, {white_low, white_up}, {red1_low, red1_up}, {orange_low, orange_up}, {yellow_low, yellow_up}, {green_low, green_up}, {blue1_low, blue1_up}, {purple_low, purple_up}};
std::vector <std::vector<cv::Scalar>> mycolors_backup = {{black_low,black_up}, {blue2_low, blue2_up}, {white_low, white_up}, {red1_low, red1_up}, {red2_low, red2_up}, {orange_low, orange_up}, {yellow_low, yellow_up}, {green_low, green_up}, {blue1_low, blue1_up}, {purple_low, purple_up}};

std::vector <std::string> types = {"None", "Point", "Line", "Triangle", "Rectangle", "5", "6", "Round"};
std::vector <std::string> color_types = {"blake", "white", "red", "orange", "yellow", "green", "blue", "purple"};

int main ()
{
    std::string path = "../imgs/4.jpg";
    cv::Mat img, Mask;
    img = cv::imread (path);
    cv::resize (img, img, cv::Size (), 0.4, 0.4);

    
    cv::imshow ("Img", img);

    cv::Mat img2;
    // while (true)
    // {
    //     img.copyTo (img2);
    //     int key = cv::waitKey (0);

    //     if (key == 27)
    //     {
    //         break;
    //     }
        
    //     getColor (img2, mycolors[key - 48][0], mycolors[key - 48][1]);
    // }
    
    img.copyTo (img2);
    for (int i = 0; i < mycolors.size (); i++)
    {
        getColor (img2, mycolors[i][0], mycolors[i][1], i);
    }
    
    if (cv::waitKey (0) == 27)
    {
        std::exit (0);
    }
    

    return 0;
}

void getColor (cv::Mat img, cv::Scalar lower, cv::Scalar upper, int num)
{
    cv::Mat imgHSV, imgBlur, imgMask;
    std::vector <std::vector <cv::Point>> contours;

    cv::cvtColor (img, imgHSV, cv::COLOR_BGR2HSV);
    cv::GaussianBlur (imgHSV, imgBlur, cv::Size (5, 5), 2);
    cv::inRange (imgBlur, lower, upper, imgMask);

    cv::findContours (imgMask, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    for (int i = 0; i < contours.size (); i++)
    {
        double area = cv::contourArea (contours[i]);
        std::vector <std::vector <cv::Point>> con;
        std::vector <cv::Rect> re;

        if (area > 500)
        {
            std::vector <cv::Point> conpoly;
            cv::approxPolyDP (contours[i], conpoly, 5, true);
            cv::Rect boundingrect = cv::boundingRect (contours[i]);
            con.push_back (conpoly);
            re.push_back (boundingrect);
        }
        for (int j = 0; j < con.size (); j++)
        {
            if (con[j].size () >= 7)
            {
                cv::putText (img, color_types[num], re[j].tl (), cv::FONT_HERSHEY_SIMPLEX, 0.75, cv::Scalar (255, 255, 255), 2);
                // cv::drawContours (img, con, 0, cv::Scalar (255, 255, 255), 1);
                cv::rectangle (img, re[j], cv::Scalar (255, 255, 255), 2);

            }
            else
            {
                cv::putText (img, color_types[num], re[j].tl (), cv::FONT_HERSHEY_SIMPLEX, 0.75, cv::Scalar (255, 255, 255), 2);
                // cv::drawContours (img, con, 0, cv::Scalar (255, 255, 255), 1);
                cv::rectangle (img, re[j], cv::Scalar (255, 255, 255), 2);
            }
            
        }
        
        
    }

    cv::imshow ("Img", img);
    
}