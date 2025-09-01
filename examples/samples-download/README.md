# Sample Download Example

In this example, we show how to fetch samples from the samples api using
the API object. 

We start with a project like this:

![project overview](./project_screenshot.png)

and then:
* query for all audio regions
* extract the sample entity from all audio regions
* go to the sample API to get flac, wav, mp3 urls
* download the sample & play it