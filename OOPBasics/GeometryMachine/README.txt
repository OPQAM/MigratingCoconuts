# README file

"""
The idea behind this small program was to recall the stuff
I've learned about Python OOP. It would have been much easier
to just use some other programming paradigm, and it would
have been easier, but the difficulty and learning slope
of OOP were my aim.

1 - I started by creating a user menu (main_menu) and adding
different options related to the creation of points and
calculating the distance between them.

2 - I then added the capacity to keep changes, so that each
new session allowed for the possibility of saving the created
points, adding new points, etc. This was accomplished by
creating a list of points, and saving said list to a simple
txt file. Finally, I added controls and exceptions so that
the program won't crash with bad user input.

3 - Stepping forward, I added some more functionality by
allowing for the deletion of points. So, the user can now
create new points, delete said points, and choose to save or
not to save the currently created points.
Worthy of note is that the points.txt file is automatically
created once the user adds the first point.

4 - Once that had been done, I added a new class Lines,
with its respective functionality (the user can create and
remove lines - these are created from existing points, and
they can also display said lines in its standard form).
The save functionality was removed and joined together with
the exit functionality. Upon exiting the program, all points
and lines are saved automatically.

5 - To finish this initial stage of the process, I've added
comments and notes so that the user can constantly be
informed of what is happening.

To be done:

- Adding more functionality - I'm keeping on with the theme
of geometry. So I'll intercept lines, I'll add squares and
other 2D objects as well. Might consider adding movement.

- Hunt for bugs and bad code - need to keep on doing this.
I'm certain, as I type, that there are exceptions and issues
that will break my code. I just haven't found them yet.

- Adding a visual support - namely though turtles (which I
haven't touched in years) or perhaps PyGame (which I've
never tried before).

- Place all this work and place it in my GitHub. Adding to
my repository is a pretty good idea, and ensures that I can
work on this little thing whenever and wherever I'd like.

- Perhaps adding submenus - otherwise we'll start having
tens of items to choose from. Adding submenus might make it
all cleaner and a better experience overall.



"""
