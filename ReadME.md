<img src="https://i.imgur.com/4fl55Df.jpg"/>

> Daily COVID monitoring via WhatsApp Automation

## Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Getting Started](#getting-started)
- [Next Steps](#next-steps)
- [Installations](#installation)

## About
This script allows you to automate the process of checking active cases within your country of choice.

## Features
- Updates daily at 9 am via the Seamlesss Cloud Service
- Updates on ACTIVE Covid Cases via Covid API
- Sends message via WhatsApp via Twilio

## Tech Stack
- Python
- Seamless Cloud
- Twilio

## Getting Started
1. Set up a Twilio account and connect it to WhatsApp via Sandbox
2. Update the Python Script with the OUTBOUND and "from" numbers.
3. Upload the Python Script into the Seamless Cloud for it to run daily!

## Next Steps
- Allow for users to reply with checking country of choice cases.
- Application should provide recommendations based on COVID activity in country

## Installation
- pip3 install twilio.rest
- pip3 install covid
