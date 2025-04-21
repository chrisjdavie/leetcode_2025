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

----------------

### To revisit - algorithm

#### l_0135_candy
2025/04/16
- got the right answer, but wasn't optimal
- when optimizing, made 2 typos

### mine/find_maxima
2025/04/21
- I got confused with the ordering of things - it's easier if I make sure arguments are geometrically aligned with the problem

### l_0042_trapping_rain
2025/04/21
- Not solved yet, I got tied up in finding maxima and being confused

----------------

### To revisit - coding details

#### l_0150_rotate_array
2025/03/26
- didn't go for obvious solution
- took me a while to understand the in place solution
- got some details in the place solution wrong

2025/04/06
- got most of the above, fluffed some of the coding

2025/04/14
- got it all correct, except when the index is greater than length

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

#### l_0015_3sum

2025/04/11
- first, quick solution good
- went down a weird side track with the optimization
- got stuck trying to think if there's an O(N) time solution, which there isn't structurally, and I think that's obvious?
- once I went back to a more sensibly optimized solution, I made a couple simple mistakes

2025/04/13
- single typo didn't catch by eye :_(

#### l_0055_jump_game_ii
2025/03/27
- didn't twig the obvious algorithm

2025/04/06
- didn't twig the obvious algorithm, again...

2025/04/13
- kinda messy in the order of things
- got the zero index wrong


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


### interviews/repeated_strings
2025/04/20
- struggled with counter behaviour in if statements

2025/04/21
- solved it - I was thinking incorrectly about loops, better now, but want to make sure I've got it
