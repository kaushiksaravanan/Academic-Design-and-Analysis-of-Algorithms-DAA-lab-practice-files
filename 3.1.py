string=input()
string=string.upper()
words=string.split()
no_words=len(words)

dict_freq={}
curr_ind=0
for word in words:
    for letter in word:
        if letter in dict_freq:
            word_ind=dict_freq[letter][1]
            if word_ind!=curr_ind:
                freq_old=dict_freq[letter][0]
                dict_freq[letter]=(freq_old+1,curr_ind)
        if letter not in dict_freq:
            dict_freq[letter]=(1,curr_ind)
    curr_ind+=1
no_distinct=len(dict_freq)
curr_ind=0
for i in dict_freq:
    if curr_ind+1==no_distinct:
        print(i+'-'+str(dict_freq[i][0]))
    else:
        print(i+'-'+str(dict_freq[i][0]),end=',')
    curr_ind+=1
#tc o(letters)
#sc o(n)