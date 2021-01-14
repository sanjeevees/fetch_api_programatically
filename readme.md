# Fetch API Programatically Project

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#Installation)
  - [Usage](#usage)
- [Overview](#Overview)
- [Things I would add given more time](#things-you-would-add-given-more-time)
- [Contact](#contact)

<!-- ABOUT THE PROJECT -->

## About The Project

Extract the data from a publically accessible API programatically, propose a schema and store it in Staging table.

<!-- GETTING STARTED -->

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites

This project requires knowledge of Python

### Installation

Installing for bash:

1. Clone this repo

```sh
$ git clone https://github.com/sanjeevees/fetch_api_programatically.git
```

2. Change directory to above cloned repo

```sh
$ cd fetch_api_programatically
```

<!-- USAGE EXAMPLES -->

## Usage

To generate summary data file for given Chicago bird collision dataset please use below command

Running From bash::

```sh
#make sure that you are inside project("fetch_api_programatically") directory
$ python3 fetch_save_api.py --url "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=kgWJgJ5G3b2l7CpOStlTuquWTw5ugZJi" --tableName "staging_table" 
```
with dropTable

```sh
#make sure that you are inside project("fetch_api_programatically") directory
$ python3 fetch_save_api.py --url "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17?apiKey=kgWJgJ5G3b2l7CpOStlTuquWTw5ugZJi" --tableName "staging_table" --dropTable True
```

<!-- Overview -->

## Overview

The idea is to fetch data from any api and append it to table programmatically. The data fetched can be further used to connect with a visualization tool like Tableau or accumulated for later usage for analysis.

In the current implementation done using polygon api which is used for stocks. The API key generated is the free version which is passed with the URL as apiKey.

Data Description:

The data fetched from the polygon api gets the data for given set of days for a particular stock. The schema of response is controlled by polygon which when tested for the given url as above produces a JSON with one of the key 'results' generating nested JSON.

Concept note on implementation:

Fetch the response from the api, create a table programatically parsing the respone, insert the values into the table and prints the entire table.

It is not bounded by the specific api used to create, any api can be passed to it.

<!-- Things I would add given more time -->

## Things I would add given more time

Features: 

- Break the api into multiple calls for print data or only drop table.
- Include a shell script to make multiple calls
- Improve on error handling 
- It can only handle list of JSON with one layer nested JSON containing a list. Enable it to handle any data format.
- The schema defined is all varchar, using a libarary to detect each column type and add it programatically

<!-- CONTACT -->

## Contact

Sanjeev Ahuja - [Linkedin](https://www.linkedin.com/in/sanjeev-ahuja/), [Github](https://github.com/sanjeevees)

[Project Link](https://github.com/sanjeevees/fetch_api_programatically)

