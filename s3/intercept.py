""" 
:mod:`intercept` -- Dead parrot access
===================================

.. module:: intercept
    :platform: Unix, Windows
    :synopsis: Analyze and reanimate dead parrots.
.. moduleauthor:: Eric Cleese <eric@python.invalid>
.. moduleauthor:: John Idle <john@python.invalid>

What happens if I put something up here?
Do a bit of maths: :math:`x^2`
Write some more stuff :math:`x`.
hellow?

"""

def x_intercept(m, b):
    """Brief synopsis on 1 line, COMPULSORY
    Return the x intercept of the line y=m*x+b.  The x intercept
    of a line is the point at which it crosses the x axis (y=0).
 
    This is a longer explanation, which 
    may include math :math:`\\alpha`, which is OPTIONAL
 
    Followed by compulsory sections: 
      - "Parameters"
      - "Returns"
      - "Examples"
 
    The "Returns Type" section being optional
 
    The "Examples" uses the doctest syntax. They must be self consistent as much as possible, 
    and they can be copy and paste into a ipython session.
 
    Note the syntax for the "parameters": 
    [2 spaces, a dash, a space, a backquote, argument name, backquote, space, (type), space, dash, space, description]
 
    Then, add optional section using sphinx directives ".. todo::, ".. warnings::" etc. 
 
    Note again the space between ".." and    the keyword.
 
    Add 1 blank line betweem sections
 
    Add indentation when starting the content of a section.
 
    :Parameters:
      - `arg1` (int,float,...) - the first value
      - `arg2` (int,float,...) - the first value
      - `arg3` (int,float,...) - the first value
 
    :Returns:
        arg1/arg2 +arg3
 
    :Returns Type:
        int,float 
 
    :Examples:        
 
    >>> import template
    >>> a = MainClass()
    >>> a.function2(1,1,1)
    2
 
    .. note:: can be useful to emphasize 
        important feature (NOTE THE INDENTATION)
    .. seealso:: :class:`MainClass2`
    .. warning:: arg2 must be non-zero.
    .. todo:: check that arg2 is non zero.
    """
    return -b/m
