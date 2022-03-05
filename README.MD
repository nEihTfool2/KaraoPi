<br />
<p align="center">
  <a href="https://github.com/Neihtq/KaraoPi">
    <img src="src/main/icons/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">KaraoPi</h3>

  <p align="center">
    Everyone's music/video at a party
    <br />
    <br />
    <br />
    <!--<a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>-->
    ·
    <a href="https://github.com/Neihtq/KaraoPi/issues">Report Bug</a>
    ·
    <a href="https://github.com/Neihtq/KaraoPi/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)



<!-- ABOUT THE PROJECT -->
## About The Project
![Product Name Screen Shot][product-screenshot]
![Product Name Screen Shot][interface-screenshot]

My friends and I often enjoy singing Karaoke at a private place by plugging in some Mics and singing karaoke versions of our favorite songs from YouTube (I call it low budget) - hence the weird project name! 

But project is not all about Karaoke. You can plug some speakers into a computer (e.g. a Raspberry**Pi**) and optionally also a TV as well. The second image shows the web interface where everyone can simply add a video or song or their choice to the queue (via phone and desktop possible).

This application is set in a simple client-server-architecture. Note that the host machine (server) and everyone adding videos to the queue (clients) have to be in the same network!

Everything to know about this project:
* Server: Plays videos from YouTube and provides a queue
* Search Window: (running on host machine): Search for YouTube videos and add them queue; delete queue elements; provides QR code and URL for web interface
* Client (Web interface): Shows queue and currently playing video; search for YouTube videos and them to queue

When having a (karaoke) party/gathering with music running in the background, everyone can add play their videos of choice (but FCFS)-

**tl;dr: remote YouTube player with queue functionality and access via web browser**

### Built With 
Server and Search Window
* [PyQt5](https://www.riverbankcomputing.com/software/pyqt/)
* [Tornado](https://github.com/tornadoweb/tornado)
* [pafy](https://pypi.org/project/pafy/)
* [fman build system](https://build-system.fman.io/)
* [youtube_search](https://github.com/joetats/youtube_search)
* [Python QR Code](https://github.com/lincolnloop/python-qrcode)

Web interface:
* [Bootstrap](https://getbootstrap.com/)


<!-- GETTING STARTED -->
## Getting Started

You only need one machine to run this application. To get a local copy up and running follow these simple example steps.

### Prerequisites
You'll need
* [Python (at the time of this writing version 3.7)](https://www.python.org/)
* [pipenv](https://github.com/pypa/pipenv)

### Installation
With all prerequisites met, these steps should apply for any OS
1. Clone the repo
```sh
git clone https://github.com/Neihtq/KaraoPi
```
3. Navigate to the project folder and install pip packages
```sh
cd KaraoPi/
pipenv install
```
4. Start the application with
```sh
fbs run
```

<!-- USAGE EXAMPLES -->
## Usage

TODO



<!-- ROADMAP -->
## Roadmap
* Bugfix: Queue has more than one video - when pausing the video for a second the next video from the queue will be played after resuming [TODO]
* Add demo and usage example to `README`

See the [open issues](https://github.com/Neihtq/KaraoPi/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
## Contact
Github: [neihtq](https://github.com/Neihtq)

E-mail: q.thien.nguyen@outlook.de

[LinkedIn](https://www.linkedin.com/in/thien-quang-nguyen-808101143/)

## Acknowledgements
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template#license)

[product-screenshot]: images/screenshot_app.png
[interface-screenshot]: images/screenshot_website.png
