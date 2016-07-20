# Reverse Words
# 
# https://www.codeeval.com/open_challenges/8/
#
# Challenge Description: Write a program which reverses the words in an
# input sentence. 

reverseWords = function(inputSequence) {
  splittedWords = strsplit(inputSequence, " ")
  vapply(splittedWords, function(x) {
    wordsInReverse = rev(x)
    paste(wordsInReverse, collapse = " ")
  }, character(1L))
}

inputFile = file(commandArgs(TRUE)[[1L]], "r")
testCases = readLines(inputFile)
cat(reverseWords(testCases), sep = "\n")
