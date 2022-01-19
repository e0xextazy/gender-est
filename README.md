[![GitHub issues](https://img.shields.io/github/issues/e0xextazy/gender-est)](https://github.com/e0xextazy/gender-est/issues)
[![GitHub license](https://img.shields.io/github/license/e0xextazy/gender-est?color=purple)](https://github.com/e0xextazy/gender-est/blob/main/LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-black-black)](https://github.com/psf/black)

# gender-est

### Everything is simple! Send a photo -> take a gender
![gender-est](https://user-images.githubusercontent.com/49094658/150114517-6daf8faa-7ff4-4e18-a757-4ad50e4eee3d.png)

## 👶 Dependencies
* [Python 3.8 or higher](https://www.python.org/downloads/)
* [Git SCM](https://git-scm.com/downloads)
* [Docker](https://docs.docker.com/get-docker/)

## 🛠️ Installation
* ### From GitHub
Step 1: 
```sh
git clone https://github.com/e0xextazy/gender-est.git
```
Step 2: 
```sh
cd gender-est
```
Step 3:
```sh
docker build -t <IMAGE_NAME> .
```
Step 4:
```sh
docker run -d -p 5000:5000 <IMAGE_NAME>
```

* ### From DockerHub
Step 1: 
```sh
docker pull mbaushenko/gender-classification-mobilenet_v2:mvp_V2
```
Step 2:
```sh
docker run -d -p 5000:5000 mbaushenko/gender-classification-mobilenet_v2:mvp_V2
```

* ### From PyPI
Soon...

## 🚀 Usage

* ### From GitHub/DockerHub
```sh
python3 utils/send_data.py
```

* ### From PyPI
Soon...

## ⚖️ License
[MIT © 2022 Mark Baushenko](https://github.com/e0xextazy/gender-est/blob/main/LICENSE)
