## Amazon Agent

<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

While there currently are many projects being built with LLMs, Agent technology that really utilizes the LLM to reason as it
goes through a process is yet to fruitfully go into production. This project aims to demonstrate a simple use case for building
LLM agents that is able to retrieve order details from an Amazons customer page

It will offer the following:

- A flask application dockerized and can be executed anywhere
- Utilization of llama3 locally allowing free usage of the LLM
- Selenium methods to navigate and perform actions on the web
- Robust logging, making debugging easier

Of course, this project is not going to be perfect and cannot serve for all the different tasks users may want from an LLM Agent,
however it demonstrates how much can be done utilizing local LLMs

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

The following gives you instructions on how you might setup this enviroment locally to allow further testing the system or develop further on the concepts of this repository.

### Prerequisites

You will need Python 3.8 or above to run this project. It is recommended that you run this in a virtual enviroment, you can create the virtual environment using the following commands.

- python
  ```sh
  python3 -m venv myenv
  virtualenv myenv
  source myenv/bin/activate
  ```

The project requires a llama3 installation of your local computer to operate, currently we would advice that you use Ollama which simply enables you to install the LLMs and run them locally. To install, you can follow the following link and click download: https://ollama.com/

- After installing it, you can run the following command:

  ```
      ollama run llama3
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Clone the repo
   ```sh
   git clone https://github.com/Basi10/Amazon-Agent.git
   ```
2. Install python packages
   ```sh
   pip install requirements.txt
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

After cloning the repository, there are two ways you can interact with the current application

### Docker

1. Build the docker image
   ```sh
   docker build -t my_image_name:tag_name .
   ```
2. Run the image in your local environment
   ```sh
   docker run -p 8000:8000 my_image_name:tag_name
   ```

### Python

You have to install the dependencies as well in the installation process.

1. Navigate to the project root directory
   ```sh
   cd Yolo-MicroService-Deployment
   ```
2. Run the flask application
   ```sh
   python app.py
   ```

To interact with the application, you can utilize postman and follow the following steps:

1. Send your amazon account email address and password to register user

   Method: POST
   URL: http://localhost:5000/users/
   Body (JSON):

   ```json
   {
     "email": "test@example.com",
     "password": "test123"
   }
   ```

2. Login with Valid Credentials

   Method: POST
   URL: http://localhost:5000/users/login
   Body (JSON):

   ```json
   {
     "email": "test@example.com",
     "password": "test123"
   }
   ```

3. Retrieve Order Details
   Method: GET
   URL: http://localhost:5000/users/
   Headers:
   ```makefile
    Authorization: Bearer <access_token>
   ```
   The response will be in json format consisting of the order details for the amazon account

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Basilel Birru - basilelbirru@gmail.com

Project Link: [https://github.com/Basi10/Amazon-Agent.git](https://github.com/Basi10/Amazon-Agent.git)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
