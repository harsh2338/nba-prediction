# NBA Data Analysis

.... Pranav

### Results of games

... Nishant

#### Box Score

... Nishant

### Synergy

In Basketball, player-player chemistry plays a big role in predicting the output of the games. Here, the motivation of this model is to understand the role that player-player chemistry (synergy) may play in predicting game outcomes and providing quantitative predictions of chemistry between players. 

The inputs for our algorithm will be the identity of the players on each team for a given game. We will then use logistic regression with a linear model and a quadratic.

model to output a prediction on which team will win the match. We also provide a comparison using a multi-layer perceptron neural net.

**Linear Model**

![alt_text](images/image1.png)

**Quadratic Model**

![alt_text](images/image2.png)

We’ll also take a look at the learned parameters of the quadratic model which will give us quantitative parameters to compare the chemistry of the players. 

The feature vector for every team would have a length of total number of players. It would have 1s in positions corresponding to its players and 0s elsewhere. Using this as input to our quadratic model we get two matrices **S** and **A**. 



*   Diagonal elements of S - indicator of player’s individual skill 
*   Off-diagonal elements of S - indicator of how much the two players as teammates contribute positively to the win percentage of their team 
*   Off-diagonal elements of A - indicator of the difference in the players’ contribution to their teams’ winning chance when they are on opposing teams

These are very important parameters. Using these we can calculate how well would any two players fit together. Players i and j would fit together well if the value of **S**[i][j] is high and **A**[i][j] is low.

This work has a lot of potential as it can effectively predict which players should be paired together. Also, it can predict successful transfers and trades. But there are some drawbacks such as we have to include age as a factor. Also it doesn’t account for new players. Nevertheless, this has a lot of scope and can be explored further.

### Positive and Negative Synergies

**About the paper**

Allan Z. Maymin et al. provide a novel Skills Plus Minus (“SPM”) framework that can be used to measure synergies within basketball lineups, provide roster-dependent rankings of free agents, and generate mutually beneficial trades.

An evaluation on each player’s offense and defense in the SPM framework for three basic skill categories is done:

1. **Ball-handling Category**: Steal, Non-steal turnover
2. **Rebounding Category**: Rebound of a missed field goal, Rebound of a missed free throw
3. **Scoring Category**: Made field goal (2 or 3 points),

The synergies of each NBA team is calculated by comparing their 5-player lineup’s effectiveness to the “sum-of-the-parts.” The framework generates mutually beneficial trades between teams. Because skills have different synergies with other skills, the framework predicts that a player’s value depends on the other nine players on the court.

While these box score ratings can measure an individual’s contributions, they do not
necessarily explain how players interact on the court. For example, it is possible that the five
best players in the NBA are all centers. In this case, a team with five centers may not be the
optimal lineup, since there would be no one to bring the ball up the court or guard the quicker
opposing guards.

Certain trades can also be predicted using the framework.
It predicted that in the 2009-10 season, if the New Orleans Hornets traded Chris Paul for Deron Williams from the Utah Jazz, both the teams would have been a mutually beneficial trade.

The Probabilty of an event to occur is calculated using the below formula

![Conditional probability of each event](https://github.com/harsh2338/nba-prediction/blob/main/images/conditional_probability.png)

For example, the probabilty of a steal by Rondo is given as:

![Example of probability of a steal](https://github.com/harsh2338/nba-prediction/blob/main/images/example_prob_of_steal.png)

Using the probabilities the series of events can be predicted using the flow diagram

![Flow of events](https://github.com/harsh2338/nba-prediction/blob/main/images/events_flow.png)

**Individual Player Ratings**:
By this example we can explain how a player is rated. Let’s say we create a fictional player who has Ronnie Brewer’s “steals” ratings, but is replacement level in all other skills. We then simulate games where one team consists of the fictional player and four replacement players, and their opponent utilizes five replacement players. The estimated point differential of this game is the player’s ratings for that particular skill.

Synergies are measured by how many additional points a combination of two skills create. For
example, Chris Paul's offensive ballhandling is worth 4.8 points, while Reggie Evans' offensive
rebounding is worth 3.1 points. We calculate that a team with Chris Paul's offensive
ballhandling and Reggie Evans’ defensive rebounding will have a 8.1 point advantage.
Therefore we calculate synergies as worth 0.2 points (8.1-4.8-3.1). Synergies are the difference
between the point differential of the combined team and the sum of the two individual players;
they tell us which types of players work well with one another.

For constructing a team, a few star players are chosen for a team and all the other players are made as free agents. By generating multiple combinations, a team can be completed by calculating the maximum team rating.

### Generating Line ups

...


**LightGBM**

Gradient boosting refers to a class of ensemble machine learning algorithms that can be used for classification or regression predictive modeling problems.

Ensembles are constructed from decision tree models. Trees are added one at a time to the ensemble and fit to correct the prediction errors made by prior models. This is a type of ensemble machine learning model referred to as boosting.

Models are fit using any arbitrary differentiable loss function and gradient descent optimization algorithm. This gives the technique its name, “gradient boosting,” as the loss gradient is minimized as the model is fit, much like a neural network.

LightGBM is a gradient boosting framework that uses a tree based learning algorithm. It extends the gradient boosting algorithm by adding a type of automatic feature selection as well as focusing on boosting examples with larger gradients. It is widely used in cases of tabular data for regression and classification.

LightGBM is prefixed as ‘Light’ because of its high speed. Light GBM can handle the large size of data and takes lower memory to run. Tble his is suitable as the number of records in the dataset is about 1.2 lakhs. Another reason of why Light GBM is popular is because it focuses on accuracy of results.

Since it is based on decision tree algorithms, it splits the tree leaf wise with the best fit whereas other boosting algorithms split the tree depth wise or level wise rather than leaf-wise. So when growing on the same leaf in Light GBM, the leaf-wise algorithm can reduce more loss than the level-wise algorithm and hence results in much better accuracy which can rarely be achieved by any of the existing boosting algorithms.

![LightGBM vs Boosting](https://github.com/harsh2338/nba-prediction/blob/main/images/tree_growth.png)

### Bayesian Opt

**Bayesian Optimization** is a probabilistic model based approach for finding the minimum of any function that returns a real-value metric. It is very effective with real-world applications in high-dimensional parameter-tuning for complex machine learning algorithms. Bayesian optimization utilizes the Bayesian technique of setting a prior over the objective function and combining it with evidence to get a posterior function.

![alt_text](images/image3.png)

Hyperparameter tuning by Bayesian Optimization of machine learning models is more efficient than Grid Search and Random Search. Bayesian Optimization has better overall performance on the test data and takes less time for optimization. 

NN Pranav

GA Prajna

### Expert Opinion

... Prajna
