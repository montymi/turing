<div id="readme-top"></div>

<!-- PROJECT SHIELDS -->
[![Creator][creatorLogo]][creatorProfile]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![GPL License][license-shield]][license-url]

<!-- PROJECT HEADER -->
# Turing

A local TTS & STT python library powered by Coqui and Whisper.

<!-- CALL TO ACTIONS -->
[![🚀 Explore Demo][demoLogo]][demoLogo-url]
[![🐛 Report Bug][bugLogo]][bugLogo-url]
[![✨ Request Feature][featureLogo]][featureLogo-url]

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
    <li><a href="#installation">Installation</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#setup">Setup</a></li>
      </ul></li>
    <li><a href="#usage">Usage</a>
      <ul>
        <li><a href="#getting-started">Getting Started</a></li>
        <li><a href="#advanced">Advanced</a></li>
      </ul></li>
    </li>
    <li><a href="#structure">Structure</a></li>
    <li><a href="#tasks">Tasks</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<br />

<!-- ABOUT THE PROJECT -->
## About The Project

This project is a Python library designed to simplify the implementation of a Speech-to-Text (STT) and Text-to-Speech (TTS) pipeline in local environments. The STT functionality leverages the power of OpenAI's Whisper model, known for its robust transcription capabilities and multilingual support. For TTS, the library integrates Coqui-AI, providing high-quality and customizable speech synthesis. The goal is to offer developers an easy-to-use and modular solution for incorporating speech processing into their applications. By running entirely on local systems, the library prioritizes privacy and reduces reliance on external APIs. It is designed to be lightweight yet flexible enough to adapt to diverse project needs, from voice assistants to accessibility tools.

### Built With

[![Python][pythonLogo]][pythonLogo-url]
[![OpenAI][openaiLogo]][openaiLogo-url]
[![Coqui-AI][coquiaiLogo]][coquiaiLogo-url]
[![Markdown][markdownLogo]][markdownLogo-url]
[![HTML][htmlLogo]][htmlLogo-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Installation

### Prerequisites
Ensure you have [git](https://git-scm.com/), [python][pythonLogo-url] (and presumably pip too). Best bet, download the official release for your platform (Operating System) from the provided homepages and their download section. On Windows, your best bet is to use the resulting Git Bash application that will become available after installing git.

Comfirm prerequisites by running the following command:
```bash
git --version && python --version && pip --version
```

Download and navigate into the repository:
```bash
git clone https://github.com/montymi/linguist/ && cd linguist
```

### Setup

Create and activate the virtual environment:
```bash
python -m venv .venv
```
In Unix:
```bash
source .venv/bin/activate
```
In Windows:
```bash
.venv/Scripts/Activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```
*This will take a long time, Coqui is large.*

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage


### Getting Started

Run the following command:
```bash
python main.py
```

### Advanced

TODO; Check [Tasks](#tasks) for updates coming soon!

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- STRUCTURE -->
## Structure

```
my_audio_lib/
├── main.py
├── microphone.py
├── requirements.txt
└── README.md
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- TASKS -->
## Tasks

- [X] Initialize project as git repo
- [ ] Structure project for easier growth
- [ ] Include STT portion of pipeline

See the [open issues][bugLogo-url] for a full list of issues and proposed features.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

1. [Fork the Project](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. [Open a Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Currently not licensed since we are new but will have this:
Distributed under the GPL-3.0 License. See `LICENSE.txt` for more information.

<br />

<!-- CONTACT -->
## Contact

Michael Montanaro

[![LinkedIn][linkedin-shield]][linkedin-url] 
[![GitHub][github-shield]][github-url]

<br />

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list any resources used or that may be helpful in understanding the project

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[demoLogo]: https://img.shields.io/badge/🚀%20Explore%20Demo-grey?style=for-the-badge
[demoLogo-url]: https://github.com/montymi/linguist
[bugLogo]: https://img.shields.io/badge/🐛%20Report%20Bug-grey?style=for-the-badge
[bugLogo-url]: https://github.com/montymi/linguist/issues
[featureLogo]: https://img.shields.io/badge/✨%20Request%20Feature-grey?style=for-the-badge
[featureLogo-url]: https://github.com/montymi/linguist/issues
[pythonLogo]: https://img.shields.io/badge/Python-black?style=for-the-badge&logo=python&logoColor=natural
[pythonLogo-url]: https://python.org/
[openaiLogo]: https://img.shields.io/badge/Whisper-black?style=for-the-badge&logo=openai&logoColor=natural
[openaiLogo-url]: https://openai.com/
[coquiaiLogo]: https://img.shields.io/badge/Coqui-black?style=for-the-badge&logo=envato&logoColor=natural
[coquiaiLogo-url]: https://coqui.ai/
[markdownLogo]: https://img.shields.io/badge/Markdown-black?style=for-the-badge&logo=markdown&logoColor=natural
[markdownLogo-url]: https://daringfireball.net/projects/markdown/
[htmlLogo]: https://img.shields.io/badge/HTML5-black?style=for-the-badge&logo=html5&logoColor=natural
[htmlLogo-url]: https://html.spec.whatwg.org/
[creatorLogo]: https://img.shields.io/badge/-Created%20by%20montymi-maroon.svg?style=for-the-badge
[creatorProfile]: https://montymi.com/
[contributors-shield]: https://img.shields.io/github/contributors/montymi/linguist.svg?style=for-the-badge
[contributors-url]: https://github.com/montymi/linguist/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/montymi/linguist.svg?style=for-the-badge
[forks-url]: https://github.com/montymi/linguist/network/members
[stars-shield]: https://img.shields.io/github/stars/montymi/linguist.svg?style=for-the-badge
[stars-url]: https://github.com/montymi/linguist/stargazers
[issues-shield]: https://img.shields.io/github/issues/montymi/linguist.svg?style=for-the-badge
[issues-url]: https://github.com/montymi/linguist/issues
[license-shield]: https://img.shields.io/github/license/montymi/linguist.svg?style=for-the-badge
[license-url]: https://github.com/montymi/linguist/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin
[linkedin-url]: https://linkedin.com/in/michael-montanaro
[github-shield]: https://img.shields.io/badge/-GitHub-black.svg?style=for-the-badge&logo=github
[github-url]: https://github.com/montymi
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
