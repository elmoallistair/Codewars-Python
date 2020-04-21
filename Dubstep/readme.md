# Dubstep

## Instructions
Recently, Jonny has heard Polycarpus's new dubstep track, but since he isn't into modern music, he decided to find out what was the initial song that Polycarpus remixed. Help Jonny restore the original song.
Input

The input consists of a single non-empty string, consisting only of uppercase English letters, the string's length doesn't exceed 200 characters
Output

Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.

Examples
```
song_decoder("WUBWEWUBAREWUBWUBTHEWUBCHAMPIONSWUBMYWUBFRIENDWUB")
  # =>  WE ARE THE CHAMPIONS MY FRIEND
```

## Solution
```
def song_decoder(song):
    return ' '.join(song.replace('WUB',' ').split())
```
