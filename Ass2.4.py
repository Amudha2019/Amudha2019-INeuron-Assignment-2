def largest_words(str1):
    word = "";
    all_words = [];
    str1 = str1 + " ";
    for i in range(0, len(str1)):
        if(str1[i] != ' '):
            word = word + str1[i];  
        else:
            all_words.append(word);  
            word = "";  
          
    large = all_words[0];  
   
#Find largest word in the str1  
    for k in range(0, len(all_words)):
        if(len(large) < len(all_words[k])):
            large = all_words[k];
    return large;

str1 = "Write a Java program to sort an array of given integers using Quick sort Algorithm.";  
print("Original Strings:\n",str1)
large = largest_words(str1)  
print("Largest word: " + large);
