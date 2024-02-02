# JPG to PDF - Simple solution to fix simple problem
<a name="readme-top"></a>
## About The Project
I made it for the use in WebCon APP - since app does not support jpg natively.
## Types of Files:

* JPG to PDF - Standard Version
it takes every jpg and makes pdf copy in selected new location

* Del to PDF - Eco Version
does exacly the same but instead of saving them it just deletes it

* JPG to Loop -
does the same as jpg to pdf but i accidentaly writen it again

<p align="right">(<a href="#readme-top">back to top</a>)</p>

# Getting Started
With this quick tutorial we help we can guide you with instalation and startup

## Prerequisites

To even start our Instalation process u need to have python & pip installed
* [![VS][py.dev]][py-url]
* [![VS][pip.dev]][pip-url]

## Instalation
1. Clone the repo
 ```sh
   git clone https://github.com/SARSUnicorn/jpgtopdf
   ```

2. Install Pillow for handling pictures
 ```sh
   pip install Pillow
   ```
3. Install  reportlab to handle pdf operation
 ```sh
   pip install reportlab
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Configuration

In every file go to the bottom part until u find main_loop
```
def main_loop():
    input_folders = ["C:/data/companya", "C:/data/companyb", "C:/data/companyc"]
    archive_path = "C:/data/arch.zip"
```
write ur preffered folders into input_folder
and (if u selected archiving variant) ur prefered archive path


<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Licence

Created and updated by
* Marcin Gut-Borowy -  [![sars][git.dev]][sars-url]   [![sars2][linked.dev]][sars2-url] 
Under an [MIT licence](https://en.wikipedia.org/wiki/MIT_License)

<p align="right">(<a href="#readme-top">back to top</a>)</p>







[py.dev]:https://img.shields.io/badge/Python-3.9-green
[py-url]:https://www.python.org/downloads/

[pip.dev]:https://pypi-camo.freetls.fastly.net/cd7ef4975d71b4a87a35b3c01b5b1ec8481c4549/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f7069702e737667
[pip-url]:https://pypi.org/project/pip/


[sars2-url]: https://www.linkedin.com/in/marcin-gut-borowy-4b4854203/
[sars-url]: https://github.com/SARSUnicorn
[git.dev]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[linked.dev]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
