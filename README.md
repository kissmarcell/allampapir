# Hungarian Government Bonds Archiver

[![Automated Bond Archiver](https://github.com/kissmarcell/allampapir/actions/workflows/autorun.yml/badge.svg)](https://github.com/kissmarcell/allampapir/actions/workflows/autorun.yml)

## Description
This is a simple Python application that regularly downloads the latest rates of government bonds from the [website](https://www.allampapir.hu/kincstari_arfolyamjegyzes/) of the Government Debt Management Agency of Hungary and then commits it inside this same repository, via GitHub Actions.

## Schedule
The application is scheduled to run at a given time, specified in the GitHub Action .yml file. [According to GitHub](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#schedule), it may not run at the exact time specified during high loads. The exact moment of execution is stored in the commit name.

## Disclaimer
This application is not affiliated with the [Government Debt Management Agency of Hungary (ÁKK)](https://www.akk.hu/) or the [Hungarian State Treasury (MÁK)](https://www.allamkincstar.gov.hu/) in any way. The author is not responsible for any damage caused by the use of this application.
