#!/usr/bin/env python3
# 
from collections import namedtuple

# less than 100 titles
TITLES = """
A Beautiful Mind (2001)
Ace Ventura: Pet Detective (1994)
Aladdin (1992)
Almost Famous (2000)
Amelie (2001)
American Beauty (1999)
Apollo 13 (1995)
Back to the Future (1985)
Batman (1989)
Batman Begins (2005)
Batman Forever (1995)
Beauty and the Beast (1991)
Braveheart (1995)
Cast Away (2000)
Catch Me If You Can (2002)
Charlie's Angels (2000)
Chicken Run (2000)
Clear and Present Danger (1994)
Crouching Tiger Hidden Dragon (Wo hu cang long) (2000)
Dances with Wolves (1990)
Die Hard: With a Vengeance (1995)
Donnie Darko (2001)
Dumb & Dumber (1994)
E.T. the Extra-Terrestrial (1982)
Erin Brockovich (2000)
Eternal Sunshine of the Spotless Mind (2004)
Fargo (1996)
Fight Club (1999)
Finding Nemo (2003)
Forrest Gump (1994)
Gladiator (2000)
Harry Potter and the Chamber of Secrets (2002)
Harry Potter and the Sorcerer's Stone (a.k.a. Harry Potter and the Philosopher's Stone) (2001)
High Fidelity (2000)
Independence Day (a.k.a. ID4) (1996)
Jurassic Park (1993)
Kill Bill: Vol. 1 (2003)
Kill Bill: Vol. 2 (2004)
Lost in Translation (2003)
Meet the Parents (2000)
Memento (2000)
Men in Black (a.k.a. MIB) (1997)
Minority Report (2002)
Mission: Impossible (1996)
Mission: Impossible II (2000)
Monsters Inc. (2001)
Mrs. Doubtfire (1993)
O Brother Where Art Thou? (2000)
Ocean's Eleven (2001)
Pirates of the Caribbean: The Curse of the Black Pearl (2003)
Pretty Woman (1990)
Pulp Fiction (1994)
Raiders of the Lost Ark (Indiana Jones and the Raiders of the Lost Ark) (1981)
Requiem for a Dream (2000)
Saving Private Ryan (1998)
Schindler's List (1993)
Seven (a.k.a. Se7en) (1995)
Shrek (2001)
Shrek 2 (2004)
Sin City (2005)
Snatch (2000)
Speed (1994)
Spider-Man (2002)
Spider-Man 2 (2004)
Star Wars: Episode II - Attack of the Clones (2002)
Star Wars: Episode IV - A New Hope (1977)
Star Wars: Episode V - The Empire Strikes Back (1980)
Star Wars: Episode VI - Return of the Jedi (1983)
Stargate (1994)
Terminator 2: Judgment Day (1991)
The Bourne Identity (2002)
The Bourne Supremacy (2004)
The Dark Knight (2008)
The Departed (2006)
The Fugitive (1993)
The Godfather (1972)
The Incredibles (2004)
The Lion King (1994)
The Lord of the Rings: The Fellowship of the Ring (2001)
The Mask (1994)
The Matrix (1999)
The Matrix Reloaded (2003)
The Patriot (2000)
The Rock (1996)
The Shawshank Redemption (1994)
The Silence of the Lambs (1991)
The Sixth Sense (1999)
The Usual Suspects (1995)
Titanic (1997)
Toy Story (1995)
Traffic (2000)
True Lies (1994)
Twelve Monkeys (a.k.a. 12 Monkeys) (1995)
Twister (1996)
Unbreakable (2000)
V for Vendetta (2006)
X-Men (2000)
X2: X-Men United (2003)
"""

class Prefix(namedtuple('Prefix', 
                                 [
                                  'index', 
                                  'full_title'
                                 ])
                              ):
    __slots__ = []
    def __hash__(self):
        return hash(str(self).lower())

    def __str__(self):
        return self.full_title[:self.index].lower()

    def __lt__(self, other):
        return str(self) < str(other)

    def __repr__(self):
        return f'Prefix(\'{self.full_title}\'[:{self.index}])'

def build_title_index(lines):
    LEN_MAP = dict()

    for line in lines:
        title = line.strip()
        length = len(title)
        for i in range(1, length + 1):
            if i not in LEN_MAP:
                LEN_MAP[i] = dict()
            item = Prefix(i, title,)
            key = str(item)
            if key not in LEN_MAP[i]:
                LEN_MAP[i][key] = set()

            LEN_MAP[i][key].add(item)
    return LEN_MAP

def search_loop(index_search_map):
    import pprint
    whole_word = ''
    while (line := input('movie title: ')):
        title = line.strip()

        assert len(title) in index_search_map
        prefix_map = index_search_map[len(title)]
        if prefix_map:
            a_prefix = Prefix(len(title), title)
            key = str(a_prefix)
            if key in prefix_map:
                pprint.pprint(prefix_map[key])

if __name__ == '__main__':
  index_search_map = build_title_index(TITLES.splitlines())
  search_loop(index_search_map)
