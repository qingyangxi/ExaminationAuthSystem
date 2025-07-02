# Exam Identity Verification System via Face Recognition

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![PyQt5](https://img.shields.io/badge/PyQt-5-orange.svg)](https://riverbankcomputing.com/software/pyqt/)

This repository contains an exam identity verification system based on face recognition, developed as a first-year project at Harbin Institute of Technology (Weihai) .

## ✨ About The Project

**Please Note:** This project was developed primarily as a hands-on learning exercise. It implements several classic, and now somewhat dated, face recognition algorithms such as **LBPH** to demonstrate fundamental concepts . It serves as a practical application of traditional computer vision techniques rather than a production-ready system using state-of-the-art models.

The system is a desktop application designed for exam identity verification. It integrates two complementary face recognition algorithms:

* **LBPH (Local Binary Patterns Histograms)**: A classic, texture-based recognition algorithm known for its high efficiency and low resource consumption .
* **ResNet (Residual Network)**: A deep convolutional neural network that effectively extracts high-level abstract features from faces, significantly improving recognition accuracy .

By combining the strengths of both algorithms, this system achieves a balance between high speed and high accuracy, meeting the dual requirements of real-time performance and reliability in examination environments .

## 🚀 Key Features

* **🔐 Secure Admin Login**
    * Features a secure login interface for administrators to manage the system .
    * Supports account configuration via a settings file and includes a "Remember Me" function for convenience .

* **🖼️ Efficient Face Data Entry**
    * Captures examinee images in real-time using a camera .
    * Supports continuous, uninterrupted image capture for a single user and seamless back-to-back capture for multiple users, greatly improving efficiency .
    * A pop-up dialog guides the operator to enter the examinee's name, ensuring an intuitive workflow .

* **🎭 Intelligent Face Verification**
    * Offers two distinct solutions for face comparison to suit different needs :
        1.  **High-Efficiency Mode**: Utilizes a `Haar Cascade Classifier` for face detection combined with the `LBPH` algorithm for fast feature comparison .
        2.  **High-Accuracy Mode**: Employs `HOG` or `CNN` for face detection and a pre-trained `ResNet` model to extract 128-d feature vectors for highly accurate comparison .

* **🎨 User-Friendly GUI**
    * The graphical user interface is built with `PyQt5` and `PyQt-Fluent-Widgets`, offering a clean, modern, and intuitive user experience .

## 📸 Screenshots

<table>
    <tr>
        <td align="center"><b>Admin Login</b> </td>
        <td align="center"><b>Main Menu</b> </td>
    </tr>
    <tr>
        <td><img src="./hook/admin.jpg" alt="Admin Login" width="400"/></td>
        <td><img src="./hook/menu.jpg" alt="Main Menu" width="400"/></td>
    </tr>
    <tr>
        <td align="center"><b>Face Data Capture</b> </td>
        <td align="center"><b>Face Verification</b> </td>
    </tr>
    <tr>
        <td><img src="./hook/load.jpg" alt="Face Data Capture" width="400"/></td>
        <td><img src="./hook/verify.jpg" alt="Face Verification" width="400"/></td>
    </tr>
</table>

## 🛠️ Tech Stack

* **Core Language**: Python
* **Computer Vision**: OpenCV, opencv-contrib-python
* **GUI Framework**: PyQt5, PyQt-Fluent-Widgets
* **Core Algorithms**: LBPH , ResNet , Harr Cascades , HOG 

## 📦 Getting Started

### 1. Prerequisites

This project uses an OpenCV Haar Cascade classifier for face detection . You need to download the pre-trained model file `haarcascade_frontalface_default.xml`.

* **Download Link**: [**haarcascade_frontalface_default.xml**](https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml)
    *(Right-click the link and select "Save Link As..." to download the file.)*

* **Action**: Place the downloaded `haarcascade_frontalface_default.xml` file in the **app/common/classifier directory** of this project, or ensure your code correctly points to its location.

### 2. Installation

**a. Clone the Repository**
```bash
git clone [https://github.com/qingyangxi/ExaminationAuthSystem.git](https://github.com/qingyangxi/ExaminationAuthSystem.git)
cd your-repository-name
```

**b. Create and Activate a Virtual Environment**
```bash
# Create the virtual environment
python -m venv venv

# Activate on Windows
.\venv\Scripts\activate

# Activate on macOS/Linux
# source venv/bin/activate
```

**c. Install Dependencies**
```bash
# Install all required packages
pip install opencv-python opencv-contrib-python "PyQt-Fluent-Widgets[full]"
```

### 3. Run the Application
```bash
python main.py
```

## ⚠️ Known Issues

* **UI Layout**: The interface layout may have minor alignment issues on different screen resolutions.
* **Manual Cleanup Required**: After each use, all files within the `app/common/features` and `app/common/images` directories must be deleted manually. Failure to do so will cause errors on the next run due to residual data.
