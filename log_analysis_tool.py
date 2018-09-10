#!/usr/bin/env python3
"""Log Analysis Project for Full Stack Nanodegree by Udacity"""
import psycopg2

DBNAME = "news"


def three_most_popular_articles():
    """Queries and displays the top three most viewed articles."""
    conn = psycopg2.connect(database=DBNAME)

    cur = conn.cursor()

    query = 'VIEW_top_three_articles'

    cur.execute(query)

    result = cursor.fetchall()

    cur.close()

    conn.close()

    print()
    print('Three most popular articles of all time')
    print('=======================================')

    for result in results:
        print('"{title}" - {count} views'
              .format(title=result[0], count=result[1]))
    print()

    return


def most_popular_authors():
    """Queries and displays the Authors with the most views."""
    conn = psycopg2.connect(database=DBNAME)

    cur = conn.cursor()

    query = 'VIEW_most_popular_authors'

    cur.execute(query)

    result = cursor.fetchall()

    cur.close()

    conn.close()

    print()
    print('Three most popular authors')
    print('=======================================')

    for result in results:
        print('"{author}" - {count} views'
              .format(author=result[0], count=result[1]))
    print()

    return


def days_with_high_errors():
    """Queries and displays the days when errors were above 1%."""
    conn = psycopg2.connect(database=DBNAME)

    cur = conn.cursor()

    query = 'VIEW_days_with_over_one_percent_errors'

    cur.execute(query)

    result = cursor.fetchall()

    cur.close()

    conn.close()

    print()
    print('Days with over 1% errors')
    print('=======================================')

    for result in results:
        print('"{day}" - {error_rate} errors'
              .format(day=result[0], error_rate=result[1]))
    print()

    return


def main():
    three_most_popular_articles()
    most_popular_authors()
    days_with_high_errors()


if __name__ == '__main__':
    main()
