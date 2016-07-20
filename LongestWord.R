# Longest Word
# 
# https://www.codeeval.com/open_challenges/111/
# 
# Challenge Description: In this challenge you need to find the longest word in
# a sentence. If the sentence has more than one word of the same length you
# should pick the first one. 

longestWordInSentence = function(sentence) {
  wordsInSentence = strsplit(sentence, " ")
  numberOfCharacters = lapply(wordsInSentence, nchar)
  indexOfLongestWord = Map(which.max, numberOfCharacters)
  unlist(Map(`[`, wordsInSentence, indexOfLongestWord))
}

inputFile = commandArgs(TRUE)[[1L]]
testCases = readLines(inputFile, warn = FALSE)
cat(longestWordInSentence(testCases), sep = "\n")
