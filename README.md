
# Portfolio Project - Musicfy

I chose to do my project on a representation of Spotify. My database includes tables for users, playlists, songs, artists, and albums. It also includes one linking table that represents songs that are featured on playlists. 

The functions include:
1. users creating a playlist
2. playlist featuring a song
3. songs belonging to an album
4. songs written by an artist
5. albums belonging to an artist



API Reference Table

| Endpoint Paths | Methods | Parameters
| -------------- | ------- | -----------
|     /Users     |   GET   | users
|     /Users     |   GET   | users/id
|     /Users     |   POST  | users
|     /Users     |  DELETE | users/id
|     /Albums    |   GET   | albums
|     /Albums    |   GET   | albums/id
|     /Albums    |   POST  | albums
|     /Albums    |  DELETE | albums/id
|   /Playlists   |   GET   | playlists
|   /Playlists   |   GET   | playlists/id
|   /Playlists   |   POST  | playlists
|   /Playlists   |   POST  | playlists/song_id/features
|   /Playlists   |  DELETE | playlists
|    /Artists    |   GET   | artists
|    /Artists    |   GET   | artists/id
|    /Artists    |   POST  | artists
|    /Artists    |  DELETE | artists/id
|    /Songs      |   GET   | songs
|    /Songs      |   GET   | songs/id
|     /Songs     |  POST   | songs
|     /Songs     |  DELETE | songs/id






This project's evolution was brutal... My first attempt at some of the tables did not include an ID. I was expecting to be able to work off of just a name or title and that was a bad mistake. I also struggled with the relationships and where to include which ID on which corresponding connected tables. I ended up redoing my tables several times due to missing information when inserting data, nullability issues, datetime errors, missing columns, etc. Despite all of that I was able to successfully create 6 working tables that can connect where needed. 

I chose the ORM approach due to the fact that there was more learning material on this method within the four week course. I do feel like I understand the benefits of this method much more now than when the topic was introduced within the course. With that being said, I do believe that I could use much more practice learning raw SQL.

This database has endless amounts of future improvements available given that it mimicks Spotify. Currently, my playlists table only includes titles and users. I could create new tables for each playlist and the songs on it. I could add playlist length. I could also create a way for users to share their playlists with other users. I could include songs that are written by more than one artist. Honestly, I am just suprised I got this far...
# PORTFOLIOPROJECT_LC
