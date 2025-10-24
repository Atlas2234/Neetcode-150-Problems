"""
Time complexity is O(n * k), where n is the number of strings in the input list and k is the maximum length of a string in the list.
Dictionary lookups and insertions take O(k) time in the average case, as we need to process each character in the string to build the character count dictionary.
Dictionary comparisons also take O(k) time in the average case because we need to compare the character counts for each character in the strings.

Space complexity is O(n * k) in the worst case, where all strings are unique and stored in the final list along with their character count dictionaries.
"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Create a list to store different sets. Each set will contain all characters in a string, unordered.
        dictList = []
        # Create a parallel list of lists of strings that has the indices that match the setList
        strList = []

        # Loop thorugh strings list
        for s in strs:
            # Create a temporary word dictionary which will store each unique letter in the word and its count
            wordDict = {}
            # Create a temporary list which will be used to store a new word that is not recognized as an anagram yet
            slist = []

            # Construct the temporary word dictionary
            for ch in s:
                if ch not in wordDict:
                    wordDict[ch] = 1
                else:
                    wordDict[ch] += 1
            
            # If the temporary dictionary is not in the dictionary list that means this word is not an anagram of any of the existing
            # recorded words yet so append the dictionary into that list
            # and append the string to the temporary string list and append that temporary string list to the final string list
            if wordDict not in dictList:
                dictList.append(wordDict)
                slist.append(s)
                strList.append(slist)
            # If the temporary dictionary is in the dictionary list that means this word is an anagram of a recorded word.
            # Find the index where of the dictionary that has the recorded word and append the list of words in that index.
            else:
                for i in range(len(dictList)):
                    if dictList[i] == wordDict:
                        strList[i].append(s)
                
        return strList
    
"""
A slower but cleaner solution.

Time complexity is O(n * l Log l), where n is the number of strings in the input list and l is the maximum length of a string in the list.
Space complexity is O(n * l) in the worst case, where all strings are unique and stored in the final list.
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # The dictionary with each unique word. Key is the sorted word and the value is the index of that word in the final list
        checkDict = {}

        # The final list to be returned
        finList = []

        # Index of the final list
        index = 0
        # Loop through the string list
        for s in strs:
            # Temporary list to store new non anagram words
            tempList = []

            # Sort the word
            x = ''.join(sorted(s))

            # Check if the word exists in the set
            if x not in checkDict:
                checkDict.update({x: index})
                tempList.append(s)
                finList.append(tempList)
                index += 1
            else:
                finList[checkDict[x]].append(s)
        
        return finList


                