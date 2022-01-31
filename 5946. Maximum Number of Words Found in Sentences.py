# Databricks notebook source
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        Max = 0
        for i in sentences:
            SubStr = len(i.split(" "))
            if(SubStr > Max):
                Max = SubStr
        return Max
