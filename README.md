# Logs Analysis Project

### by Louis Magdaleno

Logs Analysis Project, part of the Udacity
[Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Project purpose
To write SQL queries to answer the following questions about a PostgreSQL
database containing the logs of a fictional newspaper website.

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Required Libraries and Dependencies
The project code requires the following software:

* Python 3.5.2
* psycopg2 2.7.3.2
* PostgreSQL 9.5.10

You can run the project in a Vagrant managed virtual machine (VM) which includes
all the required dependencies (see below for how to run the VM). For this you
will need [Vagrant](https://www.vagrantup.com/downloads) and
[VirtualBox](https://www.virtualbox.org/wiki/Downloads) software installed on
your system.

## Project contents
This project consists of the following files:

* `log_analysis_tool.py` - The Python program that connects to the PostgreSQL
  database, executes the SQL queries and displays the results.
* `newsdata.zip` - A zip file containing a file that populates the `news`
  PostgreSQL database.
* `README.md` - This read me file.
* `Vagrantfile` - Configuration file for the Vagrant virtual machine.

## How to Run the Project
Download the project zip file to your computer and unzip the file. Or clone this
repository to your desktop.

Open the text-based interface for your operating system (e.g. the terminal
window in Linux, the command prompt in Windows) and navigate to the project
directory.

### Bringing the VM up
Bring up the VM with the following command:

```bash
vagrant up
```

The first time you run this command, it will take awhile, as Vagrant needs to
download the VM image.

You can then log into the VM with the following command:

```bash
vagrant ssh
```

More detailed instructions for installing the Vagrant VM can be found
[here](https://www.udacity.com/wiki/ud197/install-vagrant).

### Make sure you're in the right place
Once inside the VM, navigate to the tournament directory with this command:

```bash
cd /vagrant
```

### Load the logs into the database
First, unzip the zip file with the command:

```bash
unzip newsdata.zip
```

Then run the following command to load the logs into the database:

```bash
psql -d news -f newsdata.sql
```

### Creating required Views
Run the following command to connect to the psql database.

```bash
psql news
```

Create View VIEW_top_three_articles
Run the following command.

```bash
CREATE VIEW VIEW_top_three_articles
AS
            SELECT articles.title,
                   count(*) as article_views
            FROM   log,
                   articles
            WHERE  log.path = '/article/' || articles.slug
            GROUP BY articles.title
            ORDER BY article_views DESC
            LIMIT 3;"""
```

Create View VIEW_most_popular_articles
Run the following command.

```bash
CREATE VIEW VIEW_most_popular_authors
			AS
			SELECT authors.name,
                   count(*) as author_views
            FROM   log ,
                   articles JOIN
                   authors ON articles.author = authors.id
            WHERE  (log.path = '/article/' || articles.slug)
            GROUP BY authors.name
            ORDER BY author_views DESC;
```

Create View VIEW_days_with_over_one_percent_errors
Run the following command.

```bash
CREATE VIEW VIEW_days_with_over_one_percent_errors
AS
WITH num_requests AS (                                                              
                SELECT time::date AS day, count(*)
                FROM log
                GROUP BY time::date
                ORDER BY time::date
              ), num_errors AS (
                SELECT time::date AS day, count(*)
                FROM log
                WHERE status != '200 OK'
                GROUP BY time::date
                ORDER BY time::date
              ), error_rate AS (
                SELECT num_requests.day,
                  num_errors.count::float / num_requests.count::float * 100
                  AS error_pc
                FROM num_requests, num_errors
                WHERE num_requests.day = num_errors.day
              )
            SELECT * FROM error_rate WHERE error_pc > 1;
```

### Running the reporting tool
The logs reporting tool is executed with the following command:

```bash
python3 log_analysis_tool.py
```

The answers to the three questions should now be displayed.

### Shutting the VM down
When you are finished with the VM, press `Ctrl-D` to log out of it and shut it
down with this command:

```bash
vagrant halt
```
