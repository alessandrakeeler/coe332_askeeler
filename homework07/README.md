# The Million Dollar Diagram 

This diagram is a flowchart that illustrates to users of the midterm project different routes they can take within the flask API!. 


![](https://raw.githubusercontent.com/alessandrakeeler/coe332_askeeler/main/homework_07/searchingiss_diagram.png)


### The various yellow brick roads of this diagram
1. The first step of using this diagram is to run the app, which is illustrated by the green start circle. To run the app run the block of commands below. 

``` 
    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run -p 5000 
```

2. Now, it's time to enter the first purple block **/read_data**. To do this, run ``` curl localhost:5000/read_data -X post ``` . If that doesn't work, it means the user is on the left side of the flow chart and need to run the next purple box ``` curl localhost:5000/help ```  which will allow the user to troubleshoot why the data isn't loading. 

3. Assuming the data has been loaded, the user is now on the right side of the diagram. Yay! Every **yellow** box on the right returns a specific entity within the previous general **purple** box. 

Starting commands. These bring the user to a specific country. 
- ``` curl localhost:5000/countries ``` will return all of the countries 
- ``` curl localhost:5000/countries/<country> ``` 

Once the user is at the country they wish to query, they can continue down the flow chart running ``` curl localhost:5000/countries/<country>/regions ``` , etc all the way to the specificity of ``` curl localhost:5000/countries/<country>/regions/<region>/cities/<city> ``` which outputs specific city sighting data. 
