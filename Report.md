<!-----
NEW: Check the "Suppress top comment" option to remove this info from the output.

Conversion time: 0.633 seconds.


Using this Markdown file:

1. Paste this output into your source file.
2. See the notes and action items below regarding this conversion run.
3. Check the rendered output (headings, lists, code blocks, tables) for proper
   formatting and use a linkchecker before you publish this page.

Conversion notes:

* Docs to Markdown version 1.0β29
* Sun Mar 21 2021 03:54:55 GMT-0700 (PDT)
* Source doc: IEEE-Project
* This is a partial selection. Check to make sure intra-doc links work.
* This document has images: check for >>>>>  gd2md-html alert:  inline image link in generated source and store images to your server. NOTE: Images in exported zip file from Google Docs may not appear in  the same order as they do in your doc. Please check the images!


WARNING:
You have 2 H1 headings. You may want to use the "H1 -> H2" option to demote all headings by one level.

----->


<p style="color: red; font-weight: bold">>>>>>  gd2md-html alert:  ERRORs: 0; WARNINGs: 1; ALERTS: 1.</p>
<ul style="color: red; font-weight: bold"><li>See top comment block for details on ERRORs and WARNINGs. <li>In the converted Markdown or HTML, search for inline alerts that start with >>>>>  gd2md-html alert:  for specific instances that need correction.</ul>

<p style="color: red; font-weight: bold">Links to alert messages:</p><a href="#gdcalert1">alert1</a>

<p style="color: red; font-weight: bold">>>>>> PLEASE check and correct alert issues and delete this message and the inline alerts.<hr></p>



# <span style="text-decoration:underline;">Synergy</span>

In Basketball, player-player chemistry plays a big role in predicting the output of the games. Here, the motivation of this model is to understand the role that player-player chemistry (synergy) may play in predicting game outcomes and providing quantitative predictions of chemistry between players. 

The inputs for our algorithm will be the identity of the players on each team for a given game. We will then use logistic regression with a linear model and a quadratic.

model to output a prediction on which team will win the match. We also provide a comparison using a multi-layer perceptron neural net.

**<span style="text-decoration:underline;">Linear Model </span>**

**<span style="text-decoration:underline;">Quadratic Model</span>**

We’ll also take a look at the learned parameters of the quadratic model which will give us quantitative parameters to compare the chemistry of the players. 

The feature vector for every team would have a length of total number of players. It would have 1s in positions corresponding to its players and 0s elsewhere. Using this as input to our quadratic model we get two matrices **S** and **A**. 



*   Diagonal elements of S - indicator of player’s individual skill 
*   Off-diagonal elements of S - indicator of how much the two players as teammates contribute positively to the win percentage of their team 
*   Off-diagonal elements of A - indicator of the difference in the players’ contribution to their teams’ winning chance when they are on opposing teams

These are very important parameters. Using these we can calculate how well would any two players fit together. Players i and j would fit together well if the value of **S**[i][j] is high and **A**[i][j] is low.

This work has a lot of potential as it can effectively predict which players should be paired together. Also, it can predict successful transfers and trades. But there are some drawbacks such as we have to include age as a factor. Also it doesn’t account for new players. Nevertheless, this has a lot of scope and can be explored further.


# <span style="text-decoration:underline;">Bayesian Opt</span>

**Bayesian Optimization** is a probabilistic model based approach for finding the minimum of any function that returns a real-value metric. It is very effective with real-world applications in high-dimensional parameter-tuning for complex machine learning algorithms. Bayesian optimization utilizes the Bayesian technique of setting a prior over the objective function and combining it with evidence to get a posterior function.



<p id="gdcalert1" ><span style="color: red; font-weight: bold">>>>>>  gd2md-html alert: inline image link here (to images/image1.jpg). Store image on your image server and adjust path/filename/extension if necessary. </span><br>(<a href="#">Back to top</a>)(<a href="#gdcalert2">Next alert</a>)<br><span style="color: red; font-weight: bold">>>>>> </span></p>


![alt_text](images/image1.jpg "image_tooltip")


Hyperparameter tuning by Bayesian Optimization of machine learning models is more efficient than Grid Search and Random Search. Bayesian Optimization has better overall performance on the test data and takes less time for optimization. 
