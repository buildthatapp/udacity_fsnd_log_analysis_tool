#!/usr/bin/env python3
"""Log Analysis Project for Full Stack Nanodegree by Udacity"""
import psycopg2

DBNAME = "news"

def three_most_popular_articles():
    """Queries and returns top three most viewed articles in the news database."""
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
    """Queries and returns top three most viewed articles in the news database."""
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
def main():
    three_most_popular_articles()

if __name__ == '__main__':
    main()

    
