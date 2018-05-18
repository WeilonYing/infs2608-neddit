# infs2608-neddit
Repo: https://github.com/WeilonYing/infs2608-neddit

Live demo: http://whale.moe/neddit

Walkthrough: https://www.youtube.com/watch?v=Yq9s1P6BKF8

Information Systems project by Group Fourteen for the course INFS2608 at the
University of New South Wales.

## Overview
“Neddit” is a web-based concept that offers a forum for peer-to-peer learning
derived from authenticated user-generated content. Distinct from existing
services, Neddit provides value-adding insights into coursework and academic
student life for UNSW communities by creating an accessible platform for current
students, staff and UNSW alumni across degree disciplines and years of study to
create discussions based on student experiences. The authentication of users and
content is verified via user reviews of shared resources and discussion points,
with a voting system which allows the most relevant and insightful posts to be
voted up. Hence, the core features of Neddit entails uploading user-generated
content and different user types; general users, top contributors and moderators.

## The Team
Group Fourteen comprises of five university students with disciplines in Commerce,
Marketing, Information Systems and Computer Science:
- Irene Dao - Project Head
- Justin Yap - Business & Requirements Analyst
- Katherine Chen - Marketing & Design
- Malin Wijesuriya - Business & Requirements Analyst
- Weilon Ying - Software Engineer & Architect

## Dependencies
This project depends on Python 3.6+ and Django 2.0+. It also depends on the
bootstrap4 form plugin.

## Development & Testing Environment Setup
- Use of your favourite Python virtual environment is highly recommended.
  `virtualenv` is a good one if you don't know where to start.
- Create your virtual environment. Ensure your Python version is set to 3.6 or higher.
- Enter your virtual environment and install `django` with pip (i.e. `pip install django`)
- Install [bootstrap4 plugin](https://github.com/zostera/django-bootstrap4)
  - You can do this by typing in `pip install django-bootstrap4`.
- Clone this repository `git clone https://github.com/WeilonYing/infs2608-neddit.git`
- Navigate to the `neddit` directory and initialise the SQLite database with
  `python manage.py migrate`
- Start the local development web server by running `python manage.py runserver`
- By default, your server will be located at `127.0.0.1:8000`. Navigate to this
  IP using your web browser to test your build of Neddit.

Further development tutorials can be found on [Python Docs](https://docs.python.org)
and [Django Project](https://www.djangoproject.com/)

## Credits
- [Django Project](https://www.djangoproject.com/)
  - [bootstrap4 plugin](https://github.com/zostera/django-bootstrap4)
- [Python](https://www.python.org/)
- [Bootstrap Framework](https://getbootstrap.com/)

## Disclaimer
This is a university software project built for the sole purpose of prototyping
a hypothetical crowdsourcing tool for the students of University of New South Wales.
Neddit is not an actual website, and is not affiliated with the University of
New South Wales in any shape or form.

This code was also hacked together over the course of two weeks by a former
[Facebook software engineer intern](https://linkedin.com/in/weilonying/), with a
lot of googling, tears and elbow grease. There are probably some bugs around.
This software is provided as is, without warranty. While it shouldn't happen,
we won't take any responsibility if the use of this project somehow breaks or
violently disassembles your computer.

## Can I distribute, modify and make derivatives of this work?
Feel free to use the code written here for your own projects, but we do ask that you
credit us if you do so. The best way to do this is to link back to this repository.

Happy coding :)
