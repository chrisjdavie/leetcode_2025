### Got right

#### l_0088_merge_sorted_array
2025/03/23
- didn't get solution first time
- errors in coding
- - typos
- - not thinking correctly about exit conditions

2025/03/24
- although I got it right before running it, 2 mistakes during writing
- - got an equality the wrong way round
- - forgot to decrement the indicies

2025/04/03
- solved it correctly


#### l_0080_remov_duplicated_from_sorted_array_ii
2025/03/24
- got order of operations wrong
- did the wrong thing with range
- solution can be much more elegant

2025/04/03
- solved it correctly
- different way of thinking about it using pointers, so should try that too
- implemented pointer approach. During optimisation, made an error, but probably won't count that for revisiting


#### l_0055_jump_game
2025/03/27
- basically everything
- didn't read the instructions carefully, and it all went wrong

2025/04/06
- solved it correctly


#### l_0380_insert_delete_getrandom_o1
2025/04/13
- got lost in thinking if I can pull random from a hashmap
- didn't think of the obvs thing I could do with a list here

2025/04/14
- solved it correctly


#### l_0238_product_of_array_except_self
2025/04/14
- my solution was correct and worked first time, but found a clearer solution in other peoples submissions (and showed a clearer mental model of the problem)

2025/04/15
- solved it well


#### l_0134_gas_station
2025/04/15
- got the brute force right
- touched on the correct high speed answer, but didn't think it through
- my answer was right ball park, but less elegent
- solution coppied from someone else shows more intuition for the problem

2025/04/16
- solved it well


#### l_0055_jump_game_ii
2025/03/27
- didn't twig the obvious algorithm

2025/04/06
- didn't twig the obvious algorithm, again...

2025/04/13
- kinda messy in the order of things
- got the zero index wrong

2025/04/30
- solved it well


#### l_0199_binary_tree_right_side_view
2025/05/07
- solved it, buuuut, made a real mess of the tests, did not read or think about the code. Not going to hit myself for that, but it's worth being aware of if I do it more than once


----------------

### To revisit - conceptual

#### l_0017_letter_combinations_of_a_phone_number
2025/05/27
- I mostly got this right, but messed up thinking about the implementation, dived right in

#### l_0909_snakes_and_ladders
2025/05/22
- this is a bfs solution to do optimally - I think you need to think about it in terms of what you're trying to minimise, the number of moves, and always process the fewest. Therefore, if you've enqueued a position in the same or fewer number of moves, you don't have to do it again
- a way to do this in bfs is to store a map of pos: moves, and if you're in a pos in more moves, skip it

2025/05/26
- got the bit at the start wrong, and its mainly because I wasn't brining the correct focus to the problem. Need to do better I think

2025/05/28
- issues in the bit at the beginning, different from above. I need to practice gently bringing my attention to code tbh

#### l_maximum_subarray
2025/06/11
- missed the simple solution (very similar to the rain problem, except simpler). Ah well.


----------------

### To revisit - coding details

#### l_0125_valid_palindrome
2025/03/25
- got 2 things wrong with handling string cleaning...

#### l_0150_rotate_array
2025/03/26
- didn't go for obvious solution
- took me a while to understand the in place solution
- got some details in the place solution wrong

2025/04/06
- got most of the above, fluffed some of the coding

2025/04/14
- got it all correct, except when the index is greater than length

2025/04/26
- got it all correct, except didn't think carefully enough about iteration conditions

#### l_0209_minimum_size_subarray
2025/04/26
- didn't read the question fully
- got the min size and output slightly wrong

#### l_0274_h_index
2025/03/27
- got the O(1) memory and O(NlogN) time solution, but missed the
hashmap solution that is O(N) time and O(N) memory

2025/04/03
- got the solution fast, but really screwed up coding it well

2025/04/07
- forgot the return value of `<list>.sort`, again
- forgot what happens to a counter when you successfully leave a loop in Python
- forgot to look over the code afterwards before running

2025/04/28
- got confused with inequalities again...
- got really confused with inequalities. Starting to see how people do this stuff reliably though...

#### l_0036_valid_sudoku
2025/04/28
- got most right, but made a mistake at the end as to what I was indexing over

#### l_0015_3sum

2025/04/11
- first, quick solution good
- went down a weird side track with the optimization
- got stuck trying to think if there's an O(N) time solution, which there isn't structurally, and I think that's obvious?
- once I went back to a more sensibly optimized solution, I made a couple simple mistakes

2025/04/13
- single typo didn't catch by eye :_(

2025/04/29
- typo
- arguments to sorted wrong

#### l_0383_ransom_note

2025/04/29
- wasn't paying attention when defining variables


#### l_0169_majority_element
2025/03/24
- didn't go for the obvious solutions
- didn't go for the solution I knew, nerd sniped myself
- didn't know Moore's voting algorithm (fine, but know now)

2025/04/04
- forgot return type of `<list>.sort()` is `None` (I mean, of course it is but...)
- hashmap solution, got the break condition wrong, twice

2025/04/08
- didn't think in detail about the middpoint of the simple solution

2025/04/13
- thought in detail about the middpoint, but forgot arrays a zero-indexed

2025/04/14
- when using Counter, I got the interface for a method wrong

2025/05/02
- thought in detail about the middpoint, but forgot arrays a zero-indexed
- when using Counter, I got the interface for a method wrong
- accessed the first element in an array using `[1]`...

#### interviews/repeated_strings
2025/04/20
- struggled with counter behaviour in if statements

2025/04/21
- solved it - I was thinking incorrectly about loops, better now, but want to make sure I've got it

2025/05/05
- messed up in small ways, struggling less with this now but still not perfect

2025/05/06
- got it right, but keeping it here cos it was more of a struggle to get to this point than it should have been


#### l_0141_linked_list
2025/05/05
- the initial simple solution, I assumed the val was a representation of the node, when it was just a val in a linked list
- I didn't know you could add any object to a set so long as __repr__ isn't overloaded with something immutable
- there was a bit of mess in there
- I think, probably, I'm not that great at puzzles involving nodes

2025/05/06
- got it right, but keeping it here cos it should have been more straightforward getting it right


#### mine/find_maxima
2025/04/21
- I got confused with the ordering of things - it's easier if I make sure arguments are geometrically aligned with the problem

2025/04/22
- wasn't quite there with anticipating corner cases

2025/05/07
- couple of minor typos

#### l_0042_trapping_rain
2025/04/21
- Not solved yet, I got tied up in finding maxima and being confused

2025/04/22
- I got something very overcomplicated that worked, but I didn't think about it correctly. Classic working down a dead end. The Pythonic solution I came up with is nice though

2025/04/24
- got it right, but made 2 small typos. Picked one up before running, second caused the tests to fail

2025/05/08
- got it exactly backwards


#### l_0530_minimum_absolute_different_in_bst
2025/05/08
- there was a property of binary trees I didn't understand, so I came up with a working but slow and over complicated solution

2025/05/09
- made a typo


#### l_0200_number_of_islands
2025/05/09
- silly mistake in bounds checking


#### l_2095_find_median_from_a_data_stream
2025/05/14
- apparently I struggle with intution around comparing the length of heaps to each other, I get the inequality the wrong way round?...
- I checked the zeroth value of an empty list...

2025/05/15
- developing more fluency in coding with heaps, but still making small mistakes

2025/05/19
- I think there's an approach to this using values not sizes, need to think about that



#### l_0480_sliding_window_median
2025/05/14
- this came up in an interview, the way to solve it is much, much more straight forward if you've covered 295 first

2025/05/21
- I've found a simple solution that could be straightforwardly answered in time, and is clear. Now I have to make sure its in my mind :)


#### l_0208_implement_prefix_tree
2025/05/26
- didn't think to use a sentinel, simplify all this
- I wasn't very smooth in the implementation

2025/05/27
- better, bunch of typos today
