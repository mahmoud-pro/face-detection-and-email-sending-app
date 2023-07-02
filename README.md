# Face Detection and Email Sending App

This Python application uses computer vision techniques to detect faces using the webcam and sends the detected faces via email. It provides a simple and convenient way to automate the process of capturing and sending face images.

## Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.x
- OpenCV library: `pip install opencv-python`
- smtplib library: `pip install smtplib`

## Getting Started

1. Clone this repository or download the source code.
2. Open a terminal or command prompt and navigate to the project directory.

## Setup

- Create the `.env` file and provide the required information:

   - `APP_PASS`: Your google password app.
   - `EMAIL`: Your email address.

## Usage

1. Run the application by executing the following command in your terminal:

   ```
   python main.py
   ```

2. The webcam feed will open, and the application will start detecting faces.

3. When a face is detected, the application captures the image and sends it via email.

4. Press the `Q` key to quit the application.

## Customization

- You can modify the face detection parameters in `main.py` to fine-tune the face detection process. For example, you can change the minimum face size or adjust the detection sensitivity.

- If you want to customize the email message, modify the `send_email` function.

## Notes

- Make sure you have a stable internet connection to send emails.

- For security reasons, it is recommended to use an app password or two-factor authentication for your email account.

- This application is intended for educational and personal use only. Be sure to comply with applicable laws and regulations when using the face detection and email sending capabilities.


## Acknowledgments

- This application utilizes the OpenCV library for face detection.
