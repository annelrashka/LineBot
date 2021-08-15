# Milestone02_K04
## SELEKTA : Seleksi Fakta
Sebuah Bot yang dibuat untuk meminimalisir penyebaran hoax<br><br>
Diciptakan oleh Kelompok 4 - Epimilis

## Anggota (Kelompok 4 - Epimilis)
| Nama               | NIM     | Job Desc  |
|--------------------|---------|-----------|
| Gresya Angelina Eunike Leman | 16520082 | Desain Karakter, Backend Utility (Command Help) |
| Frederik Imanuel Louis | 16520103 | Backend Main |
| Andreana Hartadi Suliman | 16520113 | Desain Karakter, Backend Utility (Error Message) |
| Wesly Giovano | 16520363 | Deploy Heroku, Bot (OA) Set Up |
| M Syahrul Surya Putra | 16520430 | Backend Utility (Validasi + Prefix) |
| David Nathanio Gabriel Siahaan | 16520432 | Backend Utility (Command Creator) |
| Annel Rashka Perdana | 16520448 | Backend Main |
| Afkar Dhiya Ulhaq | 16520452 | Backend Utility (QA) |
| Rifki Kaida | 16520496 | Backend Utility (Welcome Message) |

## Cara Menggunakan

Heroku settings:

Config vars: 

CHROMEDRIVER_PATH=/app/.chromedriver/bin/chromedriver

Buildpacks:

heroku/python

https://github.com/heroku/heroku-buildpack-chromedriver

https://github.com/heroku/heroku-buildpack-google-chrome.git



Heroku deploy:

heroku ps:scale worker=1

heroku ps:scale web=1

