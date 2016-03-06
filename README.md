theRealPOD is a project for learning. It uses PostgreSQL, Redis, DynamoDB, Elastic Beanstalk and Django.

This project uses Continuous Integration. Unit tests are run on every pull request via a Jenkins server.

As of now it is a basic webpage that uses 3 links (DB, Cache, NoSQL) to track page views. Each time DB is clicked its page views are updated in a PostgreSQL database hosted on AWS. Each time Cache is clicked its page views are updated in a Redis cache hosted on AWS. Each time NoSQL is clicked its page views are updated in a DynamoDB table hosted on AWS.
