# Python script that uses the slack API to send messages to a slack channel.

## Run Commands


```bash
docker run -it slackmessager python main.py -n "x" -num 5 -nea 4 -url "google.com"

python main.py -n "test1" -num 5 -nea 4 -url "google.com"
```
## Flags

-n stands for job name  
-num stands for job number  
-nea stands for the node on which the job failed  
-url is the job url