# WhatsApp Marketing Automation for Car Rental Websites
An automation script for sending professional marketing messages to potential car rental business clients via WhatsApp Web.

## Overview
This Python script automates the process of sending personalized marketing messages to contacts from a CSV file through WhatsApp Web. It's specifically designed for promoting car rental website development services but can be adapted for other purposes.

## Features
Automated message sending to multiple contacts
Professional formatting preserved in messages
Clipboard-based content pasting for better formatting retention
Error handling for failed messages
Configurable delay between messages

## Prerequisites

Python 3.6+
Chrome browser installed
ChromeDriver matching your Chrome version
Internet connection
## Installation
Clone this repository:
git clone https://github.com/yourusername/whatsapp-marketing-automation.git
cd whatsapp-marketing-automation
Install required dependencies:
pip install selenium pyperclip
Download the ChromeDriver that matches your Chrome version and place it in your PATH or in the script directory.
## Usage
Create a CSV file named contact.csv with phone numbers in the first column:
212600000000
212611111111
212622222222
Note: Phone numbers should include country code without any + symbol or spaces
Run the script:
python whatsapp_sender.py
When the WhatsApp Web interface loads, scan the QR code with your phone within 40 seconds.
The script will automatically send messages to all contacts in the CSV file.
## Customization
You can modify the MESSAGE_TEMPLATE variable in the script to customize your marketing message:

python
MESSAGE_TEMPLATE = """Bonjour,

Je suis [Votre Nom], développeur web spécialisé dans la création de sites pour les sociétés de location de voitures.

...

Cordialement,
[Votre Nom]"""
## Example Message
The default message promotes car rental website development services with features like:

WhatsApp integration for customer communication
Contact forms for lead capture
Custom branding and responsive design
Strategy for increasing Google Maps reviews
## Important Notes
Use this tool responsibly and ethically.
Respect privacy laws and regulations in your region.
Avoid sending too many messages in a short period to prevent being flagged as spam.
Make sure you have the right to contact the people in your list.

## Website Template Example
The script includes a link to an example car rental website: https://car-rental-rho-sandy.vercel.app/



