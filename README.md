# CodeSignal Developer Docs

A place to put documentation about interacting with our APIs.

## Running locally
You can view the documentation site locally by running `npm start` -- you just need to have Python 2 installed on your local machine.
The start script serves the docs here: http://localhost:8000

Since it's a static site, you can also just open `/docs/index.html` directly in a web browser if you prefer.

## Generating GraphQL docs
GraphQL API docs are generated with graphqldoc:
https://github.com/codesignal/graphqldoc

To generate documentation:
- Check out the main repository containing the GraphQL server.
- Run it the usual way so that GraphQL is accessible here: http://localhost:3000/graphql
- Check out this repository and run `npm install`, then `npm run build`.
- Static pages will be generated under `/docs/types`.
 - Make sure they look okay, then commit and push.
 
 ## How to publish updated docs
This repo is hosted with GitHub Pages, so any change under `/docs` on the `master` branch will be published here:
https://codesignal.github.io/graphql-api-docs/
Which in return should be redirected to this subdomain: developer.codesignal.com

That's it! You should see your changes there once they reach the master branch, as long as they are under `/docs`. 

Don't change the GraphQL `/docs/types/` pages manually, since your changes will be overwritten the next time those pages are generated.
It's okay to change other pages manually.
