# iReporter_api

[![Build Status](https://travis-ci.org/brucenelm/iReporter_api.svg?branch=develop)](https://travis-ci.org/brucenelm/iReporter_api)

[![Coverage Status](https://coveralls.io/repos/github/brucenelm/iReporter_api/badge.svg?branch=develop)](https://coveralls.io/github/brucenelm/iReporter_api?branch=develop)

## About
This is an API for an iReport application that allows users to report corruption and report things that need government intervention
## Goal
The goal of this project is to provide a uniform API for web frontend ireport applications.
## Features
With this API;
- You can create a user account - Registration
- You can login and log out - Authorization and Authentication
- You can create, view, update, and delete a red-flags and intervation in your user account

## API Documentation
Documentation for this API can be found at http://127.0.0.1:5000, when you run the application locally or you can
navigate to the [heroku](https://myurl) deployment and view the documentation
## Tools

- [Flask](http://flask.pocoo.org/) - this is a python micro-framework
## Requirements
- Python 2.7.1x+. preferably use Python 3.x.x+
## Tests

```
## Running the application

## Base URL for the API

```
#### Endpoints for ireport
HTTP Method|End point | Public Access|Action
-----------|----------|--------------|------
POST | /api/<version>/red-flags | False | Create an incident
GET | /api/<version>/red-flags | False | View all red-flags
GET | /api/<version>/red-flags/<int:red_flag_id> | False | View specific red-flag
PATCH | /api/<version>/red-flags/<int:red_flag_id> | False | Edits the location of a specific red-flag
PATCH | /api/<version>/red-flags/<int:red_flag_id>/comment | False | Edits the comments of a specific red-flag
DELETE | /api/<version>/red-flags/<int:red_flag_id>| False | Deletes a redflag with a given id


