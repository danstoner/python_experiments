### GatorLUG Codeslinger 2011 Problem
### http://www.gatorlug.org/node/315

Problem
-------
Given a list of words, we want to know all permutations of each word that
result in matching words of a dictionary.

Assuming the English dictionary, some valid permutations are as follows:


    Word                              Valid Permutations
    -------------------------------   ----------------------------
    apt                               pat, tap
    ate                               eat, tea
    care                              race
    monday                            dynamo
    plates                            staple


Input
-----
Number of dictionary words will be from 0 to 200000.
Each word will be on its own line.
All characters will be lower case alpha.

Standard Input Format:

    [NUM_DICTIONARY_LINES]
    [DICTIONARY_WORD_LINES]
    [LOOKUP_WORD_1]
    [LOOKUP_WORD_2]
          .
          .
          .
    [LOOKUP_WORD_N]
    [EOF]


Output
------
Standard output; write out the lookup word followed by each of its valid
permutations in lexicographical order;

Example
-------
Input:

    6
    apt
    ate
    tap
    pat
    care
    race
    apt
    tap
    care

Output:

    apt pat tap
    tap apt pat
    care race
