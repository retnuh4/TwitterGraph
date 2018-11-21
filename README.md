# TwitterGraph
Scripts that use twitter API to mine tweets in real time that are defined by a word search. Then uses the mined tweets to display a bar graph.


**The minit file**
is used for connecting to the twitter API and starting a stream that is listening for all tweets defined by the search keyword or keywords in the code. Be sure to register your app with developer.twitter.com to get your API keys and Access tokens


**The grapx file**
is used for analyzing the data collected from the minit file. It opens the text file that is created by the minit and reads it to a json file. Then, after the text file is parsed it outputs the total number of tweets collected and outputs a bar graph depicting the number as well.
