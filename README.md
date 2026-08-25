<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a id="readme-top"></a>

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
<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/abhic117/startup-searcher">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Startup-Searcher</h3>

  <p align="center">
     A dashboard for viewing tech startups
    <!-- <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/repo_name">View Demo</a>
    &middot;
    <a href="https://github.com/github_username/repo_name/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/github_username/repo_name/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a> -->
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#running">Running</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
    <!-- <li><a href="#acknowledgments">Acknowledgments</a></li> -->
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

[![Product Name Screen Shot][main-screenshot]](https://github.com/abhic117/startup-searcher)

A web application that scrapes and normalises sydney tech startup information then displays it on a dashboard.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

- [![Python][python.org]][python-url]
- [![Streamlit][streamlit.io]][streamlit-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple steps.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/abhic117/startup-searcher.git
   ```
2. Create and activate virtual environment
   ```sh
   python -m venv venv
   ```
   ```
   venv\Scripts\activate.bat
   ```
   or
   ```
   venv\Scripts\activate.ps1
   ```
3. Install python packages
   ```sh
   python -m pip install -r requirements.txt
   ```
4. Download Ollama
   ```sh
   https://ollama.com/download
   ```
5. Pull Qwen model
   ```sh
   ollama pull qwen2.5:7b-instruct-q4_K_M
   ```

### Running

1. Run Ollama desktop application
2. Run command
   ```sh
   streamlit run st_chatbot.py
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

This dashboard has many features centred around finding a start-up suitable for a job role.

The interactive table shows the complete list of startups within the database. The table includes features to search, sort and select different fields. The sidebar also contains filters for each column, allowing them to be toggled on or off.
![Usage Database][usage-1]

The chat window features an AI chatbot connected to the database via RAG, allowing the user to ask semantic questions relating to the database.
![Usage Chat][usage-2]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Abhishek Chand - AbhishekC117@hotmail.com

Project Link: [https://github.com/abhic117/startup-searcher](https://github.com/abhic117/startup-searcher)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[main-screenshot]: images/main.png
[usage-1]: images/usage-database.png
[usage-2]: images/usage-chat.png

<!-- Shields.io badges. You can a comprehensive list with many more badges at: https://github.com/inttter/md-badges -->

[python.org]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff
[python-url]: https://www.python.org/
[streamlit.io]: https://img.shields.io/badge/Streamlit-red
[streamlit-url]: https://streamlit.io/
