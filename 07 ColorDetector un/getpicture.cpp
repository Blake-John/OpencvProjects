#include <opencv2/imgproc.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>

int main ()
{
    cv::Mat img(500, 1000, CV_8UC3, cv::Scalar (255, 255, 255));

    //todo draw the different color of rectangle
    cv::rectangle (img, cv::Point (0, 0), cv::Point (250, 250), cv::Scalar (0, 0, 0), cv::FILLED);
    cv::rectangle (img, cv::Point (250, 0), cv::Point (500, 250), cv::Scalar (255, 0, 0), cv::FILLED);
    cv::rectangle (img, cv::Point (500, 0), cv::Point (750, 250), cv::Scalar (0, 255, 0), cv::FILLED);
    cv::rectangle (img, cv::Point (750, 0), cv::Point (1000, 250), cv::Scalar (0, 0, 255), cv::FILLED);
    cv::rectangle (img, cv::Point (0, 250), cv::Point (250, 500), cv::Scalar (255, 255, 0), cv::FILLED);
    cv::rectangle (img, cv::Point (250, 250), cv::Point (500, 500), cv::Scalar (0, 255, 255), cv::FILLED);
    cv::rectangle (img, cv::Point (500, 250), cv::Point (750, 500), cv::Scalar (20, 20, 159), cv::FILLED);
    cv::rectangle (img, cv::Point (750, 250), cv::Point (1000, 500), cv::Scalar (100, 16, 78), cv::FILLED);

    cv::imwrite ("../imgs/3.jpg", img);
}