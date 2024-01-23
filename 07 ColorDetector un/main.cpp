#include <opencv2/imgproc.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <string>
#include <vector>

void getColor (cv::Mat, cv::Scalar, cv::Scalar);

int main ()
{
    // The parameters and basic settings
    std::string path = "../imgs/4.jpg";
    cv::Mat img;
    img = cv::imread (path);

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

    std::vector <std::vector<cv::Scalar>> mycolors = {{black_low,black_up}, {blue2_low, blue2_up}, {white_low, white_up}, {red1_low, red1_up}, {red2_low, red2_up}, {orange_low, orange_up}, {yellow_low, yellow_up}, {green_low, green_up}, {blue1_low, blue1_up}, {purple_low, purple_up}};

    cv::imshow ("Image", img);

    // int his;
    cv::Mat img2;
    while (true)
    {
        img2 = cv::imread ("../imgs/1.jpg");
        int key = cv::waitKey (0);
        // cv::destroyWindow (("Img" + std::to_string(his - 48)));


        if (key == 27)
        {
            std::exit (0);
        }

        getColor (img2, mycolors[key - 48][0], mycolors[key - 48][1]);        

        // cv::imshow (("Img" + std::to_string(key - 48)), getColor (img, mycolors[key - 48][0], mycolors[key - 48][1]));

        // if (key == 48)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, black_low, black_up));
        // }
        // else if (key == 49)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, gray_low, gray_up));
        // }
        // else if (key == 50)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, white_low, white_up));
        // }
        // else if (key == 51)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, red1_low, red1_up));
        // }
        // else if (key == 52)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, red2_low, red2_up));
        // }
        // else if (key == 53)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, orange_low, orange_up));
        // }
        // else if (key == 54)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, yellow_low, yellow_up));
        // }
        // else if (key == 55)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, green_low, green_up));
        // }
        // else if (key == 56)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, blue_low, blue_up));
        // }
        // else if (key == 57)
        // {
        //     cv::destroyWindow ("Img");
        //     cv::imshow ("Img", getColor (img, purple_low, purple_up));
        // }
        // else if (key == 27)
        // {
        //     std::exit (0);
        // }
        // his = key;
        
    }

    return 0;
}

void getColor (cv::Mat img, cv::Scalar lower, cv::Scalar upper)
{
    cv::Mat imgHSV, imgBlur, imgMask;
    std::vector <std::vector <cv::Point>> contours;
    
    // img2 = img;
    cv::cvtColor (img, imgHSV, cv::COLOR_BGR2HSV);
    cv::GaussianBlur (imgHSV, imgBlur, cv::Size (5, 5), 2);
    cv::inRange (imgBlur, lower, upper, imgMask);

    cv::findContours (imgMask, contours, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

    for (int i = 0; i < contours.size (); i++)
    {   
        // cv::RotatedRect rorect;
        // cv::Point2f points[4];

        // rorect = cv::minAreaRect (contours[i]);
        // rorect.points (points);
        // // cv::drawContours (img2, contours, i, cv::Scalar (0, 255, 255), 2);
        // for (int j = 0; j < 4; j++)
        // {
        //     cv::line (img2,points[i], points[(i + 1) % 4], cv::Scalar (255, 255, 255), 2);
        // }
        // int x = points[1].x, y = (points[1].y - 30);

        double area = cv::contourArea (contours[i]);

        if (area > 500)
        {
            cv::Rect boundingrect = cv::boundingRect (contours[i]);

            cv::rectangle (img, boundingrect, cv::Scalar (255, 255, 255), 2);

            cv::putText (img, "Target Color", boundingrect.tl (), cv::FONT_HERSHEY_SIMPLEX, 2, cv::Scalar (255, 255, 255), 2);
        }
    }

    cv::imshow ("Img", img);
    
}