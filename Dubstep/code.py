# Written: 20-Apr-2020
# https://www.codewars.com/kata/551dc350bf4e526099000ae5/train/python

def song_decoder(song):
    return ' '.join(song.replace('WUB',' ').split())
