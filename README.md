# 🎥 TikTok Downloader

---

## 📋 Table of Contents
- 🏷️ [Project Description](#project-description)
- ✨ [Features](#features)
- 🛠️ [Technologies](#technologies)
- 🗂️ [Project Structure](#project-structure)
- ⚙️ [Requirements](#requirements)
- 💾 [Installation](#installation)
- ▶️ [Usage](#usage)
- 🔧 [Configuration](#configuration)
- 🧪 [Running Tests](#running-tests)
- 🫱🏻‍🫲🏼 [Contributing](#contributing)
- 📜 [License](#license)
- 👨🏻‍💻 [Author](#author--acknowledgments--contact) / 🙏🏻 [Acknowledgments](##author--acknowledgments--contact) / 📩 [Contact](##author--acknowledgments--contact)
- 💰 [Support Me!](##if-you-want-to-support-me)

---

## Project Description
A simple Python script to download TikTok videos without watermark, using a public API.
The program asks for a TikTok video link, retrieves the video through an API call, and saves it locally as tiktok_video_without_watermark.mp4.
<!-- ## Badges -->
<!-- ## Live Demo -->
<!-- ## Screenshots -->

---

## Features
- Download TikTok videos without watermark
- Save videos locally in .mp4 format
- Simple CLI interface
- Error handling for invalid URLs or failed API responses

---

## Technologies
- Python
- Requests
- PyTest

---

## Project Structure
- │ 📁 TikTok Downloader/
- ├── main.py
- ├── test_main.py
- ├── requirements.txt
- ├── README.md
- ├── LICENSE
- └── .gitignore

---

## Requirements
- Python 3.10+
- Dependencies listed in [requirements.txt](requirements.txt)

---

## Installation
Clone the repo and install dependencies:
```bash
git clone https://github.com/xAndreiix/TikTok_Downloader.git
```
```bash
cd tiktok_downloader
```
```bash
pip install -r requirements.txt
```

---

## Usage
Run the script and provide a TikTok video link:
```bash
python main.py
```
Example input:

Enter TikTok video URL: https://www.tiktok.com/@example/video/123456789

The script will download the video and save it as: "tiktok_video_without_watermark.mp4"

CLI Example:

Enter TikTok video URL: https://www.tiktok.com/@example/video/123456789

Download complete: "tiktok_video_without_watermark.mp4"

---

## Configuration
Currently, the script always saves the output file as: "tiktok_video_without_watermark.mp4"

If you want to customize the filename or output path, modify this section in main.py:

    with open("tiktok_video_without_watermark.mp4", "wb") as f:
        f.write(video_content)

---

## Running Tests
pytest
<!-- ## Deployment -->
<!-- ## Notes -->
<!-- ## Road Map -->
<!-- ## FAQ -->

---

## Contributing
Pull requests are welcome.
For major changes, please open an issue first to discuss what you’d like to change.
<!-- ## Changelog -->

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE)

---

## Author / Acknowledgments / Contact
**Author:** 
Andrei Iliescu

[![Website](https://img.shields.io/badge/Website-PORTFOLIO-gold?style=for-the-badge&logo=about-dot-me&logoColor=white)](https://xandreiix.github.io/Andrei-Iliescu-Portfolio/)

**Acknowledgments:**  
- Inspired by [@1minutepython](https://www.tiktok.com/@1minutepython) tutorial on TikTok.

[![TikTok](https://img.shields.io/badge/TikTok-000000?style=for-the-badge&logo=TikTok&logoColor=white)](https://www.tiktok.com/@1minutepython/video/7541884991215537463?is_from_webapp=1&sender_device=pc)
- All thanks to him for the tutorial!

**Contact:**  

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/andrei-iliescu-aa7910214)<br>
[![Email Yahoo](https://img.shields.io/badge/Email-andrey_iliescu%40yahoo.com-6001D2?style=for-the-badge&logoColor=white)](mailto:andrey_iliescu@yahoo.com)<br>
[![Email Gmail](https://img.shields.io/badge/Gmail-andrei.iliescu13102000%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:andrei.iliescu13102000@gmail.com)

---

## If you want to support me
[![PayPal](https://img.shields.io/badge/PayPal-xAndreiix-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/xAndreiix)<br>
[![Revolut](https://img.shields.io/badge/Revolut-xAndreiix-001B2E?style=for-the-badge&logoColor=white)](https://revolut.me/xandreiix)
